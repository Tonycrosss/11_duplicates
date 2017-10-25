import os


def find_duplicates(parent_directory):
    # Dups in format {hash:[names]}
    dups = {}
    for dirName, subdirs, fileList in os.walk(parent_directory):
        print('Scanning %s...' % dirName)
        for filename in fileList:
            print(filename)


if __name__ == '__main__':
    find_duplicates('./')
