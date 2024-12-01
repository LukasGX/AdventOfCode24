def pt1():
    with open('data1.txt', 'r') as file:
        # init arrays
        left = []
        right = []
        for line in file:
            # sort in left/right
            line = line.strip()
            split = line.split('   ')
            left.append(int(split[0]))
            right.append(int(split[1]))
        # sort arrays
        left_sort = sorted(left)
        right_sort = sorted(right)
        # pair up
        sum = 0

        for x,y in zip(left_sort, right_sort):
            sum += abs(x - y)

        print(sum)
def pt2():
    with open('data1.txt', 'r') as file:
        # init arrays
        left = []
        right = []
        for line in file:
            # sort in left/right
            line = line.strip()
            split = line.split('   ')
            left.append(int(split[0]))
            right.append(int(split[1]))
        score = 0
        for value in left:
            in_right = right.count(value)
            score += value * in_right
        print(score)

pt2()