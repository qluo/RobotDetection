__author__ = 'qluo'

class Bid(object):

    def __init__(self, id_, bidder_id_, auction_id_, merchandise_, device_, time_, country_, ip_, url_):
        self.id = id_
        self.bidder_id = bidder_id_
        self.auction_id = auction_id_
        self.merchandise = merchandise_
        self.device = device_
        self.time = time_
        self.country = country_
        self.ip = ip_
        self.url = url_

    def get_id(self):
        return self.id

    def get_bidder_id(self):
        return self.bidder_id

    def get_auction_id(self):
        return self.auction_id

    def get_merchandise(self):
        return self.merchandise

    def get_device(self):
        return self.device

    def get_time(self):
        return self.time

    def get_country(self):
        return self.country

    def get_ip(self):
        return self.ip

    def get_url(self):
        return self.url
