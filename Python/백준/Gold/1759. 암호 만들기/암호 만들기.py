import sys
input = sys.stdin.readline

def makelist(arr,c,l):
    passwords = []
    vowel = set(arr).intersection(set(['a','e','i','o','u']))
    def backtracking(password,depth,v_count):
        if depth == l:
            if v_count < 1 or l - v_count < 2:
                return
            passwords.append("".join(password))
            return
        for x in words:
            if password and x<= password[-1]:
                continue
            password.append(x)
            if x in vowel:
                v_count += 1
            backtracking(password,depth+1,v_count)
            if password.pop() in vowel:
                v_count -= 1
    backtracking([],0,0)
    return passwords

l,c = map(int,input().split())
words = [*map(str,input().split())]
words.sort()
passwords = makelist(words,c,l)
print("\n".join(passwords))