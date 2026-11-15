
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class DragDropDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Drag and Drop Demo")
        self.setGeometry(300, 300, 600, 400)

        layout = QHBoxLayout()

        # List kiri
        left_container = QVBoxLayout()
        left_container.addWidget(QLabel("Source (drag from here):"))

        self.left_list = QListWidget()
        self.left_list.setDragEnabled(True)
        self.left_list.setSelectionMode(
            QAbstractItemView.SingleSelection
        )

        for item in ["Apple", "Banana", "Cherry", "Date", "Elderberry"]:
            self.left_list.addItem(item)

        left_container.addWidget(self.left_list)

        # List kanan
        right_container = QVBoxLayout()
        right_container.addWidget(QLabel("Target (drop here):"))

        self.right_list = QListWidget()
        self.right_list.setAcceptDrops(True)

        right_container.addWidget(self.right_list)

        # Tombol clear
        clear_btn = QPushButton("Clear Target")
        clear_btn.clicked.connect(self.right_list.clear)

        right_container.addWidget(clear_btn)

        layout.addLayout(left_container)
        layout.addLayout(right_container)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DragDropDemo()
    window.show()
    sys.exit(app.exec_())
