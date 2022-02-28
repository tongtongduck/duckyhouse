#내가 쓴 답
i = 1
fibo_current = 1
fibo_previous = 0
while i <= 25:
    fibo_current += fibo_previous
    fibo_previous += fibo_current
    print(fibo_current)
    print(fibo_previous)
    i += 1

#모범 답안 - 중간에 이어줄 저장소를 만들기.
previous = 0
current = 1
i = 1

while i <= 50:
    print(current)
    temp = previous  # previous를 임시 보관소 temp에 저장
    previous = current
    current = current + temp  # temp에는 기존 previous 값이 저장돼 있음
    i += 1