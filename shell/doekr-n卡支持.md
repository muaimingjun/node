
# docker 容器缺少文件


docker cp jupyterhub001:/usr/local/share/jupyterhub/static/js/admin-react.js .


# 容器配置
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["http://hub-mirror.c.163.com"]
}
EOF

sudo systemctl enable docker
sudo systemctl start docker
sudo groupadd docker
sudo gpasswd -a ${USER} docker
sudo chmod a+rw /var/run/docker.sock


#参考教程
https://note.youdao.com/s/T7041SGO

sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["http://hub-mirror.c.163.com"]
}
EOF

sudo systemctl enable docker
sudo systemctl start docker
sudo groupadd docker
sudo gpasswd -a ${USER} docker
sudo chmod a+rw /var/run/docker.sock

docker run命令参考下面

https://docs.docker.com/engine/reference/commandline/run/#access-an-nvidia-gpu

NVIDIA runtime
Migration Notice | nvidia-container-runtime
curl -s -L https://nvidia.github.io/nvidia-container-runtime/gpgkey | \
  sudo apt-key add -
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-container-runtime/$distribution/nvidia-container-runtime.list | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-runtime.list
sudo apt-get update


NVIDIA/nvidia-container-runtime: NVIDIA container runtime (github.com)

sudo apt-get install nvidia-container-runtime

docker NVIDIA显卡镜像


docker pull nvidia/cuda:11.8.0-devel-ubuntu22.04
cuda 11.7
docker pull nvidia/cuda:11.8.0-devel-ubuntu22.04


pip3 install torch torchvision torchaudio
cuda 11.6
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116
https://note.youdao.com/s/T7041SGO
