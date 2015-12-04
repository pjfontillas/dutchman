# The delivery person challenge

Right now, if you click the `Order Shrimp` button on the Frying Dutchman
site, a JSON message gets placed on the `orders` queue, but there is
nothing to consume that message and deliver the shrimp to the stockroom.  
For this challenge, implement the delivery person.  This is a program that will:

* Upon startup, update our delivery person, Pat, in the `employee` table to 
have a status of `working`
* Consume messages from the `orders` queue
* Create a record in the `stockroom_item` table in the SQLite database with the 
name of the item and count delivered from the order
* Simulate a 20 second delay for processing each order
* Upon shutdown, update working employees back to idle

Write this program in the `delivery_person` directory in any language and with
any tools that you want (feel free to add anything that you want to the
`provisioning.sh` file to make it available in the Vagrant VM).  The only
requirement is that the program can be started in the Vagrant VM by running
`make start` in the `delivery_person` directory.

When this challenge is complete, you should see orders moving out of the queue 
and shrimp showing up in your stockroom on the The Frying Dutchman web page.
