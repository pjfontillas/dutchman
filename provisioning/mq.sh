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
