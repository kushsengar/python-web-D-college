List1 = ['abc', 'xyz', 'aba', '1221']
cnt = 0
for s in List1:
    if s[0]==s[len(s)-1]:
        cnt+=1

print(cnt)