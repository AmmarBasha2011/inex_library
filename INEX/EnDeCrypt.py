from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Cipher import Blowfish
import binascii
import base64

class EnDeCrypt:
    
    @staticmethod
    class aes:
        """
        AES encryption and decryption operations.

        Methods:
        - encrypt: Encrypts a file using AES encryption.
        - decrypt: Decrypts a file encrypted using AES encryption.

        Attributes:
        - None
        """

        def __init__(self):
            pass

        @staticmethod
        def encrypt(file_path="", password=""):
            """
            Encrypts a file using AES encryption.

            Args:
            - file_path: Path to the file to encrypt.
            - password: Password used for encryption.

            Returns:
            - 'done' if encryption is successful.
            - Raises an exception if encryption fails.
            """
            try:
                with open(file_path, 'rb') as f:
                    data = f.read()
                key = password.encode('utf-8').ljust(32, b'\0')
                cipher = AES.new(key, AES.MODE_CBC)
                ct_bytes = cipher.encrypt(pad(data, AES.block_size))
                result = cipher.iv + ct_bytes
                output_path = file_path + ".ywpdne"
                with open(output_path, 'wb') as f:
                    f.write(result)
                return 'done'
            except Exception as e:
                raise e

        @staticmethod
        def decrypt(file_path="", password=""):
            """
            Decrypts a file encrypted using AES encryption.

            Args:
            - file_path: Path to the file to decrypt.
            - password: Password used for decryption.

            Returns:
            - 'done' if decryption is successful.
            - Raises an exception if decryption fails.
            """
            try:
                with open(file_path, 'rb') as f:
                    data = f.read()
                key = password.encode('utf-8').ljust(32, b'\0')
                iv = data[:16]
                ct = data[16:]
                cipher = AES.new(key, AES.MODE_CBC, iv)
                result = unpad(cipher.decrypt(ct), AES.block_size)
                output_path = file_path.replace(".ywpdne", "")
                with open(output_path, 'wb') as f:
                    f.write(result)
                return 'done'
            except Exception as e:
                raise e

    @staticmethod
    class BlowFish:
        """
        Blowfish encryption and decryption operations.

        Methods:
        - encrypt: Encrypts a file using Blowfish encryption.
        - decrypt: Decrypts a file encrypted using Blowfish encryption.

        Attributes:
        - None
        """

        def __init__(self):
            pass

        @staticmethod
        def encrypt(file_path="", password=""):
            """
            Encrypts a file using Blowfish encryption.

            Args:
            - file_path: Path to the file to encrypt.
            - password: Password used for encryption.

            Returns:
            - 'done' if encryption is successful.
            - Returns error message as string if encryption fails.
            """
            try:
                with open(file_path, 'rb') as f:
                    data = f.read()
                key = password.encode('utf-8').ljust(32, b'\0')
                cipher = Blowfish.new(key, Blowfish.MODE_CBC)
                ct_bytes = cipher.encrypt(pad(data, Blowfish.block_size))
                result = cipher.iv + ct_bytes
                output_path = file_path + ".ywpdne"
                with open(output_path, 'wb') as f:
                    f.write(result)
                return 'done'
            except Exception as e:
                return str(e)

        @staticmethod
        def decrypt(file_path="", password=""):
            """
            Decrypts a file encrypted using Blowfish encryption.

            Args:
            - file_path: Path to the file to decrypt.
            - password: Password used for decryption.

            Returns:
            - 'done' if decryption is successful.
            - Returns error message as string if decryption fails.
            """
            try:
                with open(file_path, 'rb') as f:
                    data = f.read()
                key = password.encode('utf-8').ljust(32, b'\0')
                iv = data[:8]
                ct = data[8:]
                cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
                result = unpad(cipher.decrypt(ct), Blowfish.block_size)
                output_path = file_path.replace(".ywpdne", "")
                with open(output_path, 'wb') as f:
                    f.write(result)
                return 'done'
            except Exception as e:
                return str(e)

    @staticmethod
    class Base64:
        """
        Base64 encoding and decoding operations.

        Methods:
        - encrypt: Encrypts a file using Base64 encoding.
        - decrypt: Decrypts a file encoded using Base64 encoding.

        Attributes:
        - None
        """
        
        def __init__(self):
            pass

        @staticmethod
        def encrypt(file_path=""):
            """
            Encrypts a file using Base64 encoding.

            Args:
            - file_path: Path to the file to encrypt.

            Returns:
            - 'done' if encryption is successful.
            - Returns error message as string if encryption fails.
            """
            try:
                with open(file_path, 'rb') as f:
                    data = f.read()
                result = base64.b64encode(data)
                output_path = file_path + ".ywpdne"
                with open(output_path, 'wb') as f:
                    f.write(result)
                return 'done'
            except Exception as e:
                return str(e)
            
        @staticmethod
        def decrypt(file_path=""):
            """
            Decrypts a file encoded using Base64 encoding.

            Args:
            - file_path: Path to the file to decrypt.

            Returns:
            - 'done' if decryption is successful.
            - Returns error message as string if decryption fails.
            """
            try:
                with open(file_path, 'rb') as f:
                    data = f.read()
                result = base64.b64decode(data)
                output_path = file_path.replace(".ywpdne", "")
                with open(output_path, 'wb') as f:
                    f.write(result)
                return 'done'
            except Exception as e:
                return str(e)
            
    @staticmethod
    class Hex:
        """
        Hexadecimal encoding and decoding operations.

        Methods:
        - encrypt: Encrypts a file by converting it to hexadecimal format.
        - decrypt: Decrypts a file from hexadecimal format.

        Attributes:
        - None
        """
        
        def __init__(self):
            pass

        @staticmethod
        def encrypt(file_path=""):
            """
            Encrypts a file by converting it to hexadecimal format.

            Args:
            - file_path: Path to the file to encrypt.

            Returns:
            - 'done' if encryption is successful.
            - Returns error message as string if encryption fails.
            """
            try:
                with open(file_path, 'rb') as f:
                    data = f.read()
                result = binascii.hexlify(data)
                output_path = file_path + ".ywpdne"
                with open(output_path, 'wb') as f:
                    f.write(result)
                return 'done'
            except Exception as e:
                return str(e)
            
        @staticmethod
        def decrypt(file_path=""):
            """
            Decrypts a file from hexadecimal format.

            Args:
            - file_path: Path to the file to decrypt.

            Returns:
            - 'done' if decryption is successful.
            - Returns error message as string if decryption fails.
            """
            try:
                with open(file_path, 'rb') as f:
                    data = f.read()
                result = binascii.unhexlify(data)
                output_path = file_path.replace(".ywpdne", "")
                with open(output_path, 'wb') as f:
                    f.write(result)
                return 'done'
            except Exception as e:
                return str(e)
