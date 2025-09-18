import os
import pathlib
from collections import deque
from itertools import combinations

import geopy as gpd
import pandas as pd

import numpy as np

import folium
import openrouteservice as ors
from shapely.geometry import Point, LineString

import warnings
warnings.filterwarnings('ignore')

# Declare all global variables

with open(r"api\openrouteservice.pem") as f_in:
    ORS_API = f_in.read()

PROFILE = "driving-car"
ORS_OPTIONS = {"avoid_borders": "all"}

MAX_PER_MIN = 30
WINDOW_SEC = 60.0
EPS = 0.02
BASE_SLEEP = 0.20

MAX_PER_SEC = 1
SEC_WINDOW = 1.0

MAX_RETRIES = 3
WRITE_POINTS = True

SNAP_RADIUS_M = 10000
USE_RADIUSES = [-1, -1]

town_halls_coor = pd.read_excel("data/Coordinates/coor.xlsx")
town_halls_coor['coordinates'] = town_halls_coor.apply(lambda row: [row['lon'], row['lat']], axis=1)
coords = tuple(town_halls_coor['coordinates'])
pairs_coords = list(combinations(coords, 2))


m = folium.Map(
    location=list(reversed([100.5019413, 13.7533776])),
    tiles='Cartodb Positron',
    zoom_start=13
)

test_coords = [[100.5019413, 13.7533776], [98.9173938, 8.0590009]]

client = ors.Client(key=ORS_API)
test_route = client.directions(
    coordinates=test_coords, 
    profile='driving-car',
    optimize_waypoints=True,
    format='geojson',
    instructions=False,
    validate=False,
    radiuses=USE_RADIUSES)

folium.PolyLine(locations=[list(reversed(coord)) for coord in test_route['features'][0]['geometry']['coordinates']], color='blue').add_to(m)

m