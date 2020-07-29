def solution(number):
    numbers = []
    for i in range (1, number):
        if i % 3 == 0:
            numbers.append(i)
        if i % 5 == 0 and i not in numbers:
            numbers.append(i)
    total = 0
    for n in numbers:
        total += n
    return total

solution(15)