import xlrd
import MySQLdb

RESULTS_SHEET = "Compiled Tests.xlsx"
MATERIALS_SHEET = ""

TEST_RESULT_COLUMNS = ['Capacitance', 'Charge_Count', 'Cycles', 'Pin']
CAPACITOR_COLUMNS = ['Serial_Number']
MATERIAL_COLUMNS = ['Electrolyte', 'Seperator', 'DPI', 'Form_Factor']

DATABASE_CONNS = {
    # DB Name : Credentials
    'CapacitorTests': {
        'db': 'CapacitorTests',
        'host':'localhost',
        'user':'root',
        'password':"",
    }
}

class DatabaseInsert:
    """Insert excel sheet data into database"""
    def __init__(self, workbook, database):
        self.workbook = workbook
        self.database = database
        self.workbook = xlrd.open_workbook(workbook)
        self.SHEETS = []
        [self.SHEETS.append(self.workbook.sheet_by_name(str(i))) for i in self.workbook.sheet_names()]

    # Establish connection to databse and enable the cursor, which will
    # walk line by line through the DB and assign values
    def connect_to_db(self):
        host, passwd, db, user = self.database.values()
        self.db_connection = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
        self.cursor = self.db_connection.cursor()
        # get names of columns from the database
        #num_fields = len(cursor.description)
        #field_names = [i[0] for i in cursor.description]
        #print(field_names)
        #return field_names


    # This function needs to be changed on a per sheet basis until
    # excel sheet headers are updated
    def insert_to_database(self, table, columns, query):
        self.connect_to_db()
        #column_names = self.connect_to_db()
        values = {}

        for sheet in self.SHEETS[1:]:
            values['Date_Tested'] = self.SHEETS.index(sheet)
            for column in range(0, sheet.ncols)[::3][:-1]:
                values['Serial_Number'] = sheet.cell(0,column).value
                values['Pin'] = str(sheet.cell(1, column).value)
                for row in range(2, sheet.nrows):
                    values["Capacitance"] = sheet.cell(row, column).value
                    values["Charge_Count"] = sheet.cell(row, column + 1).value
                    values["Cycles"] = sheet.cell(row, column + 2).value
                    db_columns = []
                    for key in values.keys():
                        if key in columns:
                            db_columns.append(values[key])

                    self.cursor.execute(query, tuple(db_columns))

        self.cursor.close()
        self.db_connection.commit()
        self.db_connection.close()
        print 'Wrote %s Rows to %s Columns for Table %s' % (sheet.nrows, sheet.ncols, table)

#query = """INSERT INTO {0} {1} VALUES {2}""".format(table, tuple(db_columns), tuple(values.values()))

results = DatabaseInsert(RESULTS_SHEET, DATABASE_CONNS['CapacitorTests'])

results.insert_to_database('TestResults', TEST_RESULT_COLUMNS, \
                """INSERT INTO TestResults (Pin, Charge_Count, Capacitance, Cycles) VALUES (%s, %s, %s, %s)""")

results.insert_to_database('Capacitor', CAPACITOR_COLUMNS, """INSERT INTO Capacitor (Serial_Number) VALUES (%s)""")

#results.insert_to_database('Materials', MATERIAL_COLUMNS)
