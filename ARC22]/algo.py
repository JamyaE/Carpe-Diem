import math
import numpy as np

waypoint = []

#if __name__ == '__main__':
#s	main("waypoint_1.txt")


def determinePath(waypoint):
    # COMPLETE HERE
    #42.27690 N -83.73063 E 10 H
    #42.33905 N -83.06404 E 10 Ax
    #42.63678 N -83.29613 E 10 C
    #42.29201 N -83.71624 E 10 B
    #42.29198 N -83.71561 E 10 A

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
    UminimumDistances = min(Distances)
    P1 = UminimumDistances, "DistanceHtoB"
    print(UminimumDistances, "UminimumDistances")
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
    SminimumDistances = min(Distances2)
    print("SminimunDistances", SminimumDistances)
    P2 = SminimumDistances, "DistanceBtoA2"
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
    TminimumDistances = min(Distances3)
    print("TminimunDistances", TminimumDistances)
    P3 = TminimumDistances, "DistanceA2toA"
    print("DistanceA2toA", DistanceA2toA)
    print("DistanceA2toC", DistanceA2toC)

##################################################
    DistanceAtoC = np.linalg.norm(waypointA-waypointC)
    Distances4 = [DistanceAtoC]
    FminimumDistances = Distances4
    P4 = FminimumDistances, "DistanceAtoC"

    Path = ([P1, P2, P3, P4])
    print(Path)
    print("This is the waypoint order")
    return Path
    order = [0, 1, 2, 3, 4]
    return order
