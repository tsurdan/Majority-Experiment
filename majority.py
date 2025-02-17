import math
import random
import matplotlib.pyplot as plt


CITY_POPULATION = 100
NUMBER_OF_EXPERIMENTS = 10

def init_city(city_proper_precentage):
    city = [1 for i in range(math.floor(CITY_POPULATION * (city_proper_precentage / 100)))]  
    city += [0 for j in range(CITY_POPULATION - (math.floor(CITY_POPULATION * (city_proper_precentage / 100))))]
    return city

def get_random_group(city, group_size):
    random_group = random.sample(city, group_size)
    return random_group

def get_property_precentage(group):
    property_precentage = (sum(group) / len(group)) * 100
    return property_precentage

def experiment(city_proper_precentage):
    city = init_city(city_proper_precentage)
    group_size = random.randint(1, CITY_POPULATION)
    random_group = get_random_group(city, group_size)
    return get_property_precentage(random_group)

def main():
    results = []
    for city_proper_precentage in range(51, 101):
        for i in range(NUMBER_OF_EXPERIMENTS):
            results.append((experiment(city_proper_precentage), city_proper_precentage))

    x, y = zip(*results)
    plt.scatter(x, y)
    plt.xlabel('Result Property Percentage')
    plt.ylabel('City Proper Percentage')
    plt.title('Result Property Percentage vs. City Proper Percentage')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()