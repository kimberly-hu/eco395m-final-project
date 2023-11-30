# Generate the vector embeddings for each chunk of text.
# This code snippet may run for a few minutes.

from langchain.embeddings import VertexAIEmbeddings
from google.cloud import aiplatform
import time

aiplatform.init(project=f"{project_id}", location=f"{region}")
embeddings_service = VertexAIEmbeddings()


# Helper function to retry failed API requests with exponential backoff.
def retry_with_backoff(func, *args, retry_delay=5, backoff_factor=2, **kwargs):
    max_attempts = 10
    retries = 0
    for i in range(max_attempts):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"error: {e}")
            retries += 1
            wait = retry_delay * (backoff_factor**retries)
            print(f"Retry after waiting for {wait} seconds...")
            time.sleep(wait)


batch_size = 5
for i in range(0, len(chunked), batch_size):
    request = [x["content"] for x in chunked[i : i + batch_size]]
    response = retry_with_backoff(embeddings_service.embed_documents, request)
    # Store the retrieved vector embeddings for each chunk back.
    for x, e in zip(chunked[i : i + batch_size], response):
        x["embedding"] = e

# Store the generated embeddings in a pandas dataframe.
product_embeddings = pd.DataFrame(chunked)
product_embeddings.head()