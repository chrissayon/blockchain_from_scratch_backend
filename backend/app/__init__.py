# import os
import random

from flask import Flask, jsonify

from backend.blockchain.blockchain import Blockchain
from backend.pubsub import PubSub

app = Flask(__name__)
blockchain = Blockchain()
pubsub = PubSub(blockchain)


@app.route('/')
def default():
    return 'Welcome to the blockchain'


@app.route('/blockchain')
def route_blockchain():
    return jsonify(blockchain.to_json())


@app.route('/blockchain/mine')
def route_blockchain_mine():
    transaction_data = 'stubbed_transaction_data'

    blockchain.add_block(transaction_data)

    block = blockchain.chain[-1]
    pubsub.broadcast_block(block)

    return jsonify(block.to_json())


# If instance running on port 5000 already, switch to a different port
# PORT = 5000

# if os.environ.get('PEER') == 'True':
PORT = random.randint(4000, 6000)

if __name__ == '__main__':
    app.run(port=PORT)
