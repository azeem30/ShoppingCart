from PyQt5 import QtCore, QtGui, QtWidgets
import cart_window

class Item:
    def __init__(self, name, quantity, amount):
        self.name = name
        self.quantity = quantity
        self.amount = amount

class Ui_CART(object):
    def __init__(self):
        self.items = []

    def setupUi(self, CART):
        CART.setObjectName("CART")
        CART.resize(334, 271)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        CART.setFont(font)
        self.label = QtWidgets.QLabel(CART)
        self.label.setGeometry(QtCore.QRect(34, 32, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.item_name = QtWidgets.QLineEdit(CART)
        self.item_name.setGeometry(QtCore.QRect(80, 25, 201, 31))
        self.item_name.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-radius: 5px;")
        self.item_name.setObjectName("item_name")
        self.label_2 = QtWidgets.QLabel(CART)
        self.label_2.setGeometry(QtCore.QRect(34, 70, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.quantity = QtWidgets.QLineEdit(CART)
        self.quantity.setGeometry(QtCore.QRect(75, 67, 30, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.quantity.setFont(font)
        self.quantity.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-radius: 5px;")
        self.quantity.setText("")
        self.quantity.setObjectName("quantity")
        self.plus = QtWidgets.QPushButton(CART, clicked=self.increase)
        self.plus.setGeometry(QtCore.QRect(70, 93, 20, 20))
        self.plus.setStyleSheet("image: url(inc.jpeg);")
        self.plus.setText("")
        self.plus.setObjectName("plus")
        self.minus = QtWidgets.QPushButton(CART, clicked=self.decrease)
        self.minus.setGeometry(QtCore.QRect(92, 93, 20, 20))
        self.minus.setStyleSheet("image: url(dec.jpeg);")
        self.minus.setText("")
        self.minus.setObjectName("minus")
        self.label_3 = QtWidgets.QLabel(CART)
        self.label_3.setGeometry(QtCore.QRect(160, 70, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.price = QtWidgets.QLabel(CART)
        self.price.setGeometry(QtCore.QRect(205, 69, 60, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.price.setFont(font)
        self.price.setText("$0.00")
        self.price.setAlignment(QtCore.Qt.AlignCenter)
        self.price.setObjectName("price")
        self.add_button = QtWidgets.QPushButton(CART, clicked=self.add_item)
        self.add_button.setGeometry(QtCore.QRect(110, 180, 131, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.add_button.setFont(font)
        self.add_button.setStyleSheet("border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"")
        self.add_button.setObjectName("add_button")
        self.view_button = QtWidgets.QPushButton(CART, clicked=self.go_cart)
        self.view_button.setGeometry(QtCore.QRect(110, 220, 131, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.view_button.setFont(font)
        self.view_button.setStyleSheet("border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"")
        self.view_button.setObjectName("view_button")
        self.message = QtWidgets.QLabel(CART)
        self.message.setGeometry(QtCore.QRect(40, 120, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.message.setFont(font)
        self.message.setStyleSheet("color: rgb(255, 0, 0);")
        self.message.setText("")
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        self.message.setObjectName("message")

        self.retranslateUi(CART)
        QtCore.QMetaObject.connectSlotsByName(CART)

    def retranslateUi(self, CART):
        _translate = QtCore.QCoreApplication.translate
        CART.setWindowTitle(_translate("CART", "Add to Cart"))
        self.label.setText(_translate("CART", "Item"))
        self.label_2.setText(_translate("CART", "Qty."))
        self.label_3.setText(_translate("CART", "Price:"))
        self.add_button.setText(_translate("CART", "ADD TO CART"))
        self.view_button.setText(_translate("CART", "VIEW CART"))
        self.cart_logo_map = QtGui.QPixmap("cart_logo.jpg")
        self.cart_logo = QtGui.QIcon(self.cart_logo_map)
        CART.setWindowIcon(self.cart_logo)

    def add_item(self):
        try:
            self.str_item = self.item_name.text()
            self.str_qty = self.quantity.text()
            self.int_price = 10
            self.total = self.int_price * int(self.str_qty)
            self.str_total = str(self.total)
            self.price.setText("$" + self.str_total + ".00")
            item = Item(self.str_item, self.str_qty, self.str_total)
            self.items.append(item)
            self.write_to_file()
            self.message.setStyleSheet("color: rgb(0, 255, 0);")
            self.message.setText("Item Added Successfully to Cart!")
        except Exception as e:
            self.message.setText(str(e))
            print(str(e))

    def increase(self):
        self.str_qty = self.quantity.text()
        if self.str_qty == "":
            int_qty = 0
        else:
            int_qty = int(self.str_qty)
        new_qty = int_qty + 1
        str_new_qty = str(new_qty)
        self.quantity.setText(str_new_qty)

    def decrease(self):
        self.str_qty = self.quantity.text()
        if self.str_qty == "":
            int_qty = 0
        else:
            int_qty = int(self.str_qty)
        new_qty = int_qty - 1
        str_new_qty = str(new_qty)
        self.quantity.setText(str_new_qty)

    def write_to_file(self):
        with open("cart_items.txt", "a") as file:
            file.write(self.str_item + ", " + self.str_qty + ", " + self.str_total + "\n")

    def go_cart(self):
        self.cwin = QtWidgets.QWidget()
        self.cui = cart_window.Ui_CART_WINDOW()
        self.cui.setupUi(self.cwin)
        self.cwin.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CART = QtWidgets.QWidget()
    ui = Ui_CART()
    ui.setupUi(CART)
    CART.show()
    sys.exit(app.exec_())
