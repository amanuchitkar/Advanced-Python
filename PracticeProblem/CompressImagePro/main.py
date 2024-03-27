from PIL import Image
import PyPDF2
import os
import fitz 

def compress_image(input_image_path, output_image_path, quality=50):
    imp=input_image_path
    imp.split
    image = Image.open(input_image_path)
    image.save(output_image_path, quality=quality, optimize=True)
    return output_image_path

def compress_pdf(input_pdf_path, output_pdf_path, quality=5):
    # with open(input_pdf_path, 'rb') as f:
    #     reader = PyPDF2.PdfReader(f)
    #     writer = PyPDF2.PdfWriter()

    #     for page_num in range(len(reader.pages)):
    #         page = reader.pages[page_num]
    #         page.compress_content_streams(compression_quality)
    #         writer.add_page(page)

    #     with open(output_pdf_path, 'wb') as output_file:
    #         writer.write(output_file)
    try:
        doc = fitz.open(input_pdf_path)
        doc.save(output_pdf_path, compress_pdf )
        doc.close()
        return output_pdf_path
    except Exception as e:
        # messagebox.showerror('Error', f'An error occurred: {str(e)}')
        print('Error', f'An error occurred: {str(e)}')
        return None

    return output_pdf_path
compress_pdf("pdf.pdf","output.pdf")
# Example Usage:
# input_image_path = 'jpg.jpg'
# output_image_path = 'output.jpg'
# compressed_image_path = compress_image(input_image_path, output_image_path)
# print(f'Image compressed and saved to: {compressed_image_path}')


