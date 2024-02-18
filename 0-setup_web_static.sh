#!/usr/bin/env bash
#install nginx if not skip
sudo apt-get update
sudo apt-get -y install nginx

#copy default
cp -n /etc/nginx/sites-available/default /etc/nginx/sites-available/origine

#create folders if not exist
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/releases/test/

#creat index.html
echo "
<html>
  <head>
  </head>
  <body>
    Holberton School 'release/test'
  </body>
</html>
" | sudo tee /data/web_static/releases/test/index.html

#Create a symbolic link
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

#Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

#Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i "s@^\tlocation / {@\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;}\n\n\tlocation / {@g" /etc/nginx/sites-available/default

# restart nginx
sudo service nginx restart
