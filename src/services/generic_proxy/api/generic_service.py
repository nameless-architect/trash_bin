

from common.communication.generic_service_contract import GenericServiceContract
from services.generic_proxy.bl.generic_manager import GenericManager


class GenericService(GenericServiceContract):

    def __init__(self, collection_name) -> None:
        super().__init__()
        self._generic_manager: GenericManager = GenericManager.construct(
            collection_name)

    def create(self, model: dict):
        return self._generic_manager.create(model)

    def replace(self, model: dict):
        return self._generic_manager.replace(model)

    def get_by_id(self, model_id: str):
        return self._generic_manager.get_by_id(model_id)

    def get_all(self):
        return self._generic_manager.get_all()

    def delete(self, model_id: str):
        return self._generic_manager.delete(model_id)
