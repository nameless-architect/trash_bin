from abc import ABC, abstractmethod


class GenericServiceContract(ABC):

    @abstractmethod
    def create(self, model: dict):
        pass

    @abstractmethod
    def replace(self, model_data: dict):
        pass

    @abstractmethod
    def get_by_id(self, model_id: str):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def delete(self, model_id: str):
        pass
