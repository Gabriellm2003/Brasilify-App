#!/bin/bash

echo "Buscando no Music Graph API"
time python api-scripts/init/getMscGrphInfo.py spotID_artistas.txt dbdecadas.csv

echo "Buscando no Spotify API"
time python api-scripts/init/getSptfyInfo.py spotID_artistas.txt dbartistas.csv dbsimilares.csv dbartgenero.csv dbalbuns.csv  dbmusicas.csv

# echo "Criando brasilifyDB..."
# sqlite3 brasilify.db

# time python createpy.py

# echo "Iniciando interface"
# google-chrome ../../public-ws/index.html

echo "Removendo arquivos temporarios"
#rm spotID_artistas.txt dbartistas.csv dbdecadas.csv dbsimilares.csv dbartgenero.csv dbalbuns.csv dbmusicas.csv
rm api-scripts/init/temp*

#criando o banco de dados a partir de um dump 
cat pulic-ws/db/banco.sql | sqlite3 pulic-ws/db/brasilifydb.db