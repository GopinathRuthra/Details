from flask import Flask, render_template, request
import sqlite3

app=Flask(__name__)

@app.route('/')
@app.route('/index')

def homepage():
    return render_template('index.html')

@app.route('/display', methods=['POST','GET'])
def index():
    rows = list()
    if request.method=="POST":
        a=request.form.get('GID')
        b=request.form.get('Emp_Name')
        c=request.form.get('CCName')
        d=request.form.get('CCID')
        e=request.form.get('DOJ')
        f=request.form.get('W_Email')
        g=request.form.get('Manager')
        h=request.form.get('Band_Change_Date')
        i=request.form.get('Lead')
        j=request.form.get('AGM_VP')
        k=request.form.get('Job_Role')
        l=request.form.get('T_Name')
        m=request.form.get('SPOC')
        n=request.form.get('Core_Process')
        o=request.form.get('Sub_process')
        p=request.form.get('Higher_Qualification')
        q=request.form.get('DOB')
        r=request.form.get('Work_Location')
        s=request.form.get('P_Team')
        t=request.form.get('Vaccine_Action_Plan')
        u=request.form.get('Vaccinated_Status')
        v=request.form.get('Vaccination_Certificate_Uploaded')
        w=request.form.get('Accomodation')
        x=request.form.get('Personal_Email')
        y=request.form.get('Insurance')
        z=request.form.get('ECName')
        a1=request.form.get('ECNumber')
        b1=request.form.get('Mob')
        c1=request.form.get('Marital')
        d1=request.form.get('Transport')
        e1=request.form.get('Distance')
        f1=request.form.get('Pickup')
        g1=request.form.get('Address')
        h1=request.form.get('City_Pin')
        i1=request.form.get('Native_District')
        j1=request.form.get('Native_State')
        k1=request.form.get('Type_of_Asset')
        l1=request.form.get('CPU_Laptop')
        m1=request.form.get('Docking_Station')
        n1=request.form.get('Monitor_1')
        o1=request.form.get('Monitor_2')
        p1=request.form.get('Desk_No')
        q1=request.form.get('Dual_Moniter_SetUp')
        r1=request.form.get('Internet_availability')
        s1=request.form.get('Head_Phone_availability')
        t1=request.form.get('Additional_Key_Board')
        u1=request.form.get('Mouse')
        v1=request.form.get('UPS')
        w1=request.form.get('Proper_Table_availability')
        x1=request.form.get('Proper_Chair_availability')
        y1=request.form.get('Spike_Buster')

        try:  
            with sqlite3.connect("Emp_Asset.db") as con:
                print("Connected")    
                cur = con.cursor()  
                print("Got cursor")  
                cur.execute("INSERT into Details (GID, Emp_Name, Band, CCName, CCID, DOJ, W_Email, Manager, Band_Change_Date, Lead, AGM_VP, Job_Role, T_Name, SPOC, Core_Process, Sub_process, Higher_Qualification, GENDER, DOB, Work_Location, P_Team, Vaccine_Action_Plan, Vaccinated_Status, Vaccination_Certificate_Uploaded, Accomodation, Personal_Email, Insurance, ECName, ECNumber, Mob, Marital, Transport, Distance, Pickup, Address, City_Pin, Native_District, Native_State, Type_of_Asset, CPU_Laptop, Docking_Station, Monitor_1, Monitor_2, Desk_No, Dual_Moniter_SetUp, Internet_availability, Head_Phone_availability, Additional_Key_Board, Mouse, UPS, Proper_Table_availability, Proper_Chair_availability, Spike_Buster) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,a1,b1,c1,d1,e1,f1,g1,h1,i1,j1,k1,l1,m1,n1,o1,p1,q1,r1,s1,t1,u1,v1,w1,x1,y1))  
                print("executed successfully")  
                con.commit()  
                print("Customer successfully Added")  
                
                cur.execute("select * from Details")  
                rows = cur.fetchall()
                print(rows)  
        except Exception as e:   
            con.rollback()
            print(e)  
            print("We can not add the customer to the list" ) 
        finally:  
            
            return render_template("display.html",rows = rows) 
            con.close() 

    if __name__=='__main__':
        app.run(debug=True)