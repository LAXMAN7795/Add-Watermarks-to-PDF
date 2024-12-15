PDF Watermark Converter:
A Python-based tool for applying watermarks to PDF files. This project leverages the PyPDF2 library to overlay watermark designs on every page of a target PDF. It's efficient, easy to use, and perfect for securing and branding your documents.

Features:
Automatically merges a watermark onto all pages of a PDF.
Generates a new watermarked PDF file as the output.
Simple and straightforward implementation using Python.
Supports batch watermarking of multi-page PDFs.
Lightweight and efficient script.

Prerequisites
Python 3.7 or later.
PyPDF2 library.
Install it using pip:
pip install PyPDF2

Project Structure:
📁 pdf-watermark-converter
├── watermark_converter.py   # Main script for watermarking PDFs
├── textpage.pdf             # Sample PDF to be watermarked
├── water_mark.pdf           # Watermark PDF
├── Result_watermarked.pdf   # Output: watermarked PDF
└── README.md                # Project documentation

Code Explanation
Import Required Libraries:
The PyPDF2 library is used to read, merge, and write PDF files.

Load PDF Files:

The textpage.pdf is the main document you want to watermark.
The water_mark.pdf contains the watermark design (applied to all pages).
Merge Watermark with PDF Pages:
Each page of the main PDF is iteratively merged with the first page of the watermark PDF.

Save Output:
The modified pages are saved as a new file, Result_watermarked.pdf.

Sample Output:
After running the script, you'll get a PDF file with your watermark overlaid on every page of the original PDF.

