# Split long text reviews into smaller chunks that can fit into the API request size limit, as expected by the LLM providers.

from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    separators=[".", "\n"],
    chunk_size=500,
    chunk_overlap=0,
    length_function=len,
)
chunked = []
for index, row in df.iterrows():
    product_id = row["product_id"]
    desc = row["description"]
    splits = text_splitter.create_documents([desc])
    for s in splits:
        r = {"product_id": product_id, "content": s.page_content}
        chunked.append(r)