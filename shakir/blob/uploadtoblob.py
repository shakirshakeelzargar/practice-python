


from jinja2 import Environment, FileSystemLoader
from azure.storage.blob import BlockBlobService, PublicAccess
from datetime import datetime
import json
#https://github.com/swaathi/eda/blob/master/data.csv
from urllib.request import urlopen, Request
printedd='None'
try:
    file_url = "https://raw.githubusercontent.com/shakirshakeelzargar/practice-python/master/assets/fd-reminder.json"
    req = Request(url=file_url) 
    file =(urlopen(req))
    data=json.load(file)
    #dict={}
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    print("Fetching file from url")
except Exception:
    print("File not found, incorrect URL")
else:
    try:
        print("Getting template")
        template = env.get_template('bank_template.txt')
    except:
        print("Template not found")
    else:
        print("Template found")
    #template = env.get_template('hello_world.txt')
    #view='customer_id'

        try:
            print("Iterating data for each customer and creating files")
            for d in data:
            #print(d[view])
                output = template.render(dataCustomer=d)
                #print(type(output))
                ###########print(output)
                #f=open("D:/python/practice-python/shakir/basic_jinja/"d['customer_name']"-"d['customer_id']".txt","w")
                local_path='./outputs'
                local_file_name= "{}-{}.txt".format(d['customer_name'],d['customer_id'])
                full_path_to_file=local_path+"/"+local_file_name
                f=open(full_path_to_file,"w+")
                f.write("{}".format(output))
                f.close()
                try:
                    block_blob_service = BlockBlobService(account_name='accountnamehere', account_key='accountkeyhere')
                    container_name ='containernameheree'
                    block_blob_service.create_container(container_name)
                    #uploading file to
                    block_blob_service.set_container_acl(container_name, public_access=PublicAccess.Container)
                    block_blob_service.create_blob_from_path(container_name, local_file_name, full_path_to_file)
                    #downloading file from the blob
                    full_path_to_file2 = './downloads/'+str.replace(local_file_name ,'.txt', '_DOWNLOADED_from_blob.txt')
                
                    block_blob_service.get_blob_to_path(container_name, local_file_name, full_path_to_file2)
                except Exception as ex:
                    if(printedd=='None'):
                        print("some error in uploading to blob")
                    logtext="[{}]-'{}'   \n".format(str(datetime.now().time()),ex)
                    LogPath='./logs/log-{}.txt'.format(str(datetime.now().date()))
                    log=open(LogPath,"a")
                    log.write(logtext)
                    log.close()
                    printedd='Done'
                else:
                    if(printedd=='None'):
                        print("Uploading files to blob")
                    logtext="[{}]-File '{}' uploaded to blob Successfully \n".format(str(datetime.now().time()),local_file_name)
                    LogPath='./logs/log-{}.txt'.format(str(datetime.now().date()))
                    log=open(LogPath,"a")
                    log.write(logtext)
                    log.close()
                    printedd='Done'
                        

        except:
            print("Some error in creating text files")
        else:
            print("text files for users created successfully")
            print("log generated in '{}'".format(LogPath))

            

finally:
    print("Program executed")


#Output
'''
Fetching file from url
Getting template
Template found
Iterating data for each customer and creating files
Uploading files to blob
text files for users created successfully
log generated in '/logs/log-2019-07-19.txt'
Program successfully executed
'''