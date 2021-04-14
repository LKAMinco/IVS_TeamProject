#Concept for getting input from user

import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Calculator')
		self.setGeometry(200,200,500,500)
		self.UI()

	def UI(self):
		self.resultTextBox = qtw.QLineEdit(self)
		self.resultTextBox.move(150,150)
		self.button = qtw.QPushButton("=",self)
		self.button.move(200,180)
		self.button.clicked.connect(self.save)
		self.show()

	def save(self):
		result = self.resultTextBox.text()
		process = eval(result)
		self.resultTextBox.setText(str(process))

app = qtw.QApplication([])
mv = MainWindow()
app.exec_()
