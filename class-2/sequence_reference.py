import re
import base64

def main(): 
    option = input('''
        Choose an option to continue with: 
        1. Encryption
        2. Decryption
    ''')
    if(option=='1'):
        encrypt()
    elif(option == '2'):
        decrypt()
    else:
        print('Invalid Option')


def encrypt():
    # Input
    ref_id = input('''Choose a valid password: 1. At least 1 letter between [a-z]
    2. At least 1 number between [0-9]
    3. At least 1 character from [$#@]
    4. Minimum length of transaction password: 6
    5. Maximum length of transaction password: 12: ''')
    # Validation
    is_valid = validate(ref_id)
    if is_valid:
        print('Valid Ref Id')
    else:
        print('Invalid Ref Id')
    
    ref_id_b = ref_id.encode('ascii')
    # Encryption
    encoded_data_b = base64.b64encode(ref_id_b)
    encoded_data = encoded_data_b.decode('ascii')
    print("Encrypted ref_id: ", encoded_data)


def decrypt():
    encoded_data = input('''
    Enter Encrypted Reference Id: 
    ''')
    encoded_data_b = encoded_data.encode('ascii')
    # Encryption
    ref_id_b = base64.b64decode(encoded_data_b)
    ref_id = ref_id_b.decode('ascii')
    print(ref_id)



def validate(ref_id):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#])[A-Za-z\d@$!#%*?&]{6,12}$"
    pattern = re.compile(reg)
    matched = re.match(pattern, ref_id)
    return matched

main()