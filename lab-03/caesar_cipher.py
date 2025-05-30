import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        print("DEBUG call_api_encrypt:")
    print("  txt_key type:", type(self.ui.txt_key))
    print("  txt_key has toPlainText:", hasattr(self.ui.txt_key, "toPlainText"))
    print("  txt_key content:", self.ui.txt_key.toPlainText())

    url = "http://127.0.0.1:5000/api/caesar/encrypt"
    payload = {
        "plain_text": self.ui.txt_plain_text.toPlainText(),
        "key": self.ui.txt_key.toPlainText()
    }
    # phần còn lại giữ nguyên...

    def call_api_decrypt(self):
        print("DEBUG call_api_decrypt:")
        print("  txt_key type:", type(self.ui.txt_key))
        print("  txt_key has toPlainText:", hasattr(self.ui.txt_key, "toPlainText"))
        print("  txt_key content:", self.ui.txt_key.toPlainText())

        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            "cipher_text": self.ui.txt_cipher_text.toPlainText(),
            "key": self.ui.txt_key.toPlainText()
        }
        # phần còn lại giữ nguyên...

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
