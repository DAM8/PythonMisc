import xlrd

loc =("C:\Govi\Python\productivity.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
print(sheet.cell_value(0,0))