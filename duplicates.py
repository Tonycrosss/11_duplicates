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
    dups = {'duplicates': []}
    files_info = {}
    # TODO: Нормальные имена переменных
    for dirName, subdirs, fileList in os.walk(parent_directory):
        print('Scanning %s...' % dirName)
        for filename in fileList:
            path_to_file = dirName + '/' + filename
            file_md5 = hash_counter(path_to_file)
            if filename in files_info.keys() and files_info[filename]['md5'] == file_md5:
                dups['duplicates'].append(filename)
            else:
                files_info[filename] = {'md5': file_md5, 'path': path_to_file}
                print(files_info)

    print(dups)

if __name__ == '__main__':
    find_duplicates('E:/distr/python/devman/11_duplicates/')
    print(hash_counter('./dubles/alala.txt'))
    print(hash_counter('./dubles/dubles1/alala.txt'))
