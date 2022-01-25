<h1 align="center">
    Raspberry Giggle
</h1>
<h4 align="center">
    Raspberry server docker softwares
</h3>
<p align="center">
    <img src="https://img.shields.io/github/last-commit/wesleyadriann/raspberry_giggle" />
    <img src="https://img.shields.io/github/license/wesleyadriann/raspberry_giggle" />
    <img src="https://img.shields.io/github/repo-size/wesleyadriann/raspberry_giggle" />
</p>


### Softwares

#### :white_check_mark: Done 

- [ArchiSteamFarm](https://github.com/JustArchiNET/ArchiSteamFarm) 
- [Pi-hole](https://pi-hole.net) 
- [Dozzle](https://dozzle.dev) 
- [Heimdall](https://heimdall.site) 


#### :warning: Pending
- [Samba](https://www.samba.org)
- [FileRun](https://filerun.com)

### Docker Images

- [ArchiSteamFarm](https://hub.docker.com/r/justarchi/archisteamfarm)
- [Pi-hole](https://hub.docker.com/r/pihole/pihole)
- [Dozzle](https://hub.docker.com/r/amir20/dozzle/)
- [Heimdall](https://hub.docker.com/r/linuxserver/heimdall)
- [Samba](https://hub.docker.com/r/servercontainers/samba)
- [FileRun](https://hub.docker.com/r/filerun/filerun)



### Setting up

Docker - disable unnecessary software steps in docker-compose.yml  
ArchiSteamFarm - put the settings in ./archi_steam_farm_config ([setting up](https://github.com/JustArchiNET/ArchiSteamFarm/wiki/Setting-up))  
Samba - set user and local to share in environment variables ([setting up](https://github.com/ServerContainers/samba#environment-variables-and-defaults))  
Heimdall - set environment variables (PGID and PUID, executing ```id``` in terminal)  

### Running
```sh
docker-compose up --build &
```

### Additional information

#### Web interface

Heimdall: [http://localhost:8080](http://localhost:8080)  
ArchiSteamFarm IPC: [http://localhost:3333](http://localhost:3333)  
Pi-hole admin: [http://localhost/admin](http://localhost/admin)  
Dozzle: [http://localhost:9999](http://localhost:9999)  

#### Others

get Pi-hole admin password
```sh
docker logs pi_hole | grep random
```
