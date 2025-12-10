import math

def readfile(filename):
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split(',')
    rtn = []
    for line in data:
        spt = [int(line.split('-')[0]), int(line.split('-')[1])]
        rtn += [spt]
    return rtn

def main():
    data = readfile('input.txt')
    result = 0
    for line in data:
        for i in range(line[0], line[1]+1):
            j = str(i)
            mid = (len(j) + 1) // 2
            # print(j[:mid], j[mid:])
            if j[:mid] == j[mid:]:
                result += i
    print(result)

if __name__ == '__main__':
    main()