players=str(input() .split())
dangerous1="1111111"
dangerous0="0000000"

if dangerous1 in players or dangerous0 in players:
    print("YES")
else:
    print("NO")