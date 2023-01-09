def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    # YOUR CODE HERE
    stop_num = stop + 1
    numbers =  list(range(start ,stop_num))
    return  print(numbers)

count_up(5, 10)        
