from django.db import models

armed_forces_europe = 'AS'
armed_forces_pacific = 'AP'
armed_forces_america = 'AA'
alabama = 'AL'
alaska = 'AK'
american_samoa = 'AS'
arizona = 'AZ'
california = 'CA'
colorado = 'CO'
connecticut = 'CT'
delaware = 'DE'
dc = 'DC'
florida = 'FL'
georgia = 'GA'
Guam = 'GU'
hawaii = 'HI'
idaho = 'ID'
illinois = 'IL'
indiana = 'IN'
iowa = 'IA'
kansas = 'KS'
kentucky = 'KY'
louisiana = 'LA'
maine = 'ME'
maryland = 'MD'
massachusetts = 'MA'
mississippi = 'MS'
missouri = 'MO'
montana = 'MT'
nebraska = 'NE'
nevada = 'NV'
new_hampshire = 'NH'
new_jersey = 'NJ'
new_mexico = 'NM'
michigan = 'MI'
new_york = 'NY'
north_carolina = 'NC'
minnesota = 'MN'
north_dakota = 'ND'
northern_marianas = 'MP'
ohio = 'OH'
oklahoma = 'OK'
oregon = 'OR'
pennsylvania = 'PA'
puerto_rico = 'PR'
rhode_island = 'RI'
south_carolina = 'SC'
south_dakota = 'SD'
tennessee = 'TN'
texas = 'TX'
utah = 'UT'
vermont = 'VT'
virginia = 'VA'
virgin_islands = 'VI'
washington = 'WA'
west_virginia = 'WV'
wisconsin = 'WI'
wyoming = 'WY'
mexico = '88'
canada = '99'
other = 'XX'

State_Code_Choices = (

    (armed_forces_europe, '(ZIPs 09xxx) for Armed Forces Europe which includes Canada, Middle East, and Africa'),
    (armed_forces_pacific, '(ZIPs 962xx 966xx) for Armed Forces Pacific'),
    (armed_forces_america, '(ZIPs 340xx) for Armed Forces (Central and South) Americas'),
    (alabama, 'Alabama'),
    (alaska, 'Alaska'),
    (american_samoa, 'American Samoa'),
    (arizona, 'Arizona'),
    (california, 'California'),
    (colorado, 'Colorado'),
    (connecticut, 'Connecticut'),
    (dc, 'District of Columbia'),
    (delaware, 'Delaware'),
    (florida, 'Florida'),
    (georgia, 'Georgia'),
    (hawaii, 'Hawaii'),
    (idaho, 'Idaho'),
    (illinois, 'Illinois'),
    (indiana, 'Indiana'),
    (iowa, 'Iowa'),
    (kansas, 'Kansas'),
    (kentucky, 'Kentucky'),
    (louisiana, 'Louisiana'),
    (maine, 'Maine'),
    (maryland, 'Maryland'),
    (massachusetts, 'Massachusetts'),
    (michigan, 'Michigan'),
    (minnesota, 'Minnesota'),
    (mississippi, 'Mississippi'),
    (missouri, 'Missouri'),
    (montana, 'Montana'),
    (nebraska, 'Nebraska'),
    (nevada, 'Nevada'),
    (new_hampshire, 'New Hampshire'),
    (new_jersey, 'New Jersey'),
    (new_mexico, 'New Mexico'),
    (new_york, 'New York'),
    (north_carolina, 'North Carolina'),
    (north_dakota, 'North Dakota'),
    (northern_marianas, 'Northern Marianas'),
    (ohio, 'Ohio'),
    (oklahoma, 'Oklahoma'),
    (oregon, 'Oregon'),
    (pennsylvania, 'Pennsylvania'),
    (puerto_rico, 'Peurto Rico'),
    (rhode_island, 'Rhode Island'),
    (south_carolina, 'South Carolina'),
    (south_dakota, 'South Dakota'),
    (tennessee, 'Tennessee'),
    (texas, 'Texas'),
    (utah, 'Utah'),
    (vermont, 'Vermont'),
    (virgin_islands, 'Virgin Islands'),
    (virginia, 'Virginia'),
    (washington, 'Washington'),
    (west_virginia, 'West Virginia'),
    (wisconsin, 'Wisconsin'),
    (wyoming, 'Wyoming'),
    (mexico, 'Mexico'),
    (canada, 'Canada'),
    (other, 'Other (Not Listed Above)')

)


class LocationInformation(models.Model):

    postal_code = models.CharField(max_length=2, choices=State_Code_Choices)
    fips_code = models.CharField(max_length=5)
    zip_code = models.CharField(max_length=5)

