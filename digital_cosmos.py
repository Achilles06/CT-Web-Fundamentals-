import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    planet_data = []
    for planet in planets:
        if planet['isPlanet']:
            name = planet.get('englishName', 'N/A')
            mass = planet.get('mass', {}).get('massValue', 0)
            orbit_period = planet.get('sideralOrbit', 0)
            planet_data.append({
                'name': name,
                'mass': mass,
                'orbit_period': orbit_period
            })
    return planet_data

def find_heaviest_planet(planets):
    heaviest_planet = max(planets, key=lambda p: p['mass'])
    return heaviest_planet['name'], heaviest_planet['mass']

def find_longest_orbit_planet(planets):
    longest_orbit_planet = max(planets, key=lambda p: p['orbit_period'])
    return longest_orbit_planet['name'], longest_orbit_planet['orbit_period']

planets = fetch_planet_data()

# Print planet data
for planet in planets:
    print(f"Planet: {planet['name']}, Mass: {planet['mass']} x 10^24 kg, Orbit Period: {planet['orbit_period']} days")

# Find the heaviest planet
heaviest_name, heaviest_mass = find_heaviest_planet(planets)
print(f"\nThe heaviest planet is {heaviest_name} with a mass of {heaviest_mass} x 10^24 kg.")

# Find the planet with the longest orbit period
longest_orbit_name, longest_orbit_period = find_longest_orbit_planet(planets)
print(f"The planet with the longest orbit period is {longest_orbit_name} with an orbit period of {longest_orbit_period} days.")
