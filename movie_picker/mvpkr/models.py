from django.db import models

# Create your models here.
# Index(['imdb_title_id', 'title', 'original_title', 'year', 'date_published',
#        'genre', 'duration', 'country', 'language', 'director', 'writer',
#        'production_company', 'actors', 'description', 'avg_vote', 'votes',
#        'budget', 'usa_gross_income', 'worlwide_gross_income', 'metascore',
#        'reviews_from_users', 'reviews_from_critics'],
#       dtype='object')

class Movies(models.Model) :
	title = models.CharField(max_length=128)
	