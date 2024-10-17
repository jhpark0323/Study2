n, k = map(int, input().split())
ls = list(map(int, input().split()))


def find_next(idx):
    new_ls = ls[idx:]
    new_multitab = set(multitab)

    for next_ in range(len(new_ls)):
        if new_ls[next_] in new_multitab:
            new_multitab.discard(new_ls[next_])
            if len(new_multitab) == 1:
                break

    # 남아있는 기기가 없으면 임의로 첫 번째 기기 반환
    return list(new_multitab)[0] if new_multitab else multitab[0]


multitab = []
ans = 0
for i in range(k):
    if len(multitab) < n:
        if ls[i] not in multitab:
            multitab.append(ls[i])
    else:
        if ls[i] in multitab:
            continue

        if i == k - 1:
            ans += 1
            break

        change = find_next(i + 1)
        multitab.remove(change)
        multitab.append(ls[i])
        ans += 1

print(ans)
