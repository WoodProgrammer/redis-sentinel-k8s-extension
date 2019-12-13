import redis
import os

class Connect(object):

    def __init__(self):
        sentinel_svc = os.environ["SENTINEL_SERVICE_HOST"]
        self.master_name = os.environ["MASTER_NAME"]
        self.sentinel = redis.StrictRedis(sentinel_svc, 26379)
        
    
    def get_master(self):
        master = self.sentinel.execute_command("SENTINEL get-master-addr-by-name {}".format(self.master_name))
        return master[0].decode("utf-8")