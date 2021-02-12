

class BaseServiceClient:

    def __init__(self, service_class) -> None:
        self._service_instance = service_class()
        
    def call(self, endpoint_name, *args, **kwargs):
        method_to_call = getattr(self._service_instance, endpoint_name)
        return method_to_call(args, kwargs)