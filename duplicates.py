import os
import sys
import hashlib


def hash_counter(path_to_file, blocksize = 65536):
    with open(path_to_file, 'rb') as file_handler:
        hasher = hashlib.md5()
        buffer = file_handler.read(blocksize)
        while len(buffer) > 0:
            hasher.update(buffer)
            buffer = file_handler.read(blocksize)
            return hasher.hexdigest()


def find_duplicates(parent_directory):
    # Dups in format {hash:[names]}
    dups = {}
    filename_list = []
    # TODO: Нормальные имена переменных
    for dirName, subdirs, fileList in os.walk(parent_directory):
        print('Scanning %s...' % dirName)
        for filename in fileList:
            if filename in filename_list:
                dups['{}'.format(filename)] = '{}'.format(dirName)
            else:
                filename_list.append(filename)

if __name__ == '__main__':
    find_duplicates('./')
    print(hash_counter('./dubles/alala.txt'))
    print(hash_counter('./dubles/dubles1/alala.txt'))
