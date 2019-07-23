import os
url=r'C:\Users\Ashwin\Desktop\Exam'
set1=5
def setset():
    global set1
    set1=10
def printset():
    print(set1)
def sethome():
    return url
def setsrc():
    newurl=url+'\src'
    return newurl
def files():
    newurl=url+'\Files'
    return newurl
def result():
    newurl=url+'\Results'
    return newurl
def getlatestfolder():
    now=os.getcwd()
    os.chdir(result())
    all_subdirs = [d for d in os.listdir('.') if os.path.isdir(d)]
    latest_subdir = max(all_subdirs, key=os.path.getmtime)
    os.chdir(now)
    latest_subdir=url+'\Results\\'+latest_subdir
    return latest_subdir
def setlatestfolder():
    os.chdir(getlatestfolder())
def makefinalfolder():
    os.makedirs(getlatestfolder()+"\Final")
    with open("results.csv",'w') as file:
        line="Name,Marks\n"
        file.write(line)
    file.close()
def setfinalfolder():
    os.chdir(getlatestfolder()+"\Final")

