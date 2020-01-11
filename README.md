# 项目部署

## Niginx
### 安装Nginx
```
yum -y install openssl openssl-dev openssl-devel gcc pcre pcre-devel
useradd nginx -s /sbin/nologin -M
cd /usr/local/src/
wget http://nginx.org/download/nginx-1.13.11.tar.gz
tar xf nginx-1.13.11.tar.gz 
cd nginx-1.13.11
./configure --user=nginx --group=nginx --prefix=/opt/nginx --with-http_stub_status_module --with-http_ssl_module --without-http-cache --with-http_gzip_static_module
make && make install
ln -s /opt/nginx/sbin/* /usr/local/sbin/

```

###  配置Nginx
```
cat /opt/nginx/conf/nginx.conf
user  nginx;
worker_processes  1;

#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

#pid        logs/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    #access_log  logs/access.log  main;

    sendfile        on;
    keepalive_timeout  65;
    gzip  on;

    server {
        listen       80;
        server_name  localhost;

        charset utf-8;
        client_max_body_size 75M;
        #access_log  logs/host.access.log  main;

        location / {
            root   html;
            index  index.html index.htm;
            include uwsgi_params;
            uwsgi_pass 127.0.0.1:8000;
            uwsgi_read_timeout 60;
        }

        location /static {
            expires 30d;
            autoindex on; 
            add_header Cache-Control private;
            alias /opt/wkflow/static/;
        }
 
        location /media {
             alias  /opt/wkflow/media/;
        }        

        error_page  404              /404.html;

        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
    }
}


```
## MySQL

```
yum install -y  ncurses-devel libaio-devel gcc gcc-c++
yum install cmake -y
useradd -s /sbin/nologin -M mysql
id mysql


tar xf mysql-5.6.38.tar.gz
cd mysql-5.6.38

cmake . -DCMAKE_INSTALL_PREFIX=/opt/mysql-5.6.38 \
-DMYSQL_DATADIR=/opt/mysql-5.6.38/data \
-DMYSQL_UNIX_ADDR=/opt/mysql-5.6.38/tmp/mysql.sock \
-DDEFAULT_CHARSET=utf8 \
-DDEFAULT_COLLATION=utf8_general_ci \
-DWITH_EXTRA_CHARSETS=all \
-DWITH_INNOBASE_STORAGE_ENGINE=1 \
-DWITH_FEDERATED_STORAGE_ENGINE=1 \
-DWITH_BLACKHOLE_STORAGE_ENGINE=1 \
-DWITHOUT_EXAMPLE_STORAGE_ENGINE=1 \
-DWITH_ZLIB=bundled \
-DWITH_SSL=bundled \
-DENABLED_LOCAL_INFILE=1 \
-DWITH_EMBEDDED_SERVER=1 \
-DENABLE_DOWNLOADS=1 \
-DWITH_DEBUG=0

make && make install
ln -s /opt/mysql-5.6.38/ /opt/mysql
cd /opt/mysql
cp support-files/my-default.cnf /etc/my.cnf	
/opt/mysql/scripts/mysql_install_db --basedir=/opt/mysql/ --datadir=/opt/mysql/data --user=mysql
chown -R mysql.mysql /opt/mysql-5.6.38/
cp support-files/mysql.server /etc/init.d/mysqld
chmod 700 /etc/init.d/mysqld
echo 'PATH=/opt/mysql/bin/:$PATH' >>/etc/profile
source /etc/profile
mkdir -p /opt/mysql-5.6.38/tmp
chown -R mysql.mysql /opt/mysql-5.6.38/

vim /etc/my.cnf
character_set_server = utf8

/etc/init.d/mysqld start
netstat -nlput | grep 3306

mysql -uroot -p

create database easyops default character set = 'utf8';
select schema_name,default_character_set_name from information_schema.schemata where schema_name = 'easyops';
grant all privileges on easyops.* to easyops@'%' identified by 'easyops';
flush privileges;

```

## 安装Redis

```
wget http://download.redis.io/releases/redis-4.0.14.tar.gz
tar xf redis-4.0.14.tar.gz
cd redis-4.0.14
make MALLOC=jemalloc
make PREFIX=/opt/redis install
echo 'PATH=/opt/redis/bin/:$PATH' >> /etc/profile
source /etc/profile
which redis-server
mkdir /opt/redis/conf
cp redis.conf /opt/redis/conf/
vim /opt/redis/conf/redis.conf
requirepass root

redis-server /opt/redis/conf/redis.conf &

----------验证密码-----
方法一：
[root@db03 ~]# redis-cli -a root
127.0.0.1:6379> set k v
OK
127.0.0.1:6379> exit
方法二：
[root@db03 ~]# redis-cli
127.0.0.1:6379> auth root
OK
127.0.0.1:6379> set a b


```

## Python环境

```
yum -y groupinstall "Development tools"
yum -y install gcc zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel libffi-devel wget libcurl-devel
mkdir /usr/local/python3
cd /usr/local/src/
wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
tar -zxvf Python-3.6.5.tgz
cd Python-3.6.5
./configure --prefix=/usr/local/python3
make && make install
ln -s /usr/local/python3/bin/python3.6 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3.6 /usr/bin/pip3

pip3 install -r requirements.txt

```










