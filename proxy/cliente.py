# main.py

from resource import RealResource
from proxy import ProxyResource

def client_code(resource, user):

    resource.access(user)

if __name__ == "__main__":

    real_resource = RealResource()
    users_permitidos = ["Alastor", "Lilith"]

    proxy = ProxyResource(real_resource, users_permitidos)

    proxy.access("Lilith")
    proxy.access("Alastor")
    proxy.access("Charlie")

    access_log = proxy.get_access_log()
    print("Log de acessos: ", access_log)
