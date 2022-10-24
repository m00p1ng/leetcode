-- Write your MySQL query statement below
SELECT Users.name name, COALESCE(SUM(Rides.distance),0) travelled_distance
FROM Users
LEFT JOIN Rides ON Rides.user_id = Users.id
GROUP BY Users.id
ORDER BY travelled_distance DESC, name ASC;
