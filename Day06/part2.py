def read_from_file(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            data.append(line.strip().split())
    return data

def main():
    data = read_from_file('input.txt')
    results = []
    for x in range(len(data[0])):
        if data[-1][x] == "*":
            result = 1
            for y in range(len(data)-1):
                result *= int(data[y][x])
            results.append(result)
        if data[-1][x] == "+":
            result = 0
            for y in range(len(data)-1):
                result += int(data[y][x])
            results.append(result)
    print(sum(results))
        
if __name__ == '__main__':
    main()
