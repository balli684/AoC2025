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
        old_start = start
        # if number < -99 and start == 100:
        #     count += 1
        start += number
        while start < 0:
            # print("less than 1")
            start += 100
            count += 1
        while start > 99:
            # print("greater than 100")
            start -= 100
            count += 1
        
        print(f"{old_start} {number} {start}")
        print(count)
    print(count)
        

if __name__ == '__main__':
    main()