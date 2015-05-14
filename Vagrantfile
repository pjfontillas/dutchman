# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  config.vm.box = "chef/centos-7.0"
  config.vm.network "private_network", type: "dhcp"
  config.vm.provision "shell", path: "provision.sh"
  config.vm.network "forwarded_port", guest: 3000, host: 3001
  config.vm.network "forwarded_port", guest: 15672, host: 15673
end
