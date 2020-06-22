import os
import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback


pnconfig = PNConfiguration()
pnconfig.publish_key = os.environ.get('pubnub_publish_key')
pnconfig.subscribe_key = os.environ.get('pubnub_subscribe_key')
pubnub = PubNub(pnconfig)

TEST_CHANNEL = 'TEST_CHANNEL'

# Tells that pubnub is now subscribed to all designated channels
pubnub.subscribe().channels([TEST_CHANNEL]).execute()


class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- Incoming message_object: {message_object}')


# Deals with what happens when packet received
pubnub.add_listener(Listener())


# We need to overwrite channel to publish to
def main():
    time.sleep(1)

    pubnub.publish().channel(TEST_CHANNEL).message({'foo': 'bar'}).sync()


if __name__ == '__main__':
    main()
