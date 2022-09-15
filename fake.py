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
    house = f'{random.randint(10000, 99999)}'
    house_num.append(house)

states = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
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

cities = [
    "Montgomery", "Janeau", "Pheonix", "Little Rock", "Sacramento", "Denver", "Hartford", "Dover",
    "Tallahassee", "Atlanta", "Honolulu", "Boise", "Springfeild", "Indianapolis", "Des Moines", "Topeka",
    "Frankfort", "Baton Rouge", "Augusta", "Annapolis", "Boston", "Lansing", "Saint Paul", "Jackson", 
    "Jefferson City", "Helena", "Lincoln", "Carson City", "Concord", "Trenton", "Santa Fe", "Albany",
    "Raleigh", "Bismarck", "Columbus", "Oklahoma City", "Salem", "Harrisburg", "Providence", "Columbia",
    "Pierre", "Nashville", "Austin", "Salt Lake City", "Montpelier", "Richmond", "Olympia", "Charleston",
    "Madison", "Cheyenne"
]

street = [
    "1st St", "2nd St", "3rd St", "4th St", "5th St", "6th St", "7th St", "8th St", "9th St", 
    "Oak Avenue", "Main St", "Park St", "Pine St", "Maple Rd", "Cedar St", "Elm St", "Hill Rd",
    "Veiw Blvd", "King Rd", "Preston Rd"
]



phone = []
for x in range(20):
    phone_num = f'{random.randint(10000, 99999)}'
    phone.append(phone_num)

zip_list = []
for x in range(20):
    zip_code = f'{random.randint(10000, 99999)}'
    zip_list.append(zip_code)

# make zip match to state

people = {}

while len(people) < 20:
    first_num = random.randint(0, 19)
    first_name = first[first_num]

    last_num = random.randint(0, 19)
    last_name = last[last_num]

    house_number = random.randint(0, 19)
    address = house_num[house_number]

    state_num= random.randint(0, 49)
    state = states[state_num]

    cities_num = random.randint(0, 19)
    city = cities[cities_num]

    street_num = random.randint(0, 19)
    streets = street[street_num]

    name = " ".join(first_name, last_name)

    # people[first_name] = 



print(people)

#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