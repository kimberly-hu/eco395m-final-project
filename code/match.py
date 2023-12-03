from sentence_transformers import SentenceTransformer
from sqlalchemy import create_engine, text, bindparam

DATABASE_USERNAME="postgres"
DATABASE_PASSWORD="321psswrd123"
DATABASE_HOST="35.224.144.136"
DATABASE_PORT="5432"
DATABASE_DATABASE="yelp"

SQLALCHEMY_DATABASE_URL = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_DATABASE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

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
		test_table c
	where
		1 - (c.embedding <=> :user_embedding_string) >0.3
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
    else
        print("done")
        for r in result:
        # Convert the tuple to a dictionary
            row_as_dict = {column: value for column, value in zip(result.keys(), r)}
        # Now you can access values using column names
            matches.append(f"The name of the restaurant is {row_as_dict['name']}."
    return result

if __name__ == "__main__":


    try:
        matches = match()
        for record in matches: 
            print("\n", record) 
    except Exception as e:
        print(e)

