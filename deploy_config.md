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

8. Install Docker and Docker Compose
   - sudo apt-get install curl
   - sudo apt-get install gnupg
   - sudo apt-get install ce-certificates
   - sudo mkdir -p /etc/apt/keyrings
   - curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
   - echo "deb [arch=$(dpkg --print-architecture) signed_by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list  > /dev/null
   - sudo apt-get update
   - sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
   - sudo systemctl status docker
   - sudo ufw status numbered