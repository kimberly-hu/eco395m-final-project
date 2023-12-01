from database import engine
from sentence_transformers import SentenceTransformer
from sqlalchemy import text, bindparam

model = SentenceTransformer('all-MiniLM-L6-v2')


def match():

    user_query = input("Enter your query: ")
    user_embedding = model.encode([user_query])[0]
    user_embedding_list = user_embedding.tolist()
    
    q = """
        WITH cosine_table AS (
            SELECT *, :user_embedding <=> embedding::numeric[] AS cos_similarity
            FROM california
        )
        SELECT * FROM cosine_table
        WHERE cos_similarity > 0.7
        ORDER BY cos_similarity DESC
        LIMIT 20;
        """
    
    with engine.connect() as conn:
        stmt = text(q).bindparams(bindparam('user_embedding', value=user_embedding_list))
        result = conn.execute(stmt)

    matches = []

    if result.rowcount == 0:
        raise Exception("Did not find any results.")
    else:
        for r in result:
            matches.append(f"The name of the restaurant is {r['name']}.")

    return matches


if __name__ == "__main__":

    try:
        matches = match()
        for match in matches:
            print(match)
    except Exception as e:
        print(e)



          
