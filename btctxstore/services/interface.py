# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


class BlockchainService(object):

    def __init__(self, testnet=False, dryrun=False):
        """TODO doc string"""
        self.testnet = testnet
        self.dryrun = dryrun

    def get_tx(self, txid):
        """TODO doc string"""
        raise NotImplementedError()

    def send_tx(self, tx):
        """TODO doc string"""
        raise NotImplementedError()

    def spendables_for_address(self, bitcoin_address):
        """TODO doc string"""
        raise NotImplementedError()

    def spendables_for_addresses(self, bitcoin_addresses):
        spendables = []
        for addr in bitcoin_addresses:
            spendables.extend(self.spendables_for_address(addr))
        return spendables


