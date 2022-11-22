import streamlit as st
from openpyxl import load_workbook
import pandas as pd
import asyncio
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

def main():
    st.title("Attendance")
    path = str(st.text_input("Enter path of Excel file : "))
    path = path.replace('"','')

    df = pd.read_excel(path)
    wb = load_workbook(path)

    sheet = wb.active

    day = int(st.text_input("Enter day \"ex : if day-1 then enter 1\": "))
    index = chr(day+67)
    head = index+'1'
    sheet[head]='Day-'+str(day)
    nlist = str(st.text_input("Enter N Absenties : ")).split()
    llist = str(st.text_input("Enter L Absenties : ")).split()

    n= ['21L31A54'+i for i in nlist]
    l= ['22L35A54'+i for i in llist]

    for i in range(2,74):
        roll='B'+str(i)
        atnd=index+str(i)
        if (sheet[roll].value in n) or (sheet[roll].value in l):
            sheet[atnd]= 0
        else:
            sheet[atnd]= 1 

    st.write(filtered_df)
    wb.save(filename="sample.xlsx")

if __name__=='__main__':
    main()