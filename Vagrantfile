# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

default_box = "opensuse/Leap-15.6.x86_64"
defalt_version = "15.6.13.197"
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  
  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.

  config.vm.define "course5" do |master|
    master.vm.box = default_box
    master.vm.box_version = defalt_version
    master.vm.hostname = "course5"  
    master.vm.boot_timeout = 900
    master.vm.network 'private_network', ip: "192.168.0.200",  virtualbox__intnet: true
    
    # Disable automatic box update checking. If you disable this, then
    # boxes will only be checked for updates when the user runs
    # `vagrant box outdated`. This is not recommended.
    # config.vm.box_check_update = false

    # Create a forwarded port mapping which allows access to a specific port
    # within the machine from a port on the host machine. In the example below,
    # accessing "localhost:8080" will access port 80 on the guest machine.
    # NOTE: This will enable public access to the opened port
    master.vm.network "forwarded_port", guest: 80, host: 8080
    master.vm.network "forwarded_port", guest: 9090, host: 9090
    master.vm.network "forwarded_port", guest: 9090, host: 8888
    master.vm.network "forwarded_port", guest: 3000, host: 3000
    master.vm.network "forwarded_port", guest: 3030, host: 3030
    master.vm.network "forwarded_port", guest: 8080, host: 8080
    master.vm.network "forwarded_port", guest: 16686, host: 8088
    master.vm.network "forwarded_port", guest: 8888, host: 8888
    master.vm.network "forwarded_port", guest: 8000, host: 8000
    master.vm.network "forwarded_port", guest: 22, host: 2222, id: "ssh", disabled: true
    master.vm.network "forwarded_port", guest: 22, host: 2000 # Master Node SSH
    master.vm.network "forwarded_port", guest: 6443, host: 6443 # API Access

    master.vm.provider "virtualbox" do |vb|
      vb.cpus = 3
      # Customize the amount of memory on the VM:clear
      vb.memory = "6096"
      vb.name = "course 5"
      end

    master.vm.provision "shell", inline: <<-SHELL
      sudo zypper refresh
      #sudo zypper --non-interactive install helm
      sudo zypper install -y git
      curl -sfL https://get.k3s.io | sh -
    SHELL
  end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Enable provisioning with a shell script. Additional provisioners such as
  # Ansible, Chef, Docker, Puppet and Salt are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   apt-get update
  #   apt-get install -y apache2
  # SHELL

  # args = []
  #     config.vm.provision "k3s shell script", type: "shell",
  #         path: "scripts/k3s.sh",
  #         args: args
end