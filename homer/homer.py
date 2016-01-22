import pika
import time


params = pika.ConnectionParameters()
conn = pika.BlockingConnection(parameters=params)
channel = conn.channel()
channel.basic_qos(prefetch_count=1)
queue = channel.queue_declare('buffet')

print("Can't talk... eating...")

def woohoo():
    ascii = '''\

      ___  _____    
    .'/,-Y"     "~-.  
    l.Y             ^.           
    /\               _\_      "Woohoo!"   
   i            ___/"   "\ 
   |          /"   "\   o !   
   l         ]     o !__./   
    \ _  _    \.___./    "~\  
     X \/ \            ___./  
    ( \ ___.   _..--~~"   ~`-.  
     ` Z,--   /               \    
       \__.  (   /       ______) 
         \   l  /-----~~" / 
          Y   \          / 
          |    "x______.^ 
          |           \    
          j            Y 

'''
    return ascii

def doh():
    ascii = '''\

      ___  _____    
    .'/,-Y"     "~-.  
    l.Y             ^.           
    /\               _\_      "D'oh!"   
   i            ___/"   "\ 
   |          /"   "\   o !   
   l         ]     o !__./   
    \ _  _    \.___./    "~\  
     X \/ \            ___./  
    ( \ ___.   _..--~~"   ~`-.
     ` Z,--   /               \ 
       \__.  (  /------- ______)
         \   l  \-----~~" /
          Y   \          /
          |    "x______.^
          |           \ 
          j            Y

'''
    return ascii

try:
    for method, properties, body in channel.consume('buffet'):
        if body == 'shrimp':
            time.sleep(5)
            print woohoo()
            channel.basic_ack(method.delivery_tag)
        elif body == 'biscuit':
            time.sleep(30)
            print doh()
            channel.basic_ack(method.delivery_tag)
finally:
    channel.cancel()
    conn.close()
