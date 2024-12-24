# 基于jupyterhub 官方镜像开始构建
FROM jupyterhub/jupyterhub:latest

# 暴露一个 8000 端口
EXPOSE 8000

ARG user=test

RUN cd /srv/jupyterhub && jupyterhub --generate-config
RUN echo -e "c.JupyterHub.admin_access = True  \nc.JupyterHub.admin_users = set(['${user}','root']) # 设置管理员用户  \nc.JupyterHub.authenticator_class = 'jupyterhub.auth.PAMAuthenticator' \nc.LocalAuthenticator.create_system_users = True # 可以使用web页面添加用户 \n" >> /srv/jupyterhub/jupyterhub_config.py

# 修改 创建用户的命令
RUN sed -i 's/SHELL = \/bin\/sh/SHELL = \/bin\/bash/g' /etc/default/useradd


# 安装基础的软件
RUN apt update && apt install vim wget sudo -y

# 创建用户的命令并且给添加密码
RUN useradd --create-home --no-log-init --shell /bin/bash ${user} \
    && adduser ${user} sudo \
    && echo "${user}:1" | chpasswd




# 更新pip包管理器
RUN python3 -m pip install --upgrade pip

# 安装jupyter notebook  和 lab 以及相关依赖
RUN pip install jupyter_server jupyterlab jupyter \
 jupyterlab-language-pack-zh-CN nodejs jupyterlab-lsp \
 jupyter_contrib_nbextensions jupyter_nbextensions_configurator \
 'python-lsp-server[all]' -i https://pypi.tuna.tsinghua.edu.cn/simple




