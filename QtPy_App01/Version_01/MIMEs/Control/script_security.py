from passlib.context import CryptContext
import pathlib

sec_file_desc = 'password_file'
pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)

def save_password (password) :
    encrypt_pwd = encrypt_password(password)
    with open ( sec_file_desc , 'w') as writer :
        writer.write(encrypt_pwd)

def encrypt_password(password):
    return pwd_context.encrypt(password)


def check_encrypted_password(password, hashed):
    return pwd_context.verify(password, hashed)


def check_pwd_file():
    file = pathlib.Path(sec_file_desc)
    return file.exists()


def validate_pwd (password):
    with open (sec_file_desc , 'r') as reader :
        return check_encrypted_password( password,  reader.read() )
