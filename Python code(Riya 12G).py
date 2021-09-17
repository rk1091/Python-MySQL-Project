#FEW FUNCTIONS FOR CODE-
    
    
def bo():

    while True:
        
        import mysql.connector
        r=input("enter FNO (Flight Number)")
        db=mysql.connector.connect(host='localhost',user='root',password='1234',
        database='airsys')
        cursor=db.cursor()
        Query1=("select * from flights where FNO='%s'" %(r))
        cursor.execute(Query1)
        res=cursor.fetchall()
        
        if not res:
            print("No such flight exists")
            cursor.close()
            
        else:
            print("Enter passenger details:")
            s=input("enter your name")
            
            while True:
                t=int(input("enter your age"))
                if t>100 or t<=0:
                    print(" Enter age 0 to 100")
                else:
                    break

            while True:        
                u=input("enter your gender: (F/M)")
                if  not (u=="F" or u=="M"):
                    print("Enter only F or M")
                else:
                    break
            
            print("This is your booking:","FNO:",r,"PASSENGER_NAME:",s,"AGE:",t,"GENDER:",u,end='\n')
            o=input("Are you sure you want to confirm this booking? (Y/N)")

            if o!="Y":
                break
            
            else:
                
                cursor.execute("select max(bno) from bookings;")
                result=cursor.fetchall()
                
                for i in result:
                    tbno=int(i[0])
                    
                l=tbno+1
                Query=("insert into bookings(BNO,FNO,PASSENGER_NAME,AGE,GENDER) values(%s,%s,%s,%s,%s)")
                data=(l,r,s,t,u)
                cursor.execute(Query,data)
                db.commit()
                print("Your booking has been confirmed.\n")
                print("This is your booking:","YOUR BOOKING NO.",l,"FNO:",r,"PASSENGER_NAME:",s,"AGE:",t,"GENDER:",u,end='\n')
                cursor.close()

                break


def plotter():
    
    import mysql.connector
    import matplotlib.pyplot as plt
    db=mysql.connector.connect(host='localhost',user='root',password='1234',
    database='airsys')
    cursor=db.cursor()
    Query1=("select fare from flights")
    cursor.execute(Query1)
    res=cursor.fetchall()

    a=[]
    for i in res:
        a.append(i[0])

    Query2=("select destination from flights")
    cursor.execute(Query2)
    rees=cursor.fetchall()

    b=[]
    for j in rees:
        b.append(j[0])

    plt.bar(b,a,width=0.25,color=["m","turquoise","orange","g","r","cyan"])
    plt.title("Fare Vs Destination",color="purple")
    plt.ylabel("Fare",color="purple")
    plt.xlabel("Destination",color="purple")
    plt.plot(a,c='purple',ls="--")
    plt.show()
        

            
def af():

    import mysql.connector
    db=mysql.connector.connect(host='localhost',user='root',password='1234',
    database='airsys')
    cursor=db.cursor()
    cursor.execute("select * from flights")
    result=cursor.fetchall()

    print("{0:10}{1:12}{2:14}{3:15}{4:7}{5:13}{6:12}".format("===","========","======","===========","====","===========","===========")) 
    print("{0:10}{1:12}{2:14}{3:15}{4:7}{5:13}{6:12}".format("FNO","AIRLINES","SOURCE","DESTINATION","FARE","FLIGHT_DATE","FLIGHT_TIME"))
    print("{0:10}{1:12}{2:14}{3:15}{4:7}{5:13}{6:12}".format("===","========","======","===========","====","===========","==========="))
    
    for x in result:

        print ("{0:10}{1:12}{2:14}{3:13}{4:6}".format(x[0],x[1],x[2],x[3],x[4])," ",x[5]," ",x[6])

    cursor.close()

    
def anf():

    import mysql.connector

    h=input("enter flight number")
    db=mysql.connector.connect(host='localhost',user='root',password='1234',
    database='airsys')
    cursor=db.cursor()
    Query1=("select * from flights where FNO='%s'" %(h))
    cursor.execute(Query1)
    res=cursor.fetchall()
    
    if not res:

        a=input("enter name of airlines ")
        b=input("enter source")
        c=input("enter destination")
        e=int(input("enter flight fare "))
        f=input("enter flight date (YYYY-MM-DD)")
        g=input("enter flight time (HH:MM:SS)")
        Query=("insert into flights(FNO,AIRLINES,SOURCE,DESTINATION,FARE,FLIGHT_DATE,FLIGHT_TIME) values(%s,%s,%s,%s,%s,%s,%s)")
        data=(h,a,b,c,e,f,g)
        cursor.execute(Query,data)
        db.commit()

        print("New Flight number '%s' has been successfully added." %(h))

        cursor.close()
        
    else:    

        print("No such flight exists")
        cursor.close()

    
