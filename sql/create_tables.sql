-- Create the reviews tables

CREATE TABLE review_1 (
    review_id varchar(22) CONSTRAINT review_id_key PRIMARY KEY,
    user_id varchar(22) NOT NULL,
    business_id varchar(22) NOT NULL,
    stars numeric NOT NULL,
    useful numeric NOT NULL,
    funny numeric NOT NULL,
    cool numeric NOT NULL,
    review_text varchar  NOT NULL,
    review_date date  NOT NULL
);

CREATE TABLE review_2 (
    review_id varchar(22) CONSTRAINT review2_id_key PRIMARY KEY,
    user_id varchar(22) NOT NULL,
    business_id varchar(22) NOT NULL,
    stars numeric NOT NULL,
    useful numeric NOT NULL,
    funny numeric NOT NULL,
    cool numeric NOT NULL,
    review_text varchar  NOT NULL,
    review_date date  NOT NULL
);

CREATE TABLE review_3 (
    review_id varchar(22) CONSTRAINT review3_id_key PRIMARY KEY,
    user_id varchar(22) NOT NULL,
    business_id varchar(22) NOT NULL,
    stars numeric NOT NULL,
    useful numeric NOT NULL,
    funny numeric NOT NULL,
    cool numeric NOT NULL,
    review_text varchar  NOT NULL,
    review_date date  NOT NULL
);

CREATE TABLE review_4 (
    review_id varchar(22) CONSTRAINT review4_id_key PRIMARY KEY,
    user_id varchar(22) NOT NULL,
    business_id varchar(22) NOT NULL,
    stars numeric NOT NULL,
    useful numeric NOT NULL,
    funny numeric NOT NULL,
    cool numeric NOT NULL,
    review_text varchar  NOT NULL,
    review_date date  NOT NULL
);

CREATE TABLE review_5 (
    review_id varchar(22) CONSTRAINT review5_id_key PRIMARY KEY,
    user_id varchar(22) NOT NULL,
    business_id varchar(22) NOT NULL,
    stars numeric NOT NULL,
    useful numeric NOT NULL,
    funny numeric NOT NULL,
    cool numeric NOT NULL,
    review_text varchar  NOT NULL,
    review_date date  NOT NULL
);

CREATE TABLE review_6 (
    review_id varchar(22) CONSTRAINT review6_id_key PRIMARY KEY,
    user_id varchar(22) NOT NULL,
    business_id varchar(22) NOT NULL,
    stars numeric NOT NULL,
    useful numeric NOT NULL,
    funny numeric NOT NULL,
    cool numeric NOT NULL,
    review_text varchar  NOT NULL,
    review_date date  NOT NULL
);

CREATE TABLE review_7 (
    review_id varchar(22) CONSTRAINT review7_id_key PRIMARY KEY,
    user_id varchar(22) NOT NULL,
    business_id varchar(22) NOT NULL,
    stars numeric NOT NULL,
    useful numeric NOT NULL,
    funny numeric NOT NULL,
    cool numeric NOT NULL,
    review_text varchar  NOT NULL,
    review_date date  NOT NULL
);

-- Create the business table

CREATE TABLE business (
    business_id varchar(22) CONSTRAINT business_id_key PRIMARY KEY,
    name varchar NOT NULL,
    address varchar,
    city varchar NOT NULL,
    state varchar NOT NULL,
    postal_code varchar,
    latitute numeric,
    longitude numeric,
    business_stars numeric,
    review_count numeric,
    is_open integer NOT NULL,
    categories varchar
);