#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
#caso de erro na linha a seguir, instale: sudo apt-get install python-pip
import pip
pip.main(['install', 'spotipy'])
import threading
#caso de erro na linha a seguir: sudo pip install spotipy
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pprint
import time
from arquivos import *

def getSpotifyClient(clientID, clientSecret):
    client_credentials_manager = SpotifyClientCredentials(clientID, clientSecret)
    return spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def search_artist(spclient, spotify_id ):
    #pesquisa no spotify
    try:
        artresult = spclient.artist( spotify_id )
    except:
        try:
            time.sleep(2)
            artresult = spclient.artist( spotify_id )
        except:
            artresult = None
            print "retornando um NONE procurando o artista ", spotify_id

    return artresult

def add_artista( obj_artista, gender ,arq_saida):
    gender = gender.replace("\n", "").replace(" ", "")

    try:
        popularidade = str(obj_artista["popularity"])
    except:
        popularidade = ""

    try:
        url_image = '"' +obj_artista["images"][0]["url"].encode('utf-8') + '"'
    except:
        url_image = ""

    arq_saida.write( '"'+ obj_artista["id"].encode('utf-8') + '", "' +  obj_artista["name"].encode('utf-8').replace(",", "^") + '", "' + gender + '", ' + popularidade + ', ' +  url_image +'\n')

    return

def add_artista_genero( dict_artgen, arq_saida):
    for (art, gen) in dict_artgen:
        arq_saida.write( '"'+unicode(art).encode('utf-8')  + '", "' + unicode(gen).encode('utf-8') +'"\n' )

    return

def search_related_artists(spclient, spotify_id):
    try:
        result = spclient.artist_related_artists( spotify_id )
    except:
        try:
            time.sleep(3)
            result = spclient.artist_related_artists( spotify_id )
        except:
            result = None

    return result

def add_rel_artists( dict_artsim, dict_art, arq_saida):
    for (art, similar) in  dict_artsim:
        #conferir se o similar tambem e brasileira
        if similar in dict_art:
            arq_saida.write( '"'+ art.encode("utf-8") +'", "'+  similar.encode('utf-8')+'"\n' )

def search_albums(spclient, spotify_id):
    try:
        result = spclient.artist_albums( spotify_id )
    except:
        try:
            time.sleep(2)
            result = spclient.artist_albums( spotify_id )
        except:
            result = None
            print "retornando um NONE procurando os albuns do artista ", spotify_id

    return result

def add_albums(sp_client, arq_saida_album, listatuplas):
    #listatuplas tem (artista, album)
    arq_saida_album = open(arq_saida_album, 'w')
    for (art, album) in listatuplas:
        #print "Pesquisando ", art, " ", album
        albumfullobj = search_fullalbum(sp_client, album)

        if not type(albumfullobj) == None :
            try:
                releasedate = albumfullobj["release_date"].encode('utf-8')
            except:
                releasedate = ""

            try:
                url_image =  albumfullobj["images"][0]["url"].encode('utf-8')
            except:
                url_image = ""

            try:
                popularidade = str(albumfullobj["popularity"])
            except:
                popularidade = ""

            arq_saida_album.write( '"'+ art + '", "' + albumfullobj["id"].encode('utf-8') + '", "' +  albumfullobj["name"].encode('utf-8').replace(",", "^") + '", "' + releasedate + '", "' + url_image + '", '+  popularidade +'\n')

    arq_saida_album.close()
    return

def search_fullalbum(sp_client, album):
    try:
      albumfullobj = sp_client.album(album)
    except:
        try:
            time.sleep(2)
            albumfullobj = sp_client.album(album)
        except:
            albumfullobj = None

    return albumfullobj

def add_tracks(clientID, clientSecret, arq_saida_musicas, listamus):
    sp = getSpotifyClient(clientID, clientSecret)
    starttime = time.time()
    dict_musicas = {}
    arq_saida_musicas = open(arq_saida_musicas, 'w')

    #lista tem: (artista, album)
    for (art, album) in listamus:
        if( int(time.time() - starttime) > 3580 ):
            print " ---- Renovando access token ----"
            sp = getSpotifyClient( clientID, clientSecret )
            starttime = time.time()
        resultado = search_fullalbum(sp, album)
        for m in resultado["tracks"]["items"]:
            if not ( art, album, m["id"]) in dict_musicas:
                dict_musicas[ ( art, album, m["id"]) ] = True
                try:
                    numero = str(m["track_number"])
                except:
                    numero = ""

                try:
                    previewurl =  m["preview_url"].encode('utf-8')
                except:
                    previewurl = ''

                arq_saida_musicas.write('"'+art.encode("utf-8") + '", "' + album.encode('utf-8') + '", "' + m["id"].encode('utf-8') + '", '+ numero + ', "' + m["name"].encode("utf-8").replce(",", "^") + '", "' + previewurl+ '"\n' )

    arq_saida_musicas.close()
    return

def fct_t1( clientID, clientSecret, art_dict, arq_saida_art, arq_saida_gen):
    print "Inicio T1"
    dict_artgen = {}

    arq_saida_art = open( arq_saida_art, 'w')
    arq_saida_gen = open( arq_saida_gen, 'w')

    sp = getSpotifyClient(clientID, clientSecret)
    starttime = time.time()
    for art in art_dict:
        if( int(time.time() - starttime) > 3580 ):
            print " ---- Renovando access token ----"
            sp = getSpotifyClient( clientID, clientSecret )
            starttime = time.time()

        resultado = search_artist(sp, art)
        add_artista(resultado, art_dict[art][1], arq_saida_art)
        for gen in resultado['genres']:
            if not( (art, gen) in dict_artgen ):
                dict_artgen[(art, gen)] = True

    add_artista_genero( dict_artgen, arq_saida_gen )

    arq_saida_gen.close()
    arq_saida_art.close()
    print "Fim T1"
    return

