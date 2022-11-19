from openpyxl import load_workbook

wb = load_workbook(filename="c++ attendance.xlsx")

sheet = wb.active

nlist = input("Enter N Absenties : ").split()
llist = input("Enter L Absenties : ").split()

n= ['21L31A54'+i for i in nlist]
l= ['22L35A54'+i for i in llist]

for i in range(2,74):
    roll='B'+str(i)
    atnd='G'+str(i)
    if (sheet[roll].value in n) or (sheet[roll].value in l):
        sheet[atnd]= 0
    else:
        sheet[atnd]= 1 


    
wb.save(filename="c++ attendance.xlsx")