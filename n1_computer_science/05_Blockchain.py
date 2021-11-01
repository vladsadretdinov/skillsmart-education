from hashlib import md5
from time import time
from json import dumps
from typing import List
from random import random


class Block:
    def __init__(self, prev_block_hash=None, prev_block_index=0, timestamp=0.0, data=None, tail_of_hash=""):
        self.prev_block_hash = prev_block_hash
        self.index = prev_block_index + 1
        self.timestamp = timestamp
        self.data = dumps(data)
        self.tail_of_hash = tail_of_hash
        self.nonce = ""
        self.hash: str or None = None
        self.make_hash_block()

    def make_hash_block(self):
        self.hash = self.hashing_data()

        if self.tail_of_hash != "":
            self.search_nonce()

    def hashing_data(self):
        return md5(f"{self.prev_block_hash}{self.index}{self.timestamp}{self.data}{self.nonce}".encode()).hexdigest()

    def search_nonce(self):
        while not self.hash.endswith(self.tail_of_hash):
            self.nonce = random()
            self.hash = self.hashing_data()


class Blockchain:
    def __init__(self, tail_of_hash=None):
        self.tail_of_hash = tail_of_hash
        self.chain: List[Block] = []

    def add_block(self, data):
        if len(self.chain) == 0:
            prev_block_hash = ""
            prev_block_index = 0
            tail_of_hash = "00000"
        else:
            prev_block_hash = self.chain[-1].hash
            prev_block_index = self.chain[-1].index
            tail_of_hash = self.tail_of_hash
        new_block = Block(
            prev_block_hash=prev_block_hash,
            prev_block_index=prev_block_index,
            timestamp=time(),
            data=data,
            tail_of_hash=tail_of_hash,
        )
        self.chain.append(new_block)

    def find_block(self, hash: str):
        for block in self.chain:
            if block.hash == hash:
                return block
        return None

    def check_hash_sum(self):
        for block in self.chain:
            test_hash = block.hash
            if test_hash != block.hashing_data():
                return False
        return True


if __name__ == "__main__":
    from datetime import datetime

    for i in range(1, 3):
        print('--------------------')
        print(f'test with {i} zeros')
        start = datetime.now()
        print('start', start)
        chain = Blockchain("0" * i)
        chain.add_block({'vlad': 'sad'})
        chain.add_block({'vlad': 'sad'})
        chain.add_block({'vlad': 'sad'})
        end = datetime.now()
        print('  end', end)
        print('  dur', end - start)
        print('--------------------')

    block_to_find = chain.chain[-1]
    hash_to_find = block_to_find.hash
    print("Find block by hash? -", chain.find_block(hash_to_find) == block_to_find)
    print("Is chain correct? -", chain.check_hash_sum())

    print('--------------------')
    block_to_find = chain.chain[-1]
    hash_to_find = "trololo"
    print("Find block by hash? -", chain.find_block(hash_to_find) == block_to_find)
    len_of_chain = len(chain.chain)
    mid_of_chain = len_of_chain // 2
    mid_block = chain.chain[mid_of_chain]
    mid_block.nonce = '123456'
    print("Is chain correct? -", chain.check_hash_sum())
