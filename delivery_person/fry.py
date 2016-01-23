from models.DeliveryPerson import DeliveryPerson
from ConfigParser import ConfigParser

if __name__ == '__main__':

    # read config to pass to class instantiation
    config = ConfigParser()
    config.read("config/contract.ini")

    channel = config.get("queue", "channel")
    host = config.get("queue", "host")
    db_path = config.get("database", "db_path")

    pat = DeliveryPerson('Pat', channel, host, db_path)
    pat.init()