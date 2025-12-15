def readfile(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            data.append(line.strip())
    return data

def main():
    data = readfile('input.txt')
    output = 0
    batteries = 12
    
    for line in data:
        start = 0
        for i in range(batteries, 0, -1):
            max = 0
            # print("Battery ", i)
            for position in range(start, len(line) + 1 - i):
                # print(position, max)
                number = int(line[position])
                if number > max:
                    max = number
                    start = position + 1
            output += max * (10 ** (i - 1))
    print(output)

if __name__ == '__main__':
    main()