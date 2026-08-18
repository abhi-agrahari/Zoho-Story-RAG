# define a function that divides a large piece of text into smaller chunks

def create_chunks(text, chunk_size = 1000, overlap = 200):

    # empty list to store generated chunks
    chunks = []

    # idx for char position
    start = 0

    #continue creating chunks until we reach end of file
    while start < len(text):

        # ending position of current chunk
        end = start + chunk_size

        # extract chunk between start and end
        chunk = text[start : end]

        # appending in chunks
        chunks.append(chunk)

        # moving forward
        start += chunk_size - overlap

    # return the complete list of chunks
    return chunks