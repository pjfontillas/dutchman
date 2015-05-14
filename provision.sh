export PATH=/usr/local/bin:$PATH
# Ruby stuff
sudo yum -y install ruby-2.0.0.598-24.el7
sudo yum -y install ruby-rdoc ruby-devel
sudo yum -y install gcc openssl-devel libyaml-devel libffi-devel readline-devel zlib-devel gdbm-devel ncurses-devel patch sqlite-devel
sudo gem install bundler

# Python stuff
sudo yum -y install epel-release
sudo yum -y install python-pip
sudo pip install virtualenv

# MQ stuff
wget https://www.rabbitmq.com/releases/erlang/erlang-17.4-1.el6.x86_64.rpm
sudo rpm -ivh erlang-17.4-1.el6.x86_64.rpm
rm erlang-17.4-1.el6.x86_64.rpm

wget https://www.rabbitmq.com/releases/rabbitmq-server/v3.5.2/rabbitmq-server-3.5.2-1.noarch.rpm
sudo rpm -ivh rabbitmq-server-3.5.2-1.noarch.rpm
rm rabbitmq-server-3.5.2-1.noarch.rpm

# Make 'guest' able to connect from a remote machine
sudo sh -c 'echo [{rabbit, [{loopback_users, []}]}]. > /etc/rabbitmq/rabbitmq.config'
sudo rabbitmq-plugins enable rabbitmq_management --offline
sudo rabbitmq-server -detached

echo "cd /vagrant" >> /home/vagrant/.bashrc

# The Frying Dutchman
cd /vagrant/the_frying_dutchman
make deps
make db
./bin/rake mq:init

# Homer
cd /vagrant/homer
make clean
make deps
