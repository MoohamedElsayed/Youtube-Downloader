from PyQt5 import  QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from PyQt5.QtWidgets import QComboBox, QLineEdit, QPushButton, QFileDialog
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout
import sys
from pathlib import Path
from downloader import downloadURL

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle('Youtube Downloader')
        self.initUI()

    def initUI(self):

        # Initalizing the download type layout
        download_type_layout = self.initTypeLayout()

        # Initalizing download single video layout
        download_single_layout = self.initSingleLayout()

        # Initalizing the download from a playlist layout
        download_playlist_layout = self.initPlaylistLayout()

        # Initalizing download from a txt file layout
        download_file_layout = self.initFileLayout()

        # Adding all layouts together
        final_layout = QVBoxLayout()
        final_layout.addLayout(download_type_layout)
        final_layout.addLayout(download_single_layout)
        final_layout.addLayout(download_playlist_layout)
        final_layout.addLayout(download_file_layout)

        # Placing the final layout to the main window
        widget = QWidget()
        widget.setLayout(final_layout)
        self.setCentralWidget(widget)

    def initTypeLayout(self):

        # Initalizing the download type layout
        download_type_layout = QHBoxLayout()

        types_label = QLabel('Please select the download type')

        self.types_widget = QComboBox()
        self.types_widget.addItems(['audio', 'video']) 

        download_type_layout.addWidget(types_label)
        download_type_layout.addWidget(self.types_widget)

        return download_type_layout

    def initSingleLayout(self):
        download_single_layout = QVBoxLayout()

        single_label = QLabel('Download a single URL')

        self.single_url_widget = QLineEdit()
        self.single_url_widget.setPlaceholderText('Please Enter the Youtube Video URL')

        single_download_button = QPushButton()
        single_download_button.setText('Download')
        single_download_button.clicked.connect(self.singleDownloadClicked)

        download_single_layout.addWidget(single_label)
        download_single_layout.addWidget(self.single_url_widget)
        download_single_layout.addWidget(single_download_button)
        
        return download_single_layout

    def initPlaylistLayout(self):
        download_playlist_layout = QVBoxLayout()

        playlist_label = QLabel('Download a playlist')

        playlist_url_widget = QLineEdit()
        playlist_url_widget.setPlaceholderText('Please Enter the Youtube playlist URL')

        playlist_download_button = QPushButton()
        playlist_download_button.setText('Download')

        download_playlist_layout.addWidget(playlist_label)
        download_playlist_layout.addWidget(playlist_url_widget)
        download_playlist_layout.addWidget(playlist_download_button)

        return download_playlist_layout

    def initFileLayout(self):
        # Initalizing download from a txt file layout
        download_file_layout = QVBoxLayout()

        file_label = QLabel('Download from a txt file')


        file_download_button = QPushButton()
        file_download_button.setText('Download')



        # file selection
        select_file_layout = QHBoxLayout()
        file_browse = QPushButton('Browse')
        file_browse.clicked.connect(self.open_file_dialog)
        self.filename_edit = QLineEdit()

        select_file_layout.addWidget(QLabel('File:'))
        select_file_layout.addWidget(self.filename_edit)
        select_file_layout.addWidget(file_browse)


        download_file_layout.addWidget(file_label)
        download_file_layout.addLayout(select_file_layout)
        download_file_layout.addWidget(file_download_button)

        return download_file_layout

    def open_file_dialog(self):
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

            msg = MassageWindow(title = 'Single Url Downloader',
                                text="Succesfully downloaded.",
                                button = 'Ok',
                                icon='Information')
            msg.exec_()


        except:
            msg = MassageWindow(title = 'Single Url Downloader',
                                text="Failed to download.",
                                button = 'Abort',
                                icon='Critical')
            msg.exec_()

class MassageWindow(QMessageBox):
    """Window ro show message to the user"""
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



def window():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

window()