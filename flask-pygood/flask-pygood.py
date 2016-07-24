import good as G
from functools import wraps

class EndpointDecorator:
    def __init__(self, schema, callback, *args, **kwargs):
        pass

    def __call__(self, func, *args, **kwargs):
        def func_wrapper(func):
            @wraps(func)
            def returned_wrapper(*args, **kwargs):
                request_data = {}

                try:
                    test_schema = schema(request_data)
                except G.schema.errors.Invalid:
                    callback()

                return func(test_schema)

            return returned_wrapper

        return func_wrapper
