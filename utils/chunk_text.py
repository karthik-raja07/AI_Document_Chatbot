def chunk_text(text, chunk_size=500, overlap=100):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        if end < len(text):

            while end < len(text) and text[end] != " ":
                end += 1

        chunks.append(text[start:end])

        start += chunk_size - overlap

    return chunks