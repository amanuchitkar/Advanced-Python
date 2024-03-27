import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import PyPDF2
import os

def compress_to_pdf(input_path, output_path, compression_quality=85):
    with open(input_path, 'rb') as f:
        reader = PyPDF2.PdfFileReader(f)
        writer = PyPDF2.PdfFileWriter()

        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            writer.addPage(page)

        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

    return output_path

def compress_to_jpg(input_path, output_path, quality=85):
    image = Image.open(input_path)
    image.save(output_path, quality=quality, optimize=True)
    return output_path

def compress_file():
    input_path = file_path_var.get()
    output_format = format_var.get()
    compression_quality = int(quality_var.get())
    output_location = output_location_var.get()

    if not input_path:
        messagebox.showerror('Error', 'Please select a file.')
        return

    try:
        if output_location:
            output_path = os.path.join(output_location, 'compressed_output')
        else:
            output_path = 'compressed_output'

        if output_format == 'PDF':
            output_path += '.pdf'
            compress_to_pdf(input_path, output_path, compression_quality)
        else:
            output_path += '.jpg'
            compress_to_jpg(input_path, output_path, compression_quality)
        messagebox.showinfo('Success', f'File compressed successfully! Output saved as: {output_path}')
    except Exception as e:
        messagebox.showerror('Error', f'An error occurred: {str(e)}')

def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("All files", "*.*")])
    file_path_var.set(filename)

def select_output_location():
    output_location = filedialog.askdirectory()
    output_location_var.set(output_location)

# Create the main window
root = tk.Tk()
root.title("File Compressor")
# root.iconbitmap('image.ico')

# Variables to store file path, output format, quality, and output location
file_path_var = tk.StringVar()
format_var = tk.StringVar(value='PDF')
quality_var = tk.StringVar(value='85')
output_location_var = tk.StringVar()

# Create the GUI elements
tk.Label(root, text="Select File:").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=file_path_var, width=50).grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=browse_file).grid(row=0, column=2, padx=5, pady=5)

tk.Label(root, text="Choose Output Format:").grid(row=1, column=0, padx=5, pady=5)
tk.OptionMenu(root, format_var, "PDF", "JPEG").grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Compression Quality (0-100):").grid(row=2, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=quality_var, width=10).grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Select Output Location:").grid(row=3, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=output_location_var, width=50).grid(row=3, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=select_output_location).grid(row=3, column=2, padx=5, pady=5)

tk.Button(root, text="Compress File", command=compress_file).grid(row=4, column=1, padx=5, pady=10)

# Run the Tkinter event loop
root.mainloop()
