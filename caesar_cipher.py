# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 16:47:07 2021

@author: Charles
"""
import art

def main():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    print(art.logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))          
    
    def caesar(message, shift, direction):
        final_message = ""
        if direction == "decode":
            shift *= -1
        for char in message:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift
                final_message += alphabet[new_position]
            else:
                final_message += char
        print(f"Message {direction}d: {final_message}")    
    
    caesar(text, shift, direction)
    
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if again == "yes":
        main()
    else:
        print("Goodbye.")
        
            
        


if __name__ == "__main__":
  main()        