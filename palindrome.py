import sys

if len(sys.argv) == 2:
    script_name = sys.argv[0]
    name = sys.argv[1]
    if name == name[::-1]:
        print("is a plaindrome")
    else: 
        printJ("not a palindrome")
