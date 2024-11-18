def square_range(pebbles):
    i = 0
    while pow(i, 2) < pebbles:
        i += 1
    return i

def min_circum(num, pebbles):
    if (num-1) * num > pebbles:
        return (num-2 + num-1) * 2
    else:
        return (num-1) * 4

if __name__ == "__main__":
    pebbles = int(input())

    # 1은 0 <- 아니지! 2는 4가 맞긴함
    if pebbles == 0: # 핸들 해줄필요 없긴함
        print(0)
    elif pebbles == 1:
        print(4)
    else:
        sq_num = square_range(pebbles)
        circumference = min_circum(sq_num, pebbles)
        print(circumference)