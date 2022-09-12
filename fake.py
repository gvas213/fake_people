import random

first = [
    'Nancy', 'Sam', 'Liam', 'Fiona', 'Gigi', 'Landon', 'Isaac', 'Lisa', 'Matt', 'Fran',
    'Lydia', 'Hannah', 'Trey', 'Jonas', 'Avery', 'Gretchen', 'Debbie', 'Rhiannon', 'Mayme', 'Cian'
]

last = [
    'Smith', 'Ramirez', 'Gonzalez', 'Worth', 'Turner', 'Bloom', 'Stevens', 'Diaz', 'Moreno', 'Vesper', 
    'Clarke', 'McCarthy', 'Cook', 'Henry', 'Sutherland', 'McPolin', 'McCardell', 'Webber', 'Stuart', 'Colangelo'
]

house_num = []

for x in range(20):
    house_num.append(random.randrange(1000, 5000))

states = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
}

cities = {
    "Alabama": ["Prattville", "Homewood", "Center Point", "Trussville", "Talladega"],
    "Alaska": ["Fairbanks", "Anchorage", "Eagle River", "Badger", "Juneau"]

}



phone = []
for x in range(20):
    phone.append(random.randrange(2147653494, 2150038765))

zip = []
for x in range(20):
    zip.append(random.randrange(75056, 94768))
#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