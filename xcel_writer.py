import xlsxwriter
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()

for i in range(0,20):
    for j in range(i,20):
        worksheet.write(i,j, 'Hello')
workbook.close()