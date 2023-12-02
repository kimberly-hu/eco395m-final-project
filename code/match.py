from database import engine
from sentence_transformers import SentenceTransformer
from sqlalchemy import text, bindparam
model = SentenceTransformer('all-MiniLM-L6-v2')
conn=engine.connect()
# conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
# register_vector(conn)

def match():
    user_query = input("Enter your query: ")
    user_embedding = model.encode([user_query])[0]
    user_embedding_list=user_embedding.tolist()
    user_embedding_string= str(user_embedding_list)
    print(user_embedding_string)
    q = """
    WITH vector_matches AS (
    SELECT
        c.review_id,
        1 - (c.embedding_sample <=> :user_embedding) AS similarity
    FROM
        california c
        --where 1 - (c.embedding_sample <=> :user_embedding)>0.9
    	ORDER by similarity DESC
    	LIMIT 1
)

SELECT
    c.review_id,
    c.embedding,
    c."review_text" 
FROM
    california c
WHERE
    c.review_id IN (SELECT review_id FROM vector_matches)
        """
   
    with engine.connect() as conn:
        stmt = text(q) 
        result = conn.execute(
                stmt,
                user_embedding=user_embedding_string)
    matches = []


    if result.rowcount == 0:
        raise Exception("Did not find any results.")
    else:
        print("done")
        # for r in result:
        # # Convert the tuple to a dictionary
        #     row_as_dict = {column: value for column, value in zip(result.keys(), r)}
        # # Now you can access values using column names
        #     matches.append(f"The name of the restaurant is {row_as_dict['name']}.")
    return

if __name__ == "__main__":


    try:
        matches = match()
        for match in matches:
            print(match)
    except Exception as e:
        print(e)


          
