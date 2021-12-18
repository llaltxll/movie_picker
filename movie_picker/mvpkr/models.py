from django.db import models

# Create your models here.
# M = Index(['imdb_title_id', 'title', 'original_title', 'year', 'date_published',
#        'genre', 'duration', 'country', 'language', 'director', 'writer',
#        'production_company', 'actors', 'description', 'avg_vote', 'votes',
#        'budget', 'usa_gross_income', 'worlwide_gross_income', 'metascore',
#        'reviews_from_users', 'reviews_from_critics'],
#       dtype='object')

# N = Index(['imdb_name_id', 'name', 'birth_name', 'height', 'bio', 'birth_details',
#        'date_of_birth', 'place_of_birth', 'death_details', 'date_of_death',
#        'place_of_death', 'reason_of_death', 'spouses_string', 'spouses',
#        'divorces', 'spouses_with_children', 'children'],
#       dtype='object')

class Movies(models.Model) :
	title = models.CharField(max_length=128)
	year = models.IntegerField()
	duration models.IntegerField()
	country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
	language_id = models.ForeignKey(Language, on_delete=models.CASCADE)
	prod_company_id = models.ForeignKey(ProductionComp, on_delete=models.CASCADE)
	votes = models.IntegerField()
	avg_vote float
	gross_income = models.IntegerField()
	n_user_reviews = models.IntegerField()
	n_critic_reviews = models.IntegerField()
	imdb_title_id = models.IntegerField()
	# imdb ids are stored as ints the actual id can be reconstructed later
	# tt#######
	
	# many-to-many fileds below:
	generes = models.ManyToManyField('Geners', through='GenersOfMovies')
	credits = models.ManyToManyField('Names', through='TitlePrincipal')

	def __str__(self) :
		return self.title

class Country(models.Model) :
	name = models.CharField(max_length=128)

	def __str__(self) :
		return self.name

class Language(models.Model) :
	name = models.CharField(max_length=128)

	def __str__(self) :
		return self.name

class ProductionComp(models.Model) :
	name = models.CharField(max_length=128)

	def __str__(self) :
		return self.name

class Geners(models.Model):
	name = models.CharField(max_length=128)

	def __str__(self) :
		return self.name

# https://www.geeksforgeeks.org/datefield-django-models/#field-options
class Names(models.Model):
	name = models.CharField(max_length=128)
	height = models.IntegerField()
	bio = models.CharField(max_length=128)
	birth_details = models.CharField(max_length=128)
	date_of_birth = models.DateField()
	place_of_birth = models.CharField(max_length=128)
	death_details = models.CharField(max_length=128)
	date_of_death = models.DateField()
	place_of_death = models.CharField(max_length=128)
	reason_of_death_id = models.ForeignKey(ReasonOfDeath, on_delete=models.CASCADE)
	spouses = models.IntegerField()
	divorces = models.IntegerField()
	spouses_with_children = models.IntegerField()
	children = models.IntegerField()
	imdb_name_id = models.IntegerField()
	# imdb ids are stored as ints the actual id can be reconstructed later
	# nn#######

	def __str__(self) :
		return self.name
class ReasonOfDeath(models.Model):
	name = models.ForeignKey(Geners, on_delete=models.CASCADE)

	def __str__(self) :
		return self.name

class GenersOfMovies(models.Model):
	movie_id = models.ForeignKey(Movies, on_delete=models.CASCADE)
	genere_id = models.ForeignKey(Geners, on_delete=models.CASCADE)
	def __str__(self) :
		return self.movie_id +', '+ self.genere_id

class TitlePrincipal(models.Model):
	movie_id = models.ForeignKey(Movies, on_delete=models.CASCADE)
	name_id = models.ForeignKey(Names, on_delete=models.CASCADE)
	ordering = models.IntegerField()
	category = models.CharField(max_length=128)
	def __str__(self) :
		return self.movie_id +', '+ self.name_id

