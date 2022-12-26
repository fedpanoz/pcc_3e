def make_album(artist, title, songs=None):
    album = {'Artist': artist, 'Title': title}
    if songs:
        album['songs'] = songs
    return album

while True:
    artista = input("Tell me the artist")
    titolo = input("Tell me the title")
    question1 = input("vuoi mettere il numero ?")
    if question1 == 'yes':
        songs = int(input("Tell me the number of songs"))
        print(make_album(artista, titolo, songs))
    else:
        print(make_album(artista, titolo))


    question = input("Do you want to continue? \n")
    if question == 'no':
        break