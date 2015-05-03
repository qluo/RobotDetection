__author__ = 'qluo'

import pickle
from sys import argv
import time

def load_training_data(bidders_pickle):
    bidders_dict = pickle.load( open(bidders_pickle, 'rb'))
    for id in bidders_dict.keys():
        print("%s : %s" % (id, bidders_dict[id].get_address()))

if __name__ == '__main__':
    start = time.time()
    load_training_data(bidders_pickle=argv[1])
    print("Completed in %f sec" % (time.time()-start))