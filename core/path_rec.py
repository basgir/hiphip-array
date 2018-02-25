import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import linear_kernel,cosine_similarity

# Load city metadata
df_cities = pd.read_csv('./cities_mockup.csv',
                        low_memory=False, delimiter=";")

# load preferences gets replaced by json input
pref =pd.DataFrame({'city':pd.Series(['Input']),
                    'latitude':pd.Series([0]),
                    'longitude': pd.Series([0]),
                    'ID':pd.Series([999]),
                    'sport': pd.Series([1]),
                    'monuments': pd.Series([1]),
                    'nature': pd.Series([1]),
                    'food': pd.Series([0]),
                    'cheap': pd.Series([0]),
                    'normal': pd.Series([0]),
                    'expensive': pd.Series([1]),
                    'single': pd.Series([1]),
                    'couple': pd.Series([0]),
                    'family': pd.Series([0]),
                    })

df_cities = df_cities.append(pd.DataFrame(data = pref), ignore_index=True)
print(df_cities)

# decode preferences and prices  in set of boolean
#pref = pd.get_dummies(df_cities['Preference'])
#price = pd.get_dummies(df_cities['Price'])
#people = pd.get_dummies(df_cities['People'])

# delete old variables
#del df_cities['Preference']
#del df_cities['Price']

# add boolean to df
#df_cities = pd.concat([df_cities.reset_index(drop=True), pref], axis=1)
#df_cities = pd.concat([df_cities.reset_index(drop=True), price], axis=1)
#df_cities = pd.concat([df_cities.reset_index(drop=True), people], axis=1)


print(pref)
# look at data





# which variables should be included in similariy scoring?
df3 = df_cities[['sport','monuments','nature','cheap','normal', 'food',
                 'expensive', 'single', 'couple', 'family']]


# Compute the cosine similarity matrix
cosine_sim = cosine_similarity(df3)


#Construct a reverse map of indices and city names
indices = pd.Series(df_cities.index, index=df_cities['city']).drop_duplicates()

# Function that takes in city name as input and outputs most similar cities

def get_recommendations(name, cosine_sim=cosine_sim):
    # Get the index of the city that matches the title
    idx = indices[name]

    # Get the pairwise similarity scores of all cities with user preferences
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the city based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 5 most similar cities + user preference (will be deleted for output)
    sim_scores = sim_scores[0:6]

    # Get the city indices
    city_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    #return df_cities[['city', 'sport','nature', 'monuments', 'food','cheap', 'normal',
     #                 'expensive', 'single', 'couple', 'family']].iloc[city_indices]
    return(df_cities)[['city']].iloc[city_indices]
    # return cosine_sim




# get top 5 cities
# delete input row -> make sure input is not a recommendation
recom = (get_recommendations('Input'))
recom = recom[recom.city.str.contains("Input") == False]
print(recom)
