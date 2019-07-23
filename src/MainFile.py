#import NewFolder
import json
import pandas as pd
#foldername=NewFolder.getFoldername()
#print(foldername)
y='[{"glno":74,"Option":2,"Section":"Aptitude","Localno":1},{"glno":75,"Option":2,"Section":"Aptitude","Localno":2},{"glno":76,"Option":3,"Section":"Aptitude","Localno":3},{"glno":77,"Option":4,"Section":"Aptitude","Localno":4},{"glno":78,"Option":1,"Section":"Aptitude","Localno":5},{"glno":79,"Option":2,"Section":"Aptitude","Localno":6},{"glno":80,"Option":3,"Section":"Aptitude","Localno":7},{"glno":81,"Option":4,"Section":"Aptitude","Localno":8},{"glno":82,"Option":1,"Section":"Aptitude","Localno":9},{"glno":83,"Option":2,"Section":"Aptitude","Localno":10},{"glno":84,"Option":3,"Section":"Aptitude","Localno":11},{"glno":85,"Option":4,"Section":"Aptitude","Localno":12},{"glno":86,"Option":1,"Section":"Aptitude","Localno":13},{"glno":87,"Option":2,"Section":"Aptitude","Localno":14},{"glno":88,"Option":3,"Section":"Aptitude","Localno":15},{"glno":89,"Option":4,"Section":"Aptitude","Localno":16},{"glno":90,"Option":1,"Section":"Aptitude","Localno":17},{"glno":91,"Option":2,"Section":"Aptitude","Localno":18},{"glno":92,"Option":3,"Section":"Aptitude","Localno":19}]'
result=json.loads(y)
globallist=[]
optionlist=[]
for arr in result:
    globallist.append(arr['glno'])
    optionlist.append(arr['Option'])
df = pd.DataFrame({'Globalno': globallist,'Option':optionlist})
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet5')
writer.save()