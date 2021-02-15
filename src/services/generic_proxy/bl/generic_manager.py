

from typing import Any, List
from services.generic_proxy.dal.generic_dal import GenericDAL


class GenericManager:

    def __init__(self, generic_dal: GenericDAL) -> None:
        self._generic_dal = generic_dal

    def create(self, model: dict) -> Any:
        return self._generic_dal.create(model)

    def replace(self, model: dict) -> Any:
        return self._generic_dal.replace(model)

    def get_by_id(self, model_id: str) -> Any:
        return self._generic_dal.get_by_id(model_id)

    def delete(self, model_id: str):
        return self._generic_dal.delete(model_id)

    def get_all(self) -> List[Any]:
        return self._generic_dal.get_all()

    @classmethod
    def construct(cls, collection_name: str):
        generic_dal = GenericDAL(collection_name)
        return cls(generic_dal)
