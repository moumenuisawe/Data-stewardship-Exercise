import pandas as pd
import seaborn as sns

movie = pd.read_csv('Data/Row/movie_ratings.csv', names=['index', 'Movie Name', 'year', 'imdp', 'metascore','votes'])
print(movie.head())
