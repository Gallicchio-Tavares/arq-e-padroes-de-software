from resource import Resource

class ProxyResource(Resource):
    def __init__(self, real_resource: Resource, users_permitidos: list) -> None:
        self._real_resource = real_resource
        self._users_permitidos = users_permitidos
        self._access_log = []

    def access(self, user: str) -> None:
        """
        Verificar a permissão do usuário antes de deixá-lo acessar o recurso confidencial
        """

        if user in self._users_permitidos:
            self._real_resource.access(user)
        else:
            print(f"ProxyResource: \033[31mUsuário '{user}' não tem permissão para acessar o recurso.\033[m")
            
        self.log_access(user)

    def log_access(self, user: str) -> None:
        """
        Logs do acesso feito pelo user.
        """
        self._access_log.append(user)

    def get_access_log(self) -> list:
        """
        Retorna a lista de nomes dos usuários que tentaram acessar o recurso.
        """
        return self._access_log
