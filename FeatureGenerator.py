__author__ = 'qluo'

import pickle
from sys import argv
import time
import numpy as np


def load_training_data(bidders_pickle):
    return pickle.load( open(bidders_pickle, 'rb'))

def write_features(bidders_dict, out_name):
    data = list()
    for id in bidders_dict.keys():
        data.append(bidders_dict[id].generate_feature_vector())
    np.save(out_name, np.array(data))

def load_feature(feature_file_name):
    data = np.load(feature_file_name)
    return data

if __name__ == '__main__':
    start = time.time()
    bidders_dict = load_training_data(bidders_pickle=argv[1])
    write_features(bidders_dict, out_name=argv[2])
    print("Completed in %f sec" % (time.time()-start))