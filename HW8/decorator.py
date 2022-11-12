from datetime import datetime


def timer(name: str):
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = function(*args, **kwargs)
            end = datetime.now()
            time = end - start
            print(
                f"Function [{name}] execution time: {time.seconds}s, {time.microseconds}ms"
            )
            return result

        return wrapper

    return real_decorator

