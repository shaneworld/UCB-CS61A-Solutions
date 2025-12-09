-- Pizza places that open before 1pm in alphabetical order
SELECT p.NAME FROM pizzas p WHERE p.open < 13 ORDER BY p.NAME DESC;


-- Pizza places and the duration of a study break that ends at 14 o'clock
SELECT p.name, MAX(14-p.open, 0) AS duration FROM pizzas p ORDER BY duration DESC;


-- Pizza places that are open for late-night-snack time and when they close
SELECT p.name || " closes at " || p.close AS status
FROM pizzas p
JOIN meals m ON m.meal = 'snack'
WHERE m.time <= p.close;


-- Two meals at the same place
SELECT m1.meal AS first, m2.meal AS second, pizzas.name
FROM meals m1, meals m2, pizzas
WHERE m1.time < m2.time
  AND m2.time - m1.time > 6
  AND pizzas.open <= m1.time
  AND pizzas.close >= m2.time;
