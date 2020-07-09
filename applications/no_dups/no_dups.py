def no_dups(s):
    # Your code here
    arr = s.split()
    no_duplicates = []
   #  no_duplicates = list(set(arr))
   # #  print('====== ', ' '.join(no_duplicates))
   #  return ' '.join(no_duplicates)
    for i in arr:
        if i not in no_duplicates:
            no_duplicates.append(i)
    return ' '.join(no_duplicates)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
