while True:
    s = input()
    if s == '.':
        break

    stack = []
    balanced = True

    for char in s:
        if char in '([': 
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                balanced = False
                break
        elif char == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                balanced = False
                break

    if balanced and not stack:
        print("yes")
    else:
        print("no")
