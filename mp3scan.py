# challenge
import os
import fnmatch


def find_music(start, extension):
    for path, directories, files in os.walk(start):
        print("-" * 40)
        for file in fnmatch.filter(files, '*.{}'.format(extension)):
            absolute_path = os.path.abspath(path)
            yield os.path.join(absolute_path, file)

            # abspath i guess its a location of the file where it is located

# this or like this
# for f in find_music("music", "emp3"):
#     print(f)
# or this


my_music = find_music("music", "emp3")

for f in my_music:
    print(f)
