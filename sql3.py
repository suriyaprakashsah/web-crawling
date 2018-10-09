import pymysql

# Open database connection
db = pymysql.connect("46.4.115.158", "root", "Mysql@rhombus123", "demo" )

# prepare a cursor object using cursor() method
cursor = db.cursor()
count = 0
tablename = raw_input("enter the TableName: ")
str = "create table" + " " + tablename + " ("
while (count < 2):
    column = raw_input("enter the column name: ")
    datatype = raw_input("enter the datatype of column type: ")
    str = str + " " + column + " " + datatype + ","
    count = count + 1
print(str)
str = str.rstrip(',')
str = str + ")"
print(str)
try:
    cursor.execute(str)
    db.close()
    print("Table Created Successfully in DataBase")
except:
    print("Problem While Creating The Table")

