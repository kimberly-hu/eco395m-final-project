-- Create table for reviews
-- To handle a large data set, the data set was divided into 7 segments.
CREATE TABLE review_1 (
    review_id varchar(22) CONSTRAINT review_id_key PRIMARY KEY,
    user_id varchar(22),
    business_id varchar(22),
    stars numeric,
    useful numeric,
    funny numeric,
    cool numeric,
    review_text varchar,
    review_date date
);

CREATE TABLE review_2 (
    review_id varchar(22) CONSTRAINT review2_id_key PRIMARY KEY,
    user_id varchar(22),
    business_id varchar(22),
    stars numeric,
    useful numeric,
    funny numeric,
    cool numeric,
    review_text varchar,
    review_date date
);

CREATE TABLE review_3 (
    review_id varchar(22) CONSTRAINT review3_id_key PRIMARY KEY,
    user_id varchar(22),
    business_id varchar(22),
    stars numeric,
    useful numeric,
    funny numeric,
    cool numeric,
    review_text varchar,
    review_date date
);

CREATE TABLE review_4 (
    review_id varchar(22) CONSTRAINT review4_id_key PRIMARY KEY,
    user_id varchar(22),
    business_id varchar(22),
    stars numeric,
    useful numeric,
    funny numeric,
    cool numeric,
    review_text varchar,
    review_date date
);

CREATE TABLE review_5 (
    review_id varchar(22) CONSTRAINT review5_id_key PRIMARY KEY,
    user_id varchar(22),
    business_id varchar(22),
    stars numeric,
    useful numeric,
    funny numeric,
    cool numeric,
    review_text varchar,
    review_date date
);

CREATE TABLE review_6 (
    review_id varchar(22) CONSTRAINT review6_id_key PRIMARY KEY,
    user_id varchar(22),
    business_id varchar(22),
    stars numeric,
    useful numeric,
    funny numeric,
    cool numeric,
    review_text varchar,
    review_date date
);

CREATE TABLE review_7 (
    review_id varchar(22) CONSTRAINT review7_id_key PRIMARY KEY,
    user_id varchar(22),
    business_id varchar(22),
    stars numeric,
    useful numeric,
    funny numeric,
    cool numeric,
    review_text varchar,
    review_date date
);

--Create business table
CREATE TABLE business (
    business_id varchar(22) CONSTRAINT business_id_key PRIMARY KEY,
    name varchar,
    address varchar,
    city varchar,
    state varchar,
    postal_code varchar,
    latitude numeric,
    longitude numeric,
    business_stars numeric,
    review_count numeric,
    is_open integer,
    categories varchar
);