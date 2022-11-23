#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Nov 2022
# This program prints all possible RGB combination


def main():
    # this function uses a nested loop

    red = 0
    green = 0
    blue = 0
    for red in range(0, 256):
        for green in range(0, 256):
            for blue in range(0, 256):
                print("RGB({0},{1},{2})".format(red, green, blue))
            blue += 1
            green += 1
        red += 1

        print("\nDone.")


if __name__ == "__main__":
    main()
