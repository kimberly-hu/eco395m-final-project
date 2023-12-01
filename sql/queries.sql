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
WHERE b.state = 'CA' AND b.categories LIKE '%Restaurants%'
ORDER BY b.business_id;

ALTER TABLE california ADD embedding real[];

