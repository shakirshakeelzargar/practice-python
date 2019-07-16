#cloud computing cost

cost=float(input("Enter cloud computing cost per hour for one server : "))
noOfServers=int(input("Enter number of servers : "))
budget=float(input("Enter your budget : "))
costPerDay=cost*noOfServers*24
costPerMonth=costPerDay*30
operationalDays=budget/costPerDay

print("The cost of cloud computing per day for {} server is $ {:.2f}".format(noOfServers,costPerDay))
print("The cost of cloud computing per month for {} server is $ {:.2f}".format(noOfServers,costPerMonth))
print("In the budget of {} you can run the cloud computing for {:.0f} days".format(budget,operationalDays))