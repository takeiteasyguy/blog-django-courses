import os


def collect_subdirs(rootdir:str, data:list):
    data.append(rootdir)
    for root, subdirs, files in os.walk(rootdir):
        for subdir in subdirs:
            collect_subdirs(root + subdir, data)
    return data
