#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pprint
import requests
import json
import sys
import time

def build_basepath():
    mg_api_key = 'insira_aqui'
    mg_api_basepath = 'http://api.musicgraph.com/api/v2/artist/search?api_key='+mg_api_key
    return mg_api_basepath

def searchall_BRartists(basepath, out_artid, out_decadas, out_semdec ):
    basepath = basepath + '&country=brazil&limit=100'
    offset = 0;

    while True:
        if offset == 0 :
            result = requests.get(basepath)
        else:
            result = requests.get(basepath+"&offset="+str(offset))

        result.encoding = 'utf-8'
        result = result.json()


        if result["pagination"]["total"] <= ( result["pagination"]["offset"] + result["pagination"]["count"] ) :
                print "Todos os "+ str( result["pagination"]["offset"] + result["pagination"]["count"] ) +"resultados foram buscados"
                break;
        else:

            if(result["status"]["code"] == 0):
                for j in result["data"]:
                    try:
                        # Escrevendo no arquido o spotify_id e o genero
                        out_artid.write( unicode(j["spotify_id"]).encode('utf-8') )
                        try:
                            out_artid.write(', '+ unicode(j["gender"]).encode('utf-8'))
                        except KeyError:
                            out_artid.write(',  ')
                            #print "Artista ", j["name"].encode("utf8"), "(", unicode( j["id"] ).encode('utf-8'), ") nao tem genero"
                        out_artid.write("\n")
                    except KeyError:
                        print "Artista ", j["name"].encode("utf8"), "(", unicode( j["id"] ).encode('utf-8'), ") nao tem SptfID"
                        continue


                    try:
                        # Escrevendo no arquido spotify_id  e decadas
                        decadas = j["decade"].encode('utf-8')
                        decadas = decadas.split("/")

                        for element in decadas:
                            e = element.replace("s", "")
                            e = e.replace(" ", "")
                            out_decadas.write( '"'+unicode( j["spotify_id"] ).encode('utf-8')+'", "'+ e +'"\n' )
                    except KeyError:
                        #print "Provavelmente " + j["name"].encode('utf-8') + " nao possui o campo 'decades' "
                        out_semdec.write( j["name"].encode("utf8") +'\n'+'INSERT INTO Decadas [(artista, decada)] VALUES (' + unicode(j["spotify_id"]).encode('utf-8') + ', **** )'+'\n\n')


                offset = offset + 100

            else:
                print "Status code:" + str(result["status"]["code"]) + result["status"]["message"]
                print "Abortando script"
                exit()

        time.sleep(5)   #Para nao exceder o limite de requisicoes/minuto (15)

def main():
    bp = build_basepath()

    out_artid = open(sys.argv[1], 'w')
    out_decadas = open(sys.argv[2], 'w')
    out_semdec = open("semdecadas.txt", 'w')

    searchall_BRartists(bp, out_artid, out_decadas, out_semdec)

    out_artid.close()
    out_decadas.close()
    out_semdec.close()


main()