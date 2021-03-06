# Docker Swarm

```
vagrant up
vagrant ssh manager
docker node ls
docker node inspect manager --pretty
docker node inspect worker1 --pretty
docker node inspect worker2 --pretty

docker service create -p 80:80 --replicas 3 --name helloworld rstarmer/hostname:latest
docker stack deploy -c app/docker-compose.yml hostname-app
http://192.168.10.2:80/
```

## Instalacja SwarmPit

```
git clone https://github.com/swarmpit/swarmpit -b master
docker stack deploy -c swarmpit/docker-compose.yml swarmpit
http://192.168.10.2:888/
```

## Instalacja Portainer

```
curl -L https://downloads.portainer.io/portainer-agent-stack.yml -o portainer-agent-stack.yml
docker stack deploy -c portainer-agent-stack.yml portainer	
https://192.168.10.2:9443
```	

## Uruchomienie NFS
```
https://blog.ruanbekker.com/blog/2020/09/20/setup-a-nfs-server-with-docker/
docker-compose -f nfs.docker-compose.yml up -d
```

