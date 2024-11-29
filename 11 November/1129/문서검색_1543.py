string = input().strip()
search = input().strip()

count = 0
index = 0

while index <= len(string) - len(search):
    if string[index: index + len(search)] == search:
        count += 1
        index += len(search)
    else:
        index += 1

print(count)