import numpy as np

def search_chunks(query_embedding, index, chunks, k=3):

    distances, indices = index.search(
        np.array([query_embedding]).astype("float32"),
        k
    )

    results = []

    for idx in indices[0]:

        if 0 <= idx < len(chunks):
            results.append(chunks[idx])

    return results