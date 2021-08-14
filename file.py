import os

import file_search

root = "music"

for path, directions, files in os.walk(root, topdown=True):
    if files:
        print(path)
        first_path = os.path.split(path)
        print(first_path)
        second_split = os.path.split(first_path[0])
        print(second_split)
        for f in files:
            # song_details = f.strip('.emp3').split(path)
            song_details = f[:-5].split("-")
            print(song_details)

        print("*" * 80)
# import os
# # it fetsches content and its an operating system
# root = "music"
# # walk() generates the file name in the directtrary tree either topdown and bottom up
#
# # top down is false directries are scanned from bottom up
# for path, directions, files in os.walk(root, topdown=True):
#     if files:
#         print(path)
#         first_split = os.path.split(path)
#         print(first_split)
#         second_split = os.path.split(first_split[0])
#         print(second_split)
#         for f in files:
#             song_details = f.split("-")
#             #song_details = f.strip('emp3').split("-")
#             print(song_details)
#         print("*"*80)
#
#
#     # print(directions)
#     # print(files)
#     # input()
#
#     # for f in files:
#     #     print("\t{}".format(f))
