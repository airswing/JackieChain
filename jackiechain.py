import hashlib
import json


class JackieChain:
    def __init__(self):
        self.blockchain = []
        self.blockchain.append(self.generate_genesis_block())
        self.blockchain[0].hash = self.hash_block(self.blockchain[0])

    @staticmethod
    def generate_genesis_block():
        genesis_block = {
            'prev_hash': None,
            'height': 0,
            'transactions': []
        }
        return genesis_block

    def create_block(self, transactions):
        if not self.verify_txs(transactions):
            raise Exception(f"Create block failed! Bad transactions:\n{transactions}")

        block = {
            'prev_hash': self.blockchain[-1].hash

        }

    @staticmethod
    def hash_block(block):
        serialized = json.dumps(block, sort_keys=True).encode('utf-8')
        return hashlib.sha256(serialized).hexdigest()

    @staticmethod
    def verify_txs(transactions):
        return True

    @staticmethod
    def verify_block(block):
        #if block.height