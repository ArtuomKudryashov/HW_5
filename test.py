def rot13(message):
    abc='abcdefghijklmnopqastuvwxyzabcdefghijklm'
    r=''
    for c in message:
        if c in abc:
            r+=abc[abc.index(c)+13]





    return r
print(rot13("d"))