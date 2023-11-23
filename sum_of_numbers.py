import sys


def pos_num_sums(i, n, k):
    """Return the sum of positive odd and even numbers of a range of numbers."""
    sum_of_even_nums = sum((j for j in range(i, n, k) if j%2 == 0))
    sum_of_odd_nums = sum((j for j in range(i, n, k) if j%2 != 0))
    return (f"\nSum of even numbers from {i} to {n}, step {k} = "
            f"{sum_of_even_nums}; Sum of odd numbers from {i} to {n}, "
            f"step {k} = {sum_of_odd_nums}.\n")


def neg_num_sums(i, n, k):
    """Return the sum of negative odd and even numbers of a range of numbers."""
    sum_of_even_nums = sum((j for j in range(i, n, k) if j%2 == 0))
    sum_of_odd_nums = sum((j for j in range(i, n, k) if j%2 != 0))
    return (f"\nSum of even numbers from {i} to {n}, step {k} = "
            f"{sum_of_even_nums}; Sum of odd numbers from {i} to {n}, "
            f"step {k} = {sum_of_odd_nums}.\n")



# main program loop
while True:
    try:
        i = input("\nEnter a starting number or 'q' to quit: ")
        if i == 'q' or i == 'Q':
            sys.exit('Goodbye')
        else:
            i = int(i)
        n = input("Enter an ending number or 'q' to quit: ")
        if n == 'q' or n == 'Q':
            sys.exit('Goodbye')
        else:
            n = int(n)
        k = input("Enter a step or 'q' to quit: ")
        if k == 'q' or k == 'Q':
            sys.exit('Goodbye')
        else:
            k = int(k)
    except(ValueError):
        print("\nEnter a valid number ⚠️")
    else:
        if k < 0:
            print(neg_num_sums(i, n, k))
        elif k > 0:
            print(pos_num_sums(i, n, k))

        
