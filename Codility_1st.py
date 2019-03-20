def solution(S):
    l = len(s)
    ans = ""

    for i in range(l-1):
        if (s[i]<s[i+1]):
            ans+=s[i]
    if s[l-2] > s[l-1]:
            ans+=s[l-2]
    return len(s)-len(ans)
if __name__ == "__main__":
    s = "banana"
    print(solution(s))