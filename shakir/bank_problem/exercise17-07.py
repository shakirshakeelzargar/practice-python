


from jinja2 import Environment, FileSystemLoader
import json
#https://github.com/swaathi/eda/blob/master/data.csv
from urllib.request import urlopen, Request
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
                output = template.render(customerName=d['customer_name'],schemeName=d['deposit_type'],amountDeposited=d['amount_deposited'],maturityAmount=d['maturity_amount'],maturesOn=d['matures_on'],depositDate=d['deposit_date'],depositType=d['deposit_type'],truth=True)
                #print(type(output))
                ###########print(output)
                #f=open("D:/python/practice-python/shakir/basic_jinja/"d['customer_name']"-"d['customer_id']".txt","w")
                f=open("D:/python/practice-python/shakir/bank_problem/outputs/{}-{}.txt".format(d['customer_name'],d['customer_id']),"w+")
                f.write("{}".format(output))
        except:
            print("Some error in creating text files")
        else:
            print("text files for users created successfully")

            

finally:
    print("Program executed")


    #output
'''
Fetching file from url
Getting template
Template found
Iterating data for each customer and creating files
text files for users created successfully
Program executed
'''