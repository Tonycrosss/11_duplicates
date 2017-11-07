import os
import hashlib
import sys


def hash_counter(path_to_file, blocksize = 65536):
    with open(path_to_file, 'rb') as file_handler:
        hasher = hashlib.md5()
        buffer = file_handler.read(blocksize)
        while len(buffer) > 0:
            hasher.update(buffer)
            buffer = file_handler.read(blocksize)
            return hasher.hexdigest()


def find_duplicates(parent_directory):
    dups = {'duplicates': []}  # type: dict{str: list}
    files_info = {}
    for dir_name, sub_dirs, file_list in os.walk(parent_directory):
        print('Scanning %s...' % dir_name)
        for filename in file_list:
            path_to_file = dir_name + '/' + filename
            file_md5 = hash_counter(path_to_file)
            if filename in files_info.keys() and files_info[filename]['md5'] == file_md5:
                dups['duplicates'].append(path_to_file)
            else:
                files_info[filename] = {'md5': file_md5, 'path': path_to_file}
    return dups


def dups_print(dups_dict):
    print('В данной папке имеются дубликаты :')
    print(dups_dict['duplicates'])

if __name__ == '__main__':
    path_to_scan = sys.argv[1]
    dups_dict = find_duplicates(path_to_scan)
    print(dups_dict)
    dups_print(dups_dict)
