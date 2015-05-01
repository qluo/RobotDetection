__author__ = 'qluo'

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
