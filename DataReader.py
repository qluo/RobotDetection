__author__ = 'qluo'

import pickle
import csv
from Bidder import Bidder

from sys import argv
import time
import numpy as np

def load_csv(input_name):
    data = list()
    csv_reader = csv.reader(open(input_name, 'rb'))
    header = csv_reader.next()
    for row in csv_reader:
        data.append(row)
    data = np.array(data)
    return header,data

def load_bidders_info(input_name, is_train):
    bidders_dict = dict()
    num_column = 3
    if is_train:
        num_column = 4
    with open(input_name, 'rb') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for line in reader:
            if line[0] == 'bidder_id' or len(line)!=num_column:
                continue
            id = line[0]
            payment_account = line[1]
            address = line[2]
            if is_train:
                label = float(line[3])
            else:
                label = -1.0
            bidders_dict[id] = Bidder(id, payment_account, address)
            bidders_dict[id].set_label(label)
    print("Finished loading %d bidders" % len(bidders_dict.keys()))
    return bidders_dict

def load_bids_info(input_name):
    header, data = load_csv(input_name)
    return header, data

def set_bids_to_bidders(bidders_dict, bids_file_name):
    counter = 0
    for bid in bids_generator(bids_file_name):
        bidder_id = bid[1]
        if bidder_id in bidders_dict.keys():
            bidders_dict[bidder_id].add_one_bid(bid)
            counter += 1
    print("Finished adding %d bids to bidders" % counter)
    return bidders_dict

def get_unique_bids_info(input_name, output_name):
    columns = [2,3,4,6,7]
    header, bids_data = load_bids_info(input_name)
    with open(output_name, 'w') as out:
        for col in columns:
            print("processing column: %d" % col)
            out.write(header[col]+',')
            unique_info = np.unique(bids_data[0::,col]).tolist()
            out.write(len(unique_info)+'\n')
            for e in unique_info:
                out.write(e+',')
            out.write('\n')
    print("Finished loading info from "+input_name)

def run(bidders_file_name, bids_file_name, option):
    if option == 'train':
        bidders_dict = load_bidders_info(bidders_file_name, is_train=True)
        bidders_dict = set_bids_to_bidders(bidders_dict, bids_file_name)
        pickle.dump(bidders_dict, open('bidders_train.p', 'wb'))
    elif option == 'bid':
        get_unique_bids_info(bids_file_name, "unique_bids_info.txt")
    elif option == 'test':
        bidders_dict = load_bidders_info(bidders_file_name, is_train=False)
        pickle.dump(bidders_dict, open('bidders_test.p', 'wb'))
    else:
        print("This option %s is not supported" % option)

if __name__ == '__main__':
    if len(argv)!=4:
        print("Usage: python DataReader.py bidders.csv bids.csv train/bid/test")
        exit(1)
    start = time.time()
    run(bidders_file_name=argv[1], bids_file_name=argv[2], option=argv[3])
    print("Completed in %f sec" % (time.time()-start))