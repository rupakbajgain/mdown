base = "http://www.mangareader.net/"
manganame = input("Enter manga name:")
downloadM = ".\\downloads\\"
userAgent = 'Mozilla 5.10'
sf = int(input("Start chapter:"))
st = int(input("End chapter:"))

import urllib.request
import os
from bs4 import BeautifulSoup
url = base+manganame+"/"

def downloadlink(u):
    req = urllib.request.Request(u)
    req.add_header('User-agent',userAgent)
    res=urllib.request.urlopen(req)
    return res.read()

def downloadImage(u,name):
    f=open(downloadM+name,"wb")
    f.write(downloadlink(u))
    f.close()

def createFolder(n):
    if not os.path.exists(n):
        os.mkdir(n)

def downloadChapter(num):
    createFolder(downloadM+manganame+("\\%d"%num))
    r=downloadlink(url+str(num))
    soup=BeautifulSoup(r,"html.parser")
    starturl = ""
    for i in soup.find_all('img'):
        t=i.get('src')
        if(len(t)):
            starturl=t
    total=0
    for i in soup.find_all('div'):
        if i.get('id')=="selectpage":
           a=i.text.split('\n')
           total=len(a)
    t1=starturl.split('-')
    t2=t1[len(t1)-1].split(".")
    i1=int(t2[0])
    uindex=0
    i=0
    while True:
        if(i==total-1):
            break
        t1[len(t1)-1]=str(i1+i+uindex)+".jpg"
        starturl="-".join(t1)
        print("%d of %d"%(i+1,total-1))
        try:
            downloadImage(starturl,("%s\\%d\\%d.jpg"%(manganame,num,i)))
            i=i+1
        except:
            uindex=uindex+1

createFolder(downloadM+manganame)
for i in range(sf,st+1):
    print("Downloading chapter %d" % i)
    downloadChapter(i)
