c.JupyterHub.admin_access = True
c.JupyterHub.admin_users = set(['jupyterhub','root'])

c.JupyterHub.authenticator_class = 'jupyterhub.auth.PAMAuthenticator'
c.LocalAuthenticator.create_system_users = True
