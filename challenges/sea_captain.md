# The Sea Captain Challenge

The Sea Captain is the owner of the fine Frying Dutchman establishment, and he
doesn't like Homer eating all of the shrimp in the buffet.  He doesn't feel
comfortable directly telling Homer to stop eating though.  He would really like
to tell the delivery person to sneak something into the buffet every time he
makes a delivery; something that may stop Homer from eating shrimp for enough
time for other customers to get some.  He can only get the delivery boy to do
this when he is at work, however.  If he is not at work, then the delivery
person won't sabotage the buffet.  These metaphors are getting stretched a bit
thin at this point, so more clearly:

* Write a program in the `sea_captain` directory to be run with `make start`.
* This program should somehow signal the `delivery_person` program when it
  is running and when it is not running.
* While this program is running, every time the `delivery_person` program makes
  a delivery, the `delivery_person` program should put something on the buffet
  that will make Homer stop eating shrimp for a while (so you will have to
  modify the `delivery_person` program too).
* If this program shuts down, the `delivery_person` program should not sabotage
  the buffet in this manner.
