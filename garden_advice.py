
#  Fix for issue # 1 -Replace with input() to allow user interaction.
needs_season = False
while not needs_season:  # Prints options for the user.
    print("Select season:")
    print("1. Summer")
    print("2. Winter")
    season_selection = input()

    if (season_selection == "1"):
        season = "summer"
        needs_season = True
    elif (season_selection == "2"):
        season = "winter"
        needs_season = True
    else:
        print("Invalid input. Please select 1 or 2.")

needs_plant = False
while not needs_plant:
    print("Select plant:")
    print("1. Flower")
    print("2. Vegetable")
    plant_selection = input()

    if (plant_selection == "1"):
        plant_type = "flower"
        needs_plant = True
    elif (plant_selection == "2"):
        plant_type = "vegetable"
        needs_plant = True
    else:
        print("Invalid input. Please select 1 or 2.")

# Variable to hold gardening advice
advice = ""

# Fix for issue # 3 - Store advice in a
# Dictionary for multiple plants and seasons
advice_data = {
    "season": {
        "summer": "Water your plants regularly and provide some shade.",
        "winter": "Protect your plants from frost with covers."
    },
    "plant": {  
        "flower": "Use fertilizer to encourage blooms.",
        "vegetable": "Keep an eye out for pests!"
    }
}

# Determine advice based on the season.
# Season and plant type are used as keys to access the advice.
advice = advice_data["season"].get(season, "No advice for this season") +\
     "\n" + advice_data["plant"].get(plant_type, "No advice for this "
                                     "type of plant.")


# Print the generated advice
print(advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
