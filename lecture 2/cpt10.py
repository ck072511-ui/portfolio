# transportation mode selection :
# problem : choose a mode of transport based on the distance (ex.- <3 km : walk,3-15 km: bike, > 15 km :car)

dis = int(input("enter distance for killometer :="))

if (dis < 3):
    dis = 'go to walk'
elif (dis >= 3 and dis < 15):
    dis = 'go to bike' 
else:
    dis = 'go to car' 

print("traveling distance accoding :=",dis)