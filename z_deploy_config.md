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
   - sudo ufw allow 22/tcp
   - sudo ufw allow 80
   - sudo ufw allow 443
   - sudo ufw allow 81
   - sudo ufw enable
   - sudo ufw status numbered

9. Configurating the NGINX Proxy
   - nginxproxymanager.com
   - cd ../../opt
   - sudo mkdir nginxproxymanager
   - cd nginxproxymanager
   - sudo nano docker-compose.yml
      - copy proxy.yml and paste to file
   - sudo docker network create reverseproxy_nw
   - sudo docker compose up -d
   - sudo docker ps (verification)
   - http://{VM_IP}:81
      - username: admin@example.com
      - password: changeme

10. Configurating portainer
   - portainer.io
   - sudo docker volume create portainer_data
   - sudo docker run -d -p 8000:8000 --network=reverseproxy_nw --name portainer --restart=awalys -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest
   - sudo docker ps (verification)
   - htop (verification)
   - sudo docker network inspect reverseproxy_nw
   - add proxy host in nginx manager:
      - hosts > proxy host > add proxy host
         - Detail
           - colect sub-domain in digital ocean
           - paste to Domain Names
           - Forward Hostname / ip: portainer
           - Forward Port: 9000
           - Block Common Exploits: true
        - SSL
           - SSL Certificate: Request a new SSL Certificate
           - Force SSL: true
           - HTTP/2 Support: true
           - Agree terms
   - http://portainer.domain/
   - sudo docker restart portainer
   - create shell script
   - comment out the .envs line in the .ignore file
   - set this line in shell terminal > export DIGITAL_OCEAN_IP_ADDRESS={VM_IP}
   - bash docker/digital_ocean_server_deploy.sh
     - insert the pass phrase
   - verify in portainer.io the container

11. Configurating the HTTPS in NGINX
   - create a new proxy host
     - add domain and www.domain
     - Forward Hostname/IP: api (this name is in the container in the production.yml file)
     - Port: 1998
     - Block Common Exploits: true
     - Custom Location > add Location
       - define location: /api/v1/
       - Forward Hostname/IP: api
       - Port: 1998

       - define location: /
       - Forward Hostname/IP: api
       - Port: 1998

       - define location: /supersecretadmin
       - Forward Hostname/IP: api
       - Port: 1998
       - add SSL
         - Force SLL: true
         - HTTP/2 SUpport: true
   - create a new proxy hosts
     - flower.domain.com
     - Forward Hostname/IP: flower
     - Port: 5555
     - Block Common Exploits: true
     - add SSL
         - Force SLL: true
         - HTTP/2 SUpport: true

12. Testing in Inmsonia
   - create a new enviroments with the domain

13. Create a superuser
   - access the root project in VM_IP /app
   - in /app write 
     - sudo docker compose -f production.yml exec api python manage.py createsuperuser

14. Adding the new proxy host
   - new proxy host
      - proxymanager.domain
      - Forward Hostname/Ip: {VM_IP}
      - Port: 81
      - Block Common Exploits: true
      - SSL
         - Force SSL: true
         - HTTP/2 Support: true
         - Agree terms