#importing Library
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from wordcloud import WordCloud

# Loading the dataset
file_path = r"E:\Research\PRODIGY_DS_02\PRODIGY_DS_02\Netflix_dataset\netflix_titles.csv"
data = pd.read_csv(file_path)

# Cleaning 'rating' column to remove unwanted durations (like '74 min', '84 min', '66 min')
data['rating'] = data['rating'].apply(lambda x: x if isinstance(x, str) and not any(char.isdigit() for char in x) else np.nan)
data = data.dropna(subset=['rating'])

# Checking for missing values in the dataset again
missing_values = data.isnull().sum()

# Getting the distribution of 'type' (Movie vs TV Show)
type_counts = data['type'].value_counts()

# Getting the distribution of 'rating'
rating_counts = data['rating'].value_counts()

# Getting the distribution of 'release_year'
release_year_counts = data['release_year'].value_counts().sort_index()

# Getting the distribution of 'duration'
# Extracting the numeric part of the duration (for movies, the number of minutes, for TV shows, the number of seasons)
data['duration_numeric'] = data['duration'].apply(lambda x: ''.join(filter(str.isdigit, str(x))) if pd.notnull(x) else '0')
data['duration_numeric'] = pd.to_numeric(data['duration_numeric'], errors='coerce')

# Plotting each visualization individually

# 1. Distribution of 'type'
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='type', palette='Set2')
plt.title('Distribution of Movie vs TV Show', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# 2. Distribution of 'rating'
plt.figure(figsize=(10, 6))
sns.countplot(data=data, y='rating', palette='Set2')
plt.title('Distribution of Content Ratings', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# 3. Distribution of 'release_year' 
data_after_2000 = data[data['release_year'] > 2000]
release_year_counts_after_2000 = data_after_2000['release_year'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
sns.countplot(data=data_after_2000, x='release_year', palette='Set2', order=release_year_counts_after_2000.index)
plt.title('Distribution of Release Year (After 2000)', fontsize=14, fontweight='bold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. Distribution of 'duration_numeric'
movies = data[data['type'] == 'Movie']
tv_shows = data[data['type'] == 'TV Show']
tv_shows['duration_numeric'] = tv_shows['duration_numeric'].astype(int)
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.histplot(data=movies, x='duration_numeric', kde=True, bins=20, color='blue')
plt.title('Distribution of Movie Duration (Minutes)', fontsize=14, fontweight='bold')
plt.xlabel('Duration (Minutes)')
plt.ylabel('Count')
plt.subplot(1, 2, 2)
sns.histplot(data=tv_shows, x='duration_numeric', kde=True, bins=20, color='green')
plt.title('Distribution of TV Shows (Number of Seasons)', fontsize=14, fontweight='bold')
plt.xlabel('Number of Seasons')
plt.ylabel('Count')
plt.tight_layout()
plt.show()


# 5. Number of movies/shows by 'listed_in' category 
top_genres = data['listed_in'].str.split(',').explode().str.strip().value_counts().head(10)
plt.figure(figsize=(8, 6))
top_genres.plot(kind='bar', color='teal')
plt.title('Top 10 Netflix Genres', fontsize=14, fontweight='bold')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# 6. Top 10 Genres by Content Type Based Movies/TV show
movies_data = data[data['type'] == 'Movie']
tv_shows_data = data[data['type'] == 'TV Show']
movie_genre_counts = movies_data['listed_in'].str.split(',').explode().str.strip().value_counts()
tv_show_genre_counts = tv_shows_data['listed_in'].str.split(',').explode().str.strip().value_counts()
top_movie_genres = movie_genre_counts.head(10)
top_tv_show_genres = tv_show_genre_counts.head(10)
plt.figure(figsize=(8, 6))
top_movie_genres.plot(kind='bar', color='darkblue')
plt.title('Top 10 Most Common Genres in Movies', fontsize=14, fontweight='bold')
plt.xlabel('Genres', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
plt.figure(figsize=(8, 6))
top_tv_show_genres.plot(kind='bar', color='darkgreen')
plt.title('Top 10 Most Common Genres in TV Shows', fontsize=14, fontweight='bold')
plt.xlabel('Genres', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# 7. Distribution of ratings by release year 
filtered_data = data[data['release_year'] > 2000]
plt.figure(figsize=(12, 6))
sns.countplot(data=filtered_data, x='release_year', hue='rating', palette='Set1')
plt.title('Distribution of Ratings by Release Year (After 2000)', fontsize=14, fontweight='bold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 8. Country vs Content Type (Movie vs TV Show)
plt.figure(figsize=(12, 6))
sns.countplot(data=data, x='country', hue='type', order=data['country'].value_counts().head(10).index, palette='Set2')
plt.title('Distribution of Movie vs TV Show by Country', fontsize=14, fontweight='bold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 9. Relationship between 'duration_numeric' and 'release_year'
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='release_year', y='duration_numeric', hue='type', palette='Set2')
plt.title('Duration vs Release Year', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# 10. Word Cloud of Content Descriptions
text = ' '.join(data['description'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Netflix Content Descriptions', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# 11. Content Type and Ratings Distribution
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='rating', hue='type', palette='Set1')
plt.title('Ratings Distribution by Content Type (Movie vs TV Show)', fontsize=14, fontweight='bold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Number of Movies and TV Shows Added Each Year (After 2000)
data['date_added'] = pd.to_datetime(data['date_added'], errors='coerce')
data_filtered = data[data['date_added'].dt.year > 2000]
data_grouped = data_filtered.groupby([data_filtered['date_added'].dt.year, 'type']).size().unstack(fill_value=0)
ax = data_grouped.plot(kind='bar', figsize=(12, 6), position=0)
ax.set_title('Number of Movies and TV Shows Added Each Year (After 2000)')
ax.set_xlabel('Year')
ax.set_ylabel('Count')
ax.set_xticks(range(len(data_grouped.index)))
ax.set_xticklabels(data_grouped.index, rotation=45)
plt.tight_layout()
plt.show()


# Summarize missing values
missing_values_summary = missing_values[missing_values > 0]
print("Missing values in the dataset:")
print(missing_values_summary)
