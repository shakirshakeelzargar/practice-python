import json
import jinja2
import sys
import os
from datetime import datetime


# Get the FD details from the JSON file
def getFDDetails():
    try:
        with open("./practice-python/assets/fd-reminder.json") as jsonFile:
            fdDetails = json.load(jsonFile)
    except ValueError as ve:
        print("Error in JSON decoding: %s" % ve)
        sys.exit()
    else:
        return fdDetails

# Generate the template based on the given FD data


def generateTemplate(tmplName, tmplData):
     # Check if template exists
    if not os.path.exists("./practice-python/mani/"+tmplName):
        print('No template file present: %s' % tmplName)
        sys.exit()

    # Redering the template based on the FD data
    templateLoader = jinja2.FileSystemLoader(
        searchpath="./practice-python/mani/")
    templateEnv = jinja2.Environment(loader=templateLoader)
    templ = templateEnv.get_template(tmplName)
    userTmpl = []
    for data in tmplData:
        userTmpl.append((data["customer_id"], data["customer_name"],
                         templ.render(fd=data)))
    return userTmpl

# Store the output to a dir with current timestamp
def outputReport(userFDInfoEmail):
    currentDay = datetime.now().strftime("%m")
    currentMonth = datetime.now().strftime('%d')
    currentYear = datetime.now().strftime('%Y')
    outputDir = "./practice-python/mani/output/" + \
        currentYear + "/"+currentDay+currentMonth + "/"
    # Creating the Output directory for current date
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    # Store the result for each user in output dir. Ex: <customerName>_<customerId>.txt
    for userTmpl in userFDInfoEmail:
        try:
            with open(outputDir + str(userTmpl[1])+"_"+str(userTmpl[0])+".txt", "w+") as email:
                email.write(userTmpl[2])
        except IOError as io:
               print('IO error on write a file: %s' % io)


 # Main function
def main():
    fdData = getFDDetails()
    userFDInfoEmail = generateTemplate('template.tpl', fdData)
    outputReport(userFDInfoEmail)


main()


"""
Output:
Dear  Arul Prakash

    Here the details of your FD
    
    --
    --
    
    This is the FD based on FD Scheme 2 . For this FD Scheme 2 you need to bring the following to collect the maturity amount.
    
    <INSTRUCTIONS SPECIFIC to SCHEME>
   Matures_on: 28/07/19,
   Amount_deposited: 3200,
   Maturity_amount: 6390,
   Deposit_date: 15/07/16
       
    Regards
    ABC Bank

"""
