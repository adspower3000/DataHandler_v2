from PySide6 import QtWidgets, QtSql
from ui_mainu import Ui_MainWindow


class Data:
    def __int__(self):
        super(Data, self).__init__()
        self.create_connection()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)




    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('data_handler.db')
        db.open()
        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS data_day_suz (ID integer primary key AUTOINCREMENT , date_time date , I1 decimal, I2 decimal, I3 decimal, I4 decimal, N decimal, deltaT decimal")

    # def execute_query_with_params(self, sql_query):
    #     query = QtSql.QSqlQuery()
    #     query.exec(sql_query)
    #     return query

    # нужен фильтр по диапазону дат от и до


    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()

        return query

    def get_total(self, column, filter=None, value=None):

        sql_query = f"SELECT SUM({column}) FROM data_day_suz"

        if filter is not None or value is not None:
            sql_query += f" WHERE {filter} = ?" + f"BETWEEN '{self.ui.date1}' AND '{self.ui.date2}'"
                          # .format(self.ui.date1, self.ui.date2))

        query_values = []

        if value is not None:
            query_values.append(value)

        query = self.execute_query_with_params(sql_query, query_values)

        if query.next():
            return str(query.value(0))

        return '0'








    # def get_total(self, column):
    #     sql_query = f"SELECT SUM({column}) FROM data_day_suz"
    #
    #     # if filter is not None:
    #     #     sql_query += f"WHERE  {filter} = ? BETWEEN {self.execute_date1()} and {self.execute_date2()}"
    #
    #     query = self.execute_query_with_params(sql_query)
    #
    #     return str(query)

    # def get_average(self, column, filter=None):
    #     sql_query = f"SELECT AVERAGE ({column}) FROM data_day_suz"
    #
    #
    #     # if filter is not None:
    #     #     sql_query += f"WHERE  {filter} = ? BETWEEN @date1 and @date2"
    #
    #     query = self.execute_query_with_params(sql_query)
    #
    #     return str(query)

    def total_N(self):
        return self.get_total(column="N", filter="date_time")
        # filter="date_time")

    # def total_JobHour(self):
    #     return self.get_total(column="JobHour", filter="date_time")

    # def get_deltaT(self):
    #     return self.get_average(column="deltaT")

        # filter="date_time")
# f"WHERE @bytimepickerdate.date <= {filter} <= @untiltimepicker.date = ?"



#   # current = QtCore.QDateTime.currentDateTime()
#   #       self.startDate.setDate(current.date())
#   #       self.endDate.setDate(current.date())
#   #       self.startDate.setDisplayFormat("M/dd/yyyy")
#   #       self.endDate.setDisplayFormat("M/dd/yyyy")
#
#
# # def FilterBetweenDates(self):
# #     start = str(self.startDate.text())
# #     finish = str(self.endDate.text())
# #     filter = "EventDate BETWEEN '{}' AND '{}'".format(start, finish)
# #     print(filter)  # for debugging
# #     self.model.setFilter(filter)
#
