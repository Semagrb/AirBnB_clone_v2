#!/usr/bin/env bash

# Update and install nginx
apt-get update
apt-get install -y nginx

# Create directories and index.html file
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Holberton School" > /data/web_static/releases/test/index.html

# Create a symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership to ubuntu
chown -R ubuntu /data/
chgrp -R ubuntu /data/

# Configure Nginx
cat > /etc/nginx/sites-available/default <<EOF
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By \$HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}
EOF

# Restart nginx
service nginx restart
