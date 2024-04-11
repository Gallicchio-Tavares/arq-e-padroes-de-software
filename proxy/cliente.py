# main.py

from resource import RealResource
from proxy import ProxyResource

def client_code(resource, user):

    resource.access(user)

if __name__ == "__main__":

    real_resource = RealResource()
    users_permitidos = ["Adnaldo", "Rosimeire"]

    proxy = ProxyResource(real_resource, users_permitidos)

    proxy.access("Rosimeire")
    proxy.access("Adnaldo")
    proxy.access("Cesar")

    access_log = proxy.get_access_log()
    print("Log de acessos: ", access_log)
