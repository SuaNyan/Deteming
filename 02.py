str1 = "パトカー"
str2 = "タクシー"
ans = []
for i in range(4): #i=0~7まで8回繰り返す。
    ans.append(str1[i])
    ans.append(str2[i])
print("".join(ans))