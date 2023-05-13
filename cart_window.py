from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CART_WINDOW(object):
    def setupUi(self, CART_WINDOW):
        CART_WINDOW.setObjectName("CART_WINDOW")
        CART_WINDOW.resize(600, 349)
        self.cart_table = QtWidgets.QTableWidget(CART_WINDOW)
        self.cart_table.setGeometry(QtCore.QRect(50, 20, 501, 221))
        self.cart_table.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.cart_table.setObjectName("cart_table")
        self.cart_table.setColumnCount(3)
        self.cart_table.setRowCount(100)
        self.cart_table.setHorizontalHeaderLabels(["ITEM", "QUANTITY", "AMOUNT"])
        self.cart_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.label = QtWidgets.QLabel(CART_WINDOW)
        self.label.setGeometry(QtCore.QRect(420, 255, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cart_table.setFont(font)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.total_label = QtWidgets.QLabel(CART_WINDOW)
        self.total_label.setGeometry(QtCore.QRect(470, 255, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.total_label.setFont(font)
        self.total_label.setText("")
        self.total_label.setAlignment(QtCore.Qt.AlignCenter)
        self.total_label.setObjectName("total_label")
        self.message = QtWidgets.QLabel(CART_WINDOW)
        self.message.setGeometry(QtCore.QRect(40, 290, 511, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.delete_button = QtWidgets.QPushButton(CART_WINDOW, clicked=self.delete_item)
        self.delete_button.setText("DELETE")
        self.delete_button.setStyleSheet("background-color: rgb(0, 0, 0);\n color: rgb(255, 255, 255);\n border-radius: 5px;")
        self.delete_button.setGeometry(QtCore.QRect(60, 255, 90, 30))
        self.delete_button.setFont(font)
        self.delete_entry = QtWidgets.QLineEdit(CART_WINDOW)
        self.delete_entry.setStyleSheet("color: rgb(0, 0, 0);")
        self.delete_entry.setFont(font)
        self.delete_entry.setGeometry(160, 255, 30, 30)
        self.message.setFont(font)
        self.message.setStyleSheet("color: rgb(255, 0, 0);")
        self.message.setText("")
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        self.message.setWordWrap(True)
        self.message.setObjectName("message")
        self.retranslateUi(CART_WINDOW)
        self.display_items()
        QtCore.QMetaObject.connectSlotsByName(CART_WINDOW)

    def retranslateUi(self, CART_WINDOW):
        _translate = QtCore.QCoreApplication.translate
        CART_WINDOW.setWindowTitle(_translate("CART_WINDOW", "Cart"))
        self.label.setText(_translate("CART_WINDOW", "Total:"))
        self.cart_logo_map = QtGui.QPixmap("cart_logo.jpg")
        self.cart_logo = QtGui.QIcon(self.cart_logo_map)
        CART_WINDOW.setWindowIcon(self.cart_logo)

    def display_items(self):
        with open("cart_items.txt", "r") as file:
            lines = file.readlines()
            name_row = 0
            qty_row = 0
            amount_row = 0
            item_names = []
            item_qty = []
            item_amount = []
            amounts_without_newline = []
            for line in lines:
                each_item = line.split(",")
                item_names.append(each_item[0])
                item_qty.append(each_item[1])
                item_amount.append(each_item[2])
            for amounts in item_amount:
                amount_without_newline = amounts.removesuffix("\n")
                amounts_without_newline.append(amount_without_newline)
            for name in item_names:
                self.cart_table.setItem(name_row, 0, QtWidgets.QTableWidgetItem(name))
                name_row += 1
            for qties in item_qty:
                self.cart_table.setItem(qty_row, 1, QtWidgets.QTableWidgetItem(qties))
                qty_row += 1
            for amount in amounts_without_newline:
                self.cart_table.setItem(amount_row, 2, QtWidgets.QTableWidgetItem(amount))
                amount_row += 1
            self.calculate_total(amounts_without_newline)

    def calculate_total(self, list_of_amounts):
        int_amounts = []
        sum = 0
        for str_amount in list_of_amounts:
            int_amounts.append(int(str_amount))
        for int_amount in int_amounts:
            sum += int_amount
        self.total_label.setText("$" + str(sum) + ".00")

    def delete_item(self):
        try:
            index = int(self.delete_entry.text())
            selected_item_name = self.cart_table.item(index-1, 0)
            selected_item_qty = self.cart_table.item(index-1, 1)
            selected_item_amount = self.cart_table.item(index-1, 2)
            str_selected_name = selected_item_name.text()
            str_selected_qty = selected_item_qty.text()
            str_selected_amount = selected_item_amount.text()
            with open("cart_items.txt", "r") as file:
                contents = file.read()
            new_contents = contents.replace(f"{str_selected_name},{str_selected_qty},{str_selected_amount}\n", "")
            with open("cart_items.txt", "w") as file:
                file.write(new_contents)


        except Exception as e:
            print(str(e))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CART_WINDOW = QtWidgets.QWidget()
    ui = Ui_CART_WINDOW()
    ui.setupUi(CART_WINDOW)
    CART_WINDOW.show()
    sys.exit(app.exec_())
