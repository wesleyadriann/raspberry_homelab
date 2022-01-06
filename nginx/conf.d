user nobody;

events {}

http {
  server {
        # configuration of HTTP virtual server 1       
        location /archi {
            proxy_pass archi_steam_farm:1242;
            allow 192.168.0.0;
            deny all;
        }
    } 

}