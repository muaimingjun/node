import os


home = './xinghuo/'

os.system('sudo apt update && sudo apt install -y unzip wget ssh')
os.system(f'mkdir {home} && cd {home} && wget https://code.gitlink.org.cn/shenmo7192/spark-store-dependencies/raw/branch/master/spark-store-dependencies-kylin.zip')
os.system(f'cd {home} && wget https://gitee.com/deepin-community-store/spark-store/releases/download/4.2.4/spark-store_4.2.4_amd64.deb')
os.system(f'cd {home} && unzip spark-store-dependencies-kylin.zip  && tar -xf 解压我.tar ')
os.system(f'cd {home}/all-depends/Debian10-or-ubuntu-20.04/ && bash 一键安装.sh')
os.system(f'sudo apt install -y {home}spark-store_4.2.4_amd64.deb')

os.system(f'sudo rm -fr {home}')

