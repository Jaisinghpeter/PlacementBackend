import pandas as pd
ExcelData = pd.DataFrame()
def setUserlist():
    global ExcelData
    ExcelData = pd.read_excel("User_list.xlsx")
def UserPresent(Username,Password):
    flag=0
    user_id=0
    for i in range(0,ExcelData.shape[0]):
        if(Username==ExcelData['Username'][i]):
            if(Password==str(ExcelData['Password'][i])):
                user_id=int(ExcelData['User ID'][i])
                flag=1
                break;
    return flag,user_id
