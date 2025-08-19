from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from pathlib import Path
import base64, hashlib


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

def salvar_priv_pem(priv, caminho="rsa_priv.pem"):
    with open(caminho, "wb") as f:
        f.write(priv.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))

def salvar_pub_pem(pub, caminho="rsa_pub.pem"):
    with open(caminho, "wb") as f:
        f.write(pub.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

def gerar_e_salvar_chaves(bits=2048, dir_keys="keys", nome_priv="rsa_priv.pem", nome_pub="rsa_pub.pem"):
    """
    Função orquestradora p/ usar no menu:
    - Gera o par
    - Salva PEM (privada e pública)
    - Retorna caminhos das chaves
    """
    Path(dir_keys).mkdir(parents=True, exist_ok=True)
    caminho_priv = str(Path(dir_keys) / nome_priv)
    caminho_pub  = str(Path(dir_keys) / nome_pub)

    priv, pub = gerar_par_rsa(bits=bits)
    salvar_priv_pem(priv, caminho=caminho_priv)
    salvar_pub_pem(pub, caminho=caminho_pub)

    return {
        "private_key_path": caminho_priv,
        "public_key_path": caminho_pub,
    }