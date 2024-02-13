1. Connect to VM terminal
    - ssh root@{VM_IP}
    - pass phrase

2. Ubuntu VM configuration
   - apt-get upgrade && apt-get update
   - newer kernel = ok
   - which services restart:
       - dbus.services
       - irqbalance.service
       - multpathd.service
       - networkd-dispatcher.service
       - packagekit.service
       - polkit.service
       - rsyslog.service
       - ssh.service
       - systemd-logind.service

3. Adding user and password
   - adduser {username}

4. Adding new user to group sudo
   - usermod -aG sudo {username}
   - id {username}

5. Adding ssh key
   rsync --archive --chown=alpha:alpha ˜/.ssh /home/alpha

6. Install packages
   - sudo apt install htop
   - htop 

7. Allocate memory in swap file
   - sudo fallocate -l 2G /swapfile
   - sudo chmod 600 /swapfile
   - sudo mkswap /swapfile
   - sudo swapon /swapfile
