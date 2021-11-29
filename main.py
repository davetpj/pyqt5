import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()
		# Add a title
		self.setWindowTitle("Hello World!!")

		# Set (Vertical) layout
		self.setLayout(qtw.QVBoxLayout())

		# Create A Label
		my_label = qtw.QLabel("Pick Something From The List Below")
		# Change the font size of label
		my_label.setFont(qtg.QFont('Helvetica',24))
		self.layout().addWidget(my_label)

		# Create an Spin box or QDoubleSpinBox (float)
		my_spin = qtw.QSpinBox(self,
			value=10,
			maximum=100,
			minimum=0,
			singleStep=20,
			prefix="#",
			suffix=" Order")
		# Change font size of spinbox
		my_spin.setFont(qtg.QFont('Helvetica',24))

		# Put spinbox on the screen
		self.layout().addWidget(my_spin)

		# # Create an entry box
		# my_entry = qtw.QLineEdit()
		# my_entry.setObjectName("name_field")
		# my_entry.setText("")
		# self.layout().addWidget(my_entry)

		# # Create a Combo box
		# my_combo = qtw.QComboBox(self,
		# 	editable=True,
		# 	# .InsertAtBottom
		# 	insertPolicy=qtw.QComboBox.InsertAtTop)
		# # ADd Items To The Combo Box
		# my_combo.addItem("Pepperoni", "Something")
		# my_combo.addItem("Cheese", 2)
		# my_combo.addItem("Mushroom", qtw.QWidget)
		# my_combo.addItem("Peppers")
		# my_combo.addItems(["One","Two","Three"])
		# # (position(index), value(s))
		# my_combo.insertItem(2, "Third Thing")
		# # my_combo.insertItems(2, ["one","two","Third Thing"])

		# Put combobox on the screen
		# self.layout().addWidget(my_combo)


		# Create a button
		my_button = qtw.QPushButton("Press Me!",
			clicked = lambda: press_it())
		self.layout().addWidget(my_button)


		# Show the app
		self.show()

		def press_it():
			# Add name to label [my_combo.currentData,currentIndex,currentText]
			# my_spin.value 
			my_label.setText(f'You Picked {my_spin.value()}!')
			# # Clear the entry box
			# my_entry.setText("")


app = qtw.QApplication([])
mw = MainWindow()

# Run The App
app.exec_()