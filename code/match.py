from sentence_transformers import SentenceTransformer
from sqlalchemy import create_engine, text, bindparam
from database import engine 


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
select
	distinct t1.business_id,
	t1.name,
	t1.address,
	t1.city,
	t1.postal_code,
	t1.latitute,
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
		test_table c
	--where
		--1 - (c.embedding <=> :user_embedding_string) >0.3
	order by
		similarity desc
	limit 100) t1
limit 20
        """
   
    with engine.connect() as conn:
        stmt = text(q)
        result = conn.execute(stmt,user_embedding_string=user_embedding_string)

    if result.rowcount == 0:
        raise Exception("Did not find any results.")
    else:
        rows = result.fetchall()
        data_list = []
        for row in rows:
            data = {
                'business_id': row[0],
                'name': row[1],
                'address': row[2],
                'city': row[3],
                'state': row[4],
                'latitude': float(row[5]),
                'longitude': float(row[6]),
                'business_stars': float(row[7]),
                'review_count': int(row[8]),
                'is_open': int(row[9]),
                'categories': row[10].split(', ')
            }
        data_list.append(data)

    #print(data_list)
    return data_list

if __name__ == "__main__":
    matches = match()



