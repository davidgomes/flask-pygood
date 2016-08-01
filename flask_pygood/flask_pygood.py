import good as G
from flask import abort, request

from functools import wraps

class EndpointDecorator:
    def __init__(self, schema, *args, **kwargs):
        pass

    def __call__(self, func, *args, **kwargs):
        print("heyy")
        
        def func_wrapper(func):
            @wraps(func)
            def returned_wrapper(*args, **kwargs):
                request_data = {}

                print(dict(request.args))
                
                # if request.method == "GET":
                    # request_dataz = {**request_data, **y}

                try:
                    test_schema = schema(request_data)
                except G.schema.errors.Invalid:
                    return abort(400)

                return func(test_schema)

            return returned_wrapper

        return func_wrapper
