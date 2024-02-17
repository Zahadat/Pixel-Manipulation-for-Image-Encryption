from PIL import Image, ImageDraw

def generate_image():
    # Create a new image with white background
    width = 200
    height = 200
    image = Image.new("RGB", (width, height), "white")

    # Draw a red rectangle on the image
    draw = ImageDraw.Draw(image)
    draw.rectangle([50, 50, 150, 150], fill="red")

    # Save the image
    image.save("generated_image.png")
    print("Image generated successfully!")
    return image

def encrypt_image(image, key):
    pixels = image.load()
    width, height = image.size

    encrypted_pixels = []
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            encrypted_pixels.append((r, g, b))

    encrypted_img = Image.new('RGB', (width, height))
    encrypted_img.putdata(encrypted_pixels)
    encrypted_img.save('encrypted_image.png')
    print("Image encrypted successfully!")
    return encrypted_img

def decrypt_image(image, key):
    pixels = image.load()
    width, height = image.size

    decrypted_pixels = []
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            decrypted_pixels.append((r, g, b))

    decrypted_img = Image.new('RGB', (width, height))
    decrypted_img.putdata(decrypted_pixels)
    decrypted_img.save('decrypted_image.png')
    print("Image decrypted successfully!")
    return decrypted_img

# Generate the image
generated_image = generate_image()

# Encrypt the image
key = 50
encrypted_image = encrypt_image(generated_image, key)

# Decrypt the image
decrypted_image = decrypt_image(encrypted_image, key)

# Display the images
generated_image.show()
encrypted_image.show()
decrypted_image.show()
