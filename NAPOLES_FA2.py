#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def shift_letter(letter, shift):
    if letter == " ":
        return (" ")
    else:
        if ord(letter) - 65 + shift > 26:
            return chr(((ord(letter) - 65+shift)%26)+65)
        else: 
            return chr(ord(letter) - 65+shift+65)

def caesar_cipher(message, shift):
    decrypted = ""
    for i in message: 
        if i == " ":
            decrypted = decrypted + " "
        else:
            decrypted = decrypted + chr(((ord(i)-65+shift)%26)+65)
    return decrypted

def shift_by_letter(letter, letter_shift):
    if letter == " ":
        return (" ")
    else:
        return chr((ord(letter)-65+ord(letter_shift)-65)%26+65)

def vigenere_cipher(message, key):
    ciphered_message = ""
    if len(message) != len(key):
        key = key*(len(message)//len(key))+key[0:(len(message)%len(key))]
    for i in range(len(message)):
        if message[i] == " ":
            ciphered_message += " "
        else:
            ciphered_message += chr(((ord(message[i])-65)+(ord(key[i])-65))%26+65)
    return(ciphered_message)

def scytale_cipher(message, shift):
    sc_message = ""
    if (len(message)%shift) != 0:
        message += "_"*(shift-(len(message)%shift))
    for i in range(len(message)):
        sc_message += message[((i//shift)+(len(message)//shift)*(i%shift))]
    return sc_message

def scytale_decipher(message, shift):
    sc_message = ""
    for i in range(shift):
        sc_message += message[i::shift]
    return sc_message

