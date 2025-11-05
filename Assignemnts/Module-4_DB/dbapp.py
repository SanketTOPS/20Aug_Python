import sqlite3

try:
    db=sqlite3.connect("test.db")
    print("Database connected!")
except Exception as e:
    print(e)
    
#Table Create
tbl_create="create table studinfo(id integer primary key autoincrement,name varchar(20),city varchar(20))"

try:
    db.execute(tbl_create)
    print("Table created!")
except Exception as e:
    print(e)

#Insert Data
"""insert_data="insert into studinfo(name,city)values('sanket','rajkot'),('ashok','bhavnagar'),('nirav','surat'),('jaydeep','gondal'),('digvijay','wadhwan')"

try:
    db.execute(insert_data)
    db.commit()
    print("Record Inserted!")
except Exception as e:
    print(e)"""
    
#Update Data
"""update_data="update studinfo set name='mitesh',city='ahmedabad' where id=1"
try:
    db.execute(update_data)
    db.commit()
    print("Record Updated!")
except Exception as e:
    print(e)"""
    
#Delete Data
"""delete_data="delete from studinfo where id=10"
try:
    db.execute(delete_data)
    db.commit()
    print("Record Deleted!")
except Exception as e:
    print(e)"""
    
cr=db.cursor()
#Show Data
show_data="select * from studinfo"
try:
    cr.execute(show_data)
    data=cr.fetchall()
    #data=cr.fetchmany(3)
    #data=cr.fetchone()
    #print(data)
    
    for i in data:
        print(i)
except Exception as e:
    print(e)