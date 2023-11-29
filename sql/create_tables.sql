-- create the reviews table

CREATE TABLE review (
    review_id varchar(22) CONSTRAINT review_id_key PRIMARY KEY,
    user_id varchar(22) NOT NULL,
    business_id varchar(22) NOT NULL,
    review_stars integer NOT NULL,
    review_date date NOT NULL,
    review_text varchar NOT NULL,
    useful integer NOT NULL,
    funny integer NOT NULL,
    cool integer NOT NULL
);