import sys
input = sys.stdin.readline

def makelist(arr,c,l):
    passwords = []
    vowel = set(['a','e','i','o','u'])
    def backtracking(password,depth):
        if depth == l:
            v_count = 0
            for a in password:
                if a in vowel:
                    v_count += 1
            if v_count >= 1 and l - v_count >= 2:
                passwords.append("".join(password))
            return
        for x in words:
            if password and x<= password[-1]:
                continue
            password.append(x)
            backtracking(password,depth+1)
            password.pop()
    backtracking([],0)
    return passwords

l,c = map(int,input().split())
words = [*map(str,input().split())]
words.sort()
passwords = makelist(words,c,l)
print("\n".join(passwords))
