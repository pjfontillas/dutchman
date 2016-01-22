# Fry the Delivery Guy

#### Table of Contents

1. [Overview](#overview)
2. [Setup](#setup)
3. [Usage](#usage)

## Overview

Fry is your average delivery guy. He works for Springfield Express, and is currently contracted
to make deliveries to the Frying Dutchman. Although competent enough, his name is constantly
forgotten and coworkers tend to call him Pat.

This program will:

* Upon startup, update our delivery person, Pat, in the `employee` table to 
have a status of `working`
* Consume messages from the `orders` queue
* Create a record in the `stockroom_item` table in the SQLite database with the 
name of the item and count delivered from the order
* Simulate a 20 second delay for processing each order
* Upon shutdown, update working employees back to idle

## Setup

Before a delivery person can work, they need to know the scope of their contract. You can find it in
- config/contract.ini

It should look something like this:

```
[database]
db_path = /vagrant/the_frying_dutchman/db/development.sqlite3

[queue]
host = localhost
channel = orders
```

## Usage

### Clean

Running `make clean` will clean up the virtualenv.

### Deps

Running `make deps` will build the virtualenv and install dependencies. Will attempt to upgrade if already installed.

### Test

Running `make tests` will run the test suite.

### Start

Running 'make start' will send Fry, I mean Pat, to work.