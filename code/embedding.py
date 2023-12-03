from database import engine
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')


def pop():
    q="""
select review_text, review_id
from california
where embedding is null
limit 1
"""
    
    with engine.connect() as conn:
        result=conn.execute(q)
        row = result.fetchone()

    if row:
        review_list=[]
        review_list.append(row["review_text"])
        review_list.append(row["review_id"])
        # print("Review Text:", row["review_text"])
        # print("Review ID:", row["review_id"])
    else:
        print("No rows found where embedding is null.")
    return review_list


def update_embedding(review_list):
    review_text=review_list[0]
    review_id=review_list[1]
    sentence=review_text
    embedding_raw= model.encode(sentence)
    embedding_list=embedding_raw.tolist()
    embedding=str(embedding_list)
    #print(embedding)
    q="""
UPDATE california
    SET embedding = %(embedding)s
    WHERE review_id = %(review_id)s
"""
    with engine.connect() as conn:
        conn.execute(q, {"embedding": embedding, "review_id": review_id})
    # print(embedding.tolist())
    # print(review_text)
    return

def executing():
    while True:
        popped_review_review_id= pop()
        if popped_review_review_id:
            update_embedding(popped_review_review_id)
        else: 
            print("no empty rows of embedding")
            break
    return

if __name__ == "__main__":
    executing() 
    # popped=pop()
    # update_embedding(popped)
