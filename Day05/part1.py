class input:
    def __init__(self):
        self.fresh = []
        self.ingredients = []

    class_map = {
        "fresh": [],
        "ingredients": []
    }

    def read_from_file(self, filename):
        with open(filename, 'r') as file:
            append_to = "fresh"
            for line in file:
                if line.strip() == "":
                    append_to = "ingredients"
                    continue
                self.class_map[append_to].append(line.strip())
                
        self.fresh = sort_ranges(self.class_map["fresh"])
        for i in self.class_map["ingredients"]:
            self.ingredients.append(int(i))
        
        return self

def sort_ranges(ranges):
    sorted = []
    for r in ranges:
        parts = r.split("-")
        start = int(parts[0])
        end = int(parts[1])
        sorted.append((start, end))
    sorted.sort(key=lambda x: x[0])
    return sorted

def main():
    data = input().read_from_file('input.txt')
    output = 0
    for ingredient in data.ingredients:
        for start, end in data.fresh:
            if start <= ingredient <= end:
                output += 1
                break
    print(output)
        
if __name__ == '__main__':
    main()
