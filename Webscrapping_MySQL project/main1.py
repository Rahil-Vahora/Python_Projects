import requests
from bs4 import BeautifulSoup
import mysql.connector 

url = "https://www.bvmengineering.ac.in/"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
mydb=mysql.connector.connect(host='localhost',user='root',password='password',database="webapp")

mycursor=mydb.cursor()

mycursor.execute("CREATE TABLE bvm (html_doc LONGTEXT)")
mycursor.execute("SHOW TABLES")
for value in mycursor:
 print(value)

# sql = "INSERT INTO bvm (html_doc) VALUES (%s)"
# val = [
#     (soup.prettify())
# ]
# mycursor.execute(sql,val)


mycursor.execute("SELECT * FROM bvm")
result = mycursor.fetchall()

for x in result:
    print(x)
mydb.commit()