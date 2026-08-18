# import PdfReader class from pypdf library
from pypdf import PdfReader

# store path of pdf file which we want to read
pdf_path = "data/zoho_story.pdf"

# create PdfReader object that opens and read the pdf file
reader = PdfReader(pdf_path)

# get total number of pages present in the pdf
number_of_pages = len(reader.pages)

print("Number of pages ", number_of_pages)

# get the first page of pdf
first_page = reader.pages[0]

# extract the text from the first page
first_page_text = first_page.extract_text()

print(first_page_text)