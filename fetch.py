from flask import Flask,render_template
from flask_mysqldb import MySQL
from prettytable import PrettyTable
app = Flask(__name__)
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'SampleDB'
mysql = MySQL(app)
@app.route('/')
def Home():
    ipf=[]
    routerdetails=[]
    z=1
    while z<5:
        cur = mysql.connection.cursor()
        cur.execute(f"SELECT * FROM router{z}info")
        fetchdata = cur.fetchall()
        cur.close()
        ipf.append(fetchdata[0][4])
        routerdetails.append(fetchdata)
        z=z+1;
    #ipchecker
    n=len(ipf)
    r=0
    val=[]
    while r<n:
        ip=ipf[r]
        a=ip.split('.')
        if ( (len(a)==4) and ( 1<=int(a[0])<=223) and (int(a[0])!=127) and (int(a[0])!=169 or int (a[1])!=254) and (0<= int(a[1])<=255) and (0<=int(a[2]) <=255) and (0<=int(a[3])<=255)):            
            val.append(True)
        else: 
            val.append(False)
        r=r+1;
    n1=len(val)
    r1=0
    val1=[]
    while r1<n1:
            ip=ipf[r1]
            if val[r1] == True:     
                val1.append(ip)
            else:   
                continue
            r1=r1+1;    
    N=0;
    try:
        H =len(val1)
        x = PrettyTable()
        x.field_names = ["Valid IP list"]
        while N<H:
            x.add_row([val1[N]])
            N=N+1;
        print(x)
    except:
        print(-1)
    with open("validetails.csv", 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(routerdetails)
    return f"Valid IP list after checking: {val1}"
if __name__ == "__main__":
    appdebug = True
    app.run(host='192.168.132.132',port=5000)
