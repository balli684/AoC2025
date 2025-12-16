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
    state = readfile('input.txt')
    newstate = state.copy()
    output = 0
    changed = True
    while changed:
        remove = 0
        for y in range(1, len(state) - 1):
            for x in range(1, len(state[y]) - 1):
                count = 0
                if state[y][x] == "@":
                    if state[y-1][x-1] == "@":
                        count += 1
                    if state[y-1][x] == "@":
                        count += 1
                    if state[y-1][x+1] == "@":
                        count += 1
                    if state[y][x-1] == "@":
                        count += 1
                    if state[y][x+1] == "@":
                        count += 1
                    if state[y+1][x-1] == "@":
                        count += 1
                    if state[y+1][x] == "@":
                        count += 1
                    if state[y+1][x+1] == "@":
                        count += 1 
                    if count < 4:
                        remove += 1
                        newstate[y] = newstate[y][:x] + "x" + newstate[y][x+1:]
        output += remove
        if remove == 0:
            changed = False
        state = newstate.copy() 

    print(output)
            
        
if __name__ == '__main__':
    main()
