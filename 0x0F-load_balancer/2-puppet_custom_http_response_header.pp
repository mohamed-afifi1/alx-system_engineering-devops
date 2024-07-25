# install nginx
exce {'command':
command  => 'sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow "Nginx HTTP"
sudo mkdir -p /var/www/html /var/www/error
sudo chmod -R 755 /var/www
echo "Hello World!" > /var/www/html/index.html
echo "Ceci n\'est pas une page" > /var/www/html/404.html
server_config=\
"server {
	listen 80 default_server;
	listen [::]:80 default_server;
	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;
	server_name _;
	add_header X-Served-By \$hostname;
	location / {
		try_files \$uri \$uri/ =404;
	}
	if (\$request_filename ~ redirect_me){
		rewrite ^ https://youtube.com permanent;
	}
	error_page 404 /404.html;
	location = /404.html {
		internal;
	}
}"

echo "$server_config" > /etc/nginx/sites-enabled/default
sudo service nginx restart
',
provider => shell,
}
