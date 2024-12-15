# Import the PyPDF2 library to work with PDF files
import PyPDF2

# Load the main PDF document (template) that you want to watermark
# Note: The second argument ("rb") is not required when using PyPDF2.PdfReader in the latest version
template = PyPDF2.PdfReader("textpage.pdf")

# Load the watermark PDF, which contains the watermark design
watermark = PyPDF2.PdfReader("water_mark.pdf")

# Create an instance of PdfWriter to generate the new watermarked PDF
output = PyPDF2.PdfWriter()

# Loop through each page of the main PDF document
for i in range(len(template.pages)):
    # Get the current page from the main PDF
    page = template.pages[i]
    
    # Merge the first page of the watermark PDF onto the current page
    # This adds the watermark to the current page
    page.merge_page(watermark.pages[0])
    
    # Add the modified (watermarked) page to the output PDF
    output.add_page(page)

# Save the watermarked PDF to a new file
# Use 'wb' mode (write binary) since PDFs are binary files
with open('Result_watermarked.pdf', 'wb') as file:
    output.write(file)

# The resulting 'watermarked.pdf' will contain the watermark applied to all pages of the original PDF.
