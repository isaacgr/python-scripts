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


    def get_database_columns(self):
        num_fields = len(self.cursor.description)
        field_names = [i[0] for i in self.cursor.description]
        return field_names


    # This function needs to be changed on a per sheet basis until
    # excel sheet headers are updated
    def insert_to_database(self, table, columns, column_names):
        columns = tuple(columns)
        column_names = get_database_columns()
        query = "INSERT INTO" + " " + table + " " + columns + " VALUES" + " " + values
        values = {}
        db_values = []

        for sheet in self.SHEETS[1:]:
            values['Date_Tested'] = self.SHEETS.index(sheet)
            for column in range(0, sheet.ncols)[::3][:-1]:
                values['Serial_Number'] = sheet.cell(0,column).value
                values['PIN'] = sheet.cell(1, column).value
                for row in range(2, sheet.nrows):
                    values['Capacitance'] = sheet.cell(row, column).value
                    values['Charge_Count'] = sheet.cell(row, column + 1).value
                    values['Cycles'] = sheet.cell(row, column + 2).value
                    for key in values.keys():
                        for column in columns:
                            if column == key:
                                db_values.append(values[key])
                                self.cursor.execute(query, tuple(db_values))

        print 'Wrote %s Rows to %s Columns' % (self.sheet.nrows, self.sheet.ncols)


results = DatabaseInsert(RESULTS_SHEET, DATABASE_CONNS['CapacitorTests'])
results.insert_to_database('TestResults', TEST_RESULT_COLUMNS)
results.insert_to_database('Capacitor', CAPACITOR_COLUMNS)
#results.insert_to_database('Materials', MATERIAL_COLUMNS)

cursor.close()
database.commit()
database.close()
