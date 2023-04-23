sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
list = sentence.split()
ans = []
for i in range(len(list)):
    ans.append(len(list[i]))
print(ans)