import logging
# pip3 install python-logstash   
import logstash
import sys
from time import sleep



class Logging(object):
    def __init__(self, logger_name='python-logger',
                 log_stash_host='192.168.1.11',
                 log_stash_upd_port=5959

                 ):
        self.logger_name = logger_name
        self.log_stash_host = log_stash_host
        self.log_stash_upd_port = log_stash_upd_port


    def get(self):
        logging.basicConfig(
            filename="logfile",
            filemode="a",
            format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
            datefmt="%H:%M:%S",
            level=logging.INFO,
        )

        self.stderrLogger = logging.StreamHandler()
        logging.getLogger().addHandler(self.stderrLogger)
        
        self.logger = logging.getLogger(self.logger_name)
        
        # Add Logstash handler (make sure the logstash python package is installed)
        try:
            self.logger.addHandler(logstash.LogstashHandler(
                self.log_stash_host,
                self.log_stash_upd_port,
                version=1))  # Using Logstash format version 1
        except Exception as e:
            print(f"Failed to connect to Logstash: {e}")
        
        return self.logger




instance = Logging(log_stash_upd_port=5959, log_stash_host='192.168.1.11', logger_name='soumil')
logger = instance.get()



# ----------------------------- a simple App for testing ----------------------------- #
from time import sleep

count = 0

while True:
    count = count + 1

    if count % 2 == 0:
        logger.error('Error Message Code Faield :{} '.format(count))
    else:
        logger.info('python-logstash: test logstash info message:{} '.format(count))
    sleep(1)
