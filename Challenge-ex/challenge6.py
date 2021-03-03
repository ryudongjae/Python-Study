players = ["손흥민","박지성","황의조","기성용","이승우"]

print("현재 경기 중인 선수: ")
for p in players:
    print(p)
print("-"*40)
out = input("OUT 시킬 선수 번호 :")
out = int(out)
del players[out]

inp = input("IN 시킬 선수 이름 :")
players.append(inp)

print("-"*40)
print("교체결과")
for p in players:
    print(p)




    