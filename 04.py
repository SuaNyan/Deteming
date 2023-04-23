sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
list = sentence.split()
check_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
ans = {}

for i in range(len(list)): #リストの要素分繰り返す。
    number = i + 1 #one_key = check_listの要素名
    if number in check_list: #check_listのターン
        #chevk_list[i]の文字列の1文字目のみをansに追加
        word = list[i] #変数Keyにi単語目を格納
        ans[number] = word[0]
        #ans.append(key[i])
    else:
        word = list[i]
        ans[number] = word[0:2]
print(ans)