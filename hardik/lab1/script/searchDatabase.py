#!/usr/bin/python

import sqlite3
import csv
import StringIO
import sys

print "connecting.."
db=sqlite3.connect("HASHVALUE.db")
print "connected.."

cursor=db.cursor()

with open("interesting.txt","w") as target:

 with open("sha1sum.list") as file:
   lines = file.readlines()
 
   for row in lines:
 	row= StringIO.StringIO(row)
 	sha1=row.read(40)
 	sha1=sha1.lower()
  

  	sql="SELECT * FROM HASHCODE \
    	 WHERE SHA1 == '%s'" % (sha1)
   
  	cursor.execute(sql)
  	print sha1
  	results=cursor.fetchone()

  	if results is  None: 
  		#for intersting in results:
   		target.write(sha1)
   		target.write("\n")
		print sha1   		
		

db.close()
file.close()
target.close()

