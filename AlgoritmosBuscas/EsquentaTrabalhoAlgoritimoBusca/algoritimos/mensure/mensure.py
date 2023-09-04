import tracemalloc
from memory_profiler import profile, memory_usage
from functools import wraps
import time


def memit_timeit(stream):
    def decorator(func):
        @wraps(func)
        def memit_timeit_wrapper(*args, **kwargs):
            tracemalloc.start()  # Inicia o rastreamento de alocação de memória
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            current, peak = tracemalloc.get_traced_memory()  # Obtém a memória alocada
            tracemalloc.stop()  # Para o rastreamento de alocação de memória

            total_time = end_time - start_time  # Tempo total em segundos

            stream.write(
                f"# N = {len(args[-1])}:"
                f"\nFunction {func.__name__}({args[0]})"
                f"\nTime spent: {total_time} seconds"
                f"\nMemory used: {peak} bytes\n\n"
            )
            return result

        return memit_timeit_wrapper

    return decorator


def memit_timeit_busca_binaria(stream):
    def decorator(func):
        @wraps(func)
        def memit_timeit_wrapper(*args, **kwargs):
            tracemalloc.start()  # Inicia o rastreamento de alocação de memória
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            current, peak = tracemalloc.get_traced_memory()  # Obtém a memória alocada
            tracemalloc.stop()  # Para o rastreamento de alocação de memória

            total_time = end_time - start_time  # Tempo total em segundos
            stream.write(
                f"# N = {len(args[1])}:"
                f"\nFunction {func.__name__}({args[0]})"
                f"\nTime spent: {total_time} seconds"
                f"\nMemory used: {peak} bytes\n\n"
            )
            return result

        return memit_timeit_wrapper

    return decorator


# Função decorator para mensurar o uso de memória
def memit(stream, precision):
    def decorator(func):
        @wraps(func)
        def memit_wrapper(*args, **kwargs):
            mem_before = memory_usage()[0]
            result = func(*args, **kwargs)
            mem_after = memory_usage()[0]
            mem_used = mem_after - mem_before
            formatted_args = ", ".join(
                [repr(arg) for arg in args]
                + [f"{key}={val!r}" for key, val in kwargs.items()]
            )
            stream.write(
                f"Function {func.__name__}({formatted_args[0]}): Memory used: {mem_used:.{precision}f} MiB\n"
            )
            return result

        return memit_wrapper

    return decorator


# Função decorator para mensurar o uso de memória e o tempo de execução


# Função decorator para mensurar o tempo de execução
def timeit(stream, precision):
    def decorator(func):
        @wraps(func)
        def timeit_wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            total_time = end_time - start_time
            formatted_args = ", ".join(
                [repr(arg) for arg in args]
                + [f"{key}={val!r}" for key, val in kwargs.items()]
            )
            stream.write(
                f"# N = {len(args[-1])}:\n"
                f"Function {func.__name__}({formatted_args[0]}): time spent: {total_time:.{precision}f} seconds\n"
            )
            return result

        return timeit_wrapper

    return decorator
