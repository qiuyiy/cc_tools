import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()
    for i in range(len(json_data["title"])):

        title = json_data["title"][i]
        year = json_data["year"][i]
        plat_year = json_data["platform"]["launch year"][i]
        #launchYear = plat["launch year"]
        plat_name = json_data["platform"]["name"][i]

        gamePlat = test_data.Platform(plat_name, plat_year)
        game = test_data.Game(title, gamePlat, year)
        game_library.add_game(game)

    return game_library

#Part 2
input_json_file = "data/test_data.json"
with open(input_json_file, "r") as reader:
    res = json.load(reader)
#print(res)
game_lib = make_game_library_from_json(res)
print(game_lib)
### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print()
### End Add Code Here ###
