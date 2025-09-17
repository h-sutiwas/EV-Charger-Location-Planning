import os
from collections import deque

import geopy as gp
import pandas as pd

import numpy as np

import seaborn as sns
import matplotlib as plt

import openrouteservice as ors
from shapely.geometry import Point, LineString

import warnings
warnings.filterwarnings('ignore')

with open(r"api\openrouteservice.pem") as f_in:
    ORS_API = f_in.read()

PROFILE = "driving-car"
ORS_OPTIONS = {"avoid_borders": "all"}

client = ors.Client(key=ORS_API)
