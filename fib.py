#!/usr/bin/env python3
import sequences
import sys

def main(local_argv):
    n=local_argv
    try:
        type(n)==int
    except ValueError:
            print("must be integer")
    
    print(sequences.fibonacci(n)[-1])
    return(sequences.fibonacci(n)[-1])
    
    """Main function
    See below for why this would exist. The local_argv argument lists command
    line arguments taken from sys.argv within the protected main block below.
    """
if __name__ == "__main__":
    main(sys.argv)