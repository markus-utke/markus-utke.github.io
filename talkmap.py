
# %%

import glob
import getorg
from geopy import Nominatim
import pandas as pd
g = glob.glob("*.md")

#  %%
geocoder = Nominatim(user_agent='me')
location_dict = {}
location = ""
permalink = ""
title = ""

df = pd.read_excel('talks.ods')
print(df)

#%%
location_dict = {}
for i, row in df.iterrows():
    location_string = ''
    if not pd.isna(row['location_details']):
        location_string += row['location_details'] + ", "
    elif not pd.isna(row['venue']):
        location_string += row['venue'] + ", "
    if not pd.isna(row['location']):
        location_string += row['location']
    
    if len(location_string) > 0:
        print(location_string)
   
    location_dict[location_string] = geocoder.geocode(location_string)
    
#%%

m = getorg.orgmap.create_map_obj()
getorg.orgmap.output_html_cluster_map(location_dict, folder_name="talkmap", hashed_usernames=False)
