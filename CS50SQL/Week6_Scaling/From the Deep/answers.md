# From the Deep

## Random Partitioning

reasons to adopt : evenly distributed across all boats have less complexity so we have data imbalance.
reasons to not adopt : to quere the data we need  to join all tables, we dont have control to control data.

## Partitioning by Hour

reasons to adopt : useful for consistent data collection patterns, make quieres more simple.
reasons to not adopt : may lead to uneven distribution if data collection varies across hours.

## Partitioning by Hash Value

reasons to adopt : helps spread data evenly across boats and makes finding specific data easier.
reasons to not adopt : adds complexity if not done right, some boats might get more data, causing issues.

