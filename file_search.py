import os
import fnmatch

# fnmatch compares a single file name and returns true if they match and false if doest match
# it uses case sensitive file system


def find_albums(root, artist_name):
    for path, directories, files in os.walk(root):
        for artist in fnmatch.filter(directories, artist_name):
            sub_directory = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(sub_directory):
                for album in albums:
                    yield os.path.join(album_path, album)   # ,album


def find_songs(albums):
    for album in albums:
        print("*"*40)
        for song in os.listdir(album):
            yield song


album_list = find_albums("music", "Aerosmith")
# black* means wat all that has the word black all the albums will be printed

# not case sensitive
song_list = find_songs(album_list)

for a in album_list:
    print(a)

# for s in song_list:
#      print(s)
