def strlen(s):
    l = 0
    if s == '':
        return 0
    else:
        l +=1
    return l + strlen(s[1:])

def main():
    s = input("Write something here ")
    print(strlen(s))
    
if __name__ == "__main__":
    main()