#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def bin_to_dec(binary_string):
    bin = 0
    for x in range(1,len(binary_string)+1):
        bin += int(binary_string[x-1])*2**(len(binary_string)-x)
    return bin

def dec_to_bin(number):
    bin = ''
    while number >=1:
        bin += str(number%2)
        number=number//2
    return bin[::-1]

encoder_dict = {
        " ":"0",
        "A":"2",
        "B":"22",
        "C":"222",
        "D":"3",
        "E":"33",
        "F":"333",
        "G":"4",
        "H":"44",
        "I":"444",
        "J":"5",
        "K":"55",
        "L":"555",
        "M":"6",
        "N":"66",
        "O":"666",
        "P":"7",
        "Q":"77",
        "R":"777",
        "S":"7777",
        "T":"8",
        "U":"88",
        "V":"888",
        "W":"9",
        "X":"99",
        "Y":"999",
        "Z":"9999"
    }

def telephone_cipher(message):
    cipher = ""
    for x in message:
        if cipher != "" and cipher[-1] == encoder_dict[x][0]:
            cipher += "_"
        cipher += encoder_dict[x]
    return cipher

decipher_dict = {
        "0":" ",
        '2': 'A',
        '22': 'B',
        '222': 'C',
        '3': 'D',
        '33': 'E',
        '333': 'F',
        '4': 'G',
        '44': 'H',
        '444': 'I',
        '5': 'J',
        '55': 'K',
        '555': 'L',
        '6': 'M',
        '66': 'N',
        '666': 'O',
        '7': 'P',
        '77': 'Q',
        '777': 'R',
        '7777': 'S',
        '8': 'T',
        '88': 'U',
        '888': 'V',
        '9': 'W',
        '99': 'X',
        '999': 'Y',
        '9999': 'Z'
    }

def telephone_decipher(telephone_string):
    decipher = ""
    start_of_new_letter = 0
    for x in range (0,len(telephone_string)):
        if x != len(telephone_string)-1 and telephone_string[x] == telephone_string[x+1]:
            continue
        elif telephone_string[x] == "_":
            start_of_new_letter = x+1
            continue
        elif x != len(telephone_string)-1 and telephone_string[x] != telephone_string[x+1] : 
            decipher += decipher_dict[telephone_string[start_of_new_letter:x+1]]
            start_of_new_letter = x+1
        else: 
            decipher += decipher_dict[telephone_string[start_of_new_letter:x+1]]
    return(decipher)

