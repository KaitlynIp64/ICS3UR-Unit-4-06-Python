#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Nov 2022
# This program prints all possible RGB combination

def main():
    # this function uses a nested loop

    counter1 = 0
    counter2 = 0
    counter3 = 0

    # process & output
    for counter1 in range(255):
        for counter2 in range(255):
            for counter3 in range(255):
                print("RGB(" {0} "," {1} "," {2}")".format(counter1, counter2, counter3))


if __name__ == "__main__":
    main()