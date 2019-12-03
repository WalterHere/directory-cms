# Generated by Django 2.2.6 on 2019-12-02 11:07

from django.db import migrations

DATA = {
    'Australia - New Zealand': (
        ('Australia', 'australia'),
        ('New Zealand', 'new-zealand'),
        ('Papua New Guinea', 'papua-new-guinea'),
        ('Fiji', 'fiji')
    ),
    'Central European Network': (
        ('Croatia', 'croatia'),
        ('Slovakia', 'slovakia'),
        ('Slovenia', 'slovenia'),
        ('Czechia', 'czechia'),
        ('Poland', 'poland'),
        ('Romania', 'romania'),
        ('Serbia', 'serbia'),
        ('Bulgaria', 'bulgaria'),
        ('Hungary', 'hungary'),
        ('Bosnia and Herzegovina', 'bosnia-and-herzegovina')
    ),
    'China Region': (('China', 'china'), ('Hong Kong', 'hong-kong')),
    'Latin America': (
        ('Uruguay', 'uruguay'),
        ('Guyana', 'guyana'),
        ('Jamaica', 'jamaica'),
        ('Trinidad and Tobago', 'trinidad-and-tobago'),
        ('Bolivia', 'bolivia'),
        ('Brazil', 'brazil'),
        ('Chile', 'chile'),
        ('Colombia', 'colombia'),
        ('Costa Rica', 'costa-rica'),
        ('Cuba', 'cuba'),
        ('Dominican Republic', 'dominican-republic'),
        ('Ecuador', 'ecuador'),
        ('Mexico', 'mexico'),
        ('Argentina', 'argentina'),
        ('Panama', 'panama'),
        ('Peru', 'peru'),
        ('Venezuela', 'venezuela'),
        ('Barbados', 'barbados')
    ),
    'Mediterranean': (
        ('Greece', 'greece'),
        ('Portugal', 'portugal'),
        ('Cyprus', 'cyprus'),
        ('Israel', 'israel'),
        ('Italy', 'italy'),
        ('Spain', 'spain')
    ),
    'Middle East': (
        ('Afghanistan', 'afghanistan'),
        ('Bahrain', 'bahrain'),
        ('Palestinian Territories', 'palestinian-territories'),
        ('United Arab Emirates', 'the-united-arab-emirates'),
        ('Pakistan', 'pakistan'),
        ('Lebanon', 'lebanon'),
        ('Iraq', 'iraq'),
        ('Jordan', 'jordan'),
        ('Kuwait', 'kuwait'),
        ('Oman', 'oman'),
        ('Qatar', 'qatar'),
        ('Saudi Arabia', 'saudi-arabia'),
        ('Iran', 'iran'),
        ('Syria', 'syria'),
        ('Yemen', 'yemen')
    ),
    'Nordic/Baltic': (
        ('Lithuania', 'lithuania'),
        ('Sweden', 'sweden'),
        ('Latvia', 'latvia'),
        ('Norway', 'norway'),
        ('Estonia', 'estonia'),
        ('Finland', 'finland'),
        ('Iceland', 'iceland'),
        ('Denmark', 'denmark')
    ),
    'North Africa': (
        ('Egypt', 'egypt'),
        ('Libya', 'libya'),
        ('Morocco', 'morocco'),
        ('Tunisia', 'tunisia'),
        ('Algeria', 'algeria')
    ),
    'North America': (('USA', 'the-usa'), ('Canada', 'canada')),
    'North East Asia': (
        ('South Korea', 'south-korea'),
        ('Taiwan', 'taiwan'),
        ('Japan', 'japan'),
        ('North Korea', 'north-korea')
    ),
    'South Asia': (
        ('Bangladesh', 'bangladesh'),
        ('Nepal', 'nepal'),
        ('India', 'india'),
        ('Sri Lanka', 'sri-lanka')
    ),
    'South East Asia': (
        ('Malaysia', 'malaysia'),
        ('Singapore', 'singapore'),
        ('Thailand', 'thailand'),
        ('Brunei', 'brunei'),
        ('Philippines', 'the-philippines'),
        ('Cambodia', 'cambodia'),
        ('Indonesia', 'indonesia'),
        ('Vietnam', 'vietnam'),
        ('Myanmar (Burma)', 'myanmar')
    ),
    'Western Europe': (
        ('Switzerland', 'switzerland'),
        ('Belgium', 'belgium'),
        ('France', 'france'),
        ('Germany', 'germany'),
        ('Ireland', 'ireland'),
        ('Netherlands', 'netherlands'),
        ('Luxembourg', 'luxembourg'),
        ('Austria', 'austria'),
        ('Monaco', 'monaco')
    ),
    'Sub Saharan Africa': (
        ('Angola', 'angola'),
        ('Cameroon', 'cameroon'),
        ('Ivory Coast', 'ivory-coast'),
        ('South Africa', 'south-africa'),
        ('Seychelles', 'seychelles'),
        ('Rwanda', 'rwanda'),
        ('Ethiopia', 'ethiopia'),
        ('Kenya', 'kenya'),
        ('Tanzania', 'tanzania'),
        ('Uganda', 'uganda'),
        ('Ghana', 'ghana'),
        ('Mauritius', 'mauritius'),
        ('Mozambique', 'mozambique'),
        ('Namibia', 'namibia'),
        ('Nigeria', 'nigeria'),
        ('Senegal', 'senegal'),
        ('Zambia', 'zambia'),
        ('Djibouti', 'djibouti')
    ),
    'Turkey, Russia & Caucasus': (
        ('Georgia', 'georgia'),
        ('Azerbaijan', 'azerbaijan'),
        ('Russia', 'russia'),
        ('Turkey', 'turkey'),
        ('Tajikistan', 'tajikistan'),
        ('Turkmenistan', 'turkmenistan'),
        ('Uzbekistan', 'uzbekistan'),
        ('Kazakhstan', 'kazakhstan'),
        ('Armenia', 'armenia'),
        ('Mongolia', 'mongolia'),
        ('Ukraine', 'ukraine')
    )
}


