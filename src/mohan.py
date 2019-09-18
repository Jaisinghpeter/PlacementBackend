from flask import Flask ,request,redirect
from flask_cors import CORS, cross_origin
from flask import jsonify
import pandas as pd
import os
import UserDetails
import setDirectory
import json
import ExcelOperations
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
name=""
score=0
answerarray=[]
questionsdict={}
questiondict1={}
questiondict2={}
questiondict3={}
total=0
@app.before_first_request
def do_something_only_once():
    os.chdir(setDirectory.sethome())
    ExcelOperations.createFolder()
    setDirectory.makefinalfolder()
    print(os.getcwd())
    os.chdir(setDirectory.files())
    UserDetails.setUserlist()
    global questionsdict
    global questionsdict1
    global questionsdict2
    global questionsdict3
    global answerarray
    tempdict={}
    tempdict2={}
    global total
    questionsdict,answerarray,total=ExcelOperations.exceltojson()
    y=json.dumps(questionsdict)
    x=json.loads(y)
    for qs in questionsdict:
        qsdict={}
        tot=questionsdict[qs]['Total_qs']
        arr=questionsdict[qs]['Questions']
        arr = arr[int(tot/2):] + arr[:int(tot/2)] 
        qsdict['Total_qs']=tot
        qsdict['Questions']=arr
        tempdict[qs]=qsdict
        qsdict={}
        arr=questionsdict[qs]['Questions']
        arr = arr[int(tot/3):] + arr[:int(tot/3)] 
        qsdict['Total_qs']=tot
        qsdict['Questions']=arr
        tempdict2[qs]=qsdict
    questionsdict3=questionsdict.copy()
    questionsdict1=tempdict.copy()
    questionsdict2=tempdict2.copy()
@app.route('/hello',methods = ['POST'])
@cross_origin()
def hello_world():
    if request.method == 'POST':
        y=json.loads(request.get_data())
        user=y[0]['Username']
        print(user)
        password=y[1]['Password']
        os.chdir(setDirectory.files())
        returnval,userid=UserDetails.UserPresent(user,password)
        y={'result':returnval,'userid':userid}
        return jsonify(y)
#      return redirect(url_for('success',name = user))
@app.route('/getqs',methods = ['POST'])
@cross_origin()
def getquestions():
    print(request.get_data())
    x=json.loads(request.get_data())
    user=x[0]['Username']
    userid=x[0]['userid']
    modval=userid%3
    tempdict={}
    global questionsdict1
    global questionsdict2
    global questionsdict3
    if(modval==1):
        tempdict=questionsdict1.copy()
    elif(modval==2):
        tempdict=questionsdict2.copy()
    else:
        tempdict=questionsdict3.copy()
    tempdict['Name']=user
    return jsonify(tempdict)
    
@app.route('/result',methods = ['POST'])
@cross_origin()
def setExcel_data():
    x=json.loads(request.get_data())
    setDirectory.setlatestfolder()
    name=ExcelOperations.writeinfile(x)
    y={'result':1}
    return jsonify(y)
#      return redirect(url_for('success',name = user))

@app.route('/final',methods = ['POST'])
@cross_origin()
def setResult():
    x=json.loads(request.get_data())
    setDirectory.setlatestfolder()
    user=x[0]['Username']
    global answerarray
    global total
    answerlist=ExcelOperations.getresult(user)
    marksobt=0
    for ans in answerlist:
        option=ans['Option']
        option="Option"+str(option)
        gl=ans['Globalno']
        if(answerarray[gl-1]['Answer']==option):
            print(answerarray[gl-1]['Answer'])
            marksobt=marksobt+answerarray[gl-1]['Marks']
    setDirectory.setfinalfolder()
    with open("results.csv","a") as file:
        line=user+","+str(marksobt)+"\n"
        file.write(line)
    file.close()
    print(marksobt)
    y={'result':1,'Totalmarks':total,'marks_obt':marksobt}
    return jsonify(y)
   

if __name__ == '__main__':
    app.run(host='192.168.5.182')
#    app.run()
