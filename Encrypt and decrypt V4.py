# This program is design to encrypt and decrypt data, according to the user's choice
# Author: FP
# Date: 17/02/2019
# Version 3
# Modifications= used modular approach as in OOP, and introduce the choiced to either encrypt or decrypt
# Other modification included was the choice to repeat the process

def main():
# This section is the main program code
# A modular approach was adopted

    repeat= 1
    while repeat==1:
        while True:                                                                 # This section is to handle exceptions to the allowed 
            try:
                choice= int(input("Enter '1' to ENCRYPT, or '2' to DECRYPT: "))     #Integer values 1 or 2.
                break
            except ValueError:
                print("You MUST enter an Integer value of '1' OR '2'.") 

        if choice==1:
               
            #Encryption
            original_text= str(input("Enter the message you wish to encrypt: "))
            while True:
                try:
                    key= int(input("Enter the 'key' for your encryption. A whole number from 1 to 10: "))
                    break
                except ValueError:
                    print("You MUST enter an Integer value of '1' OR '2'.") 

            encrypted_message= ""

            for c in original_text:
                x_ascii= ord (c)
                x_encrypted= x_ascii+key
                encrypted_character= chr(x_encrypted)
                encrypted_message=encrypted_message+encrypted_character

            print("The original message: ",original_text, " was encrypted to: ","'", encrypted_message, "'", "using the key: ", key)

        elif choice==2:
            #Decryption
            original_text= str(input("Enter the message you wish to decrypt: "))
            while True:
                try:
                    key= int(input("Enter the 'key' for your decryption. A whole number from 1 to 10: "))
                    break
                except ValueError:
                    print("You MUST enter an Integer value of '1' OR '2'.") 
         
            decrypted_message= ""

            for c in original_text:
                x_ascii= ord (c)
                x_decrypted= x_ascii-key
                decrypted_character= chr(x_decrypted)
                decrypted_message=decrypted_message+decrypted_character

            print("The encrypted message: ",original_text, " was decrypted to: ","'",decrypted_message,"'", "using the key: ", key)

        else:
            print("You can only enter '1' OR '2'. Enter '1' to ENCRYPT, or '2' to DECRYPT")
        
        while True:
            try:
                repeat= int(input("Enter '1' to REPEAT the process OR any other number to EXIT: "))
                break
            except ValueError:
                print("You MUST enter an Integer value of '1' To repeat OR any other number to EXIT!.") 

       
        

main()
