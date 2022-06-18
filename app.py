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
        c=request.form.get('Band')
        d=request.form.get('CCName')
        e=request.form.get('CCID')
        f=request.form.get('DOJ')
        g=request.form.get('W_Email')
        h=request.form.get('Manager')
        i=request.form.get('Band_Change_Date')
        j=request.form.get('Lead')
        k=request.form.get('AGM_VP')
        l=request.form.get('Job_Role')
        m=request.form.get('T_Name')
        n=request.form.get('SPOC')
        o=request.form.get('Core_Process')
        p=request.form.get('Sub_Process')
        q=request.form.get('Higher_Qualification')
        r=request.form.get('GENDER')
        s=request.form.get('DOB')
        t=request.form.get('Work_Location')
        u=request.form.get('P_Team')
        v=request.form.get('Vaccine_Action_Plan')
        w=request.form.get('Vaccinated_Status')
        x=request.form.get('Vaccination_Certificate_Uploaded')
        y=request.form.get('Accomodation')
        z=request.form.get('Personal_Email')
        a1=request.form.get('Insurance')
        b1=request.form.get('ECName')
        c1=request.form.get('ECNumber')
        d1=request.form.get('Mob')
        e1=request.form.get('Marital')
        f1=request.form.get('Transport')
        g1=request.form.get('Distance')
        h1=request.form.get('Pickup')
        i1=request.form.get('Address')
        j1=request.form.get('City_Pin')        
        k1=request.form.get('Native_State')
        l1=request.form.get('Native_District')
        m1=request.form.get('Type_of_Asset')
        n1=request.form.get('CPU_Laptop')
        o1=request.form.get('Docking_Station')
        p1=request.form.get('Monitor_1')
        q1=request.form.get('Monitor_2')
        r1=request.form.get('Desk_No')
        s1=request.form.get('Dual_Moniter_SetUp')
        t1=request.form.get('Internet_availability')
        u1=request.form.get('Head_Phone_availability')
        v1=request.form.get('Additional_Key_Board')
        w1=request.form.get('Mouse')
        x1=request.form.get('UPS')
        y1=request.form.get('Proper_Table_availability')
        z1=request.form.get('Proper_Chair_availability')
        a2=request.form.get('Spike_Buster')

        try:  
            with sqlite3.connect("Asset.db") as con:
                print("Connected")    
                cur = con.cursor()  
                print("Got cursor")  
                cur.execute("INSERT into Data (GID, Emp_Name, Band, CCName, CCID, DOJ, W_Email, Manager, Band_Change_Date, Lead, AGM_VP, Job_Role, T_Name, SPOC, Core_Process, Sub_process, Higher_Qualification, GENDER, DOB, Work_Location, P_Team, Vaccine_Action_Plan, Vaccinated_Status, Vaccination_Certificate_Uploaded, Accomodation, Personal_Email, Insurance, ECName, ECNumber, Mob, Marital, Transport, Distance, Pickup, Address, City_Pin, Native_District, Native_State, Type_of_Asset, CPU_Laptop, Docking_Station, Monitor_1, Monitor_2, Desk_No, Dual_Moniter_SetUp, Internet_availability, Head_Phone_availability, Additional_Key_Board, Mouse, UPS, Proper_Table_availability, Proper_Chair_availability, Spike_Buster) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,a1,b1,c1,d1,e1,f1,g1,h1,i1,j1,k1,l1,m1,n1,o1,p1,q1,r1,s1,t1,u1,v1,w1,x1,y1,z1,a2))  
                print("executed successfully")  
                con.commit()  
                print("Customer successfully Added")  
                
                cur.execute("select * from Data")  
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
