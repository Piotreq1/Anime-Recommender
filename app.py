import pandas as pd
import numpy as np
import streamlit as st
import requests
from bs4 import BeautifulSoup
from PIL import Image
import io

anime_df = pd.read_csv('data_tags.csv')
cosine_sim = np.load('cosine_sim.npy')


def recommend_movies(title):
    index = anime_df[anime_df['name'] == title].index[0]
    dist = list(enumerate(cosine_sim[index]))
    dist.sort(reverse=True, key=lambda x: x[1])
    anime_list = []
    for i in dist[1:6]:
        anime_list.append((anime_df.iloc[i[0]]['name'], anime_df.iloc[i[0]]['animeID']))
    return anime_list


def get_poster(anime, column):
    name = anime[0].replace(" ", "_")
    url = "https://myanimelist.net/anime/" + str(anime[1]) + "/" + name
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    img_tag = soup.find('img', {'alt': anime[0]})
    img_url = img_tag['data-src']
    img_response = requests.get(img_url)
    img = Image.open(io.BytesIO(img_response.content))
    column.image(img)
    return url


st.title('Anime Recommender')
movies = anime_df['name'].tolist()
movie_title = st.selectbox('Select a anime title', movies)

if st.button('Recommend'):
    movies = recommend_movies(movie_title)
    col = st.columns(5)
    for idx, movie in enumerate(movies):
        url = get_poster(movie, col[idx])
        col[idx].write(f"[{movie[0]}]({url})")
