# Hadoop Handson

### u.data
user_id | movie_id | rating | rating_time

### Section 2. Using Hadoop's core: HDFS and MapReduce

#### 13. Breaking down movie ratings by rating score
1. mapper_get_ratings
    function => {rating: 1}
2. reducer_count_ratings (key = rating, value = 1)
    function => {key, sum(value)}
3. MRStep (mapper = 1, reducer = 2)

#### 17.1 Ranking movies by their popularity
popularity defined as number of people rating one movie, the more people the more popular the movie is. 
1. mapper_get_ratings
    function => {movie_id: 1}
2. reducer_count_ratings (key = movie_id, value = 1)
    function => {key, count(value)}
3. MRStep (mapper = 1, reducer = 2)

#### 17.1 Ranking movies by their numbers of ratings, order by numbers of ratings
1. mapper {movie_id: }
2. reducer
3. mapper2
4. reducer2
5. MRStep (mapper = 3, reducer = 4)

### PIG
#### 22. Pig Latin

- LOAD STORE DUMP
- FILTER DISTINCT FOREACH/GENERATE MAPREDUCE STREAM SAMPLE
- JOIN COGROUP GROUP CROSS CUBE
- ORDER RANK LIMIT
- UNION SPLIT
- AVG CONCAT COUNT MAX MIN SIZE SUM
- PigStorage TextLoader JsonLoader AvroStorage ParquetLoader OrcStorage HbaseStorage

Diagnostics
- DESCRIBE
- EXPLAIN
- ILLUSTRATE

UDF'S

- REGISTER (Jar file and import)
- DEFINE (define pig functions)
- IMPORT (import macros)

#### 24. Most popular bad movies
- Find movies with an average rating less than 2.0
- Sort them by total number of ratings


### SPARK
Transforms
- map
- flatmap
- filter
- distinct
- sample
- union, intersection, subtract, cartesian

Actions
- collect
- count
- countByValue
- take
- top
- reduce

#### 28, Find the worst movie (movie with the lowest average rating).
 