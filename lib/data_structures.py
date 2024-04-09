spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

#names
def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

names = get_names(spicy_foods)
print(names)

#spiciest_foods
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food ['heat_level'] > 5]

spiciest_food = get_spiciest_foods(spicy_foods)
print(spiciest_food)

#spicy food
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

#spicy food by cuisine
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    return None

#spiciest food
def print_spiciest_foods(spicy_foods):
     for food in spicy_foods:
        if food['heat_level'] > 5:
            print(f"{food['name']} - Cuisine: {food['cuisine']}, Heat Level: {food['heat_level']}")

#average heat level
def get_average_heat_level(spicy_foods):
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    num_foods = len(spicy_foods)
    if num_foods > 0:
        return total_heat // num_foods
    else:
        return 0 
    
#create spicy food
def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

updated_spicy_foods = create_spicy_food(spicy_foods, spicy_foods)