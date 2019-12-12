from redis.sentinel import Sentinel
import os

class Connect(object):

    def __init__(self):
        sentinel_svc = os.environ["SENTINEL_SERVICE_HOST"]
        self.master_name = os.environ["MASTER_NAME"]
        self.sentinel = Sentinel([(sentinel_svc, 26379)], socket_timeout=0.1)

    
    def get_master(self):
        master = self.sentinel.discover_master(self.master_name)
        return master[0]