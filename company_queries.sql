-- check all tables in side sqlite
Select
    name
from
    sqlite_master
where
    type = 'table'
    --- fetch data from orders
Select
    *
from
    orders
select
    *
from
    order_items
select
    *
from
    orders
where
    order_date in ('2023-03-29', '2022-07-05', '2023-10-13')
select
    order_date as date,
    round(sum(amount), 2) AS daily_total_sales
from
    orders
group by
    order_date
order by
    order_date