import math

def readfile(filename):
    with open(filename, 'r') as file:
        data = [line.strip() for line in file]
    return data

def convert_to_int(data):
    numbers = []
    for line in data:
        line = line.strip()
        if line[0] =="R":
            numbers.append(int(line[1:]))
        if line[0] =="L":
            numbers.append(-int(line[1:]))
    return numbers

def main():
    start = 50
    numbers = convert_to_int(readfile('input.txt'))
    count = 0
    for number in numbers:
        start += number
        while start < 0:
            start += 100
        while start > 99:
            start -= 100
        if start == 0:
            count += 1
    print(count)
        

if __name__ == '__main__':
    main()