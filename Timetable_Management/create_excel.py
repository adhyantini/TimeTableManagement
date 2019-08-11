#import xlrd
#from xlrd import open_workbook
#from xlutils.copy import copy
#import xlwt
#from xlwt import easyxf


from flask import Flask
from flask import send_file
import openpyxl
from openpyxl import load_workbook,Workbook

def excel_batch(batch_info,shift_info,batch_data):
    Main=[]
    print(batch_info)
    print(shift_info)
    if batch_info == 'FE' and shift_info == '1':
        print('hey this is fe1')
        loc = './excel/FE1.xlsx'
        xfile = openpyxl.load_workbook(loc)
        sheet = xfile.get_sheet_by_name('Sheet1')    
        row=10
        col=1
        for data in batch_data:
            Main.append(data)
        print (Main)
        for entry in Main:
            print(entry)
            sheet.cell(row,col).value=entry
            col=col+1
            if col == 8:
                col = 1
                row = row + 1
                if row == 14:
                    row = row+1

        xfile.save(loc)
        

    elif batch_info == 'FE' and shift_info == '2':
        print('hey this is FE2')
        loc = './excel/FE2.xlsx'
        xfile = openpyxl.load_workbook(loc)
        sheet = xfile.get_sheet_by_name('Sheet1')    
        row=10
        col=1
        for data in batch_data:
            Main.append(data)
        print (Main)
        for entry in Main:
            print(entry)
            sheet.cell(row, col).value=entry
            col=col+1
            if col == 8:
                col = 1
                row = row + 1
                if row == 14:
                    row = row+1
        xfile.save(loc)
        

    elif batch_info == 'SE' and shift_info == '1':
        print('hey this is SE1')
        loc = './excel/SE1.xlsx'
        xfile = openpyxl.load_workbook(loc)
        sheet = xfile.get_sheet_by_name('Sheet1')    
        row=10
        col=1
        for data in batch_data:
            Main.append(data)
        print (Main)
        for entry in Main:
            print(entry)
            sheet.cell(row, col).value=entry
            col=col+1
            if col == 8:
                col = 1
                row = row + 1
                if row == 14:
                    row = row+1
        xfile.save(loc)
        

    elif batch_info == 'SE' and shift_info == '2':
        loc = './excel/SE2.xlsx'
        xfile = openpyxl.load_workbook(loc)
        sheet = xfile.get_sheet_by_name('Sheet1')    
        row=10
        col=1
        for data in batch_data:
            Main.append(data)
        print (Main)
        for entry in Main:
            print(entry)
            sheet.cell(row, col).value=entry
            col=col+1
            if col == 8:
                col = 1
                row = row + 1
                if row == 14:
                    row = row+1
        xfile.save(loc) 
        

    elif batch_info== 'TE' and shift_info == '1':
        loc = './excel/TE1.xlsx'
        xfile = openpyxl.load_workbook(loc)
        sheet = xfile.get_sheet_by_name('Sheet1')    
        row=10
        col=1
        for data in batch_data:
            Main.append(data)
        print (Main)
        for entry in Main:
            print(entry)
            sheet.cell(row, col).value=entry
            col=col+1
            if col == 8:
                col = 1
                row = row + 1
                if row == 14:
                    row = row+1
        xfile.save(loc)
        

    elif batch_info == 'TE' and shift_info == '2':
        loc = './excel/TE2.xlsx'
        xfile = openpyxl.load_workbook(loc)
        sheet = xfile.get_sheet_by_name('Sheet1')    
        row=10
        col=1
        for data in batch_data:
            Main.append(data)
        print (Main)
        for entry in Main:
            print(entry)
            sheet.cell(row, col).value=entry
            col=col+1
            if col == 8:
                col = 1
                row = row + 1
                if row == 14:
                    row = row+1
        xfile.save(loc)
        


    elif batch_info == 'BE' and shift_info == '1':
        loc = './excel/BE1.xlsx'
        xfile = openpyxl.load_workbook(loc)
        sheet = xfile.get_sheet_by_name('Sheet1')    
        row=10
        col=1
        for data in batch_data:
            Main.append(data)
        print (Main)
        for entry in Main:
            print(entry)
            sheet.cell(row, col).value=entry
            col=col+1
            if col == 8:
                col = 1
                row = row + 1
                if row == 14:
                    row = row+1
        xfile.save(loc)
        

    elif batch_info == 'BE' and shift_info == '2':
        loc = './excel/BE2.xlsx'
        xfile = openpyxl.load_workbook(loc)
        sheet = xfile.get_sheet_by_name('Sheet1')    
        row=10
        col=1
        for data in batch_data:
            Main.append(data)
        print (Main)
        for entry in Main:
            print(entry)
            sheet.cell(row, col).value=entry
            col=col+1
            if col == 8:
                col = 1
                row = row + 1
                if row == 14:
                    row = row+1
        xfile.save(loc)
        

    elif batch_info == 'ME' and shift_info == '1':
        loc = './excel/ME1.xlsx'
        xfile = openpyxl.load_workbook(loc)
        sheet = xfile.get_sheet_by_name('Sheet1')    
        row=10
        col=1
        for data in batch_data:
            Main.append(data)
        print (Main)
        for entry in Main:
            print(entry)
            sheet.cell(row, col).value=entry
            col=col+1
            if col == 8:
                col = 1
                row = row + 1
                if row == 14:
                    row = row+1
        xfile.save(loc)
        

    elif batch_info == 'ME' and shift_info == '2':
        loc = './excel/ME2.xlsx'
        xfile = openpyxl.load_workbook(loc)
        sheet = xfile.get_sheet_by_name('Sheet1')    
        row=10
        col=1
        for data in batch_data:
            Main.append(data)
        print (Main)
        for entry in Main:
            print(entry)
            sheet.cell(row, col).value=entry
            col=col+1
            if col == 8:
                col = 1
                row = row + 1
                if row == 14:
                    row = row+1
        xfile.save(loc)
        
    return loc

