def getDatabaseTables(emailType):
  userList=[]
  for i in range(5):
    userInfo={}
    userInfo['email']="Table{}@gmail.com".format(i)
    userInfo['fullname']="Table {}".format(i)
    userList.append(userInfo)
  return userList

