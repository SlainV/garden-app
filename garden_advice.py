
#  Fix for issue # 1 -Replace with input() to allow user interaction.
needs_season = False
while not needs_season:
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

# Determine advice based on the season
if season == "summer":
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "winter":
    advice += "Protect your plants from frost with covers.\n"
else:
    advice += "No advice for this season.\n"

# Determine advice based on the plant type
if plant_type == "flower":
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"
else:
    advice += "No advice for this type of plant."

# Print the generated advice
print(advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
