import webbrowser
import os
import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='password',database="webapp")

mycursor=mydb.cursor()

mycursor.execute("SELECT * FROM bvm")
result = mycursor.fetchall()
mydb.commit()
f = open("bvm.html" , 'w')

# html_template = result

f.write(str(result))
f.close()

filename = 'file:///'+os.getcwd()+'/' + 'bvm.html'
webbrowser.open_new_tab(filename)