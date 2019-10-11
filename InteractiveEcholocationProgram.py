import matplotlib.pyplot as plt
#Functions
def mackenzie_sos(temp,depth,salinity):
    soundSpeed = 1448.96 + (4.591 * temp) - (5.304 * pow(10,-2) * pow(temp,2)) + (2.374 * pow(10,-4) * pow(temp,3)) + (1.630 * pow(10,-2) * depth)
    + (1.675 * pow(10,-7) * pow(depth,2)) - (1.025 * pow(10,-2) * temp * (salinity - 35)) - (7.139 * pow(10,-13) * temp * pow(depth,3)) ;
    return  soundSpeed;
    
def sal_of_seawater(latitude):
    salinity = 35;
    return salinity;
    
def temp_of_seawater(latitude,depth):
    temprature =  20;
    return temprature;

def dist_of_object(returnTime,speedSound):
    distance = (returnTime/2) * speedSound;
    return distance;


#Welcome Screen
print("Welcome to the system which models certain aspects of echolocation");
print("Please enter your patron type:");
print("0 for Rookie");
print("1 for Seasoned");
print("2 for Grizzled");

choice=int(input());

if choice == 0:
    patronType = "Rookie";
elif choice == 1:
    patronType = "Seasoned";
elif choice == 2:
    patronType = "Grizzled";
else:
    patronType = "Rookie";
    
print("Welcome "+patronType+" to the system");
go_again=1;

while go_again == 1:
    print("Enter latitude in the interval[-90,90]")
    latitude = float(input());
    salWater = sal_of_seawater(latitude);
    print("The Salinity of water at latitude " + str(latitude) + " is " + str(salWater) + " parts per thousand");
    if patronType.__eq__("Seasoned") | patronType.__eq__("Grizzled"):
        #Display a plot of temprature versus depth
        print("Inside plot");
        
        
    print("Enter depth (in 0 to 8000 meters)");
    depth = float(input());
    tempWater = temp_of_seawater(latitude,depth);
    print("Temperature at latitude " + str(latitude) + " and depth " + str(depth) + " is " + str(tempWater) + " degree celcius");
    soundSpeed = mackenzie_sos(tempWater,depth,salWater);
    print("Speed of sound at latitude " + str(latitude) + " and depth " + str(depth) + " is " + str(soundSpeed) + " m\s");
    print("Enter return time to calculate distance");
    retTime = float(input());
    objectDistance = float(dist_of_object(retTime, soundSpeed));
    print("The distance of object for return of time " + str(retTime) + " and speed of sound " + str(soundSpeed) + " is " + str(objectDistance) + " meters")
    
    print("Press 1 to enter new data or Press anything between (2 to 9) to quit.");
    go_again = int(input());
            

print("Thanks for using the system")
exit;
