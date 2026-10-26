if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split(" "))

print(n)
print(arr)
    arr.sort(reverse=True)
    set1 = set(arr)
    x = list(set1)

    print(f"{x[-1]}")