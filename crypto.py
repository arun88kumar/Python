#This module has two fucntions encrypt and decrypt a string message based the ROT-n value passed to them 
# it is just an expanded version of the ceaser cipher (ROT-13). 


import string

def encrypt(message, rot_value):
    """each character in the provided messgae is converted into the respective encrypted values 
       based on the key value pair generated using the ROT-n value
    """
    keys = get_keys(rot_value)
    return "".join([keys[c] if c in keys.keys() else c for c in message])
    
def decrypt(message, rot_value):
    """each character in the provided encrypted messgae is converted into the respective values 
       based on the key value pair generated using the ROT-n value
    """
    keys = get_keys(rot_value)
    decrypt_keys = dict (zip(keys.values(),keys.keys()))
    return "".join([decrypt_keys[c] if c in decrypt_keys.keys() else c for c in message])



def get_keys(rot_value):
    """generate the key set dictionary based on the ROT-n value provided
    
       The keys coantins both lower and uppercase alphabets
       
       No matching key for special character and numbers
    """
    small_case = list(string.ascii_lowercase)
    big_case = list(string.ascii_uppercase)
    
    keys_small = { x : small_case[(i + rot_value) % 26] for i,x in  enumerate(small_case) }
    keys_big = { x:big_case[ (i + rot_value) % 26 ] for i,x in  enumerate(big_case) }
    
    keys_small.update(keys_big)
    
    return keys_small


if __name__ == '__main__':
    message = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
    print(decrypt(message,13))

    