def fct_t2(clientID, clientSecret, art_dict, arq_saida_similares):
    print "Inicio T2"
    dict_artsim = {}

    arq_saida_similares  = open( arq_saida_similares, 'w')
    sp = getSpotifyClient(clientID, clientSecret)
    starttime = time.time()
    for art in art_dict:
        if( int(time.time() - starttime) > 3580 ):
            print " ---- Renovando access token ----"
            sp = getSpotifyClient( clientID, clientSecret )
            starttime = time.time()

        resultados = search_related_artists(sp, art)
        for r in resultados["artists"]:
            if not (art, r["id"]) in dict_artsim:
                dict_artsim[(art, r["id"])] = True


    add_rel_artists( dict_artsim, art_dict, arq_saida_similares)
    arq_saida_similares.close()
    print "Fim T2"
    return

def fct_t3(clientID, clientSecret, art_dict, arq_saida_album):
    print "Inicio T3"
    dict_artalb = {}    
    sp = getSpotifyClient(clientID, clientSecret)
    starttime = time.time()
    for art in art_dict:
        if( int(time.time() - starttime) > 3580 ):
            print " ---- Renovando access token ----"
            sp = getSpotifyClient( clientID, clientSecret )
            starttime = time.time()

        array_resultado = search_albums(sp, art)
        for album in array_resultado["items"]:
            if not (art, album["id"]) in dict_artalb:
                dict_artalb[(art, album["id"])] = True
    print "IDs de todos os albuns buscados"

    #lista de dicionarios particionados
    lista = []
    for i in range(0,5):
        lista.append([])

    i = 0
    for key in dict_artalb:
        lista[i%5].append( key )
        i += 1

    t4 = threading.Thread( target= add_albums , args=(getSpotifyClient('insira_aqui', 'insira_aqui'), "temp1.txt",lista[0] ))
    t4.start()
    t5 = threading.Thread( target= add_albums , args=(getSpotifyClient('insira_aqui', 'insira_aqui'), "temp2.txt",lista[1] ))
    t5.start()
    t6 = threading.Thread( target= add_albums , args=(getSpotifyClient('insira_aqui', 'insira_aqui'), "temp3.txt",lista[2] ))
    t6.start()
    t7 = threading.Thread( target= add_albums , args=(getSpotifyClient('ainsira_aqui', 'insira_aqui'), "temp4.txt",lista[3] ))
    t7.start()
    t8 = threading.Thread( target= add_albums , args=(getSpotifyClient('insira_aqui', 'insira_aqui'), "temp5.txt",lista[4] ))
    t8.start()

    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()

    merge5files_fullalbum("temp1.txt", "temp2.txt", "temp3.txt", "temp4.txt", "temp5.txt", arq_saida_album)
    
    print "Fim T3"
    return

def fct_t4(art_dict,  arq_saida_musicas):
    #art_dict tem: artista, album
    print "Inicio T4"
    dict_musicas = {}
    #lista - dicionario particionados
    lista = []
    for i in range(0,5):
        lista.append([])

    i = 0
    for key in art_dict:
        lista[i%5].append(key)
        i += 1

    t4 = threading.Thread( target= add_tracks , args=('insira_aqui', 'insira_aqui', "temp6.txt",lista[0] ))
    t4.start()
    t5 = threading.Thread( target= add_tracks , args=('insira_aqui', 'insira_aqui', "temp7.txt",lista[1] ))
    t5.start()
    t6 = threading.Thread( target= add_tracks , args=('insira_aqui', 'insira_aqui', "temp8.txt",lista[2] ))
    t6.start()
    t7 = threading.Thread( target= add_tracks , args=('insira_aqui', 'insira_aqui', "temp9.txt",lista[3] ))
    t7.start()
    t8 = threading.Thread( target= add_tracks , args=('insira_aqui', 'insira_aqui', "temp10.txt",lista[4] ))
    t8.start()

    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()


    print "Todas as musicas adicionados"
    merge5files_musicas("temp6.txt", "temp7.txt", "temp8.txt", "temp9.txt", "temp10.txt", arq_saida_musicas)
    print "Fim T4"

    return

def main():
    dict_entrada = {}
    in_ids = open(sys.argv[1], 'r')
    for line in in_ids:
        a = line.split(',')
        if not (a[0] in dict_entrada):
            a[1] = a[1].replace(' ', '').replace("\n", "")
            dict_entrada[a[0]] = (True, a[1])

    in_ids.close()

    #Threads
    t1 = threading.Thread( target= fct_t1 , args=('insira_aqui', 'insira_aqui', dict_entrada,  sys.argv[2], sys.argv[4]))
    t1.start()
    t2 = threading.Thread( target= fct_t2  , args=('insira_aqui', 'insira_aqui', dict_entrada, sys.argv[3]))
    t2.start()
    t3 = threading.Thread( target= fct_t3 , args=('insira_aqui', 'insira_aqui', dict_entrada,  sys.argv[5])) 
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print "Fazendo dicionario artista-album"
    dict_entrada = {}
    artalb = open(sys.argv[5], 'r')
    for line in artalb:
        a = line.split(",")

        a[0] = a[0].replace('"', '').replace(" ", "")
        a[1] = a[1].replace('"', '').replace(" ", "")
        if not ( (a[0], a[1]) in dict_entrada):
            dict_entrada[(a[0],a[1])] = True

    artalb.close()
    print "Dicionario artista-album pronto"


    t4 = threading.Thread( target= fct_t4, args=( dict_entrada, sys.argv[6] ) )
    t4.start()
    t4.join()


main()

