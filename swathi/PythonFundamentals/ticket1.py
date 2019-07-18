NoofPassengers = 3
TicketRate = 250
TicketReducedBy = 1.5
Discount = 2/100
Insurance = 4

#PerTicketCost= TicketRate - (TicketRate* TicketReducedBy/100);
#print(PerTicketCost)
#735.975
# 750 - 15 = 735 + 12 = > 747 Total Value

TotalTicketValue=  (NoofPassengers * (TicketRate - (TicketRate* TicketReducedBy/100) )) - ((NoofPassengers * 246.25) * Discount)
TotalInsuranceValue = NoofPassengers * Insurance
TotalBillValue=  TotalTicketValue + TotalInsuranceValue

print(TotalBillValue)
