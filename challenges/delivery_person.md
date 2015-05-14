# The delivery person challenge

Right now, if you click the `Restock Shrimp` button on the Frying Dutchman
site, a JSON message gets placed on the `shrimp-deliveries` queue, but there is
nothing to consume that message and deliver the shrimp.  For this challenge,
implement the shrimp delivery person.  This is a program that will:

* Consume messages from the `shrimp-deliveries` queue
* Right when a message is received, change Pat's status to `delivering`
* Create a record in the `shrimp_deliveries` table in the SQLite database with the number of shrimp in each message
* After the record in `shrimp_deliveries` is created, change Pat's status back to `idle`

Write this program in the `delivery_person` directory in any language and with
any tools that you want (feel free to add anything that you want to the
`provisioning.sh` file to make it available in the Vagrant VM).  The only
requirement is that the program can be started in the Vagrant VM by running
`make start` in the `delivery_person` directory.
