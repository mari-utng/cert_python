year = int(input("Introduce un año:"))

if not(year % 4 ==0):
   print ('Año común')
elif not (year % 100 ==0):
    print ('Año Bisiesto')
#if not (year % 400 == 0):
 #  print ('Año común')
    
