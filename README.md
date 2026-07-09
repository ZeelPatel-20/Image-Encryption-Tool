# Image Encryption & Decryption Tool

## Overview

The **Image Encryption & Decryption Tool** is a Python-based application that demonstrates a basic image encryption technique using pixel manipulation. The program encrypts and decrypts an image by modifying the RGB(A) values of each pixel using a user-defined secret key.

This project was developed to demonstrate fundamental concepts of **image processing**, **basic cryptography**, and **Python programming**. It provides a simple command-line interface that allows users to securely encrypt and decrypt image files.

---

## Features

- Encrypt images using a user-defined secret key
- Decrypt encrypted images using the same key
- Pixel-level RGB(A) value manipulation
- Preserves image dimensions and format
- Interactive command-line interface
- Beginner-friendly implementation for learning cryptography concepts

---

## Technologies Used

- Python 3
- Pillow (PIL)

---

## Project Structure

```
Image-Encryption-Tool/
│── image_encryptor.py
│── original_image.png
│── encrypted_image.png
│── decrypted_image.png
│── requirements.txt
│── README.md
│── LICENSE
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/ZeelPatel-20/Image-Encryption-Tool.git
```

Navigate to the project directory:

```bash
cd Image-Encryption-Tool
```

Install the required dependency:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the application:

```bash
python image_encryptor.py
```

The program will prompt you to:

1. Choose **Encrypt (E)** or **Decrypt (D)**
2. Enter the image file path
3. Enter a secret numeric key

The processed image will be saved automatically.

---

## Sample Output

### Encryption

```
=== Image Encryption Tool ===

Type 'E' to Encrypt or 'D' to Decrypt: E
Enter image file path: original_image.png
Enter secret key (number): 15

Encrypted image saved as encrypted_image.png
```

### Decryption

```
=== Image Encryption Tool ===

Type 'E' to Encrypt or 'D' to Decrypt: D
Enter image file path: encrypted_image.png
Enter secret key (number): 15

Decrypted image saved as decrypted_image.png
```

---

## Project Workflow

1. Load the input image.
2. Read each pixel from the image.
3. Apply the secret key to modify the RGB(A) values.
4. Save the encrypted image.
5. Reverse the process using the same key to restore the original image.

---

## Learning Outcomes

This project demonstrates practical understanding of:

- Image Processing
- Pixel Manipulation
- Basic Cryptography Concepts
- Python Programming
- File Handling
- Command-Line Application Development

---

## Future Enhancements

- AES-based image encryption
- Password-derived encryption keys
- Graphical User Interface (GUI)
- Support for multiple image formats
- Batch image encryption
- Enhanced error handling and validation

---

## Disclaimer

This project is intended for **educational purposes only**. The implemented pixel manipulation technique demonstrates encryption concepts but is **not suitable for securing sensitive or confidential data**. For real-world applications, standard cryptographic algorithms such as **AES (Advanced Encryption Standard)** should be used.

---

## Author

**Zeel Patel**

M.Sc. Digital Forensics & Cyber Security  
Institute of Advanced Research (IAR), Gandhinagar

GitHub: https://github.com/ZeelPatel-20

---

## License

This project is licensed under the MIT License.
