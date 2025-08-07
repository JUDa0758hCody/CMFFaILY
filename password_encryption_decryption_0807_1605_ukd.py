# 代码生成时间: 2025-08-07 16:05:41
import hashlib
import base64
from gradio.inputs import TextInput, Button
from gradio.outputs import Text
from gradio import Interface

"""
Password Encryption and Decryption Tool using Python and Gradio framework.
This script provides a simple interface for encrypting and decrypting passwords.
"""


# Function to encrypt password
def encrypt_password(password: str) -> str:
    """Encrypts the provided password using SHA-256 hashing."""
    password_bytes = password.encode('utf-8')
    hashed_password = hashlib.sha256(password_bytes).hexdigest()
    return hashed_password

# Function to decrypt password
def decrypt_password(hashed_password: str) -> str:
    """Since SHA-256 is a one-way hash function, decryption is not possible.
    This function will raise a ValueError to indicate that decryption is not supported."""
    raise ValueError("Decryption is not supported for SHA-256 hashed passwords.")

# Create a Gradio interface
iface = Interface(
    fn=encrypt_password,
    inputs=TextInput(label="Enter Password"),
    outputs=Text(),
    title="Password Encryption Tool",
    description="Encrypt any password using SHA-256 hashing and Gradio framework.",
)

# Start the Gradio interface
iface.launch()
