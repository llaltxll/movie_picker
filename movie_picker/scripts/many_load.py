import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from mvpkr.models import Country, Language, ProductionComp, ReasonOfDeath, Names, Movies, GenersOfMovies, TitlePrincipal

def try_int(num):
    try:
        y = int(num)
    except:
        y = None
    return y

def try_float(num):
    try:
        y = float(num)
    except:
        y = None
    return y

def try_date(date):
    try:
        d = datetime.strptime(date, '%Y-%m-%d')
    except:
        d = None
    return d

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
            height = try_int(row[3]),
            bio = row[4],
            birth_details = row[5],
            date_of_birth = try_date(row[6]),
            place_of_birth = row[7],
            death_details = row[8],
            date_of_death = try_date(row[9]),
            place_of_death = row[10],
            reason_of_death_id = reason_of_death,
            # spouses_string not in model
            spouses = try_int(row[13]),
            divorces = try_int(row[14]),
            spouses_with_children = try_int(row[15]),
            children = try_int(row[16]),
            imdb_name_id = try_int(row[0][2:]),
            )
        name.save()