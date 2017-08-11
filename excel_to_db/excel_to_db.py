import xlrd
import MySQLdb
import re


TEST_SHEETS = []
testBook = xlrd.open_workbook("Compiled Tests.xlsx")
[TEST_SHEETS.append(testBook.sheet_by_name(str(i))) for i in testBook.sheet_names()]

database = MySQLdb.connect(host="localhost", user="root", passwd="", db="CapacitorTests")

cursor = database.cursor()

testResultsQuery = """INSERT INTO TestResults (Capacitance, Charge_Count, Cycles, PIN)
                        VALUES (%s, %s, %s, %s)"""
capacitorQuery = """INSERT INTO Capacitor (Serial_Number) VALUES (%s)"""
#materialsQuery = """INSERT INTO TestResults (Electrolyte, Seperator, DPI, Form_Factor)"""

for sheet in TEST_SHEETS[1:]:
    #Date_Tested = sheet

    for column in range(0, sheet.ncols)[::3]:
        Serial_Number = sheet.cell(0,column).value
        PIN = str(sheet.cell(1, column).value)

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
