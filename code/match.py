from sentence_transformers import SentenceTransformer
from sqlalchemy import create_engine, text, bindparam
from database import engine

model = SentenceTransformer("all-MiniLM-L6-v2")
conn = engine.connect()
conn.execute(
    "CREATE EXTENSION IF NOT EXISTS vector"
)  # make sure there is pgvector extension in sql


def match(user_query):
    """
    First get embedding of input. And use pgvector to generate the similarity
    between input_embedding to the review_embedding we already had. Sort by
    similarity in descending order, choose first 100 reviews, and then get at
    most 20 unique restaurants given the 100 reviews we have. Finally, get a
    list of dictionaries with restaurant information in it.
    """
    user_embedding = model.encode([user_query])[0]
    user_embedding_list = (
        user_embedding.tolist()
    )  # transform the encoding outcome to list
    user_embedding_string = str(
        user_embedding_list
    )  # to use the pgvector we have to get the list into a string type

    q = """
select
	distinct t1.business_id,
	t1.name,
	t1.address,
	t1.city,
	t1.postal_code,
	t1.latitude,
	t1.longitude,
	t1.business_stars,
	t1.review_count,
	t1.is_open,
	t1.categories
from
	(
	select
		*,
		1 - (c.embedding <=> :user_embedding_string) as similarity
	from
		california c
	where
		1 - (c.embedding <=> :user_embedding_string) >0.7
	order by
		similarity desc
	limit 100) t1
limit 20
        """

    with engine.connect() as conn:
        stmt = text(q)
        result = conn.execute(stmt, user_embedding_string=user_embedding_string)

    if result.rowcount == 0:
        raise Exception("Did not find any results.")
    else:
        rows = result.fetchall()
        data_list = []
        for row in rows:
            data = {
                "business_id": row[0],
                "name": row[1],
                "address": row[2],
                "city": row[3],
                "state": row[4],
                "latitude": float(row[5]),
                "longitude": float(row[6]),
                "business_stars": float(row[7]),
                "review_count": int(row[8]),
                "is_open": int(row[9]),
                "categories": row[10].split(", "),
            }
            data_list.append(data)

    return data_list
