"""."""
from functools import wraps


def collect_results_in_queue(func):
    """Decorate functions to collect results into results_queue.

    Args:
        results_queue (mp.Manager.Queue): Queue to put results into.
    """
    @wraps(func)
    def func_wrapper(*args, **kwargs):
        results_queue = kwargs.pop('results_queue')
        # Pass args and kwargs as is to the function.
        try:
            result = func(*args, **kwargs)
        except Exception as ex:
            print("EXCEPTION: {}".format(args))
            print(ex.args)
            result = None
        # Put result into result_queue.
        results_queue.put(result)

    return func_wrapper


def generate_mproc_func_results(async_func, args_iterable=(), n_processes=1, queue_size=1):
    """Yield results of a async_function called multiple times using mproc.

    Args:
        async_func (func): A function that is called multiple times using mproc.
            The function MUST CONTAIN AN ARGUMENT called `result_queue`.
            OR
            A function that returns results and has a `collect_results_in_queue`
            DECORATOR.
        args_iterable (iterable): The iterable of arguments that must be passed
            to the `async_func`. The size of the iterable defines the number
            of mproc async function calls.
        n_processes (int): Number of processes in pool.
        queue_size (int): The size of the internal queue that is used to collect
            results. This helps control memory.

    Returns:
        generator of results of asyn_func
    """
    # Allocate Multiprocessing Resources
    import multiprocessing as mp
    pool = mp.Pool(n_processes)
    manager = mp.Manager()
    results_queue = manager.Queue(queue_size)
    print("MPROC          : Allocated resources")

    # Produce Async Task Processes
    func_calls = 0
    for args in args_iterable:
        pool.apply_async(async_func, args=(args,), kwds={'results_queue': results_queue})
        func_calls += 1
    else:
        print("MPROC          : Applied {} async calls".format(func_calls))

    # Consume results from queue
    item_count = 0
    while True:
        if not results_queue.empty():
            item_count += 1
            yield results_queue.get()
            results_queue.task_done()

        if item_count == func_calls:
            print("MPROC          : Joining Queue and StopIteration.")
            results_queue.join()
            raise StopIteration
