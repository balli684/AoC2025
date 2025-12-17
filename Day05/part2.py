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
    return list(dict.fromkeys(sorted))

def check_overlap(list_in):
    new_list = []
    new_list.append(list_in[0])

    for n in range(1, len(list_in)):
        m = 0
        start = list_in[n][0]
        end = list_in[n][1]
        while end >= start and m < n:
            if list_in[m][0] <= start <= list_in[m][1] or list_in[m][0] <= end <= list_in[m][1]:
                if start >= list_in[m][0] and end <= list_in[m][1]:
                    start = 0
                    end = 0
                elif start >= list_in[m][0] and end > list_in[m][1]:
                    start = list_in[m][1] + 1
                elif start < list_in[m][0] and end <= list_in[m][1]:
                    end = list_in[m][0] - 1
            m += 1
        if start > 0 and end > 0:
            new_list.append((start, end))
    new_list.sort(key=lambda x: x[0])

    return list(dict.fromkeys(new_list))

def main():
    data = (input().read_from_file('input.txt')).fresh

    checked = check_overlap(data)

    count = 0
    for item in checked:
        count += item[1] - item[0] + 1

    print(count)
    
        
if __name__ == '__main__':
    main()

# 343143696885053