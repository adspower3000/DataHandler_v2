import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtSql import QSqlTableModel

from ui_mainu import Ui_MainWindow
from connection import Data


class DataHandler(QMainWindow):
    def __init__(self):
        super(DataHandler, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()
        self.reload_data()
        self.view_data()
        self.ui.enterbtn_4.clicked.connect(self.reload_data())
        self.ui.enterbtn_4.clicked.connect(self.view_data())

    def reload_data(self):
        self.conn.create_connection()
        self.ui.Sum_N_8.setText(self.conn.total_N())
        # self.ui.JobHour.setText(self.conn.total_JobHour())
        # self.ui.deltaT_8.setText(self.conn.get_deltaT())

    def view_data(self):
        self.conn.create_connection()
        self.model = QSqlTableModel(self)
        self.model.setTable('data_day_suz')
        self.model.select()
        self.ui.tableView.setModel(self.model)

    # def execute_date1(self):
    #     date1 = self.ui.bytimepicker_4.text()
    #     # setDisplayFormat("dd.MM.yyyy"))
    #     self.reload_data()
    #     self.view_data()
    #     return str(date1)
    #
    #
    # def execute_date2(self):
    #     date2 = self.ui.untiltimepicker_4.text()
    #     # setDisplayFormat("dd.MM.yyyy"))
    #     self.reload_data()
    #     self.view_data()
    #     return str(date2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataHandler()
    window.show()

    sys.exit(app.exec())
