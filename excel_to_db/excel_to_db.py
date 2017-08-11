import xlrd
import MySQLdb
import re


RESULTS_SHEET = "Compiled Tests.xlsx"
MATERIALS_SHEET = ""

TEST_RESULT_COLUMNS = ['Capacitance', 'Charge_Count', 'Cycles', 'PIN']
CAPACITOR_COLUMNS = ['Serial_Number']
MATERIAL_COLUMNS = ['Electrolyte', 'Seperator', 'DPI', 'Form_Factor']

DATABASE_CONNS = {
    # DB Name : Credentials
    'CapacitorTests': {
        'db': 'CapacitorTests',
        'host':'localhost',
        'user':'root',
        'password':'',
    }
}

class DatabaseInsert:
    """Insert excel sheet data into database"""
    def __init__(self, workbook, database):
        self.workbook = workbook
        self.database = database
        self.connection = connection
        self.workbook = xlrd.open_workbook(workbook)
        SHEETS = []
        [SHEETS.append(workbook.sheet_by_name(str(i))) for i in workbook.sheet_names()]

    # Establish connection to databse and enable the cursor, which will
    # walk line by line through the DB and assign values
    def connect_to_db(self):
        db, host, user, passwd = self.connection.keys()
        db_connection = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
        cursor = db_connection.cursor()

    # Generic INSERT query
    def insert_to_database(self, table, columns):
        columns = tuple(columns)
        values = self.get_values(columns)
        value_strings =
        query = "INSERT INTO" + " " + table + " " + columns + "VALUES" + " " + values
        self.cursor.execute(query, values)
        print 'Wrote %s Rows to %s Columns' % (self.sheet.nrows, self.sheet.ncols)

    # This function needs to be changed on a per sheet basis
    def get_values(self, columns):
        values = []
        for sheet in self.SHEETS[1:]:
            Date_Tested = self.SHEETS.index(sheet)
            for column in range(0, sheet.ncols)[::3][:-1]:
                Serial_Number = sheet.cell(0,column).value
                PIN = sheet.cell(1, column).value

                for row in range(2, sheet.nrows):
                    Capacitance = sheet.cell(row, column).value
                    Charge_Count = sheet.cell(row, column + 1).value
                    Cycles = sheet.cell(row, column + 2).value

                    return tuple(values)


results = DatabaseInsert(RESULTS_SHEET, DATABASE_CONNS['CapacitorTests'])
results.insert_to_database('TestResults', TEST_RESULT_COLUMNS)
results.insert_to_database('Capacitor', CAPACITOR_COLUMNS)
results.insert_to_database('Materials', MATERIAL_COLUMNS)

cursor.close()
database.commit()
database.close()

#testResultsQuery = """INSERT INTO TestResults (Capacitance, Charge_Count, Cycles, PIN)
#                        VALUES (%s, %s, %s, %s)"""
#capacitorQuery = """INSERT INTO Capacitor (Serial_Number) VALUES (%s)"""
#materialsQuery = """INSERT INTO Materials (Electrolyte, Seperator, DPI, Form_Factor)"""
