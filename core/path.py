import json
import math
from pprint import pprint
import random


data = json.load(open('locations.json'))

# pprint(data["cities"])
city_names = data["cities"].keys()
list_points = []

# The parameters
min_distance = 50 #km
max_distance = 200 #km

def city_to_coord (city_name):
    # Function to go from City Name to Coordinate Position
        # The Google Api can be used, for the time being a custom
        # conversion table is used

    data["cities"][city_name]
    return [data["cities"][city_name]["lat"],data["cities"][city_name]["lon"],data["cities"][city_name]["name"]]


for city in city_names:
    list_points.append(city_to_coord(city))

def find_closest_city (coord):
    # This function will find the closest city given a set of coordinates coord=[lat,lon]
        #Returns: The coordinates of the city and the distance

    city_found = False
    short_dist = 30
    distance = 60
    closest_coord = []
    for point in list_points:
        distance = math.sqrt((coord[0]-point[0])**2+(coord[1]-point[1])**2)*100

        if (distance < short_dist):
            city_found = True
            short_dist = distance
            closest_coord = point

    return [city_found, closest_coord,point[2]]

def distance_points (coord1,coord2):
    #This function returns a distance in km between two lat, lon coord

    return math.sqrt((coord1[0]-coord2[0])**2+(coord1[1]-coord2[1])**2)*100



def path_generating (coord1,coord2,L,d):
    #This function creates a set of points between 2 cities
    #L is the max distance, d is the min distance

    distance = distance_points(coord1,coord2)
    # print("The distance between ", coord1[2], " and ", coord2[2], " is ", distance)
    if (distance < d):
        # print("The last cities",  coord1[2], " & ", coord2[2], "are close enough")
        path.append(coord2)
    else:
        small_disp = []
        small_disp.append(coord1[0] + (random.random()*2*L-L)/100)
        small_disp.append(coord1[1] + (random.random()*2*L-L)/100)
        new_distance = distance_points(small_disp,coord2)
        closest_city = find_closest_city(small_disp)

        if (closest_city[0]==True):

            small_disp = closest_city[1:3][0]

            if (new_distance<distance):

                # print("We added a new city",closest_city[3:4])
                if (small_disp== coord2):
                    path.append(small_disp)
                    print("The algo is done")

                else:
                    path.append(small_disp)
                    path_generating(small_disp,coord2,max_distance,min_distance)

            else:
                path_generating (coord1,coord2,L,d)
        else:
            path_generating (coord1,coord2,L,d)



def generate_loc():

    return []

paths = []
def start_app():
    pathFound = False
    while (not pathFound):
        path = []

        coordA = [47.4240595,9.3282648,"St Gallen"]
        coordB = [46.2050242,6.1090691,"Geneva"]

        path.append(coordA)

        path_generating(coordA, coordB,max_distance,min_distance)
        # pprint(path)
        if(len(path)==4):
            pathFound = True;
            paths.append(path)

    ###
    ###          PATH FITNESS FUNCTION
    ###
start_app()


def price_estimate(path):
    # This function estimates the price of the travel in terms of the distance
    # 3 km is 1 chfr
    dist = 0.
    for i in range(1,len(path)):
        dist += distance_points(path[i-1],path[i])

    price = dist /3.
    return price #in swiss francs


def export_geojson(all_paths):
    #This function exports all the paths in a geojson file

    path = all_paths[0]
    json_obj = {"price":price_estimate(path),"steps":[]}
    for i in range(len(path)):
        json_obj["steps"].append({"city": path[i][2],"latitude":path[i][0],"longitude":path[i][1]})


    return json_obj

def run_pathfinder():
    return export_geojson(paths)

pprint(run_pathfinder())
