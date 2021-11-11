from functions import pathToFile

choix = int(input("1 for english, 2 for french\n"))
if(choix == 1):
    language = "english.txt"
else:
    language = "francais.txt"

languagePath = "../../pokemonName/"+language
listePoke = open(languagePath,'r')
pokemons = listePoke.readlines()
aFile = open("../../database/sqlScript/dataBaseFillPokemon.sql",'w')

for index, poke in enumerate(pokemons, start=1):
    aLine = "INSERT INTO pokemon (id, nomPoke, pathToSprite) VALUES("+str(index)+",'"+poke[:-1]+"','"+pathToFile(index)+"');\n"
    aFile.write(aLine)

listePoke.close()
aFile.close()
