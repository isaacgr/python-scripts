import xlrd
import MySQLdb
import json
RESULTS_SHEET = "Compiled Tests.xlsx"
MATERIALS_SHEET = ""

class JsonConversion:
    """Convert excel sheet data into JSON
        formatted file"""
    def __init__(self, workbook):
        self.workbook = workbook
        self.workbook = xlrd.open_workbook(workbook)
        self.sheet_obj = []
        self.sheet_names = self.workbook.sheet_names()
        [self.sheet_obj.append(self.workbook.sheet_by_name(str(i))) for i in self.workbook.sheet_names()]

    # TODO: Format excel sheets so this can be made to be more generic
    def convert_results_to_json(self):
        results = {}
        values = {}
        results['capacitor'] = []

        values['Capacitance'] = []
        values['Charge_Count'] = []
        values['Cycles'] = []
        values['Pin'] = []


        # loop through spreadsheet and get the results from the columns and rows
        for sheet in self.sheet_obj[1:]:
            values['Date_Tested'] = self.workbook.sheet_names()[self.sheet_obj.index(sheet)]
            for column in range(0, sheet.ncols)[::3][:-1]:
                values['Serial_Number'] = sheet.cell(0,column).value
                # restart loop if there is no serial number
                if values['Serial_Number'] == '':
                    continue
                # pin almost as unique as serial, since only one cap on one pin at a time
                values['Pin'] = str(sheet.cell(1, column).value)
                for row in range(2, sheet.nrows):
                    values['Capacitance'].append(sheet.cell(row, column).value)
                    values['Charge_Count'].append(sheet.cell(row, column + 1).value)
                    values['Cycles'].append(sheet.cell(row, column + 2).value)

                if values['Serial_Number'] in values.values():
                    serial = values['Serial_Number']
                    handle_duplicate_serial_number(serial, values)
                    continue

                serial_number = values['Serial_Number']

                results['results'].append({

                    serial_number: [{

                        'Date_Tested':values['Date_Tested'],
                        'Capacitance':values['Capacitance'],
                        'Charge_Count':values['Charge_Count'],
                        'Cycles':values['Cycles'],
                        'Pin':values['Pin'],

                    }]
                })


    def handle_duplicate_serial_number(serial, values):

        results['results'][serial].append({

            'Date_Tested':values['Date_Tested'],
            'Capacitance':values['Capacitance'],
            'Charge_Count':values['Charge_Count'],
            'Cycles':values['Cycles'],
            'Pin':values['Pin'],

        })


        print 'Wrote %s Rows from %s Columns (%s lines)' % (sheet.nrows, sheet.ncols, (sheet.nrows*sheet.ncols))
