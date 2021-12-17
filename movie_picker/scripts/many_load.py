import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site, Category, State, Region, Iso


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    tables = [Site, Category, State, Region, Iso]
    for t in tables: t.objects.all().delete()

    for row in reader:
        print(row)

        c, created = Category.objects.get_or_create(name=row[7])
        s, created = State.objects.get_or_create(name=row[8])
        r, created = Region.objects.get_or_create(name=row[9])
        i, created = Iso.objects.get_or_create(name=row[10])

        try:
            y = int(row[3])
        except:
            y = None

        float_vals = list()
        for value in row[4:7]:
            try:
                float_vals.append(float(value))
            except:
                float_vals.append(None)
        print('float_vals: ', float_vals)

        site = Site(
            name=row[0],
            description=row[1], 
            justification=row[2], 
            year=y, 
            longitude=float_vals[0], 
            latitude=float_vals[1], 
            area_hectares=float_vals[2],
            category=c, 
            state=s,
            region=r,
            iso=i,
            )
        site.save()