"""
This program is based on Carl Friedrich Gauss' formula
for calculating the sum of n consecutive integers:
S = n(n+1) / 2.
"""


def user_input():
    """ Accept user input and return start, stop and step."""
    try:
        start = int(input("Enter your start integer (i): "))
        stop = int(input("Enter your stop integer (n): "))
        step = int(input("Enter your step (k): "))
    except ValueError:
        print("Enter an integer for i, n & k.")
    else:
        return start, stop, step    


def sum_gauss_formula():
    """Return the omplementation of Gauss' formula."""
    start, stop, step = user_input()
    # unpack values based on start, stop and step params
    seq = range(start, stop, step)
    sum_of_consec_ints = (len(seq)*(seq[0] + seq[-1])) // 2
    return sum_of_consec_ints


def run_program():
    """Main program loop."""
    print(__doc__)
    while True: 
        cont = input("Enter any  character to use the program or 'q' "
                        "to quit: ").lower()
        if cont in ['q', 'quit']:
            break
        else:
            print(sum_gauss_formula())


run_program()