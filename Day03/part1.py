def readfile(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            data.append(line.strip())
    return data

def main():
    data = readfile('input.txt')
    output = 0
    for line in data:
        ten = 0
        for position in (range(len(line)-1)):
            number = int(line[position])
            if number > ten:
                ten = number
                tenposition = position
        one = 0
        for position in (range(tenposition + 1, len(line))):
            number = int(line[position])
            if number > one:
                one = number
        output += ten * 10 + one
    print(output)

if __name__ == '__main__':
    main()