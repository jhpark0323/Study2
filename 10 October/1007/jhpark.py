# 프로그래머스 당구 연습
def solution(m, n, startX, startY, balls):
    answer = []
    
    # 상
    def up(x1, y1, x2, y2):
        # 원쿠션 조건 X
        if x1 == x2 and y1 < y2:
            return 1e9
        return (n-y1 + n-y2) ** 2 + (x1-x2) ** 2
    
    # 하
    def down(x1, y1, x2, y2):
        # 원쿠션 조건 X
        if x1 == x2 and y1 > y2:
            return 1e9
        return (y1+y2) ** 2 + (x1-x2) ** 2
    
    # 좌
    def left(x1, y1, x2, y2):
        # 원쿠션 조건 X
        if y1 == y2 and x1 > x2:
            return 1e9
        return (x1+x2) ** 2 + (y1-y2) ** 2
    
    #우
    def right(x1, y1, x2, y2):
        # 원쿠션 조건 X
        if y1 == y2 and x1 < x2:
            return 1e9
        return (m-x1 + m-x2) ** 2 + (y1-y2) ** 2
    
    ball_len = len(balls)
    
    for i in range(ball_len):
        endX, endY = balls[i]
        new_ans1 = up(startX, startY, endX, endY)
        new_ans2 = down(startX, startY, endX, endY)
        new_ans3 = left(startX, startY, endX, endY)
        new_ans4 = right(startX, startY, endX, endY)
        answer.append(min(new_ans1, new_ans2, new_ans3, new_ans4))
        
            
    print(answer)
            
            
    return answer