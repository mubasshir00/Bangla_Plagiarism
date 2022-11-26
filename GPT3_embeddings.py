import pandas as pd
import openai , numpy as np
from openai.embeddings_utils import get_embedding, cosine_similarity

api_key = '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'
openai.api_key = api_key

resp = openai.Embedding.create(
    input=["নেসা ক্যারি একজন ব্রিটিশ জীববিজ্ঞানী।",
           "স্পেনের জন্য ঐতিহাসিক এক জয়"],
    engine="text-similarity-davinci-001"
)

type(resp['data'])
len(resp['data'])
type(resp['data'][0])
resp['data'][0].keys()
resp['data'][0]['embedding']
embedding_a = resp['data'][0]['embedding']
embedding_b = resp['data'][1]['embedding']


print(np.dot(embedding_a, embedding_b))


