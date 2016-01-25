import unittest
from models.DeliveryPerson import DeliveryPerson
from ConfigParser import ConfigParser

# read config to pass to class instantiation
config = ConfigParser()
config.read("config/contract.ini")

channel = config.get("queue", "channel")
host = config.get("queue", "host")
db_path = config.get("database", "db_path")

pat = DeliveryPerson('Pat', channel, host, db_path)

class TestDeliveryPerson(unittest.TestCase):

  # make sure the delivery person has the right config
  def test_valid_contract(self):
      """Test configuration.
      Ensure that the values we read from config is what
      is used in the Delivery Person class.
      """
      contract = pat.get_contract()

      testName = contract["name"]
      testChannel = contract["channel"]
      testHost = contract["host"]
      testDbPath = contract["db_path"]

      # testing static values here since they shouldn't change without the test being updated
      self.assertEqual(testName, "Pat")
      self.assertEqual(testChannel, "orders")
      self.assertEqual(testHost, "localhost")
      self.assertEqual(testDbPath, "/vagrant/the_frying_dutchman/db/development.sqlite3")

  def test_working_status(self):
      """Test that the worker status is properly updated."""
      status = pat.get_status()
      self.assertEqual(status, "idle")
      pat.start_working()
      status = pat.get_status()
      self.assertEqual(status, "working")
      pat.stop_working()
      status = pat.get_status()
      self.assertEqual(status, "idle")

if __name__ == '__main__':
    # now that we've instantiated our delivery person we test them
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDeliveryPerson)
    unittest.TextTestRunner(verbosity=2).run(suite)