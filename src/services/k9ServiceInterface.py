from abc import abstractmethod
from abc import ABCMeta

from src.models.k9 import K9

class CrudService(metaclass=ABCMeta):
    @abstractmethod
    def find_k9_by_name(k9_name: str) -> K9:
        pass

    @abstractmethod
    def find_all_k9s() -> list[K9]:
        pass

    @abstractmethod
    def insert_k9(k9: K9) -> K9:
        pass

    @abstractmethod
    def update_k9(_id: str, k9: K9) -> K9:
        pass

    @abstractmethod
    def delete_k9(_id: str) -> None:
        pass