__author__ = 'qluo'

import pickle
import csv
from Bidder import Bidder

from sys import argv
import time

def read_bidders_info(input_name, is_train):
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

def bids_generator(input_name):
    with open(input_name, 'rb') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for line in reader:
            if len(line)!=9 or line[0] == 'bid_id':
                continue
            id = line[0]
            bidder_id = line[1]
            auction = line[2]
            merchandise = line[3]
            device = line[4]
            time = line[5]
            country = line[6]
            ip = line[7]
            url = line[8]
            yield (id, bidder_id, auction, merchandise, device, time, country, ip, url)

def set_bids_to_bidders(bidders_dict, bids_file_name):
    counter = 0
    for bid in bids_generator(bids_file_name):
        bidder_id = bid[1]
        if bidder_id in bidders_dict.keys():
            bidders_dict[bidder_id].add_one_bid(bid)
            counter += 1
    print("Finished adding %d bids to bidders" % counter)
    return bidders_dict

def load_bids_info(input_name):
    bids_list = list()
    for bid in bids_generator(input_name):
        bids_list.append(bid)
    print("Finished loading %d bids" % len(bids_list))
    return bids_list

def run(bidders_file_name, bids_file_name, option):
    if option == 'train':
        bidders_dict = read_bidders_info(bidders_file_name, is_train=True)
        bidders_dict = set_bids_to_bidders(bidders_dict, bids_file_name)
        pickle.dump(bidders_dict, open('bidders_train.p', 'wb'))
    #elif option == 'bid':
    #    bids_list = load_bids_info(bids_file_name)
    #    pickle.dump(bids_list, open('bids.p', 'wb'))
    elif option == 'test':
        bidders_dict = read_bidders_info(bidders_file_name, is_train=False)
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