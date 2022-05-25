import math


print("Akar-akar persamaan kuadrat")
print("aX^2 + bX + C")

a= int(input("\nMasukan a: "))
b= int(input("Masukan b: "))
c= int(input("Masukan c: "))

D = (b*b)-(4*a*c)

if D > 0:
    x1= (-b+ math.sqrt(D)) / (2*a)
    x2= (-b- math.sqrt(D)) / (2*a)
    print ("\nx1 = %d" %x1)
    print ("x2 = %d" %x2)
    
elif D==0:
    x1= (-b+ math.sqrt(D)) / (2*a)
    x2= x1
    print ("\nx1 = %d" %x1)
    print ("x2 = %d" %x2)

else:
    print("\nAkar imajiner")

