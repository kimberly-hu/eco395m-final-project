<h1 align="center" id="heading"> <span style="color:red"> Santa Barbara MealMapper: Vector-Based Dining Finder </span> </h1>
<h3 align="center" id="heading">  December 7, 2023 <br> 
<em> Python, Big Data, and Databases (ECO395m)  </em> <br> <h3>
<h3 align="center" id="heading"> Kimberly Hu, Yalun Wang, Yundi Xiao </h3>

## I. Introduction 
Are you tired of browsing Yelp for hours to find a good place to eat or browsing through reviews to figure out if someone mentioned whether this place has good Wifi? We created a project to save you from the restless search process. Our project consists of two parts: a vector database based on a subsample of Yelp’s open data and vector embeddings of reviews, and a vector similarity search implanted in the interactive dashboard. Our goal is to explore new ways of restaurant browsing. Our project investigates how to convert users' random thoughts or requests like "sashimi with good saki" to restaurant recommendations. 
 <p align="center"> 
 	<img src="https://github.com/kimberly-hu/eco395m-final-project/blob/main/artifacts/dallelogo.png"width="250" />
 </p>

## II. Methodology
We use Sentence Transformer's pre-trained model to create vector embeddings of restaurant reviews and store them in a PostgreSQL database on GCP. We use the PG Vector PostgreSQL extension to calculate cosine similarities between user queries and review embeddings and return restaurant recommendations based on the similarities. Streamlit, Plotly, and Mapbox are used to make the query intake process interactive. 

