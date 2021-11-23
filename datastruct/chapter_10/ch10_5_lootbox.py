def min_box(lst, number_of_boxes):
    left = max(lst)
    right = sum(lst)
    while left <= right:
        box_size = (left+right)//2
        box_count = 0
        i = 0
        while i < len(lst):  # for all item in list
            weight = 0
            while i < len(lst) and weight + lst[i] <= box_size:  # put item in box
                weight += lst[i]
                i += 1
            box_count += 1  # increase box number
        # print(box_count, box_size)

        if box_count <= number_of_boxes:  # too large
            right = box_size - 1
        else:  # too light
            left = box_size + 1

    return left


if __name__ == '__main__':
    # Output value will be between max(lst) to sum(lst)
    lst, box = input("Enter Input : ").split('/')
    box = int(box)
    lst = list(map(int, lst.split()))
    print(f"Minimum weigth for {box} box(es) = {min_box(lst, box)}")