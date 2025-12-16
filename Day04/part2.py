def readfile(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            line = "." + line.strip() + "."
            data.append(line)
    emptyline = ['.' * len(data[0])]
    data = emptyline + data + emptyline
    return data

def main():
    data = readfile('input.txt')
    output = 0
    for y in range(1, len(data) - 1):
        
        for x in range(1, len(data[y]) - 1):
            count = 0
            if data[y][x] == "@":
                if data[y-1][x-1] == "@":
                    count += 1
                if data[y-1][x] == "@":
                    count += 1
                if data[y-1][x+1] == "@":
                    count += 1
                if data[y][x-1] == "@":
                    count += 1
                if data[y][x+1] == "@":
                    count += 1
                if data[y+1][x-1] == "@":
                    count += 1
                if data[y+1][x] == "@":
                    count += 1
                if data[y+1][x+1] == "@":
                    count += 1 
                if count < 4:
                    output += 1
    print(output)
            
        
if __name__ == '__main__':
    main()
