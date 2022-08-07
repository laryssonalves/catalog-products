import time
from timeit import timeit

WALL_EXECUTION_TIMES = 5

def print_readable_time(time_type, time_elapsed):
    seconds, milliseconds = divmod(time_elapsed * 1000, 1000)
    minutes, seconds = divmod(time_elapsed, 60)
    hours, minutes = divmod(minutes, 60)
    print(f'{time_type}: {int(hours):0d} hours, {int(minutes):02d} minutes, {int(seconds):02d} seconds {int(milliseconds):03d} milliseconds')

def function_to_measure():
    time.sleep(2)
    # Write the code you want to time here
    return sum(range(10000000))

# Wall-clock time (it also includes time waiting for resources)
def wall_execution_timer():
    time_elapsed = timeit(function_to_measure, number=WALL_EXECUTION_TIMES)
    print_readable_time('Wall Time', time_elapsed / WALL_EXECUTION_TIMES)

# CPU time (it does not include time waiting for resources)
def cpu_execution_timer():
    start_time = time.process_time()
    function_to_measure()
    end_time = time.process_time()
    time_elapsed = end_time - start_time
    print_readable_time('CPU Time', time_elapsed)

def main():
    cpu_execution_timer()
    wall_execution_timer()

if __name__ == '__main__':
    main()
