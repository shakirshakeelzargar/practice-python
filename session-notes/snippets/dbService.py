def getAllUsersFromDB(emailType):
  userList=[]
  for i in range(5):
    userInfo={}
    userInfo['email']="user{}@gmail.com".format(i)
    userInfo['fullname']="USER {}".format(i)
    userList.append(userInfo)
  return userList

