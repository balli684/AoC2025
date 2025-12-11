import textwrap

def readfile(filename):
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split(',')
    rtn = []
    for line in data:
        splt = line.split('-')
        rtn += [[int(splt[0]), int(splt[1])]]
    return rtn

def main():
    data = readfile('input.txt')
    result = 0
    for line in data:
        for item in range(line[0], line[1]+1):
            string_item = str(item)
            for length in range(1, len(string_item)):
                if len(string_item) % length == 0:
                    wrapped = textwrap.wrap(string_item, length)
                    if len(set(wrapped)) == 1:
                        result += item
                        break

    print(result)

if __name__ == '__main__':
    main()