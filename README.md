# The Frying Dutchman
http://www.hulu.com/watch/23445

## Setup
To run the programs in these challenges, you'll need working versions of
[Python](http://www.python.org), [Ruby](http://www.ruby-lang.org), [Rails](http://rubyonrails.org),
[SQLite](http://www.sqlite.org), and [RabbitMQ](http://www.rabbitmq.com).  These things are
all installed in the [Vagrant](http://www.vagrantup.com) image at the root of this
repo to get an environment set up hassle-free.  The setup instructions below
assume you will be using this Vagrant environment.

1. Install [Vagrant](http://www.vagrantup.com).
1. Clone this repository.
1. From the root of this repository, run `vagrant up` (this may take a while to
   download and configure all of the dependencies).

## The Programs

### The Frying Dutchman

This program is a Rails application that renders a single web page representing
The Frying Dutchman restaurant from the best Simpsons episode ever.  The Frying
Dutchman is an all-you-can-eat fried seafood restaurant, and this web page
displays what orders the restaurant has made for food, what food is in the 
restaurant's stock room, and how many shrimp are out in the buffet.  The page 
must be reloaded to see any changes in these counts.

To start this program, follow these steps:

1. Open an SSH session to the Vagrant environment with `vagrant ssh`.  This
   should automatically place you in the `/vagrant` directory on the VM, which
   is sync'd with the root directory of your local clone of this repository.
1. In this ssh session, execute these commands to start the Frying Dutchman program:

        cd the_frying_dutchman
        make start

1. The application can be accessed on your local machine at `http://localhost:3001`.

The number of shrimp in the stockroom is kept in a SQLite database
(`/vagrant/the_frying_dutchman/db/development.sqlite3`), in the
`stockroom_items` table.  This database also keeps track of the delivery
person, named `Pat`, in the `employees` table.

Orders to have food delivered to the Frying Dutchman and items available for consumption in the buffet are represented by the `orders` and `buffet` queue respectively in the RabbitMQ instance running in the Vagrant VM. A web monitoring interface for this instance is accessible on your local machine at `http://localhost:15673`. You can log in with login: guest and password: guest.

You can try clicking on the `Order Shrimp` button to add some shrimp orders to the queue.

### Homer

> Yaar! Twas a moonless night, dark as pitch, when out of the mist came a
> beast more stomach than man.

Homer is a simple python application that endlessly consumes shrimp from the buffet.  To start him going:

1. Open another SSH session with `vagrant ssh`.
1. In this session, start the Homer program with these commands:

        cd homer
        make start

Homer says `Woohoo!` every time he consumes a message from the `buffet` queue.  You'll probably notice, however, that without a delivery person, no shrimp will make it to your stockroom for the Captain to put out on the buffet.  This first challenge fixes that problem.

## The Challenges

The following three challenges help complete the system that makes up the Frying Dutchman restaurant.  Check out the details in each challenge for more information on what is required to complete them. 

* [The Delivery Person](challenges/delivery_person.md)
* [The Sea Captain](challenges/sea_captain.md)
* [The Frying Dutchman Renovations](challenges/renovations.md)
