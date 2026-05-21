-- Write your query below
WITH max_scores AS(
    SELECT student_id, MAX(score) AS score
    FROM exam_results
    GROUP BY student_id
),
best_exams AS (
    SELECT er.student_id, MIN(er.exam_id) AS exam_id, er.score
    FROM exam_results er
    JOIN max_scores ms
    ON er.student_id = ms.student_id
    AND er.score = ms.score
    GROUP BY er.student_id, er.score 
)
SELECT *
FROM best_exams
ORDER BY student_id;
