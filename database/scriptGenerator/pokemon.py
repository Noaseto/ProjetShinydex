language = "francais.txt"
languagePath = "../../pokemonName"+language
listePoke = open

aFile = open("../sqlScript/dataBaseFillPokemon.sql",'w')

aLine = "INSERT INTO pokemon VALUES("

aFile.write(aLine)

aFile.close()