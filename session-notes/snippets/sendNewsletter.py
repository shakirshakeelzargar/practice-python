"""
- getAllUsersFromDB
- getTemplateContent
- formatValues
- createEmailEnvelope (subject,body, toaddress)
- sendEmail
"""

import dbService
from dbService import getAllUsersFromDB

"""
import sys
sys.path.insert(0, "/c/projects/folder/cloudstore/")
#These are the paths python will search for your packages
Path0:
Path1:
Path2:
Path3:

SET PATH=/c/projects/folder/cloudstore/

pip packages
"""

# sys.path


formatValues=lambda tplContent, userInfo: tplContent.replace("#USERNAME#",userInfo["fullname"])


def sendNewsletter():
  users=dbService.getAllUsersFromDB('newsletters')
  tplContent=getTemplateContent("./tpl.html")
  for user in users:
    formattedValues=formatValues(tplContent,user)
    print(formattedValues)
    #envelope=createEmailEnvelope(user,formattedValue)
    ##Write the code to send the mail via SMTP
    #print(envelope)

def createEmailEnvelope(userInfo,body):

  #addCCmail=lambda tplContent, userInfo: tplContent.replace("#USERNAME#",userInfo["fullname"])

  #for i in range(10):
  envelope={}
  envelope["to"]=userInfo["emailid"]
  envelope["body"]=userInfo[body]


#def formatValues(tplContent, userInfo):
#  return  tplContent.replace("#USERNAME#",userInfo["fullname"])

def getTemplateContent(tplFilePath):
  tplFile=open(tplFilePath)
  tplContent=tplFile.read()
  tplFile.close()
  return tplContent


#addNumbers= lambda x,y : x+y

#addNumbers=lambda x,y:x+y


#def addNumbers(x,y):
#  return x+y

#print(addNumbers(4,5))
#sendNewsletter();

axis=10
mouseAngle=45

try:
  m=mouseAngle/axis
  open("asasas.txt")
except ZeroDivisionError as ex :
  print("You cannot have axis as 0")
except Exception as ex:
  raise(ex)
except :
    print("No errors")
finally :
  print("Exceution done")


