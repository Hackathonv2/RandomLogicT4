import random
import sys

def main():
    index = 0
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip('\n'))
    first = lines[0]
    second = lines[1]
    comp = ""

    for c in first:
        for i in second:
            if i == c:
                comp = comp + c

    for c in first:
        if c == comp[index]:
            index = index + 1

    print(index, comp)
    if (len(comp) == index):
        print("TEMPETE")
    else:
        print("NORMAL")

if __name__ == "__main__":
    main()
