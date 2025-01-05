<h1 align="center">
    Raspberry Containers
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
- [Dashy](https://dashy.to)
- [File Browser](https://filebrowser.org/)

#### :warning: Pending
- torrent web

#### :no_entry: Removed 

- [Nginx](https://www.nginx.com) - [a82f7e2](https://github.com/WesleyAdriann/raspberry_giggle/blob/a82f7e2b02088823827561bfaa57392fcde46c82/docker-compose.yml#L8)
- [Heimdall](https://heimdall.site)- [d7baec8](https://github.com/WesleyAdriann/raspberry_giggle/blob/d7baec8b0dc60371e9867791434eceb58bde9675/docker-compose.yml#L47)

### Docker Images

- [ArchiSteamFarm](https://hub.docker.com/r/justarchi/archisteamfarm)
- [Pi-hole](https://hub.docker.com/r/pihole/pihole)
- [Dozzle](https://hub.docker.com/r/amir20/dozzle/)
- [Heimdall](https://hub.docker.com/r/linuxserver/heimdall)
- [File Browser](https://hub.docker.com/r/filebrowser/filebrowser)
- [Nginx](https://hub.docker.com/_/nginx)
- [Dashy](https://hub.docker.com/r/lissy93/dashy)



### Setting up

Docker - disable unnecessary software steps in docker-compose.yml  
ArchiSteamFarm - put the settings in ./archi_steam_farm_config ([setting up](https://github.com/JustArchiNET/ArchiSteamFarm/wiki/Setting-up))  
File Browser - setting up location to save file

### Running
```sh
docker-compose up --build -d
```

### Additional information

#### Web interface

Dashy: [http://localhost:8080](http://localhost:4000)  
ArchiSteamFarm IPC: [http://localhost:3333](http://localhost:3333)  
Pi-hole admin: [http://localhost/admin](http://localhost/admin)  
Dozzle: [http://localhost:9999](http://localhost:9999)  

#### Others

get Pi-hole admin password
```sh
docker logs pi_hole | grep random
```
