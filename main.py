from data_provider import extract_text_from_pdf
from data_provider import extract_text_from_website
    
# Read pdf
pdf_path = "hotel_landon.pdf"
extracted_text = extract_text_from_pdf(pdf_path)

# Write to text file
file = open("extracted_text.txt", "w", encoding='utf-8')
file.write(extracted_text)

# Read website
extract_text_from_website()


