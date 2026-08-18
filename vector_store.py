# import NumPy because FAISS expects vectors in NumPy array format.
import numpy as np

import faiss

# create class to manage vector index
class VectorStore:

    #initilize vector store with number of dimesions
    def __init__(self, dimension):

        # create a FAISS index using Eucludean distance
        self.index = faiss.IndexFlatL2(dimension)

        # create list that will store original text chunks
        self.chunks = []

    # add embeddings and their corresponding text chunks to the index.

    def add(self, embeddings, chunks):

        #convert the embeddings into NumPy float32 format
        embeddings = np.array(embeddings, dtype="float32")

        # normalize every embedding so that inner product becomes cosine similarity
        faiss.normalize_L2(embeddings)

        # add all embeddings to the FAISS index
        self.index.add(embeddings)

        # store original chunks in same order as the vectors
        self.chunks.extend(chunks)


    # search for the most similar chunks to a query embedding.
    def search(self, query_embedding, top_k=3):

        #convert the query embedding into two dimensional NumPy float32 array
        query_embedding = np.array(
            [query_embedding],
            dtype="float32"
        )

        # normalize the query vector using the same method used for document vectors
        faiss.normalize_L2(query_embedding)

        # search the FAISS index for top_k nearest vextors
        score, indices = self.index.search(
            query_embedding,
            top_k
        )

        # store retrieved chunks
        results = []

        for i, idx in enumerate(indices[0]):

            # ignore invalid indices returned by FAISS.
            if idx == -1:
                continue

            # add corresponding original text chunk

            results.append({
                "text": self.chunks[idx],
                "score": float(score[0][i])
                })

        return results







""""
vectors = np.array([
    [1.0, 0.0],
    [0.9, 0.1],
    [0.0, 1.0]
], dtype="float32")

# get number of dimensions in each vector
dimension = vectors.shape[1]

# create FAISS index that uses a Euclidean distance
index = faiss.IndexFlatL2(dimension)

# add all vectors in FAISS index
index.add(vectors)

# create a query vector
query = np.array([
    [1.0, 0.0]
], dtype="float32")

# search for two vectors most similiar to our query
distances, indices = index.search(query, 2)


print("distaces : ", distances)
print("indices : ", indices)
"""