def excel_location(location_info):
    Main=[]
    loc = './excel/Location.xlsx'
    xfile = openpyxl.load_workbook(loc)
    sheet = xfile.get_sheet_by_name('Sheet1')    
    row=10
    col=1
    for data in location_info:
        Main.append(data)
    print (Main)
    for entry in Main:
        print(entry)
        sheet.cell(row, col).value=entry
        col=col+1
        if col == 8:
            col = 1
            row = row + 1
            if row == 14:
                row = row+1

    xfile.save(loc)
    return loc

def excel_teacher(teacher_info):
    Main=[]
    loc = './excel/Teacher.xlsx'
    xfile = openpyxl.load_workbook(loc)
    sheet = xfile.get_sheet_by_name('Sheet1')    
    row=10
    col=1
    for data in teacher_info:
        Main.append(data)
    print (Main)
    for entry in Main:
        print(entry)
        sheet.cell(row, col).value=entry
        col=col+1
        if col == 8:
            col = 1
            row = row + 1
            if row == 14:
                row = row+1

    xfile.save(loc)
    return loc

def excel_master(master_info):
    Main=[]
    loc = './excel/Master.xlsx'
    xfile = openpyxl.load_workbook(loc)
    sheet = xfile.get_sheet_by_name('Sheet1')    
    row=9
    col=2
    for data in master_info:
        Main.append(data)
    print (Main)
    for entry in Main:
        print(entry)
        sheet.cell(row, col).value=entry
        col=col+1
        if col == 18:
            col = 2
            row = row + 1
    xfile.save(loc)
    return loc



























'''  from flask import Flask
from flask import send_file
app = Flask(__name__)

@app.route('/download')
def downloadFile ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "/Examples.pdf"
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(port=5000,debug=True) '''




