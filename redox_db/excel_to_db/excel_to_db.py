import xlrd
import MySQLdb

RESULTS_SHEET = "Compiled Tests.xlsx"
MATERIALS_SHEET = ""
# columns that exist in the database tables
TEST_RESULT_COLUMNS = ['Serial_Number','Capacitance', 'Charge_Count', 'Cycles', 'Pin', 'Date_Tested']
MATERIAL_COLUMNS = ['Serial_Number', 'Electrolyte', 'Seperator', 'DPI', 'Form_Factor']
# connections to various databases if needed
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
        self.sheet_obj = []
        self.sheet_names = self.workbook.sheet_names()
        [self.sheet_obj.append(self.workbook.sheet_by_name(str(i))) for i in self.workbook.sheet_names()]

    # Establish connection to databse and enable the cursor, which will
    # walk line by line through the DB and assign values
    def connect_to_db(self):
        host, passwd, db, user = self.database.values()
        self.db_connection = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
        self.cursor = self.db_connection.cursor()
    # This function needs to be changed on a per sheet basis until
    # excel sheet headers are updated
    def insert_results_to_database(self, table, columns, query):
        self.connect_to_db()
        values = {}
        # loop through spreadsheet and get the values from the columns and rows
        for sheet in self.sheet_obj[1:]:
            values['Date_Tested'] = self.workbook.sheet_names()[self.sheet_obj.index(sheet)]
            for column in range(0, sheet.ncols)[::3][:-1]:
                values['Serial_Number'] = sheet.cell(0,column).value
                # restart loop if there is no serial number
                if values['Serial_Number'] == '':
                    continue

                values['Pin'] = str(sheet.cell(1, column).value)
                for row in range(2, sheet.nrows):
                    values["Capacitance"] = sheet.cell(row, column).value
                    values["Charge_Count"] = sheet.cell(row, column + 1).value
                    values["Cycles"] = sheet.cell(row, column + 2).value
                    db_columns = []
                    for key in values.keys():
                        if key in columns:
                            db_columns.append(values[key])
                    # write values to the db
                    self.cursor.execute(query, tuple(db_columns))
        # commit the changes and close the db connection
        self.cursor.close()
        self.db_connection.commit()
        self.db_connection.close()
        print 'Wrote %s Rows to %s Columns for Table %s' % (sheet.nrows, sheet.ncols, table)

results = DatabaseInsert(RESULTS_SHEET, DATABASE_CONNS['CapacitorTests'])

results.insert_results_to_database('TestResults', TEST_RESULT_COLUMNS, \
                """INSERT INTO TestResults (Pin, Date_Tested, Charge_Count, Capacitance, Serial_Number, Cycles) \
                    VALUES (%s, %s, %s, %s, %s, %s)""")

#materials = DatabaseInsert(MATERIALS_SHEET, DATABASE_CONNS['CapacitorTests'])
#results.insert_materials_to_database('Materials', MATERIAL_COLUMNS)
