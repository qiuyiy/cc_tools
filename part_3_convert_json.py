import cc_dat_utils
import cc_classes
import json
jfile = "data/qiuyiy_cc1.json"


def read_json(jfile):
    with open(jfile, "r") as reader:
        j = json.load(reader)
    levelpack = cc_classes.CCLevelPack()
    for i in range(len(j)):
        thisJson = j[i]
        newLevel = cc_classes.CCLevel()
        newLevel.level_number = thisJson["level_number"]
        newLevel.time = thisJson["time"]
        newLevel.num_chips = thisJson["num_chips"]
        newLevel.upper_layer = thisJson["upper_layer"]
        newLevel.lower_layer = thisJson["lower_layer"]
        opFields = thisJson["optional_fields"]
        for i in range(len(opFields)):
            if opFields[i]["field_type"] == "hint":
                field = cc_classes.CCMapHintField(opFields[i]["content"])
                newLevel.add_field(field)
            if opFields[i]["field_type"] == "password":
                field = cc_classes.CCEncodedPasswordField(opFields[i]["content"])
                newLevel.add_field(field)
            if opFields[i]["field_type"] == "title":
                field = cc_classes.CCMapTitleField(opFields[i]["content"])
                newLevel.add_field(field)

            if opFields[i]["field_type"] == "monster":
                coord = opFields[i]["content"]
                c = []
                for k in range(len(coord)):
                    coordx = coord[k][0]
                    coordy = coord[k][1]
                    cccord = cc_classes.CCCoordinate(coordx, coordy)
                    c.append(cccord)
                field = cc_classes.CCMonsterMovementField(c)
                newLevel.add_field(field)
            if opFields[i]["field_type"] == "trap":
                coords = opFields[i]["content"]
                t = []
                for l in range(len(coords)):
                    btnX = coords[l][0][0]
                    btnY = coords[l][0][1]
                    trapX = coords[l][1][0]
                    trapY = coords[l][1][1]
                    print(btnX, btnY, trapX, trapY)
                    trap = cc_classes.CCTrapControl(btnX, btnY, trapX, trapY)
                    t.append(trap)
                field = cc_classes.CCTrapControlsField(t)
                newLevel.add_field(field)


        levelpack.add_level(newLevel)
    #print(levelpack)
    return levelpack
    pass

"""
{
          "field_type" : "trap",
          "content" : [[[1, 1],[2, 10]],[[11, 1],[10, 10]]]
       }
"""

filePack = read_json(jfile)
datFile = "data/qiuyiy_cc1.dat"
cc_dat_utils.write_cc_level_pack_to_dat(filePack, datFile)
#Part 3
#Load your custom JSON file
#Convert JSON data to CCLevelPack
#Save converted data to DAT file


