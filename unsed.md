
Archi Seam Farm
```yml
  archi_steam_farm:
    container_name: archi_steam_farm
    image: justarchi/archisteamfarm:latest
    volumes:
      - ./config/archi:/app/config
    ports:
      - 1242:1242
    restart: unless-stopped
    environment:
      - TZ=America/Sao_Paulo
    dns:
      - 1.1.1.1
    depends_on:
      - pi_hole
```


Netdata
```yml
   netdata:
    image: netdata/netdata
    container_name: netdata
    ports:
      - 1999:19999
    restart: unless-stopped
    cap_add:
      - SYS_PTRACE
    security_opt:
      - apparmor:unconfined
    volumes:
      - ./netdata_config/netdata:/etc/netdata:ro
      - netdatalib:/var/lib/netdata
      - netdatacache:/var/cache/netdata
      - /etc/passwd:/host/etc/passwd:ro
      - /etc/group:/host/etc/group:ro
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro
      - /etc/os-release:/host/etc/os-release:ro
    environment:
      - TZ=America/Sao_Paulo
    depends_on:
      - pi_hole
```

Homebridge
```yml
  homebridge:
    container_name: homebridge
    image: oznu/homebridge:latest
    restart: unless-stopped
    network_mode: host
    environment:
      - PGID=1001
      - PUID=1001
      - HOMEBRIDGE_CONFIG_UI=1
      - HOMEBRIDGE_CONFIG_UI_PORT=8581
      - TZ=America/Sao_Paulo
    volumes:
      - ./homebridge_config:/homebridge
    depends_on:
      - pi_hole

```


EmulatorJs (deprecated)
```
  emulatorjs:
    image: linuxserver/emulatorjs:arm64v8-latest
    container_name: emulatorjs
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=America/Sao_Paulo
      - SUBFOLDER=/
      # - DISABLE_IPFS=true
    volumes:
      - ./config/emulatorjs:/config
      - $HOME/remote_docs/share/wesley/roms:/data
    ports:
      - 8087:3000
      - 8086:80
      - 4001:4001
    restart: unless-stopped
    dns:
      - 1.1.1.1
```
