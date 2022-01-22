## Docker Swarm

```
vagrant up
vagrant ssh manager
docker node ls
docker node inspect manager --pretty
docker node inspect worker1 --pretty
docker node inspect worker2 --pretty
```

# Instalacja SwarmPit

```
git clone https://github.com/swarmpit/swarmpit -b master
docker stack deploy -c swarmpit/docker-compose.yml swarmpit
http://192.168.10.2:888/

docker service create -p 80:80 --replicas 3 --name helloworld rstarmer/hostname:latest
http://192.168.10.2:80/
```

# Instalacja Portainer

```
curl -L https://downloads.portainer.io/portainer-agent-stack.yml -o portainer-agent-stack.yml
docker stack deploy -c portainer-agent-stack.yml portainer	
http://192.168.10.2:9443
```	