# The Sea Captain Challenge

The Sea Captain is the owner of the fine Frying Dutchman establishment, and he
doesn't like Homer eating all of the shrimp in the buffet.  He'd like to kick him
out for abusing the all-you-can-eat policy, but that risks a breach of contract 
lawsuit from Lionel Hutz.  You can help him be a savvy proprietor and use a tried 
technique from Red Lobster to keep Homer from eating all of the shrimp. 

The trick: 
load up Homer on Cheddar Bay Biscuits to keep him from eating so many crustaceans.  
The delivery person knows the Sea Captain likes to do this, and will add biscuits to the shrimp orders when the Captain is there.  The delivery person should now check to see 
if the Sea Captain is at work and when he's there throw some biscuits into every order he delivers.  If the Captain is not at work, he won't add them.  These metaphors are getting 
stretched a bit thin at this point, so more clearly:

* Write a program in the `sea_captain` directory to be run with `make start`.
* Upon startup, update our captain in the `employee` table to 'working'.
* When the captain is working, every time the `delivery_person` program makes
  a delivery, it should put some biscuits in the stockroom that the Captain can place
  on the buffet to make Homer stop eating shrimp for a while.
* Upon shutdown, update the captain back to idle.
* When the captain is idle, should not put biscuits in the stockroom buffet.
  
