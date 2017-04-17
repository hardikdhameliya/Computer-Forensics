#!/usr/bin/python

import sqlite3
import csv

print "connecting.."
db=sqlite3.connect('HASHVALUE.db')
print "connected.."

cursor=db.cursor()

cursor.execute('DROP TABLE IF EXISTS HASHCODE')

sql= """ CREATE TABLE HASHCODE (
	 SHA1 CHAR(4096), 
	 FILE_SIZE CHAR(4096),
	 PRODUCT_CODE CHAR(4096),
	 OS_CODE CHAR(4096))"""

cursor.execute(sql)

with open("NSRLFile.txt") as csvfile:
 reader = csv.reader(csvfile)
 included_cols=[0,4,5,6]
 #print reader
 for row in reader:
  content=list(row[i] for i in included_cols)
  sql="""INSERT INTO HASHCODE(SHA1,FILE_SIZE, PRODUCT_CODE, OS_CODE) 
      VALUES ('%s','%s','%s','%s')""" % (content[0].lower(),content[1].lower(),content[2].lower(),content[3].lower())
  print sql
  cursor.execute(sql)
  
  #print content[0]
db.commit()
'''
print "connecting.."
db=sqlite3.connect('TESTDB.db')
print "connected.."

cursor=db.cursor()


cursor.execute('DROP TABLE IF EXISTS EMPLOYEE')

sql= """ CREATE TABLE EMPLOYEE (
	 SHA1 CHAR(40), 
	 FILE_NAME CHAR(12),
	 FILE_SIZE INT,
	 PRODUCT_CODE INT,
	 OS_CODE INT)"""

cursor.execute(sql)


sql="""INSERT INTO EMPLOYEE(FIRST_NAME, 
      LAST_NAME, AGE, SEX, INCOME)
      VALUES ('mac','wow',27,'M',150000)"""

cursor.execute(sql)

db.commit()



sql="SELECT * FROM EMPLOYEE \
     WHERE SHA1 == '%s'" % ("0000002D9D62AEBE1E0E9DB6C4C4C7C16A163D2C")

cursor.execute(sql)

results=cursor.fetchall()

#print results


for row in results:
 sha1 =row[0]
 file_name=row[1]
 file_size=row[2]
 product_code=row[3]
 os_code=row[4]

 print "%s : %s : %s: %s :%s" % \
  (sha1,file_name,file_size,product_code,os_code)
'''
db.close()

