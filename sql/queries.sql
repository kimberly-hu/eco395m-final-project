CREATE TABLE california AS
SELECT b.*, r.review_id, r.review_text
FROM business b
LEFT JOIN (
    SELECT *
    FROM (
        SELECT business_id, review_id, review_text FROM review_1
        UNION ALL
        SELECT business_id, review_id, review_text FROM review_2
        UNION ALL
        SELECT business_id, review_id, review_text FROM review_3
        UNION ALL
        SELECT business_id, review_id, review_text FROM review_4
        UNION ALL
        SELECT business_id, review_id, review_text FROM review_5
        UNION ALL
        SELECT business_id, review_id, review_text FROM review_6
        UNION ALL
        SELECT business_id, review_id, review_text FROM review_7
    ) AS combined_reviews
) r ON b.business_id = r.business_id
WHERE b.state = 'CA'
    AND b.categories LIKE '%Restaurants%'
    AND b.is_open = 1
    AND b.name IS NOT NULL
    AND b.city IS NOT NULL
    AND b.state IS NOT NULL
    AND b.latitude IS NOT NULL
    AND b.longitude IS NOT NULL
ORDER BY b.business_id;

UPDATE california SET address = 'N/A' WHERE address IS NULL;
UPDATE california SET postal_code = 'N/A' WHERE postal_code IS NULL;
UPDATE california SET business_stars = 'N/A' WHERE business_stars IS NULL;
UPDATE california SET review_count = 0 WHERE review_count IS NULL;

ALTER TABLE california ADD embedding numeric[];

ALTER TABLE public.california ALTER COLUMN embedding TYPE public.vector USING embedding::public.vector::public.vector;

