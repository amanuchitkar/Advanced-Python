from PIL import Image

def compress_image(input_image_path, output_image_path, quality=50):
    imp=input_image_path
    imp.split
    image = Image.open(input_image_path)
    image.save(output_image_path, quality=quality, optimize=True)
    return output_image_path

# Example Usage:
input_image_path = 'PracticeProblem\CompressImagePro\wallpaperflare.com_wallpaper.jpeg'
output_image_path = 'output.jpeg'
compressed_image_path = compress_image(input_image_path, output_image_path)
print(f'Image compressed and saved to: {compressed_image_path}')
