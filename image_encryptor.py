from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b, a = img.getpixel((x, y))

            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            a = (a + key) % 256

            pixels[x, y] = (r, g, b, a)

    encrypted_path = "encrypted_image.png"
    img.save(encrypted_path)

    print(f"Encrypted image saved as {encrypted_path}")


def decrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b, a = img.getpixel((x, y))

            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            a = (a - key) % 256

            pixels[x, y] = (r, g, b, a)

    decrypted_path = "decrypted_image.png"
    img.save(decrypted_path)

    print(f"Decrypted image saved as {decrypted_path}")


print("=== Image Encryption Tool ===")

choice = input("Type 'E' to Encrypt or 'D' to Decrypt: ").upper()

image_path = input("Enter image file path: ")
key = int(input("Enter secret key (number): "))

if choice == 'E':
    encrypt_image(image_path, key)

elif choice == 'D':
    decrypt_image(image_path, key)

else:
    print("Invalid choice!")
