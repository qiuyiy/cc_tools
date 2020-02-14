import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()
    for key in json_data:
        content = json_data[key]
        title = content["title"]
        year = content["year"]
        plat = content["platform"]
        launchYear = plat["launch year"]
        name = plat["name"]

        gamePlat = test_data.Platform(name, launchYear)
        game = test_data.Game(title, gamePlat, year)
        game_library.add_game(game)

    return game_library

#Part 2
input_json_file = "data/test_data.json"
with open(input_json_file, "r") as reader:
    res = json.load(reader)

game_lib = make_game_library_from_json(res)
print(game_lib)
### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print()
### End Add Code Here ###