1. _Vector Embedding_: We used the Python Framework [Sentence Transformer](https://www.sbert.net/index.html) and its pre-trained model [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) to map the restaurants’ reviews to a 384-dimensional dense vector space. Specifically, we searched for the restaurant reviews without a vector embedding in the Postgresql database `Yelp`, and passed the review to `all-MiniLM-L6-v2` to encode the review and obtain its vector embedding. Then we transform and store the vector embedding to a string type of list to be used later. We encoded 167,990 reviews in total. The vector embeddings for the restaurant reviews, restaurant information, and text reviews are stored in the Postgresql database on GCP, and together they make up our vector database. 

2. _PG Vector_: The Postgresql extension, [PG vector](https://github.com/pgvector/pgvector)  is used to generate the similarity between the user’s query to the reviews in our Postgresql database. Specifically, we take the user’s query from our interactive dashboard and obtain its vector embedding using `sentence transformer`. PG vector is used in the next step to calculate the cosine similarities between the query embedding and review embeddings. Then we sort the results by similarity in descending order, choose the first 100 reviews with the highest similarity, and get up to 20 unique restaurants based on the 100 reviews. 

## III. Database 
1. Data Source
   
   Our project is built on the [Yelp open dataset](https://www.yelp.com/dataset) for academic research. The dataset consists of a subset of actual Yelp businesses, reviews, and user data. Specifically, we are interested in the subset of reviews for restaurants in the Santa Barbara area in California. We make use of two JSONs in the dataset: “business” and “review”. The “business” JSON contains business information, including business name, address, location, rating, number of reviews, categories, etc. The “review” JSON contains information on reviews, from which we extracted the review text.
   
2. Creating the Database
   
   We utilized the Google Cloud Platform (GCP) and DBeaver to form the database used in this project. The following steps would create the database:

Step 1: Download data from the [Yelp website](https://www.yelp.com/dataset) and decompress the datasets. The two JSON files we used are `yelp_academic_dataset_business.json` and `yelp_academic_dataset_review.json`. Save these two files in the “data” folder of the project repo.

Step 2: Run `code/json_to_csv_business.py` and `code/json_to_csv_review.py` at the top of the repo to convert the JSON files into CSV files. This would generate `business.csv` in the `data` folder and seven CSV files for reviews in the `review` sub-folder. 

Step 3: Create a PostgreSQL database instance on GCP and create a database named `yelp` in the instance. You can also use an existing database instance. Create an environment file `.env` at the top of the repo using the format provided in `demo.env`, and update information about the database.

Step 4: Connect to the database with DBeaver. Copy the SQL script in `sql/create_table.sql` and execute the script in DBeaver. This would create tables to store our data.

Step 5: On GCP, create a bucket for this project and upload the CSV files generated in Step 2. Go to the database instance for this project and import the files to their corresponding tables. The table names can be found in DBeaver.  

Step 6: Return to DBeaver and refresh the database. Copy the SQL script in `sql/queries.sql` and execute it. This step would generate a new table named “California” which joins information about restaurants in Santa Barbara with their corresponding reviews. Closed restaurants are dropped. An empty column is created to store the embedding vectors generated by our models.

## IV. Running the Analysis 
 Before running the analysis, install the necessary packages with `pip install -r requirements.txt`.To rerun the analysis, run the following codes stored in the code folder: `embedding.py`, `match.py`, and `widget.py`. 

1. Get vector embedding with `embedding.py`:
   Run `code/embedding.py` to get all the embeddings for reviews in our database, and update the embedding column. This generating process might take some time. In our project, it took approximately 18 hours to generate vector embeddings for all 167,990 reviews.

2. Get the recommended restaurants with `match.py`:
   Run `code/match.py`. It receives the user's query and uses `sentence tranformer: all-MiniLM-L6-v2` to get its vector embedding. Then it uses `PGvector` to generate the similarity between this input embedding and review embeddings saved in the database. It returns a list of up to 20 unique restaurants with the highest similarity and their information in a dictionary form.

3. Create an interactive dashboard with `widget.py`:
   Our dashboard utilizes Plotly and Mapbox to create the interactive map. Before running Streamlit, go to [Mapbox](https://www.mapbox.com/) and get a free token, then update the environment file in your repo. The public token is sufficient for this project. Run `streamlit run code/widget.py` to generate the interactive dashboard. Widget.py uses the Streamlit widget feature to take the user's query. Then it passes the user’s query to the match function in match.py and returns a list of matching restaurants with their names, categories, and addresses. Two URLs will be generated, a local URL and a network URL. Open either URL to obtain the finalized interactive dashboard. Matched restaurants’ locations will be displayed on the interactive map. 

## V. Interactive Dashboard — Santa Barbara MealMapper
 Our interactive dashboard, Santa Barbara MealMapper is straightforward to use. 

Step 1: Enter your thoughts about where to eat in the input. It doesn’t even have to be where to eat. For example, if you need a place to do your homework, putting “ cafe with good WiFi so that I can finish my homework” also works! In the demo, we enter “I want authentic Chinese food but not too spicy, and close to campus” as our query.
 <p align="center"> 
 	<img src="https://github.com/kimberly-hu/eco395m-final-project/blob/main/artifacts/final1.png"width=500" />
 </p>

Step 2: After submitting the query, the matched restaurants are listed, and their locations are displayed on the map.
 <p align="center"> 
 	<img src="https://github.com/kimberly-hu/eco395m-final-project/blob/main/artifacts/final2.png"width=600" />
 </p>
  <p align="center"> 
 	<img src="https://github.com/kimberly-hu/eco395m-final-project/blob/main/artifacts/final3.png"width=600" />
 </p>
 
 
## VI. Limitation and Further Extension
 We recognized a few limitations with our dataset, model choice, and usage. 

* The model we chose, `all-MiniLM-L6-v2`generates vector embeddings with 384 dimensions due to our dataset (160,000+ rows). To save the time of obtaining vector embedding, we sacrificed model dimensions with a simpler sentence transformer model. Hence, this chosen model can be relatively small and leads to less accurate results. 

* Moreover, the dataset has data collection bias because we have more restaurant information from Santa Barbara compared to other cities in California. So it also resulted in our decision to use only the subsample of Santa Barbara. 

* As for the usage of the model, we noticed the more specific the query is, the better matching results our project will generate. For example, inputting "cake" as the query generates no results. Therefore, it performs better with more complex sentences or phrases, which suggests a limitation on the usage of our project.  

* We consider using another sentence transformer model to generate vector embeddings with more dimensions for both the reviews and the user's query. By using so, we can get more accurate results. The next steps will be adding more features to the matching process and interactive dashboard, such as allowing for selecting specific locations, price ranges for the restaurants, and categories of the restaurants. 

## VII. Conclusion 
Overall, our project represents a promising step towards a more efficient and personalized restaurant search. It jumped out of the existing restaurant search that only allows users to search for limited features of the diner. The MealMapper puts no boundaries on the user queries by expanding the database with vector embedding and cosine similarities search empowered by PG vector. However, limitations such as dataset bias should be considered in further extensions. We are excited about the future possibilities and refinements that can make the MealMapper provide more tailored dining recommendations to users. 
