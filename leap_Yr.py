yr=int(input("Enter the year to check the leap year:"))
if (yr%4==0 and yr%100!=0 )or (yr%400==0):
    print ("yr",yr," is a leap year")
else:
    print("yr",yr," is a not leap year")