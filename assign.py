
def verify(input_string):
    from cryptography.fernet import Fernet

    # Generate a Fernet key
    key = Fernet.generate_key()
    # Create a Fernet object with that key
    f = Fernet(key)
    # Encrypt the string
    encrypted_string = f.encrypt(input_string.encode())
    print(encrypted_string)
    # Decrypt the encrypted string
    decrypted_string = f.decrypt(encrypted_string)
    print(input_string)
    print(decrypted_string)
    if input_string == decrypted_string:
        response=print("True")
    else: 
        response=print("False")
    return response
verify("password1234")
# create another function to verify whether decrypted string is the same as the input string
