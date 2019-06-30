
mkdir ../etc 
sudo mv -f ./etc/hello.py /home/box/etc/

sudo rm -rf /etc/nginx/nginx.conf 
sudo mv -f /home/box/web/etc/nginx.conf /etc/nginx/

sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default

sudo ln -sf /home/box/etc/hello.py /etc/gunicorn.d/hello.py

sudo /etc/init.d/nginx restart

sudo gunicorn -b 0.0.0.0:8080 hello:app
