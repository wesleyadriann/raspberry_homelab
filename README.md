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

- [ArchiSteamFarm](https://github.com/JustArchiNET/ArchiSteamFarm)
- [Pi-hole](https://pi-hole.net)
- [Nginx](https://www.nginx.com) 


### Setting up (optional)

disable unnecessary software steps in docker-compose.yml  
if using ArchiSteamFarm put the settings in ./archi_steam_farm_config ([setting up](https://github.com/JustArchiNET/ArchiSteamFarm/wiki/Setting-up))

### Running
```sh
docker-compose up --build &
```

### Additional information

#### Web interface

ArchiSteamFarm IPC: [http://localhost:3333](http://localhost:3333)  
Pi-hole admin: [http://localhost/admin](http://localhost/admin)  

#### Others

get Pi-hole admin password
```sh
docker logs pi_hole | grep random
```