def populate_regions(apps, schema_editor):
    Region = apps.get_model('export_readiness', 'Region')
    Region.objects.bulk_create([
        Region(name=f'{name}') for name in DATA.keys()
    ])


def delete_all_regions(apps, schema_editor):
    Region = apps.get_model('export_readiness', 'Region')
    Region.objects.all().delete()


def populate_countries(apps, schema_editor):
    Country = apps.get_model('export_readiness', 'Country')
    Region = apps.get_model('export_readiness', 'Region')
    for region in DATA.keys():
        region_instance = Region.objects.get(name=region)
        Country.objects.bulk_create([
            Country(name=f'{country[0]}', slug=f'{country[1]}', region=region_instance) for country in DATA[region]
        ])


def delete_all_countries(apps, schema_editor):
    Country = apps.get_model('export_readiness', 'Country')
    Country.objects.all().delete()


def match_country_guides_to_countries(apps, schema_editor):
    CountryGuidePage = apps.get_model('export_readiness', 'CountryGuidePage')
    Country = apps.get_model('export_readiness', 'Country')
    for guide in CountryGuidePage.objects.all():
        if Country.objects.filter(name=guide.heading).exists():
            guide.country = Country.objects.get(name=guide.heading)
            guide.save()


class Migration(migrations.Migration):

    dependencies = [
        ('export_readiness', '0070_auto_20191202_1107'),
    ]

    operations = [
        migrations.RunPython(populate_regions, reverse_code=delete_all_regions),
        migrations.RunPython(populate_countries, reverse_code=delete_all_countries),
        migrations.RunPython(match_country_guides_to_countries, reverse_code=migrations.RunPython.noop)
    ]
