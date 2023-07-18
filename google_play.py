# -*- coding: utf-8 -*-
"""
Created on Fri May  5 12:07:53 2023

@author: maitrid
"""

import pandas as pd
from google_play_scraper import Sort, reviews, reviews_all

google_play_ids = {'Netflix':'com.netflix.mediaclient'}

all_app_reviews = pd.DataFrame()

for app_name, app_id in google_play_ids.items():
    
    result, continuation_token = reviews(
        app_id,
        lang='en',
        country='us',
        sort=Sort.NEWEST, # other options - NEWEST, RATING and HELPFULNESS.
        count=30, # defaults to 100
        # filter_score_with=2 # filter based on rating
    )
    
    result, _ = reviews(
        app_id,
        continuation_token=continuation_token # defaults to None(load from the beginning)
    )
    
    app_data = []
    for res in result:
        data = dict()
        
        data['author'] = res['userName']
        data['date_reviewed'] = res['at'].date()
        data['rating'] = res['score']
        data['review'] = res['content']
        data['app'] = app_name
        data['found_helpful'] = res['thumbsUpCount']
        
        app_data.append(data)
        
    app_df = pd.DataFrame(app_data)
    
    all_app_reviews = pd.concat([all_app_reviews,app_df], ignore_index = True)
        
########### To get all time reviews ###########

result_all = reviews_all(
    app_id,
    sleep_milliseconds=0, # defaults to 0
    lang='en',
    country='us',
    sort=Sort.NEWEST, # defaults to Sort.MOST_RELEVANT
    # filter_score_with=5 # defaults to None(means all score)
)   

app_all_data = []
for res in result_all:
    all_data = dict()
    
    all_data['author'] = res['userName']
    all_data['date_reviewed'] = res['at'].date()
    all_data['rating'] = res['score']
    all_data['review'] = res['content']
    all_data['app'] = app_name
    all_data['found_helpful'] = res['thumbsUpCount']
    
    app_all_data.append(all_data)
    
app_all_data_df = pd.DataFrame(app_all_data)








