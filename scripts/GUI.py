import sys
from pathlib import Path
from PyQt5 import  QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from PyQt5.QtWidgets import QComboBox, QLineEdit, QPushButton, QFileDialog
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout, QFrame, QDialog
from PyQt5.QtCore import QSize
from .Functions import downloadURL, playlist_parser, file_parser

class MainWindow(QMainWindow):
    """Main Window of the GUI"""
    def __init__(self):
        super(MainWindow,self).__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle('Youtube Downloader')
        self.setFixedSize(QSize(600,500))
        # Initalizing the download type layout
        self.download_type_layout = self.initTypeLayout()

        # Initalizing download single video layout
        self.download_single_layout = self.initSingleLayout()

        # Initalizing the download from a playlist layout
        self.download_playlist_layout = self.initPlaylistLayout()

        # Initalizing download from a txt file layout
        self.download_file_layout = self.initFileLayout()

        # Add a vertical line separator using QFrame

        self.line1 = QFrame()
        self.line1.setFrameShape(QFrame.HLine)
        self.line1.setLineWidth(3)

        self.line2 = QFrame()
        self.line2.setFrameShape(QFrame.HLine)
        self.line2.setLineWidth(2)

        self.line3 = QFrame()
        self.line3.setFrameShape(QFrame.HLine)
        self.line3.setLineWidth(2)


        # Adding all layouts together
        self.final_layout = QVBoxLayout()
        self.final_layout.addLayout(self.download_type_layout)
        self.final_layout.addWidget(self.line1)
        self.final_layout.addLayout(self.download_single_layout)
        self.final_layout.addWidget(self.line2)
        self.final_layout.addLayout(self.download_playlist_layout)
        self.final_layout.addWidget(self.line3)
        self.final_layout.addLayout(self.download_file_layout)

        # Placing the final layout to the main window
        self.widget = QWidget()
        self.widget.setLayout(self.final_layout)
        self.setCentralWidget(self.widget)

    def initTypeLayout(self):
        """Function to initalize the layout to select the type from"""
        # Initalizing the download type layout
        self.download_type_layout = QHBoxLayout()

        self.types_label = QLabel('Please select the download type')
        self.types_widget = QComboBox()
        self.types_widget.addItems(['audio', 'video']) 

        self.download_type_layout.addWidget(self.types_label)
        self.download_type_layout.addWidget(self.types_widget)

        return self.download_type_layout

    def initSingleLayout(self):
        """Function to initalize the layout to download a single video"""

        self.download_single_layout = QVBoxLayout()

        self.single_label = QLabel('Download a single Video')

        self.single_url_widget = QLineEdit(alignment=Qt.AlignCenter)
        self.single_url_widget.setPlaceholderText('Please Enter the Youtube Video URL')

        self.single_download_button = QPushButton()
        self.single_download_button.setText('Download')
        self.single_download_button.clicked.connect(self.singleDownloadClicked)

        self.download_single_layout.addWidget(self.single_label, alignment=Qt.AlignCenter)
        self.download_single_layout.addWidget(self.single_url_widget)
        self.download_single_layout.addWidget(self.single_download_button, alignment=Qt.AlignCenter)

        self.download_single_layout.setAlignment(Qt.AlignCenter)
        
        return self.download_single_layout

    def initPlaylistLayout(self):
        """Function to initalize the layout to download a playlist"""

        self.download_playlist_layout = QVBoxLayout()

        self.playlist_label = QLabel('Download a playlist')

        self.playlist_url_widget = QLineEdit(alignment=Qt.AlignCenter)
        self.playlist_url_widget.setPlaceholderText('Please Enter the Youtube playlist URL')

        self.playlist_download_button = QPushButton()
        self.playlist_download_button.setText('Download')
        self.playlist_download_button.clicked.connect(self.playlistDownloadClicked)

        self.download_playlist_layout.addWidget(self.playlist_label, alignment=Qt.AlignCenter)
        self.download_playlist_layout.addWidget(self.playlist_url_widget)
        self.download_playlist_layout.addWidget(self.playlist_download_button, alignment=Qt.AlignCenter)

        return self.download_playlist_layout

    def initFileLayout(self):
        """Function to initalize the layout to download from a txt file"""

        # Initalizing download from a txt file layout
        self.download_file_layout = QVBoxLayout()

        self.file_label = QLabel('Download from URLs in a txt file')


        self.file_download_button = QPushButton()
        self.file_download_button.setText('Download')
        self.file_download_button.clicked.connect(self.fileDownloadClicked)


        # file selection
        self.select_file_layout = QHBoxLayout()
        self.file_browse = QPushButton('Browse')
        self.file_browse.clicked.connect(self.open_file_dialog)
        self.filename_edit = QLineEdit(alignment=Qt.AlignLeft)
        self.filename_edit.setPlaceholderText('Please select the txt file')

        self.select_file_layout.addWidget(QLabel('File:'))
        self.select_file_layout.addWidget(self.filename_edit)
        self.select_file_layout.addWidget(self.file_browse)


        self.download_file_layout.addWidget(self.file_label, alignment=Qt.AlignCenter)
        self.download_file_layout.addLayout(self.select_file_layout)
        self.download_file_layout.addWidget(self.file_download_button, alignment=Qt.AlignCenter)

        return self.download_file_layout

    def open_file_dialog(self):
        """Function to open a window to select a txt file from"""

        filename, _ = QFileDialog.getOpenFileName(
            self,
            caption="Select a File",
            filter="Text files (*.txt)"
        )
        if filename:
            path = Path(filename)
            self.filename_edit.setText(str(path))

    def singleDownloadClicked(self):
        type = self.types_widget.currentText()
        url = self.single_url_widget.text()


        try:
            downloadURL(url,type)
            msg = MassageWindow(title = 'Download Status',
                                text="URL downloaded Succesfully.",
                                button = 'ok',
                                icon='Information',
                                )
            msg.exec_()


        except:
            msg = MassageWindow(title = 'Download Status',
                                text="Failed to download.",
                                button = 'Abort',
                                icon='Critical')
            msg.exec_()

    def playlistDownloadClicked(self):
        type = self.types_widget.currentText()
        url = self.playlist_url_widget.text()
        try:
            playlist_parser(url,type)

            msg = MassageWindow(title = 'Download Status',
                                text="Playlist downloaded Succesfully.",
                                button = 'Ok',
                                icon='Information')
            msg.exec_()


        except:
            msg = MassageWindow(title = 'Download Status',
                                text="Failed to download.",
                                button = 'Abort',
                                icon='Critical')
            msg.exec_()

    def fileDownloadClicked(self):
        type = self.types_widget.currentText()
        path = self.filename_edit.text()
        try:
            file_parser(path,type)

            msg = MassageWindow(title = 'Download Status',
                                text="URLs in the file downloaded succesfully.",
                                button = 'Ok',
                                icon='Information')
            msg.exec_()


        except:
            msg = MassageWindow(title = 'Download Status',
                                text="Failed to download.",
                                button = 'Abort',
                                icon='Critical')
            msg.exec_()

