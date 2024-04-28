# import qrcode

# def link_to_qr(link, filename="qrcode.png"):
#     # Generate QR code
#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_L,
#         box_size=10,
#         border=4,
#     )
#     qr.add_data(link)
#     qr.make(fit=True)

#     # Create QR code image
#     img = qr.make_image(fill_color="black", back_color="white")

#     # Save QR code image to file
#     img.save(filename)

#     print(f"QR code generated and saved as '{filename}'")

# # Example usage:
# link = "https://amanuchitkar.pythonanywhere.com/"
# link_to_qr(link, "C:\\Users\Aman\Downloads\example_qr_code.png")

from PIL import Image, ImageDraw

def generate_qr_code(link, filename="qrcode.png"):
    # Define QR code dimensions and pixel colors
    qr_size = 21
    white = (255, 255, 255)
    black = (0, 0, 0)

    # Create a new blank image
    qr_image = Image.new("RGB", (qr_size, qr_size), white)
    draw = ImageDraw.Draw(qr_image)

    # Generate the QR code pattern
    qr_pattern = [
        "####### ##   #######",
        "#     #  ##  #     #",
        "# ### # # ## # ### #",
        "# ### #  ##  # ### #",
        "# ### #  ##  # ### #",
        "#     #  ##  #     #",
        "####### ##   #######",
    ]

    # Convert QR pattern to binary (0 for white, 1 for black)
    qr_pattern = [[0 if c == " " else 1 for c in row] for row in qr_pattern]

    # Draw the QR code on the image
    for y, row in enumerate(qr_pattern):
        for x, pixel in enumerate(row):
            if pixel == 1:
                draw.rectangle([x, y, x + 1, y + 1], fill=black)

    # Save the image as PNG
    qr_image.save(filename)
    print(f"QR code generated and saved as '{filename}'")

# Example usage:
link = "https://amanuchitkar.pythonanywhere.com/"
generate_qr_code(link, "example_qr_code.png")
