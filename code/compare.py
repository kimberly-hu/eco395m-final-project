from database import engine
from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('all-MiniLM-L6-v2')

user_query = input("Enter your query: ")
user_embedding = model.encode([user_query])

def main():
    similarity_threshold = 0.7
    num_matches = 10
    q = """
        WITH vector_matches AS (
            SELECT review_id, 1 - (embedding <=> %s) AS similarity
            FROM embedding
            WHERE 1 - (embedding <=> %s) > %s
            ORDER BY similarity DESC
            LIMIT %s
        )
        SELECT name FROM california
        WHERE review_id IN (SELECT review_id FROM vector_matches)
        """

    with engine.connect() as conn:
        result = conn.execute(q, (user_embedding.tobytes(), user_embedding.tobytes(), similarity_threshold, num_matches))

    matches = []

    if result.rowcount == 0:
        raise Exception("Did not find any results. Adjust the query parameters.")

    for r in result:
        matches.append(f"The name of the restaurant is {r['name']}.")

    return matches

try:
    matches = main()
    for match in matches:
        print(match)
except Exception as e:
    print(e)

          
