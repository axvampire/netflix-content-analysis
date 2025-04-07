import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('data/netflix_titles.csv')

# Data Cleaning
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['release_year'] = pd.to_datetime(df['release_year'], format='%Y', errors='coerce').dt.year
df['listed_in'] = df['listed_in'].str.split(',').apply(lambda x: [i.strip() for i in x])

# Set the title of the app
st.title("Netflix Content Analysis Dashboard")

# Sidebar filters
st.sidebar.header("Filters")
content_type = st.sidebar.selectbox('Select Content Type', ['All', 'Movie', 'TV Show'])
if content_type != 'All':
    df = df[df['type'] == content_type]

genres = df['listed_in'].explode().unique()
selected_genres = st.sidebar.multiselect("Select Genre(s)", genres, default=genres)
df = df[df['listed_in'].apply(lambda genres: any(genre in selected_genres for genre in genres))]

# Show the filtered data
st.write(f"Showing {len(df)} entries after applying filters.")
st.dataframe(df[['title', 'type', 'release_year', 'listed_in', 'rating']])

# Content growth over time (Movies vs TV Shows)
st.subheader("Content Growth Over Time")
content_count = df.groupby(['release_year', 'type']).size().unstack(fill_value=0)
content_count.plot(kind='line', figsize=(10, 6), ax=plt.gca())
plt.title('Netflix Content Growth (Movies vs TV Shows)')
plt.xlabel('Year')
plt.ylabel('Content Count')
st.pyplot()

# Genre distribution
st.subheader("Genre Distribution")
genre_counts = df['listed_in'].explode().value_counts()
sns.barplot(x=genre_counts.values, y=genre_counts.index, palette="viridis", ax=plt.gca())
plt.title('Most Popular Genres on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Genres')
st.pyplot()

# Ratings Distribution
st.subheader("Ratings Distribution")
rating_counts = df['rating'].value_counts()
st.bar_chart(rating_counts)

# Optional: Search for a specific movie/show
st.sidebar.header("Search for a Show/Movie")
search_query = st.sidebar.text_input("Enter a Title")
if search_query:
    result = df[df['title'].str.contains(search_query, case=False, na=False)]
    if not result.empty:
        st.write(f"**{result['title'].values[0]}**")
        st.write(result[['title', 'type', 'release_year', 'rating', 'listed_in']])
    else:
        st.write("No results found.")
