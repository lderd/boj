n, m = map(int, input().split())
truths = list(map(int, input().split()))
if truths[0] > 0:
    truths = set(truths[1:])
else:
    truths = set()
parties = []
impossible = set()

for _ in range(m):
    party_people = list(map(int, input().split()))
    party_people = set(party_people[1:])
    if party_people & truths:
        impossible |= party_people
    parties.append(party_people)
while True:
    tmp = set()
    for party in parties:
        if party & impossible:
            tmp |= party | impossible
    if tmp == impossible:
        break
    impossible = tmp
answer = m
for party in parties:
    if party & impossible:
        answer -= 1
print(answer)