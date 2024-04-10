from abc import ABC, abstractmethod

class Resource(ABC):

    @abstractmethod
    def access(self, user: str) -> None:
        pass


class RealResource(Resource):

    def access(self, user: str) -> None:
        print(f"RealResource: \033[32mAcessando recurso para usuário \033[32m{user}\033[m.")
