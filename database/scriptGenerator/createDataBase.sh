#!/bin/bash
sqlite3 ../shinyDex < ../sqlScript/dataBaseCreateTables.sql
sqlite3 ../shinyDex < ../sqlScript/dataBaseFillMethode.sql
python3 ./pokemon.py
sqlite3 ../shinyDex < ../sqlScript/dataBaseFillPokemon.sql