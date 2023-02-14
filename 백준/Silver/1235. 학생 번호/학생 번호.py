n = int(input())
arr = [input() for _ in range(n)]
max_length = len(arr[0])
answer = 1
while answer <= max_length:
    students = set()
    for student in arr:
        if student[-answer:] in students:
            break
        else:
            students.add(student[-answer:])
    else:
        break
    answer += 1
print(answer)