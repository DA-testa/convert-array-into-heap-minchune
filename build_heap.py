# python3


def build_heap(array):
    swap = []
    n = int((len(array) // 2) - 1)
    for k in range(n, -1, -1):
        heapsort(array, k, swap)
    return swap

def right(val):
    return 2 * val + 2

def left(val):
    return 2 * val + 1

def heapsort(array, val, swap):
    l = left(val)
    r = right(val)
    if l < len(array) and array[l] < array[val]:
        smallest = l
    else:
        smallest = val
    if r < len(array) and array[r] < array[smallest]:
        smallest = r
    if smallest != val:
        array[smallest], array[val] = array[val], array[smallest] #changing the place of the element
        swap.append(int(val))
        swap.append(int(smallest)) #add to the list
        heapsort(array, smallest, swap)


def main():
    n = 0
    data = []
    input_data = input()
    if input_data[0] == 'F':
        path = input()
        file = open("./tests/" + path, mode="r")
        lines = file.readlines()
        n = int(lines[0])
        data = list(map(int, lines[1].split()))
    if input_data[0] == 'I':
        n = int(input())
        data = list(map(int, input().split()))

    swaps = build_heap(data)

    print(int(len(swaps) / 2))
    for i in range(len(swaps)):
        if i % 2 == 0:
            print(str(swaps[i]) + " " + str(swaps[i + 1])) #pāra skaitļu pārbaude


if __name__ == "__main__":
    main()
