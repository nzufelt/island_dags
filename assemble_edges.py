import random

people = ['Ada', 'Blaise', 'Claude', 'Diana']
artifacts = {
    'Ada': 'Fabled Compass',
    'Blaise': 'Golden Jewel',
    'Claude': 'Hallowed Idol',
    'Diana': 'Ivory Figurine'
}
locations = [
    'Shipwreck Beach', 'Mystic Lake', 'Moonlit Marsh', 'Forgotten Ruins', 'Obsidian Cliffs',
    'Hidden Cave', 'Lost Village', 'Echoing Grotto', 'Storm Peak', 'Crystal Lagoon',
    'Sunken Shrine', 'Ancient Lighthouse', 'Whispering Woods', 'Serpent Ridge', 'Twilight Grove',
    'Coral Reef', 'Pirate Bay', 'Volcano Summit', 'Emerald Forest', 'Starfall Valley'
]

# Take in a dictionary of routes so far and generate a new, compatable list of routes
def sample_with_order(routes):
    return random.sample(locations, 8)


# Ensure each location has 0, 1, or 2 visits
valid = False
routes = {}
while not valid:
    routes = {person: sample_with_order(routes) for person in people}
    location_counts = {}
    for locs in routes.values():
        for loc in locs:
            location_counts[loc] = location_counts.get(loc, 0) + 1
    if all(count <= 2 for count in location_counts.values()):
        valid = True

# Generate travel log
edges = []
for person, locs in routes.items():
    for i in range(len(locs) - 1):
        edges.append(f"{person} was seen traveling from {locs[i]} to {locs[i+1]}")

# Shuffle the edges so they don't output in order
random.shuffle(edges)

# Print all travel statements
for edge in edges:
    print(edge)


print(routes)