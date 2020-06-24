import os
import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

from backend.blockchain.block import Block

pnconfig = PNConfiguration()
pnconfig.publish_key = os.environ.get('pubnub_publish_key')
pnconfig.subscribe_key = os.environ.get('pubnub_subscribe_key')


CHANNELS = {
    'TEST': 'TEST',
    'BLOCK': 'BLOCK'
}


class Listener(SubscribeCallback):
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def message(self, pubnub, message_object):
        print(f'\n-- Channel: {message_object.channel} \n\
            Message: {message_object.message}')

        if message_object.channel == CHANNELS['BLOCK']:
            # block = message_object.message
            block = Block.from_json(message_object.message)

            # Creates complete copy of the blockchain list
            potential_chain = self.blockchain.chain[:]
            potential_chain.append(block)

            try:
                self.blockchain.replace_chain(potential_chain)
                print('\n -- Successfully replaced the local chain')
            except Exception as e:
                print(f'\n -- Did not replace chain: {e}')


class PubSub():
    """
    Handles the publish and subscribe layer of the application
    Provides the communication between the ndoes of the blockchain network
    """
    def __init__(self, blockchain):
        self.pubnub = PubNub(pnconfig)

        # Tells that pubnub is now subscribed to all designated channels
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()

        # Deals with what happens when packet received
        self.pubnub.add_listener(Listener(blockchain))

    def publish(self, channel, message):
        """
        Publish the message to the channel.
        """
        self.pubnub.publish().channel(channel).message(message).sync()

    def broadcast_block(self, block):
        """
        Broadcast a block object to all nodes.
        """
        self.publish(CHANNELS['BLOCK'], block.to_json())


# We need to overwrite channel to publish to
def main():
    pubsub = PubSub()

    time.sleep(1)

    pubsub.publish(CHANNELS['TEST'], {'foo': 'bar'})


if __name__ == '__main__':
    main()
