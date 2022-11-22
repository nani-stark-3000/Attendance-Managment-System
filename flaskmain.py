from flask import Flask,render_template,request,make_response
from openpyxl import load_workbook
app = Flask(__name__,template_folder='template')

@app.route('/nn', methods=['POST','GET'])

def index_home():
    if request.method=='POST':
        link = request.form['file']
        link = link.replace('"','')
        wb = load_workbook(link)
        sheet = wb.active
        day = request.form['day']
        index = chr(int(day)+67)
        head = index+'1'
        sheet[head]='Day-'+str(day)
        nlist = request.form['nlist'].split()
        llist = request.form['llist'].split()

        n= ['21L31A54'+i for i in nlist]
        l= ['22L35A54'+i for i in llist]

        for i in range(2,74):
            roll='B'+str(i)
            atnd=index+str(i)
            if (sheet[roll].value in n) or (sheet[roll].value in l):
                sheet[atnd]= 0
            else:
                sheet[atnd]= 1 
        wb.save(link)
        return render_template('new.html',sheet=sheet)
    return render_template('new.html')
    

if __name__ == "__main__":
    app.run(debug=True,port=47)