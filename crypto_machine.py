def crypto_machine():

    keys = 'abcdefghijklmnopqrstuvwxyz !'
    values = keys[-1] + keys[0:-1]

    dict_e = dict(zip(keys,values))
    dict_d = dict(zip(values,keys))

    msg = input("enter your message: ")
    mode = input("enter e to encrypt and d to decrypt:")

    if mode == 'e':
        new_msg = ''.join([dict_e[letter] for letter in msg.lower()])
    elif mode =='d':
        new_msg = ''.join([dict_d[letter] for letter in msg.lower()])
    return new_msg.capitalize()
    
print(crypto_machine())

