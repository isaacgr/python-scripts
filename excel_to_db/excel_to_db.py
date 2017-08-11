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
        'host':'localhost',
        'user':'root',
        'password':'',
    }
}

class DatabaseInsert():
    """Insert excel sheet data into database"""
    def __init__(self, workbook, database, connection):
        self.workbook = workbook
        self.database = database
        self.connection = connection
        self.workbook = xlrd.open_workbook(workbook)
        SHEETS = []
        [SHEETS.append(workbook.sheet_by_name(str(i))) for i in workbook.sheet_names()]


    def connect_to_db(self):
        db, host, user, passwd = self.connection
        db_connection = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)









cursor = database.cursor()

testResultsQuery = """INSERT INTO TestResults (Capacitance, Charge_Count, Cycles, PIN)
                        VALUES (%s, %s, %s, %s)"""
capacitorQuery = """INSERT INTO Capacitor (Serial_Number) VALUES (%s)"""
#materialsQuery = """INSERT INTO TestResults (Electrolyte, Seperator, DPI, Form_Factor)"""

for sheet in TEST_SHEETS[1:]:
    #Date_Tested = sheet
    for column in range(0, sheet.ncols)[::3][:-1]:
        Serial_Number = sheet.cell(0,column).value
        PIN = sheet.cell(1, column).value

        for row in range(2, sheet.nrows):
            Capacitance = sheet.cell(row, column).value
            Charge_Count = sheet.cell(row, column + 1).value
            Cycles = sheet.cell(row, column + 2).value

            testResultsValues = (Capacitance, Charge_Count, Cycles, PIN,)
            capacitorValues = (Serial_Number,)

            cursor.execute(testResultsQuery, testResultsValues)
            cursor.execute(capacitorQuery, capacitorValues)

cursor.close()

database.commit()

database.close()

print ""
print "All Done! Bye, for now."
print ""
columns = str(sheet.ncols)
rows = str(sheet.nrows)
#print "I just imported " %columns %2B " columns and " %2B rows %2B " rows to CapacitorTests!"
