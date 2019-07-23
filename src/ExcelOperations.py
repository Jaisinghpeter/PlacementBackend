from datetime import date
import os
import pandas as pd
import json
import time
import setDirectory
y='[{"name":"Jaisingh"},{"glno":74,"Option":1,"Section":"Aptitude","Localno":1},{"glno":75,"Option":2,"Section":"Aptitude","Localno":2},{"glno":76,"Option":4,"Section":"Aptitude","Localno":3},{"glno":77,"Option":1,"Section":"Aptitude","Localno":4},{"glno":78,"Option":2,"Section":"Aptitude","Localno":5},{"glno":79,"Option":3,"Section":"Aptitude","Localno":6},{"glno":80,"Option":4,"Section":"Aptitude","Localno":7},{"glno":81,"Option":1,"Section":"Aptitude","Localno":8},{"glno":82,"Option":2,"Section":"Aptitude","Localno":9},{"glno":83,"Option":3,"Section":"Aptitude","Localno":10},{"glno":84,"Option":4,"Section":"Aptitude","Localno":11},{"glno":85,"Option":1,"Section":"Aptitude","Localno":12},{"glno":86,"Option":2,"Section":"Aptitude","Localno":13},{"glno":87,"Option":3,"Section":"Aptitude","Localno":14},{"glno":88,"Option":4,"Section":"Aptitude","Localno":15},{"glno":89,"Option":1,"Section":"Aptitude","Localno":16},{"glno":90,"Option":2,"Section":"Aptitude","Localno":17},{"glno":91,"Option":3,"Section":"Aptitude","Localno":18},{"glno":92,"Option":4,"Section":"Aptitude","Localno":19}]'
x='[{"name":"Arunpandi"},{"glno":74,"Option":1,"Section":"Aptitude","Localno":1},{"glno":75,"Option":2,"Section":"Aptitude","Localno":2},{"glno":76,"Option":4,"Section":"Aptitude","Localno":3},{"glno":77,"Option":1,"Section":"Aptitude","Localno":4},{"glno":78,"Option":2,"Section":"Aptitude","Localno":5},{"glno":79,"Option":3,"Section":"Aptitude","Localno":6},{"glno":80,"Option":4,"Section":"Aptitude","Localno":7},{"glno":81,"Option":1,"Section":"Aptitude","Localno":8},{"glno":82,"Option":2,"Section":"Aptitude","Localno":9},{"glno":83,"Option":3,"Section":"Aptitude","Localno":10},{"glno":84,"Option":4,"Section":"Aptitude","Localno":11},{"glno":85,"Option":1,"Section":"Aptitude","Localno":12},{"glno":86,"Option":2,"Section":"Aptitude","Localno":13},{"glno":87,"Option":3,"Section":"Aptitude","Localno":14},{"glno":88,"Option":4,"Section":"Aptitude","Localno":15},{"glno":89,"Option":1,"Section":"Aptitude","Localno":16},{"glno":90,"Option":2,"Section":"Aptitude","Localno":17},{"glno":91,"Option":3,"Section":"Aptitude","Localno":18},{"glno":92,"Option":4,"Section":"Aptitude","Localno":19}]'
          
def exceltojson():
    os.chdir(setDirectory.files())
    y={}
    answerarray=[]
    qsid=1
    Excelnamelist=['Aptitude','Technical','Reasoning']
    total=0
    for name in Excelnamelist:
        n={}
        ExcelData = pd.read_excel(name+".xlsx")
        n['Total_qs']=ExcelData.shape[0]
        questionlist=[]
        for i in range(0,ExcelData.shape[0]):
            qs={}
            questions={}
            answer={} 
            quest=ExcelData.values[i][0]
            qs['Question']=quest
            qs['Option1']=ExcelData.values[i][1]
            qs['Option2']=ExcelData.values[i][2]
            qs['Option3']=ExcelData.values[i][3]
            qs['Option4']=ExcelData.values[i][4]
            qs['qsid']=qsid
            answer['Answer']=ExcelData.values[i][5]
            answer['Marks']=ExcelData.values[i][6]
            total=total+answer['Marks']
            answer['qsid']=qsid
            answerarray.append(answer)
            questions['Question']=qs
            questionlist.append(questions)
            qsid=qsid+1
        n['Questions']=questionlist
        y[name]=n
    return y,answerarray,total
exceltojson()
def getresult(name):
    setDirectory.setlatestfolder()
    print(os.getcwd())
    ExcelData = pd.read_excel(name+".xlsx")
    answerlist=[]
    for i in range(0,ExcelData.shape[0]):
            ans={}
            ans['Globalno']=ExcelData.values[i][1]
            ans['Option']=ExcelData.values[i][2]
            answerlist.append(ans)    
    return answerlist
def createFolder():
    os.chdir(setDirectory.sethome())
    directory = str(date.today())
    i=1
    foldername=''
    if os.path.exists("Results"):
        while True:
            try:
                foldername="Results\\"+directory+"_Test-"+str(i)
                os.makedirs(foldername)
                break;
            except:
                i=i+1;
    print(foldername)
    return foldername
def getworkingdirectory():
    cwd=os.getcwd()
    print(cwd)
def getlastcreateddirectory():
    print(os.getcwd())
    all_subdirs = [d for d in os.listdir('.') if os.path.isdir(d)]
    latest_subdir = max(all_subdirs, key=os.path.getmtime)
    os.chdir(latest_subdir)
    return latest_subdir
def findmarks():
    dfs = pd.read_excel(file_name, sheetname=None)
def writeinfile(y):
    result=y
    globallist=[]
    optionlist=[]
    name=result[0]['Username']
    id=result[0]['userid']
    answer=result[1]['Answers']
    for arr in answer:
        globallist.append(arr['glno'])
        optionlist.append(arr['Option'])
    df = pd.DataFrame({'Globalno': globallist,'Option':optionlist})
    writer = pd.ExcelWriter(name+'.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    print("Successfully saved File")
    return name
#start = time.time()
##os.chdir('..')
#foldername=getFoldername()
#os.chdir(foldername)
#filename=writeinfile(x)
#print(os.getcwd())
#print(filename)
#dfs = pd.read_excel(filename+".xlsx", sheetname='Sheet1')
#print(dfs)
#os.chdir('..')
#end = time.time()
#print(end - start)