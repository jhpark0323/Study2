def reverse_words(S):
    result = []
    word = []
    is_tag = False

    for char in S:
        if char == '<':
            if word:
                result.extend(word[::-1])
                word = []
            is_tag = True
            result.append(char)
        elif char == '>':
            is_tag = False
            result.append(char)
        elif is_tag:
            result.append(char)
        elif char == ' ':
            result.extend(word[::-1])
            result.append(char)
            word = []
        else:
            word.append(char)
    
    if word:
        result.extend(word[::-1])
    
    return ''.join(result)

S = input().strip()
print(reverse_words(S))