
1. 安装需要使用root账号如果不会设置root账号的请自行google安装mysql过程中需要设置mysql的root账号的密码不要忽略了

sudo apt-get install mysql-server
apt isntall mysql-client
apt install libmysqlclient-dev
2. 以上3个软件包安装完成后使用如下命令查询是否安装成功

sudo netstat -tap | grep mysql
查询结果如下图所示表示安装成功

root@xyz:~# netstat -tap | grep mysql
tcp6       0      0 [::]:mysql              [::]:*                  LISTEN      7510/mysqld     
root@xyz:~# 
二设置mysql远程访问

1. 编辑mysql配置文件把其中bind-address = 127.0.0.1注释了

vi /etc/mysql/mysql.conf.d/mysqld.cnf 
2. 使用root进入mysql命令行执行如下2个命令示例中mysql的root账号密码root

grant all on *.* to root@'%' identified by 'root' with grand option;
flush privileges;
3. 重启mysql

/etc/init.d/mysql restart一安装mysql

1. 安装需要使用root账号如果不会设置root账号的请自行google安装mysql过程中需要设置mysql的root账号的密码不要忽略了

sudo apt-get install mysql-server
apt isntall mysql-client
apt install libmysqlclient-dev
2. 以上3个软件包安装完成后使用如下命令查询是否安装成功

sudo netstat -tap | grep mysql
查询结果如下图所示表示安装成功

root@xyz:~# netstat -tap | grep mysql
tcp6       0      0 [::]:mysql              [::]:*                  LISTEN      7510/mysqld     
root@xyz:~# 
二设置mysql远程访问

1. 编辑mysql配置文件把其中bind-address = 127.0.0.1注释了

vi /etc/mysql/mysql.conf.d/mysqld.cnf 
2. 使用root进入mysql命令行执行如下2个命令示例中mysql的root账号密码root

grant all on *.* to root@'%' identified by 'root' with grand option;
flush privileges;
3. 重启mysql

/etc/init.d/mysql restart
