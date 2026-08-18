# import PdfReader class from pypdf library
from pypdf import PdfReader
from chunker import create_chunks

# store path of pdf file which we want to read
pdf_path = "data/zoho_story.pdf"

# create PdfReader object that opens and read the pdf file
reader = PdfReader(pdf_path)

""""

# get total number of pages present in the pdf
number_of_pages = len(reader.pages)

print("Number of pages ", number_of_pages)

# get the first page of pdf
first_page = reader.pages[0]

# extract the text from the first page
first_page_text = first_page.extract_text()

print(first_page_text)

"""

full_text = ""

for page in reader.pages:

    page_text = page.extract_text()

    full_text += page_text + "\n"

# print(full_text)


# divide complete pdf text into smaller chunks
chunks = create_chunks(
    full_text,
    chunk_size = 1000,
    overlap = 200
)

print("Number of chunks : ", len(chunks))

print("First Chunk : ")
print(chunks[0])