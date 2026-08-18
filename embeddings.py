import torch

# import SenteceTransformers class used to load an embedding model
from sentence_transformers import SentenceTransformer
# import cosine similarity class from pyTorch
from torch.nn.functional import cosine_similarity

# load pre-triained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# define a function that converts text into an embedding vector
def create_emdding(text):

    # generating an embedding vector
    embedding = model.encode(text)

    return embedding


""""

s1 = "python is a scripting language"

s2 = "python is used in AL/Ml"

s3 = "I like pizza"

e1 = create_emdding(s1)

e2 = create_emdding(s2)

e3 = create_emdding(s3)

v1 = torch.tensor(e1).unsqueeze(0)

v2 = torch.tensor(e2).unsqueeze(0)

v3 = torch.tensor(e3).unsqueeze(0)

cs12 = cosine_similarity(v1, v2)

cs13 = cosine_similarity(v1, v3)

print(cs12.item())
print(cs13.item())
"""