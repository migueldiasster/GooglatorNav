from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

# Crear una aplicación Qt
app = QApplication([])

# Crear una ventana del navegador
webview = QWebEngineView()
webview.load(QUrl("https://www.google.com"))  # Cargar una URL en el navegador
webview.show()  # Mostrar la ventana del navegador

# Ejecutar el bucle de eventos de la aplicación Qt
app.exec_()