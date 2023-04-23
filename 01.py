str = "パタトクカシーー"
ans = []
for i in range(len(str)):
    if (i+1) % 2 == 1:
        ans.append(str[i])
print("".join(ans))