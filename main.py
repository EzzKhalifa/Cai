import sys
import logging
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QTextEdit, QMessageBox, QLabel
from ai_module import process_input  # Import the process_input function from your AI module

# Set up logging configuration
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def save_to_file(self, input_text, result):
        file_path = 'sentiment_analysis_results.txt'
        with open(file_path, 'a') as file:
            file.write(f'Input: {input_text}\nResult: {result}\n\n')

    def initUI(self):
        self.setWindowTitle('AI Windows Application')
        self.setGeometry(100, 100, 600, 400)

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.layout = QVBoxLayout()

        self.instructionLabel = QLabel('Enter text below and press "Run AI" to see the sentiment prediction.', self)
        self.layout.addWidget(self.instructionLabel)

        self.userInput = QLineEdit(self)
        self.userInput.setPlaceholderText('Enter text here')
        self.layout.addWidget(self.userInput)

        self.runButton = QPushButton('Run AI', self)
        self.runButton.clicked.connect(self.runAI)
        self.layout.addWidget(self.runButton)

        self.output = QTextEdit(self)
        self.output.setReadOnly(True)
        self.layout.addWidget(self.output)

        self.centralWidget.setLayout(self.layout)

    def runAI(self):
        input_text = self.userInput.text()
        try:
            result = self.processInput(input_text)
            self.output.setText(f'Result: {result}')
            self.save_to_file(input_text, result)  # Save the result to a file
            logging.info(f'Processed input: "{input_text}" with result: "{result}"')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'An error occurred: {e}')
            self.output.setText('')
            logging.error(f'Error processing input: "{input_text}" - {e}')

    def processInput(self, input_text):
        # This method will call the AI function
        return process_input(input_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
