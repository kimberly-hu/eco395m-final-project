from database import engine
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def pop():
    """get one review that has not got its embedding, this function will return a list of one review_id and its text."""
    q = """
select review_text, review_id
from california
where embedding is null
limit 1
"""

    with engine.connect() as conn:
        result = conn.execute(q)
        row = result.fetchone()

    if row:
        review_list = []
        review_list.append(row["review_text"])
        review_list.append(row["review_id"])
    else:
        print("No rows found where embedding is null.")
    return review_list


def update_embedding(review_list):
    """use the review_list from def pop() as input.Then use sentence_transformer to encode the review_text and get its embedding, and finally write this embedding into database through GCP."""
    review_text = review_list[0]
    review_id = review_list[1]
    sentence = review_text
    embedding_raw = model.encode(sentence)
    embedding_list = (
        embedding_raw.tolist()
    )  # transform the encoding output to the list we can use.
    embedding = str(
        embedding_list
    )  # to use pgvector,we have to make sure the embedding is string type(though it is actually a list).
    # print(embedding)
    q = """
UPDATE california
    SET embedding = %(embedding)s
    WHERE review_id = %(review_id)s
"""
    with engine.connect() as conn:
        conn.execute(q, {"embedding": embedding, "review_id": review_id})
    return


def executing():
    """loop def pop() and def update_embedding(review_list), untill there is no review without embedding."""
    while True:
        popped_review_review_id = pop()
        if popped_review_review_id:
            update_embedding(popped_review_review_id)
        else:
            print("no empty rows of embedding")
            break
    return


if __name__ == "__main__":
    executing()
