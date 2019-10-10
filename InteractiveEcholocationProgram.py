#Functions
def mackenzie_sos(self,temp,depth,salinity):
    soundSpeed = 1448.96 + 4.591 * temp - 5.304 * 0.01;
    return  soundSpeed;
    
def sal_of_seawater(self,latitude):
    salinity = 0;
    return salinity;
    
def temp_of_seawater(self,latitude,depth):
    temprature =  0;
    return temprature;

def dist_of_object(self,returnTime,speedSound):
    distance = (returnTime/2) * speedSound;
    return distance;


#Welcome Screen
print("Welcome to the system which models certain aspects of echolocation");
print("Please enter your patron type:");
print("0 for Rookie");
print("1 for Seasoned");
print("2 for Grizzled");

choice=int(input());
patronType = "";

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

if go_again == 1:
    print("Enter latitude in the interval[-90,90]")
    latitude = float(input());
    salWater = sal_of_seawater(latitude);
    print("The Salinity of water at latitude " + str(latitude) + " is " + str(salWater) + " parts per thousand");
    if patronType.__eq__("Seasoned") | patronType.__eq__("Grizzled"):
        #Display a plot of temprature versus depth
        
        print("Enter depth (in meters)");
        depth = float(input());
        tempWater = temp_of_seawater(latitude,depth);
        print("Temperature at latitude " + str(latitude) + " and depth " + str(depth) + " is " + str(tempWater) + "degree celcius");
        soundSpeed = mackenzie_sos(tempWater,depth,salWater);
        print("Speed of sound at latitude " + str(latitude) + " and depth " + str(depth) + " is " + str(soundSpeed) + " meters\second");
        print("Enter return time to calculate distance");
        retTime = float(input());
        objectDistance = float(dist_of_object(retTime, soundSpeed));
        print("The distance of object for return of time " + str(retTime) + " and speed of sound " + str(soundSpeed) + " is " + str(objectDistance) + "meters")
        
        go_again = int(input("Press 1 to enter new data or Press anything else to quit."));
        #if go_again == 1:
            
    
else:
    print("Thanks for using the system")
    exit;