def ef():

    import mysql.connector
    r=input("enter flight number")        
    db=mysql.connector.connect(host='localhost',user='root',password='1234',
    database='airsys')
    cursor=db.cursor()
    Query1=("select * from flights where FNO='%s'" %(r))
    cursor.execute(Query1)
    res=cursor.fetchall()
    
    if not res:

        print("No such flight exists")

        cursor.close()

    else:

        print("MENU OF FIELDS","\n","1.AIRLINES","\n","2.SOURCE","\n","3.DESTINATION","\n","4.FARE","\n","5.FLIGHT_DATE","\n","6.FLIGHT_TIME")
        m=int(input("Enter your choice of field which you wish to update:"))
        o={1:'AIRLINES',2:'SOURCE',3:'DESTINATION',4:'FARE',5:'FLIGHT_DATE',6:'FLIGHT_TIME'}
        q=o.get(m)
        n=input("Enter new value:")
        
        Query=("update flights set %s='%s' where FNO='%s'"%(q,n,r))
        cursor.execute(Query)
        db.commit()

        print("\nFor flight number '%s', '%s' has been successfully updated to '%s'."%(r,q,n))

        cursor.close()

        
def df():

    import mysql.connector

    r=input("enter flight number")
    db=mysql.connector.connect(host='localhost',user='root',password='1234',database='airsys')
    cursor=db.cursor()
    Query1=("select * from flights where FNO='%s'" %(r))
    cursor.execute(Query1)
    res=cursor.fetchall()

    if not res:

        print("No such flight exists")
        

    else:
        query2=("select count(*) from bookings where FNO='%s'" %(r))
        cursor.execute(query2)
        rs=cursor.fetchall()

        if (rs[0][0])>0:
            
            print("This flight can not be deleted because a booking already exists.")

        else:

            Query=("delete from flights where FNO='%s'" %(r))
            cursor.execute(Query)
            db.commit()

            print("Flight number '%s' has been successfully deleted."%(r))

            cursor.close()

        
def vb():

    import mysql.connector

    db=mysql.connector.connect(host='localhost',user='root',password='1234',
    database='airsys')
    cursor=db.cursor()
    cursor.execute(" select BOOKINGS.FNO,BNO,PASSENGER_NAME,GENDER,AGE,AIRLINES,SOURCE,DESTINATION,FARE,FLIGHT_DATE,FLIGHT_TIME from FLIGHTS,BOOKINGs where FLIGHTS.FNO=BOOKINGS.FNO")
    reesult=cursor.fetchall()

    print("{0:10}{1:10}{2:15}{3:8}{4:5}{5:12}{6:14}{7:15}  {8:8} {9:13}{10:13}".format("===","===","==============","=====","===","=========","=====","============"," ====","===========","==========="))
    print("{0:10}{1:10}{2:15}{3:8}{4:5}{5:12}{6:14}{7:15}  {8:8} {9:13}{10:13}".format("FNO","BNO","PASSENGER_NAME","GENDER","AGE","AIRLINES","SOURCE","DESTINATION"," FARE","FLIGHT_DATE","FLIGHT_TIME"))
    print("{0:10}{1:10}{2:15}{3:8}{4:5}{5:12}{6:14}{7:15}  {8:8} {9:13}{10:13}".format("===","===","==============","=====","===","=========","=====","============"," ====","===========","==========="))

    for xx in reesult:
         age=xx[4]
         fare=xx[8]

         print("{0:10}{1:10}{2:15}{3:6}{4:5}  {5:12}{6:14}{7:15}{8:8}".format(xx[0],xx[1],xx[2],xx[3],age,xx[5],xx[6],xx[7],fare)," ",xx[9]," ",xx[10])

    cursor.close()

    
#MAIN CODE-

import getpass


while True:
    
    print("****************************** \nWELCOME TO OUR AIRLINE SYSTEM \n******************************","\n")
    
    a=input("Are you a Customer or an Admin?(C/A)")

    if a=="C":

        print("\n Welcome Customer!","\n")
        
        while True:

            try:

                print("--------------------------------\nCustomer Menu:\n-------------------------------- \n 1.Available flights","\n","2.Fare vs Destination plot","\n","3.Book a flight","\n","4.Exit from Customer Menu","\n","5.Exit from Airline System","\n")

                b=int(input("Enter your choice: (1/2/3/4/5)\n"))

                if b==1:
                    af()
                elif b==2:
                    plotter()
                elif b==3:
                    bo()
                elif b==4:
                    break
                elif b==5:
                    print("Goodbye")
                    quit()
                else:
                    print("Enter a number between 1 to 5 only")                                    

            except(ValueError,TypeError,NameError):
                print("Enter correct values")

    elif a=="A":

        while True:
            pwrd=input("enter password")

            if pwrd=="rk91":
                print("\n","Welcome Administrator!","\n")
                
                while True:

                    try:

                        print("-----------------------------------\nAdmin Menu: \n----------------------------------- \n 1.Available flights","\n","2.Fare vs Destination plot","\n","3.Add a new flight","\n","4.Edit a flight","\n","5.Delete a flight","\n","6.View all bookings","\n","7.Exit from Admin Menu","\n","8.Exit from Airline System","\n")
                        c=int(input("Enter your choice: (1/2/3/4/5/6/7/8) \n"))

                        if c==1:
                            af()
                        elif c==2:
                            plotter()
                        elif c==3:
                            anf()
                        elif c==4:
                            ef()
                        elif c==5:
                            df()
                        elif c==6:
                            vb()
                        elif c==7:
                            break
                        elif c==8:
                            print("Goodbye")
                            quit()
                        else:
                            print("Enter a number between 1 to 8 only")                                            

                    except(ValueError,TypeError,NameError):
                        print("enter correct values")
                break

            else:
                print("Incorrect password.","\n")       

    else:
        print("Enter only A or C")
