import time


def decorator(my_log: dict, path: str):

    def decorator_(foo):

        def new_foo(*args, **kwargs):
            start_time = time.time()
            result = foo(*args, **kwargs)
            delay = time.time() - start_time
            report = {
                'start time': time.ctime(),
                'delay': delay.__round__(4),
                'arguments': [args, kwargs],
                'result': result}

            if my_log.get(foo.__name__):
                my_log[foo.__name__].append(report)
            else:
                my_log[foo.__name__] = [report]

            with open(path, "a", encoding='UTF-8') as f:
                f.writelines(f"{report['start time']} : вызов {foo.__name__} : {report}\n")

            return result

        return new_foo

    return decorator_
