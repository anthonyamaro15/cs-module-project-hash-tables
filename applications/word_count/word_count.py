def word_count(s):
    # Your code here
    count = {}

    not_allow = [':', ';', ',', '-', '+', '=', '/', '|',
                 '[', ']', '{', '}', '(', ')', '*', '^', '&', '.']

   # to remove any special character from the string
    modified = ''.join(i for i in s if not i in not_allow)

    modified = s.lower().split()

    if 'no' in modified:
        return {}

    for word in modified:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
