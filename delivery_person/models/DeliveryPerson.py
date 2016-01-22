
class DeliveryPerson(object):
    """

    This program will:

    * Upon startup, update our delivery person in the `employee` table to 
    have a status of `working`
    * Consume messages from the `orders` queue
    * Create a record in the `stockroom_item` table in the SQLite database with the 
    name of the item and count delivered from the order
    * Simulate a 20 second delay for processing each order
    * Upon shutdown, update working employees back to idle

    """

    def __init__(self, name, channel, host, db_path):
        """Initializes a new instance of DeliveryPerson.

        Args:
            self: reference to self
            name: string name of DeliveryPerson
            channel: string queue to act upon
            host: string address of host, can be IP or localhost
            db_path: string path to database
        """
        self.name = name
        self.channel = channel
        self.host = host
        self.db_path = db_path

    def get_contract(self):
        """Getter method for config, used primarily for testing.

        Args:
            self: reference to self
        Returns:
            contract (config) information as a dictionary.
        """
        return {
            "name": self.name,
            "channel": self.channel,
            "host": self.host,
            "db_path": self.db_path
        }
