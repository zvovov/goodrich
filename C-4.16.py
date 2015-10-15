#Write a short recursive Python function that takes a character string s and
#outputs its reverse. For example, the reverse of pots&pans would be
#snap&stop .

def reverse_string(s):
    if len(s)<=0:
        #print("<=0")
        return 0
    elif len(s)==1:
        #print("==1", s)
        return s
    else:
        #print(">1", s)
        return s[-1] + reverse_string(s[:-1])

if __name__=="__main__":
    s = input()
    print(reverse_string(s))