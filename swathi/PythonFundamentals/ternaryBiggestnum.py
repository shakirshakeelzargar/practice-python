n1 = 4000000
n2 = 1000000
n3 = 1500000
n4 = 2000000
  
mx = (n1 if (n1 > n2 and n1 > n3 and n1 > n4)  
         else (n2 if (n2 > n3 and n2 > n4 and n2>n1)  
         else (n3 if (n3 > n4 and n3>n2 and n3>n1) else n4))) 
  

print("Largest number among " + str(n1) + ", " + 
            str(n2) + ", " + str(n3) + " and " + 
            str(n4) + " is " + str(mx))

#----------output---------------

Largest number among 4000000, 1000000, 1500000 and 2000000 is 4000000

