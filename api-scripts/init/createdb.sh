#!/bin/bash



#ATTACH DATABASE 'brasilify' As 'brasilifyDB';
#.databases
.read create.sql

CREATE TABLE brasilify.Artistas(
   spotify_id 		CHAR(100)	PRIMARY KEY	NOT NULL,
   name 			CHAR(500)				NOT NULL,
   genero 			CHAR(10),
   popularidade 	INTEGER,
   imagem			TEXT
);

CREATE TABLE brasilify.ArtistasSimilares(
	FOREIGN KEY(artista1) 	REFERENCES Artistas(spotify_id)		PRIMARY KEY		NOT NULL,
	FOREIGN KEY(artista2) 	REFERENCES Artistas(spotify_id)		PRIMARY KEY		NOT NULL
);

CREATE TABLE brasilify.Decadas(
	FOREIGN KEY(artista) 	REFERENCES Artistas(spotify_id)		PRIMARY KEY		NOT NULL,
	decada 		CHAR(5)											PRIMARY KEY		NOT NULL
);

CREATE TABLE brasilify.ArtistaGeneroMus(
	FOREIGN KEY(artista) 	REFERENCES Artistas(spotify_id)		PRIMARY KEY		NOT NULL,
	generomusical		 	CHAR(100)							PRIMARY KEY		NOT NULL
);

CREATE TABLE brasilify.Albuns(
	FOREIGN KEY(artista) 	REFERENCES Artistas(spotify_id)		PRIMARY KEY		NOT NULL,
	id_album 		CHAR(500)									PRIMARY KEY		NOT NULL,
	nome_album		CHAR(100)	NOT	NULL,
	lancamento		CHAR(50),
	imagem			TEXT,
	popularidade	INTEGER,
);

CREATE TABLE brasilify.AlbumMusicas(
	sqFOREIGN KEY(artista)	REFERENCES Artistas(spotify_id)		PRIMARY KEY		NOT NULL,
	FOREIGN KEY(album) 		REFERENCES Albuns(id_album)			PRIMARY KEY		NOT NULL,
	id_musica				CHAR(500)							PRIMARY KEY		NOT NULL,
	numero 					INTEGER,
	nome_musica 			CHAR(500),
	preview_url				TEXT
)

.tables

#popular tabelas
.mode csv
.import dbartistas.csv Artistas
.import dbsimilares.csv ArtistasSimilares
.import dbdecadas.csv Decadas
.import dbartgenero.csv ArtistaGeneroMus
.import dbalbuns.csv Albuns


#exibir tabelas populadas
SELECT * FROM Artistas;
SELECT * FROM ArtistaGeneros;
SELECT * FROM Decadas;
SELECT * FROM Albuns;
SELECT * FROM AlbumMusicas;

.quit

