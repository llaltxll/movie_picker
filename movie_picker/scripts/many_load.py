import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from mvpkr.models import Country, Language, ProductionComp, ReasonOfDeath, Names, Movies, GenersOfMovies, TitlePrincipal


def run():
    fhand = open('IMDB/IMDb_names.csv', encoding="utf8")
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    tables = [Country, Language, ProductionComp, ReasonOfDeath, Names, Movies, GenersOfMovies, TitlePrincipal]
    for t in tables: t.objects.all().delete()
    index = 1
    for row in reader:
        print(index, ": "+str(row[11]))
        index += 1
        reason_of_death, created = ReasonOfDeath.objects.get_or_create(name=row[11])
        print(created)

        name = Names(
            name = row[1],
            height = models.IntegerField(),
            bio = models.CharField(max_length=256),
            birth_details = models.CharField(max_length=256),
            date_of_birth = models.DateField(),
            place_of_birth = models.CharField(max_length=128),
            death_details = models.CharField(max_length=256),
            date_of_death = models.DateField(),
            place_of_death = models.CharField(max_length=128),
            reason_of_death_id = models.ForeignKey(ReasonOfDeath, on_delete=models.CASCADE),
            spouses = models.IntegerField(),
            divorces = models.IntegerField(),
            spouses_with_children = models.IntegerField(),
            children = models.IntegerField(),
            imdb_name_id = models.IntegerField(),
            )