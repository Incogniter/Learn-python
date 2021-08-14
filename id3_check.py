import os
import fnmatch
import id3reader_p3 as id3reader


def find_music(start, extension):
    for path, directories, files in os.walk(start):

        for file in fnmatch.filter(files, '*.{}'.format(extension)):
            absolute_path = os.path.abspath(path)
            yield os.path.join(absolute_path, file)


my_music = find_music("music", "emp3")

error_list = []

for f in my_music:
    try:
        id3r = id3reader.Reader(f)
        print("artist: {}, album: {}, track: {}, song: {}".format(
            id3r.get_valur("performer"),
            id3r.get_valur("album"),
            id3r.get_valur("track"),
            id3r.get_valur("title")
        ))
    except:
        error_list.append(f)

for error_file in error_list:
    print(error_file)