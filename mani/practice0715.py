#Exercise1: Ticket
noofPassengers = 3
ticketRate = 250
ticketReducedBy = 1.5
discountPercent = 2
insurance = 4

#Without any variable expressions
totalTicketAmount=  ((noofPassengers * (ticketRate - (ticketRate* ticketReducedBy/100))) - ((noofPassengers * (ticketRate - (ticketRate* ticketReducedBy/100))) * discountPercent/100)) + (noofPassengers * insurance)
print(totalTicketAmount)

#With variables
totalReducedTicketAmount = (ticketRate - (ticketRate* ticketReducedBy/100))
totalInsuranceAmount = noofPassengers * insurance
totalTicketAmount = ((noofPassengers * totalReducedTicketAmount) - ((noofPassengers * totalReducedTicketAmount) * discountPercent/100)) + totalInsuranceAmount
print(totalTicketAmount)

#Exercide2: Expression in print format:
quantity=3
price=75
item='pen'
testMessage  =  "Cost of {0} {1} price {totalCost} => {0}*{2}"
print(testMessage.format(quantity, item, price, totalCost=quantity*price))

#Exercide 3: Decimal and Floating formatting
print("Test :{0:4d}, Portal :{1:8.2f}".format(151, 354.59977)) 
data = {'first': 'Test', 'last': 'Formatting'}
print('{d[first]} {d[last]}'.format(d=data))
print('{0:>20} | {1:<10}|{2:2.3f}'.format('python', 'test',90.99))
print('{:{align}{width}}'.format('test', align='^', width='10'))
data1 = [4, 8, 15, 16, 23, 42]
print('{d[4]} {d[5]}'.format(d=data1))