class MassageWindow(QMessageBox):
    """Window to show message to the user"""
    def __init__(self, title,text,button,icon):
        super(MassageWindow, self).__init__()
        self.setWindowTitle(title)
        self.setText(text)
        if button == 'Abort':
            self.setStandardButtons(QMessageBox.Abort)
        elif button =='Ok':
            self.setStandardButtons(QMessageBox.Ok)


        if icon == 'Critical':
            self.setIcon(QMessageBox.Critical)
        elif icon == 'Information':
            self.setIcon(QMessageBox.Information)

        self.setFont(QtGui.QFont("Arial", 12))


def InitUI():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()

    app.setStyleSheet("""
                QMainWindow {
                    border: 2px solid #cccccc;
                    border-radius: 10px;
                    background-color: #152E22;}

                QPushButton {
                    font: bold 12pt Times New Roman;
                    color: #000000;
                    border: 2px solid #cccccc;
                    border-radius: 10px;
                    padding: 5px;
                    background-color: #688376;
                    min-width: 40px;
                    min-height: 15px;
                    max-width: 100;
                }
                QLabel {
                    font: bold 14pt Times New Roman;
                    color: #000000;
                    qproperty-alignment: AlignCenter;
                    border: 2px solid #cccccc;
                    border-radius: 10px;
                    padding: 10;
                    background-color: #ADA492;
                }
                QComboBox {
                    font:  12pt Arial;
                    color: #000000;
                    border: 2px solid #cccccc;
                    border-radius: 10px;
                    padding: 5px;
                    background-color: #C09D58;
                }
                QLineEdit {
                    font:  11pt Arial;
                    color: #000000;
                    border: 2px solid #cccccc;
                    border-radius: 10px;
                    padding: 5px;
                    background-color: #C09D58;
                }
                QFrame[frameShape="4"] {
                    color: #FFFFFF;
                }
            """)
    sys.exit(app.exec_())

