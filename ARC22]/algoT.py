import math
import numpy as np


#if __name__ == '__main__':
#s	main("waypoint_1.txt")


def determinePath(waypoint):
    order = []
    waypointType = waypoint['waypointType']

    #print("waypointType", waypointType)
    #for index in (waypointType):
    #    if index == 'H':
    Hindex = waypointType.index('H')
    print('Hindex', Hindex)

    # COMPLETE HERE
    #42.27690 N -83.73063 E 10 H
    #42.33905 N -83.06404 E 10 Ax
    #42.63678 N -83.29613 E 10 C
    #42.29201 N -83.71624 E 10 B
    #42.29198 N -83.71561 E 10 A
    #if waypointType: i=H save the value?

    Lat0 = float(waypoint['latitude'][0-Hindex])
    Log0 = float(waypoint['longitude'][0-Hindex])
    Alt0 = float(waypoint['altitude'][0-Hindex])

    Lat1 = float(waypoint['latitude'][1-Hindex])
    Log1 = float(waypoint['longitude'][1-Hindex])
    Alt1 = float(waypoint['altitude'][1-Hindex])

    Lat2 = float(waypoint['latitude'][2-Hindex])
    Log2 = float(waypoint['longitude'][2-Hindex])
    Alt2 = float(waypoint['altitude'][2-Hindex])

    Lat3 = float(waypoint['latitude'][3-Hindex])
    Log3 = float(waypoint['longitude'][3-Hindex])
    Alt3 = float(waypoint['altitude'][3-Hindex])

    Lat4 = float(waypoint['latitude'][4-Hindex])
    Log4 = float(waypoint['longitude'][4-Hindex])
    Alt4 = float(waypoint['altitude'][4-Hindex])

    #waypointType = waypoint['waypointType']
    #for index in range(len(waypointType)):
    #print(waypointType[index])

    waypointH = np.array((Lat0, Log0, Alt0))
    waypointA = np.array((Lat1, Log1, Alt1))
    waypointC = np.array((Lat2, Log2, Alt2))
    waypointB = np.array((Lat3, Log3, Alt3))
    waypointA2 = np.array((Lat4, Log4, Alt4))

    #if waypointDict{waypointType[i]}
    # if i=H save value

    DistanceHtoA = np.linalg.norm(waypointH-waypointA)
    DistanceHtoC = np.linalg.norm(waypointH-waypointC)
    DistanceHtoB = np.linalg.norm(waypointH-waypointB)
    DistanceHtoA2 = np.linalg.norm(waypointH-waypointA2)
    Distances = [DistanceHtoA, DistanceHtoB,
                 DistanceHtoC, DistanceHtoA2]
    minimumDistances1 = min(Distances)
    P1 = minimumDistances1, "DistanceHtoB"
    print(minimumDistances1, "minimumDistances1")
    #print("DistanceHtoA ", DistanceHtoA)
    #print("DistanceHtoC", DistanceHtoC)
    #print("DistanceHtoA2", DistanceHtoA2)
    #print("DistanceHtoB", DistanceHtoB)
    #closestwaypoint = Distances.index(minimumDistances)
    #Path = []
    #Path = Path.append(closestwaypoint)
    #Arranged = np.array([[DistanceHtoA, DistanceHtoC,
    #DistanceHtoB, DistanceHtoA2]])

    #print(np.sort(Arranged))

    ####################################
    DistanceBtoC = np.linalg.norm(waypointB-waypointC)
    DistanceBtoA = np.linalg.norm(waypointB-waypointA)
    DistanceBtoA2 = np.linalg.norm(waypointB-waypointA2)
    Distances2 = [DistanceBtoA, DistanceBtoC, DistanceBtoA2]
    minimumDistances2 = min(Distances2)
    print("minimunDistances2", minimumDistances2)
    P2 = minimumDistances2, "DistanceBtoA2"
    print("DistanceBtoC", DistanceBtoC)
    print("DistanceBtoA", DistanceBtoA)
    print("DistanceBtoA2", DistanceBtoA2)
    #Arranged2 = np.array([[DistanceAtoC,
    # DistanceAtoB, DistanceAtoA2]])

    #print(np.sort(Arranged2))

    #####################################################

    DistanceA2toA = np.linalg.norm(waypointA2-waypointA)
    DistanceA2toC = np.linalg.norm(waypointA2-waypointC)
    Distances3 = [DistanceA2toA, DistanceA2toC]
    minimumDistances3 = min(Distances3)
    print("minimunDistances3", minimumDistances3)
    P3 = minimumDistances3, "DistanceA2toA"
    print("DistanceA2toA", DistanceA2toA)
    print("DistanceA2toC", DistanceA2toC)

    ##################################################
    DistanceAtoC = np.linalg.norm(waypointA-waypointC)
    Distances4 = [DistanceAtoC]
    minimumDistances4 = Distances4
    P4 = minimumDistances4, "DistanceAtoC"

    Path = ([P1, P2, P3, P4])
    print(Path)
    #print("This is the waypoint order")
    #return Path
    order = [0, 1, 2, 3, 4]
    return order
