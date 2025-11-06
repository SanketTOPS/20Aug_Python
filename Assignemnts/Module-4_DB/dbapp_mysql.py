import pymysql

try:
    db=pymysql.connect(host='localhost',user='root',password='',database='newpydb')
    print("Database Connected!")
except Exception as e:
    print(e)
    
    
cr=db.cursor()
#Table Create
tbl_create="create table studinfo(id integer primary key auto_increment,name varchar(20),city varchar(20))"
try:
    cr.execute(tbl_create)
    print("Table created!")
except Exception as e:
    print(e)
    
#Insert Data
"""insert_data="insert into studinfo(name,city)values('sanket','rajkot'),('nirav','baroda'),('ajay','surat'),('hitesh','jamnagar'),('ashok','bhavnagar')"
try:
    cr.execute(insert_data)
    db.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""
    

#Update Data
"""update_data="update studinfo set name='prasiddh',city='ahmedabad' where id=3"
try:
    cr.execute(update_data)
    db.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""
    
#Delete Data
"""delete_data="delete from studinfo where id=3"
try:
    cr.execute(delete_data)
    db.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""
    
#Show Data
show_data="select * from studinfo"
try:
    cr.execute(show_data)
    data=cr.fetchall()
    #data=cr.fetchmany(3)
    #data=cr.fetchone()
    #print(data)
    
    for i in data:
        print(i[2])
except Exception as e:
    print(e)