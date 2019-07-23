import setDirectory
import os
import pandas as pd
os.chdir(setDirectory.files())
print(os.getcwd())
Excelnamelist=['Technical','Reasoning','Aptitude']
for name in Excelnamelist:
        n={}
        ExcelData = pd.read_excel(name+".xlsx")
        n['Total_qs']=ExcelData.shape[0]
        questionlist=[]
        for i in range(0,ExcelData.shape[0]):
            qs={}
            questions={}
            answer={} 
            qs['Option']=ExcelData.values[i][0]
            qs['Option1']=ExcelData.values[i][1]
            qs['Option2']=ExcelData.values[i][2]
            qs['Option3']=ExcelData.values[i][3]
            qs['Option4']=ExcelData.values[i][4]
            qs['qsid']=qsid
            answer['Answer']=ExcelData.values[i][5]
            answer['Marks']=ExcelData.values[i][6]
            answer['qsid']=qsid
            answerarray.append(answer)
            questions['Question']=qs
            questionlist.append(questions)
            qsid=qsid+1
        n['Questions']=questionlist
        y[name]=n