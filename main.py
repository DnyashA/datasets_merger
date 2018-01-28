import time

from PathContainer import PathContainer
from Merger import Merger

if __name__ == '__main__':
    default_pathes = PathContainer()
    m = Merger(default_pathes.pathes(), split=True)
    start = time.time()
    m.merge()
    finish = time.time()
    print("Merging have been lasted for {0} seconds".format(finish-start))