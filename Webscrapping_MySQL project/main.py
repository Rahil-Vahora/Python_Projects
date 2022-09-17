
import requests
from bs4 import BeautifulSoup
import mysql.connector 

url = "https://www.bvmengineering.ac.in/"

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
mydb=mysql.connector.connect(host='localhost',user='root',password='password',database="webapp")

mycursor=mydb.cursor()

mycursor.execute("CREATE DATABASE webapp")

sql = "INSERT INTO webapp (html_doc) VALUES (%s)"
val = [
    str(soup)
]
mycursor.executemany(sql,val)

mydb.commit()
# mycursor.execute("show tables")
# for tb in mycursor:
#     print(tb)
# url = "https://www.bvmengineering.ac.in/"

# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'html.parser')

# print(soup.prettify())