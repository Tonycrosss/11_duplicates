import os


def find_duplicates(parent_directory):
    # Dups in format {hash:[names]}
    dups = {}
    filename_list = []
    for dirName, subdirs, fileList in os.walk(parent_directory):
        print('Scanning %s...' % dirName)
        for filename in fileList:
            if filename in filename_list:
                dups['{}'.format(filename)] = '{}'.format(dirName)
            else:
                filename_list.append(filename)


if __name__ == '__main__':
    find_duplicates('./')
