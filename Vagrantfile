# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  config.vm.network "private_network", type: "dhcp"

  config.vm.define "vm-web" do |machine|
    machine.vm.box = "chef/centos-7.0"
    machine.vm.provision "shell", path: "provisioning/web.sh"
    config.vm.network "forwarded_port", guest: 3000, host: 3001
  end

  config.vm.define "vm-mq" do |machine|
    machine.vm.box = "chef/centos-7.0"
    machine.vm.provision "shell", path: "provisioning/mq.sh"
    config.vm.network "forwarded_port", guest: 15672, host: 15673
  end

  config.vm.define "vm-worker1" do |machine|
    machine.vm.box = "chef/centos-7.0"
  end

  config.vm.define "vm-worker2" do |machine|
    machine.vm.box = "chef/centos-7.0"
  end
end
