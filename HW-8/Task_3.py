import functools
import inspect


def type_check(*expected_types):
    def decorator(func):
        signature = inspect.signature(func)
        parameters = list(signature.parameters.values())

        if len(expected_types) > len(parameters):
            raise ValueError()

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            matching = signature.bind(*args, **kwargs)
            matching.apply_defaults()

            for expected_type, parameter in zip(expected_types, parameters):
                value = matching.arguments.get(parameter.name)
                if not isinstance(value, expected_type):
                    raise TypeError
            return func(*args, **kwargs)

        return wrapper

    return decorator
