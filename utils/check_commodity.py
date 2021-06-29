import xlrd

filename = '安庆标注名.xlsx'
items = [{'code': '6957575500015', 'number': 1}]

x1 = xlrd.open_workbook(filename)
sheet1 = x1.sheet_by_name("Sheet1")

weights = 0
for row in range(sheet1.nrows):
    name = str(sheet1.row(row)[1])[6:-1]
    code = str(sheet1.row(row)[3])[6:-1]
    weight = str(sheet1.row(row)[4])[6:-4]
    for item in items:
        if code == item['code']:
            print(name, item['number'])
            weights += int(weight) * int(item['number'])
print('总质量:', weights)
