import sys
import pprint
import threading

def merge4files_artists(file1, file2, file3, file4, fileout):
	fp1 = open(file1, 'r')
	fp2 = open(file2, 'r')
	fp3 = open(file3, 'r')
	fp4 = open(file4, 'r')
	fpOut = open(fileout, 'w')

	lines = fp1.readlines()
	lines = lines + fp2.readlines()
	lines = lines + fp3.readlines()
	lines = lines + fp4.readlines()

	diclines = {}
	finallines = []

	for line in lines:
		check = line.split(',')
		#[0] = artista   [1] = nome
		if check[0] in diclines:
			continue
		else:
			diclines[check[0]] = check[1]
			finallines.append(line)

	for line in finallines:
		fpOut.write(line)

	fpOut.close()

def merge4files_artgenalbum(file1, file2, file3, file4, fileout):
	fp1 = open(file1, 'r')
	fp2 = open(file2, 'r')
	fp3 = open(file3, 'r')
	fp4 = open(file4, 'r')
	fpOut = open(fileout, 'w')

	lines = fp1.readlines()
	lines = lines + fp2.readlines()
	lines = lines + fp3.readlines()
	lines = lines + fp4.readlines()

	diclines = {}
	finallines = []

	for line in lines:
		check = line.split(',')
		#[0] = artista   [1] = album/genero
		if (check[0], check[1]) in diclines:
			continue
		else:
			diclines[(check[0], check[1])] = True
			finallines.append(line)

	for line in finallines:
		fpOut.write(line)

	fpOut.close()

def merge4files_music(file1, file2, file3, file4, fileout):
	fp1 = open(file1, 'r')
	fp2 = open(file2, 'r')
	fp3 = open(file3, 'r')
	fp4 = open(file4, 'r')
	fpOut = open(fileout, 'w')

	lines = fp1.readlines()
	lines = lines + fp2.readlines()
	lines = lines + fp3.readlines()
	lines = lines + fp4.readlines()

	diclines = {}
	finallines = []

	for line in lines:
		check = line.split(',')
		#[0] = artista   [1] = album  [2] =id musica
		if check[2] in diclines:
			continue
		else:
			diclines[check[2]]  = check[3]
			finallines.append(line)

	for line in finallines:
		fpOut.write(line)

	fpOut.close()


def merge5files_fullalbum(file1, file2, file3, file4, file5, fileout):
	fp1 = open(file1, 'r')
	fp2 = open(file2, 'r')
	fp3 = open(file3, 'r')
	fp4 = open(file4, 'r')
	fp5 = open(file5, 'r')
	fpOut = open(fileout, 'w')

	lines = fp1.readlines()
	lines = lines + fp2.readlines()
	lines = lines + fp3.readlines()
	lines = lines + fp4.readlines()
	lines = lines + fp5.readlines()

	diclines = {}
	finallines = []

	for line in lines:
		check = line.split(',')

		# artista    0
		# id_album   1
		# nome_album 2
		# lancamento 3
		# imagem     4
		# popularidade 5

		if (check[0], check[1]) in diclines:
			continue
		else:
			diclines[(check[0], check[1])]  = True
			finallines.append(line)

	for line in finallines:
		fpOut.write(line)

	fpOut.close()

def merge5files_musicas(file1, file2, file3, file4, file5, fileout):
	fp1 = open(file1, 'r')
	fp2 = open(file2, 'r')
	fp3 = open(file3, 'r')
	fp4 = open(file4, 'r')
	fp5 = open(file5, 'r')
	fpOut = open(fileout, 'w')

	lines = fp1.readlines()
	lines = lines + fp2.readlines()
	lines = lines + fp3.readlines()
	lines = lines + fp4.readlines()
	lines = lines + fp5.readlines()

	diclines = {}
	finallines = []


	for line in lines:
		check = line.split(',')

		# artista
		# album
		# id_musica
		# numero
		# nome_musica
		# preview_url

		if not check[2] in diclines:
			diclines[check[2]]  = True
			finallines.append(line)

	for line in finallines:
		fpOut.write(line)

	fpOut.close()
