__author__ = 'qluo'

import numpy as np

class Bidder(object):

    def __init__(self, id_, payment_account_, address_):
        self.id = id_
        self.payment_account = payment_account_
        self.address = address_
        self.label = -1.0
        self.bids_list = list()

    def get_id(self):
        return self.id

    def get_payment_account(self):
        return self.payment_account

    def get_address(self):
        return self.address

    def get_label(self):
        return self.label

    def get_bids_list(self):
        return self.bids_list

    def set_label(self, label_):
        self.label = label_

    def set_bids(self, bids_list_):
        self.bids_list = bids_list_

    def add_one_bid(self, bid):
        self.bids_list.append(bid)

    def get_all_auction(self):
        data = np.array(self.bids_list)
        return data[0::,2]

    def get_number_of_device(self):
        data = np.array(self.bids_list)
        if data.size == 0:
            return 0
        return len(np.unique(data[0::,4]))

    def generate_feature_vector(self):
        data = np.array(self.bids_list)
        if data.size == 0:
            return np.array([0,0,0,0])
        num_device = len(np.unique(data[0::,4]))
        num_country = len(np.unique(data[0::,6]))
        num_ip = len(np.unique(data[0::,7]))
        num_url = len(np.unique(data[0::,8]))
        return np.array([num_device, num_country, num_ip, num_url, self.get_label()])

