#!/usr/bin/env python3

def get_names(spicy_foods):
    """Return a list of names from the spicy foods list."""
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    """Return foods with heat_level over 5."""
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    """Print all foods formatted with 🌶 emojis for heat level."""
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def create_spicy_food(spicy_foods, new_food):
    """Add a new spicy food to the list and return the new list."""
    return spicy_foods + [new_food]

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """Return the first food that matches the given cuisine."""
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    """Print foods with heat_level over 5 formatted with 🌶 emojis."""
    for food in spicy_foods:
        if food["heat_level"] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_average_heat_level(spicy_foods):
    """Return the average heat level of all spicy foods."""
    if not spicy_foods:
        return 0
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods)
