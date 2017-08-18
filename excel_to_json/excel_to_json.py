import xlrd
import MySQLdb
import json
from collections import OrderedDict
import sys

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
        # initialize results
        self.results = OrderedDict()
        self.results = {
            'capacitor': []
        }
        # initialize values
        values = {
            'Date_Tested': '',
            'Serial_Number': '',
            'Pin': '',
            'Capacitance': [],
            'Charge_Count': [],
            'Cycles': [],
        }

        serial_number_list = []

        # loop through spreadsheet and get the results from the columns and rows
        for sheet in self.sheet_obj[1:]:
            values['Date_Tested'] = self.workbook.sheet_names()[self.sheet_obj.index(sheet)]

            for column in range(0, sheet.ncols)[::3][:-1]:
                values['Serial_Number'] = str(sheet.cell(0,column).value)
                values['Pin'] = str(sheet.cell(1, column).value)
                # restart loop if there is no serial number
                if values['Serial_Number'] == '':
                    continue
                # reinitialize these to empty list, else they will just keep appending
                values['Capacitance'] = []
                values['Charge_Count']=[]
                values['Cycles'] = []

                for row in range(2, sheet.nrows):
                    values['Capacitance'].append(sheet.cell(row, column).value)
                    values['Charge_Count'].append(sheet.cell(row, column + 1).value)
                    values['Cycles'].append(sheet.cell(row, column + 2).value)

                # append to a serial numbers results if it shows in more than one sheet
                if values['Serial_Number'] in serial_number_list:
                    serial = values['Serial_Number']
                    results = self.results['capacitor']
                    self.handle_duplicate_serial_number(results, serial, values)
                    continue

                serial_number = values['Serial_Number']
                date_tested = values['Date_Tested']
                serial_number_list.append(values['Serial_Number'])

                self.results['capacitor'].append({

                    serial_number: [{

                        date_tested: {

                            'Capacitance':values['Capacitance'],
                            'Charge_Count':values['Charge_Count'],
                            'Cycles':values['Cycles'],
                            'Pin':values['Pin'],
                        }
                    }]
                })


    def handle_duplicate_serial_number(self, results, serial, values):
        # loop through json to find the serial number and append to it
        for result in results:
            if serial in result.keys():

                result[serial].append({

                    values['Date_Tested']: {

                        'Capacitance':values['Capacitance'],
                        'Charge_Count':values['Charge_Count'],
                        'Cycles':values['Cycles'],
                        'Pin':values['Pin'],

                    }
                })


    def write_file(self):
        with open('test_results.json', 'w') as outfile:
            json.dump(self.results, outfile, indent=4)


test_results = JsonConversion(RESULTS_SHEET)
test_results.convert_results_to_json()
test_results.write_file()
