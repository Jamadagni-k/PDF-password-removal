from pypdf import PdfReader, PdfWriter

# Input and output file paths
input_pdf = "1117571601_Sep2024.pdf"
output_pdf = "NPS_Sep24.pdf"
password = "999k2508"

# Open the PDF
reader = PdfReader(input_pdf)

# Decrypt the PDF
if reader.is_encrypted:
    reader.decrypt(password)

# Write to a new PDF without encryption
writer = PdfWriter()
for page in reader.pages:
    writer.add_page(page)

with open(output_pdf, "wb") as f:
    writer.write(f)

print("Password removed successfully. Saved as:", output_pdf)