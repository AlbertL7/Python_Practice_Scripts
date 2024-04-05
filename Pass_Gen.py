import secrets
import string
import subprocess
import getpass
from datetime import datetime

"""
How to Use
1. Have a text file you want to encrypt and keep your passwords in. I called it Vault
2. Open Disk Utility and create a new image
    - Disk Utility > got to File > New Image > Blank Image
3. Configure Disk Image
    - Save as: Give Disk Image a name
    - Name: Name that will appear when image is mounted, I called mine Vault, same as the file I want to encrypt
    - Size: Choose a small size like 10MB
    - Format: Choose Mac OS Extended (Journaled)
    - Encryption: Choose AES 128 or 256 and set your password
        NOTE: set password the same as your sudo password
    - Partitions: Choose Single Partition - Apple Partition Map
    - Image Format: Choose "read/write" disk image
4. Create and mount the Disk image. 
5. Once the Disk image is mounted move the file onto the Disk Image
6. Eject the Disk image and that file is now encrypted.
7. You must run this program in the terminal, it requires an interactive terminal session for sudo authorization.
    - an easy way to do this is to bring up spotlight and type terminal. Click ther terminal application and run this using python3.
"""

def passgen():
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation # or you can use the following to customize the exact you want to use special characters: "!@#$%^&*()-_=+[{]}|;:',<.>/?"
    alphabet = letters + digits + special_chars
    
    
    account = input('Account Name / website: ')
    username = input('Username / Email: ')
    extra = input('Amplifying Information / Pin: ')
    usr_pwd = input('Would you like to create your own password? (y / n): ').lower()
    while True:
        if usr_pwd == 'y':
            pwd = input("--> ")
            break
        elif usr_pwd == 'n':
            pwd_length = int(input('\nEnter the number length of the password: '))
            pwd = ''.join(secrets.choice(alphabet) for i in range(pwd_length))
            print('Generated Password:', pwd)
            redo = input("Do you want to generate a different password? (y / n) ").lower()
            if redo != 'y':
                break
        else:
            print("Error --> Pleae choose 'y' or 'n': ")
    time_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print(f'\nAccount: {account}\nPASSWORD: {pwd}\nUSERNAME: {username}\nAMPLIFYING INFO: {extra}\nDate: {time_date}')
    
    return account, username, extra, pwd, time_date

def is_volume_mounted(volume_path):
    result = subprocess.run(["df"], capture_output=True, text=True)
    return volume_path in result.stdout

def mount_disk(image_path, volume_path):
    if is_volume_mounted(volume_path):
        print(f"Volume at '{volume_path}' is already mounted. Writing Account info to Vault.....")
        return
    command = f"sudo hdiutil attach '{image_path}' -stdinpass"
    subprocess.run(command, shell=True, check=True)

def append_to_file(append_to_file_path, account, username, extra, pwd, time_date):
    with open(append_to_file_path, 'a') as file:
        print(f'\n\nAccount: {account}\nPASSWORD: {pwd}\nYour USERNAME: {username}\nAMPLIFYING INFO: {extra}\nDate: {time_date}', file=file)
        
    print(f"Account information written to {append_to_file_path}")
    print("\n####Password Generated####\n")

print('\n####Password Generator####\n')
image_path = 'Change this' # Example: '/Users/username/Desktop/vault.dmg'
volume_path = 'Change this'  # This is the mount point of the disk image Example: '/Volumes/Vault'
append_to_file_path = f'{volume_path}/change this' # Exmaple f'{volume_path}/Vault'

account, username, extra, pwd, time_date = passgen()
mount_disk(image_path, volume_path)
append_to_file(append_to_file_path, account, username, extra, pwd, time_date)
