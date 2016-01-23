from datetime import datetime
import pika
import sqlite3
import json
import time

SIMULATED_DELAY = 20  # in seconds


class DeliveryPerson(object):
    """Handles orders and makes deliveries.

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
            name: string name of DeliveryPerson.
            channel: string queue to act upon.
            host: string address of host, can be IP or localhost.
            db_path: string path to database.
        """
        self.name = name
        self.channel = channel
        self.host = host
        self.db_path = db_path
        self.sqlite = None
        self.rabbitmq = None
        self.on_delivery = False
        self.queue = []
        self.status = None

    def get_contract(self):
        """Getter method for config, used primarily for testing.

        Returns:
            contract (config) information as a dictionary.
        """
        return {
            "name": self.name,
            "channel": self.channel,
            "host": self.host,
            "db_path": self.db_path
        }

    def get_status(self):
        """Sets the employee row 'status' value to 'working'."""
        self.sqlite = sqlite3.connect(self.db_path)
        cursor = self.sqlite.cursor()
        query = "SELECT status FROM employees WHERE name = :name"
        args = {
            "name": self.name
        }
        cursor.execute(query, args)
        return cursor.fetchone()[0]

    def init(self):
        """Initializes worker shift. Handles interrupts to signal an idle worker."""
        self.start_working()
        try:
            self.handle_orders()
        except KeyboardInterrupt:
            self.stop_working()

    def start_working(self):
        """Sets the employee row 'status' value to 'working'."""
        self.sqlite = sqlite3.connect(self.db_path)
        cursor = self.sqlite.cursor()
        query = "UPDATE employees SET status = 'working' WHERE name = :name"
        args = {
            "name": self.name
        }
        result = cursor.execute(query, args)
        self.sqlite.commit()

    def stop_working(self):
        """Sets the employee row 'status' value to 'idle'."""
        cursor = self.sqlite.cursor()
        query = "UPDATE employees SET status = 'idle' WHERE name = :name"
        args = {
            "name": self.name
        }
        result = cursor.execute(query, args)
        self.sqlite.commit()
        self.sqlite.close()

    def handle_orders(self):
        """Wait for orders and make deliveries.

        Can only handle one order at a time, for now.
        """
        print "%s is now waiting for orders..." % (self.name)

        # establish RabbitMQ connection
        self.rabbitmq = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))

        # establish channel connection
        channel = self.rabbitmq.channel()
        channel.queue_declare(queue=self.channel)
        channel.basic_consume(self.record_order, queue=self.channel, no_ack=True)

        channel.start_consuming()

    def process_orders(self):
        """Takes the next order in the queue and starts a delivery."""
        print "%s has a delivery to make..." % (self.name)
        order = self.queue.pop(0)
        self.deliver_order(count=order["count"], name=order["name"])


    def record_order(self, ch, method, properties, body):
        """Asynchronously queues up orders.

        Args:
            ch: Channel object.
            method: Delivery method information.
            properties: Delivery information.
            body: Delivery message.
        """
        if isinstance(body, (str, unicode)):
            def bender():
                ascii = '''\
                  _
                 ( )
                  H
                  H
                 _H_
              .-'-.-'-.
             /         \ 
            |           |
            |   .-------'._
            |  / /  '.' '. \ 
            |  \ \ @   @ / /
            |   '---------'
            |    _______|
            |  .'-+-+-+|
            |  '.-+-+-+|      Order Incoming, %s!
            |    """""" |
            '-.__   __.-'
                 """
            ''' % (self.name)
                return ascii


            print bender()

            body = json.loads(body)
            order = {
                "count": body.get("num"),
                "name": body.get("name")
            }
            self.queue.append(order)

            print "Orders in queue: %d" % (len(self.queue))

            # if not on delivery then immediately process order
            if not self.on_delivery:
                self.process_orders()

    def deliver_order(self, count, name):
        """Simulates delivery time and stores shipment in stock.

        Upon returning from a trip the delivery person will
        check for more orders.

        Args:
            count: Amount of items in shipment.
            name: Name of item to be shipped.
        """

        self.on_delivery = True
        print "%s is out for delivery..." % (self.name)

        # simulating a delay for travel time
        self.rabbitmq.sleep(SIMULATED_DELAY)

        if count and name:
            # add delivery to stock
            self.sqlite = sqlite3.connect(self.db_path)
            cursor = self.sqlite.cursor()
            query = "INSERT INTO stockroom_items (name, item_count, created_at, updated_at) VALUES (:name, :count, :created, :updated)"
            now = datetime.now()
            args = {
                "name": name,
                "count": count,
                "created": now,
                "updated": now
            }
            cursor.execute(query, args)
            self.sqlite.commit()

            # back from delivery
            self.on_delivery = False
            print "%s has returned from a delivery..." % (self.name)

            # upon returning look for new queued orders
            if len(self.queue) != 0:
                print "%s has %d orders left to fulfill..." % (self.name, len(self.queue))
                self.process_orders()
