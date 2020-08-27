import inspect
import time


def measure(
    version=None,
    input_map=None,
    output_map=None,
    log_function=print,
):
    if input_map is None:
        input_map = dict()
    if output_map is None:
        output_map = dict()

    def measure_function(func):
        default = dict()
        for name, parameter in inspect.signature(func).parameters.items():
            if parameter.default is inspect._empty:
                value = None
            else:
                value = parameter.default
            default[name] = value

        def wrapper(*args, **kwargs):
            # Run function
            start_time = time.time()
            result = func(*args, **kwargs)
            stop_time = time.time()
            duration = stop_time - start_time
            # Create data about inputs
            input_kwargs = default.copy()
            for key, arg in kwargs.items():
                input_func = input_map.get(key, lambda _: _)
                input_kwargs[key] = input_func(arg)

            keys = list(default.keys())
            for k, arg in enumerate(args):
                key = keys[k]
                input_func = input_map.get(key, lambda _: _)
                input_kwargs[key] = input_func(arg)

            # Create data about outputs
            output_kwargs = dict()
            for key, output_func in output_map.items():
                output_kwargs[key] = output_func(result)

            data = ({
                "function": func.__name__,
                "module": func.__module__,
                "version": version,
                "input": input_kwargs,
                "output": output_kwargs,
                "duration": duration,
            })

            log_function(data)
            return result

        return wrapper

    return measure_function
