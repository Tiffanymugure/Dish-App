from app import app
from app import app
import urllib.request,json
from .models import 


# Getting api key
api_key = app.config['FOOD-DATABASE_API_KEY']

# Getting the food-database base url
base_url = app.config["FOOD-DATABASE_API_BASE_URL"]

#Getting api key
api_key = app.config['NUTRITION-ANALYSIS_API_KEY']

# Getting the nutrition analysis base url
base_url = app.config["NUTRITION-ANALYSIS_API_BASE_URL"]

#Getting api key
api_key = app.config['RECIPE-SEARCH_API_KEY']

# Getting the recipe search base url
base_url = app.config["RECIPE-SEARCH_API_BASE_URL"]
