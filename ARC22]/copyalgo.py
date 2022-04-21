import math
import numpy as np


def determinePath(waypoint):
	# COMPLETE HERE

    order = [0, 1, 2, 3, 4]

    waypointH = np.array((42.27690, -83.73063, 10))
    waypointA = np.array((42.33905, -83.73063, 10))
    waypointC = np.array((42.63678, -83.29613, 10))
    waypointB = np.array((42.29201, -83.71624, 10))
    waypointA2 = np.array((42.29198, -83.71561, 10))

    DistanceHtoA = np.linalg.norm(waypointH-waypointA)
    DistanceHtoC = np.linalg.norm(waypointH-waypointC)
    DistanceHtoB = np.linalg.norm(waypointH-waypointB)
    DistanceHtoA2 = np.linalg.norm(waypointH-waypointA2)
    Distances = [DistanceHtoA, DistanceHtoB, DistanceHtoC, DistanceHtoA2]
    minimumDistances = min(Distances)
    print("minimunDistances", minimumDistances)
    print("DistanceHtoA ", DistanceHtoA)
    print("DistanceHtoC", DistanceHtoC)
    print("DistanceHtoB", DistanceHtoB)
    print("DistanceHtoA2", DistanceHtoA2)
    closestwaypoint = Distances.index(minimumDistances)
    Path = []
    Path = Path.append(closestwaypoint)
    Arranged = np.array([[DistanceHtoA, DistanceHtoC,
                        DistanceHtoB, DistanceHtoA2]])

    print(np.sort(Arranged))

    #waypointH = np.array(())
    #var = (float(waypoint['longitude'][0])
    # - float(waypoint['longitude'][1])) ** 2
#    var2 = (float(waypoint['latitude'][0])-float(waypoint['latitude'][1]))**2
    #print("var=", var)
    #print("var2=", var2)

    #print(math.sqrt(var+var2))
#print(float(waypoint['longitude'][0]))
#d1 = math.sqrt((float(waypoint['longitude'][0])-float(waypoint['longitude'][0]))
#  ** 2)+((float(waypoint['latitude'][1])-(float(waypoint['latitude'][1])**2)))
#d2 =
#print(order)
#d = math.sqrt(((x2 - x1)**2) + ((y2-y1)**2))
#print("d=", d)
#dmin =
##min_index =

#if (d < dmin):
#dmin = d

#PLACEHOLDER, just send out current list

#CHALLEGE make a function to sort the waypoints
#math.sqrt((a+b)**+(a+b)**))=distance formula

#if(d < dmin)
#dmin = index

#if(max index == 5):
#appened to new_list = dmin_index


#for items in old_list
    return order
