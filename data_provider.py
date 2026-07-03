import fitz
import requests
from bs4 import BeautifulSoup


def extract_text_from_pdf(pdf_path):
    try:
        docs = fitz.open(pdf_path)
        pdf_text = ""
        for page_num in range(docs.page_count):
            page = docs.load_page(page_num)
            pdf_text += page.get_text()
        docs.close()
        return pdf_text
    except Exception as e:
        return f"Error extracting text: {e}"
    
def extract_text_from_website():
    target_url = "https://www.landonhotel.com"
    response = requests.get(target_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        text = ""
        for paragraph in soup.find_all('p'):
            text += paragraph.get_text() + "\n"

        with open("website_text.txt", "w", encoding = 'utf-8') as file:
            file.write(text)

        print("Text extracted and saved successfully")
    else:
        print(f"Failed to retrieve the website. Status code: {response.status_code}")


