import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QCheckBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize
import requests
from PIL import Image
from io import BytesIO

class TableroFlotante(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tablero de Accesos Directos")
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: #272b2d; color: #f5f0f0;")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Crear un widget para los botones
        buttons_widget = QWidget()
        buttons_layout = QGridLayout(buttons_widget)
        buttons_widget.setStyleSheet("background-color: #131516;")

        aplicaciones = [
            ("", "D:/www/Python/gadgets/lector.py/dist/lector/lector.exe", "https://cdn.icon-icons.com/icons2/3782/PNG/512/audio_bar_transmission_equalizer_sound_waveform_chat_voice_icon_232072.png"),
            ("", "D:/www/Python/Reloj/dist/reloj/reloj.exe", "https://cdn.icon-icons.com/icons2/4183/PNG/96/and_alarm_clock_timer_time_date_icon_262278.png"),
            ("", "D:/www/Python\gadgets/fondo negro.py/dist/fondo_negro.exe", "https://cdn.icon-icons.com/icons2/4183/PNG/96/monitor_language_programming_programing_computing_computer_coding_icon_262283.png"),
            ("", "D:/www/Chatbot IA/crearWebsConfoto/gemini-ui-to-code/lanzador.bat", "https://github.com/jorgedipra/panel-aplicaiones/blob/main/iconos/crearWebsConfoto.png?raw=true"),
            ("", "D:/www/Chatbot IA/chatgpt-artifacts(crear codigo)/lanzador.bat", "https://github.com/jorgedipra/panel-aplicaiones/blob/main/iconos/crear_codigo.png?raw=true"),
            ("", "D:/www/Python/gadgets/panelAplicaiones.py/pinokio.bat", "https://github.com/jorgedipra/panel-aplicaiones/blob/main/iconos/pinokio.png?raw=true"),
            ("", "D:/www/Python/gadgets/panelAplicaiones.py/Chatbox.bat", "https://github.com/jorgedipra/panel-aplicaiones/blob/main/iconos/Chatbox.png?raw=true"),
            ("", '"C:\Program Files\Google\Chrome\Application\chrome.exe" --process-per-site --profile-directory="Profile 8"', "https://cdn.icon-icons.com/icons2/3919/PNG/96/google_chrome_icon_249841.png"),
            ("", "D:/www/Python/openinterpreter.bat", "https://github.com/jorgedipra/panel-aplicaiones/blob/main/iconos/Open_Interpreter.png?raw=true"),
            
            # ("", "calc", "https://cdn.icon-icons.com/icons2/272/PNG/512/Calculator_30001.png"),
            # ("", "notepad", "https://cdn.icon-icons.com/icons2/153/PNG/256/bloc_notes_21874.png"),
        ]

        # Crear botones para cada aplicación
        for i, (nombre, comando, icon_url) in enumerate(aplicaciones):
            row = i // 3
            col = i % 3

            # Descargar y configurar el icono
            response = requests.get(icon_url)
            image_data = response.content
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            pixmap = pixmap.scaled(QSize(50, 50), Qt.KeepAspectRatio, Qt.SmoothTransformation)

            # Crear botón con el icono y texto
            btn = QPushButton(QIcon(pixmap), nombre, buttons_widget)
            btn.setIconSize(QSize(50, 50))
            btn.setStyleSheet("background-color: #131516; color: #f5f0f0;")
            btn.clicked.connect(lambda _, c=comando: self.abrir_aplicacion(c))
            buttons_layout.addWidget(btn, row, col, 1, 1, alignment=Qt.AlignCenter)

        buttons_widget.setLayout(buttons_layout)
        layout.addWidget(buttons_widget)

        # Crear un checkbox para alternar siempre al frente o no
        check_box = QCheckBox("Siempre al frente", central_widget)
        check_box.setStyleSheet("color: #f5f0f0;")
        check_box.setChecked(False)
        check_box.stateChanged.connect(self.alternar_frente)
        layout.addWidget(check_box, alignment=Qt.AlignCenter)

        self.always_on_top = True

    def abrir_aplicacion(self, comando):
        try:
            if comando.startswith("http"):
                import webbrowser
                webbrowser.open(comando)
            else:
                import subprocess
                subprocess.Popen(comando)
        except Exception as e:
            print(f"No se pudo abrir la aplicación: {e}")

    def alternar_frente(self, state):
        if state == Qt.Checked:
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
            self.always_on_top = True
        else:
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)
            self.always_on_top = False
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TableroFlotante()
    window.show()
    sys.exit(app.exec_())
