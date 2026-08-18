# import PdfReader class from pypdf library
from pypdf import PdfReader
from chunker import create_chunks
from sentence_transformers import SentenceTransformer
from vector_store import VectorStore
from llm import generate_answer

# store path of pdf file which we want to read
pdf_path = "data/zoho_story.pdf"

# create PdfReader object that opens and read the pdf file
reader = PdfReader(pdf_path)

full_text = ""

for page in reader.pages:

    page_text = page.extract_text()

    full_text += page_text + "\n"


# divide complete pdf text into smaller chunks
chunks = create_chunks(
    full_text,
    chunk_size = 1000,
    overlap = 200
)

print("Number of chunks : ", len(chunks))

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(chunks)

print("Number of embeddings : ", len(embeddings))

print("Embedding dimensions : ", len(embeddings[0]))

vector_store = VectorStore(
    dimension= len(embeddings[0])
)

vector_store.add(
    embeddings,
    chunks
)

question = input("Enter you Question : ")

question_embedding = model.encode(question)

results = vector_store.search(
    question_embedding,
    top_k = 3
)

retrieved_chunks = []

for result in results:

    retrieved_chunks.append(result["text"])


# combine all retrieed chunks into context string
context = "\n\n".join(retrieved_chunks)

# generate answer
answer = generate_answer(
    question,
    context
)

print("\n===== ANSWER =====")

print(answer)