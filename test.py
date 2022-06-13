carname="Swift"
caryear="2000"
carcolor="white"
file = open("car.txt", "w")
file.write("Car Name = " + carname + "\n" +"Car Year = "+caryear + "\n"+"Car color = "+carcolor )
file.close