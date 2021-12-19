# movie_picker
I intend to use this https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset movie data-set to create a Django app that will help one find movies they might want to watch based on their favorite movies that are in the database.
functionality:
Users may login, search the database and brows movies with an endless scroll
Users may favorite and rank movies
Users will get suggestions for movies that are likely to be a good match based on user's favorites
More like this.. (movie or movies up to two)
some of the tasks ahead:
create a data model with one-to-many (movie>-- country) and many-to-many (movie>-<genre)
create views that will enable updating the endless scroll as the user scrolls down through the list view
try using some machine learning techniques to find some interesting correlation models in the data-set
apply those  models to create effective search/suggestion algorithms to enable the core functionality
