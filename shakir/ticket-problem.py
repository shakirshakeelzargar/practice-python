



'''
NoofPassengers = 3
TicketRate = 250
TicketReducedBy = 1.5
Discount = 2/100
Insurance = 4


#PerTicketCost= TicketRate - (TicketRate* TicketReducedBy/100);
#print(PerTicketCost)
#735.975
# 750 - 15 = 735 + 12 = > 747 Total Value


TotalTicketValue=  (NoofPassengers * (TicketRate - (TicketRate * TicketReducedBy/100)) ) - ((NoofPassengers * 246.25) * Discount)
TotalInsuranceValue = NoofPassengers * Insurance
TotalBillValue=  TotalTicketValue + TotalInsuranceValue

print(TotalBillValue)



#Method2
ReducedTicketRate=TicketRate-(TicketRate*(TicketReducedBy/100))
TotalTicketValue2=  (NoofPassengers * ReducedTicketRate ) - ((NoofPassengers * ReducedTicketRate) * Discount)
TotalInsuranceValue2 = NoofPassengers * Insurance
TotalBillValue2=  TotalTicketValue2 + TotalInsuranceValue2
print(TotalBillValue2)


a=2
b=2
tplMsg="The Solution is {}"
print(tplMsg.format(a/b))
'''


try:
    numberOfPassengers=int(input("enter no of passengers: "))
    priceOfTicket=int(input("enter price of ticket in rupees: "))
    discountPercentage=float(input("enter discount percentage: "))
    insuranceAmountInRupees=float(input("enter insuarance amount in rupees: "))
    didPriceFall=input("Did price of ticket fall? [y/n]: ")
except:
    print("Invalid Entries")
else:
    if(didPriceFall=='y'):
        byHowMuchTicketFall=float(input("By how much percent did price of ticket fell: "))

        newPriceOfTicket=priceOfTicket-(priceOfTicket*(byHowMuchTicketFall/100))
        finalTicketPrice=(numberOfPassengers*newPriceOfTicket)-((numberOfPassengers*newPriceOfTicket)*discountPercentage/100)
        finalInsurance=(numberOfPassengers*insuranceAmountInRupees)
        totalBill=(finalTicketPrice+finalInsurance)
    
        invoiceMessage='''
                    Ticket Invoice  
                    Price per Ticket : {} 
                    No of Passengers : {} 
                    Did price fall down : {} 
                    Price fall percentage : {} 
                    New Base price : {} 
                    Insurance Amount : {} 
                    Total Amount Without Discount : {}
                    Discount Percentage : {} 
                    Total Amount To Be Paid : {}'''
        print(invoiceMessage.format(priceOfTicket,numberOfPassengers,
        didPriceFall,byHowMuchTicketFall,newPriceOfTicket,insuranceAmountInRupees,
        numberOfPassengers*newPriceOfTicket,discountPercentage,totalBill))
    elif(didPriceFall=='n'):
        finalTicketPrice=(numberOfPassengers*priceOfTicket)-((numberOfPassengers*priceOfTicket)*discountPercentage/100)
        finalInsurance=(numberOfPassengers*insuranceAmountInRupees)
        totalBill=(finalTicketPrice+finalInsurance)
    
        invoiceMessage='''
                    Ticket Invoice  
                    Price per Ticket : {} 
                    No of Passengers : {} 
                    Did price fall down : {} 
                    Insurance Amount : {} 
                    Total Amount Without Discount : {}
                    Discount Percentage : {} 
                    Total Amount To Be Paid : {}'''
        print(invoiceMessage.format(priceOfTicket,numberOfPassengers,didPriceFall,insuranceAmountInRupees,numberOfPassengers*priceOfTicket,discountPercentage,totalBill))
    else:
        print("Invalid Entries")
