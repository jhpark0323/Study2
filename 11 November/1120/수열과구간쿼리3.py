def solution(arr, queries):
    n = len(queries)
    for i in range(n):
        arr[queries[i][0]], arr[queries[i][1]] = arr[queries[i][1]] , arr[queries[i][0]]
    answer = arr
    return answer