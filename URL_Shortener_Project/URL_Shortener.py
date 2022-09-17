from tkinter import *
import requests
import pyperclip

# bitly account credentials
username = "Your bitly acc username"
password = "Your bitly acc password"

# get the access token
auth_res = requests.post("https://api-ssl.bitly.com/oauth/access_token", auth=(username, password))
if auth_res.status_code == 200:
    # if response is OK, get the access token
    access_token = auth_res.content.decode()
else:
    print("[!] Cannot get access token, exiting...")
    exit()

# construct the request headers with authorization
headers = {"Authorization": f"Bearer {access_token}"}

# get the group UID associated with our account
groups_res = requests.get("https://api-ssl.bitly.com/v4/groups", headers=headers)
if groups_res.status_code == 200:
    # if response is OK, get the GUID
    groups_data = groups_res.json()['groups'][0]
    guid = groups_data['guid']
else:
    print("[!] Cannot get GUID, exiting...")
    exit()



def shorten():
    # the URL you want to shorten
    url = str(a.get())
    # make the POST request to get shortened URL for `url`
    shorten_res = requests.post("https://api-ssl.bitly.com/v4/shorten", json={"group_guid": guid, "long_url": url}, headers=headers)
    if shorten_res.status_code == 200:
        # if response is OK, get the shortened URL
        link = shorten_res.json().get("link")
        # print("Shortened URL:", link)
    global b
    b.set(str(link))

def copy_URL():
    pyperclip.copy(b.get())

root = Tk()
root.title("URL Shortener")
root.geometry('500x400')
icon = PhotoImage(file="URL_icon.png")
root.iconphoto(False,icon)

a = StringVar(root)
b = StringVar(root)

lable1 = Label(root,text="Enter the URL:- ").grid(row=1,column=0)
text1 = Entry(root,textvariable=a,width=50).grid(row=1,column=1)
button1 = Button(root,text="Shorten above URL",command=shorten).grid(row=2,column=1)
lable2 = Label(root,text="Shortened URL:- ").grid(row=3,column=0)
text2 = Entry(root,textvariable=b,width=50).grid(row=3,column=1)
button2 = Button(root,text="Copy",command=copy_URL).grid(row=3,column=2)
button3 = Button(root,text="Exit Application",command=root.destroy).grid(row=4,column=1)

root.mainloop()