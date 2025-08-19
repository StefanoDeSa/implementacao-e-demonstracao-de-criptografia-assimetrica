from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

def exibir_menu():
    print("==============================")
    print("   MENU DE CRIPTOGRAFIA RSA   ")
    print("==============================\n")
    print("[1] Gerar novas chaves")
    print("[2] Encriptar uma mensagem digitada pelo usuário")
    print("[3] Decriptar a mensagem")
    print("[0] Sair\n")


def gerar_par_rsa(bits=2048):
    priv = rsa.generate_private_key(public_exponent=65537, key_size=bits)
    pub = priv.public_key()
    return priv, pub
