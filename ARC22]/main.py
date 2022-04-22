import math
from algoT import *
from in_out import *


def main(filename):
    # Read in waypoints
    waypoints = readWaypointFile(filename)

    # Determine path
    path = determinePath(waypoints)
    #print("Latitude: "+str(waypoints['latitude'][-1]))
    print(path)
    # Export path
    #CHALLEGE try to print alitiude
    for i in path:
        print(i)  # Print out order of Lat Long
        print("Latitude: "+str(waypoints['latitude'][i])
              + " Longitude: "+str(waypoints['longitude'][i])
              + " Altitude: "+str(waypoints['altitude'][i])
              + " waypointType: "+str(waypoints['waypointType'][i]))


#find home waypointType
#find waypoint clostet to home
#make home 1 second closets 2
#donato
if __name__ == '__main__':
	main("waypoint_1.txt")
