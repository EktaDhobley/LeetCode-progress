# # Write your MySQL query statement below
# SELECT distinct seat_id
# FROM Cinema
# WHERE free = 1 AND
# (seat_id - 1 in (SELECT seat_id FROM Cinema WHERE free = 1) OR
# seat_id + 1 in (SELECT seat_id FROM Cinema WHERE free = 1))
# ORDER BY seat_id

Select distinct seat_id
from Cinema
where free = 1 and
(seat_id - 1 in (select seat_id from Cinema Where free = 1) OR
 seat_id + 1 in (select seat_id from Cinema where free = 1))
 order by seat_id
 