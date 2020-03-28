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

### Spark 2.0 and DataFrames
### Spark MLlib

#### Prediction of movie

#### HIVE
CREATE VIEW IF NOT EXISTS topMovieIDs AS
SELECT movieID, count(movieID) as ratingCount, avg(rating) as avgRating
FROM ratings
GROUP BY movieID
HAVING ratingCount > 10
ORDER BY ratingCount DESC;

SELECT n.title, t.avgRating, t.ratingCount 
FROM topMovieIDs t JOIN name n ON n.movieID=t.movieID
ORDER BY t.avgRating;

DROP VIEW topMovieIDs;

#### HBASE
1. connect to guest port 8000 Hbase REST service
2. Start Hbase using ambari
3. Start REST server on top of Hbase sitting on top of HDFS
 `/usr/hdp/current/hbase-master/bin/hbase-daemon.sh start rest -p 8000 
--infoport 8001`
4. stop hbase 
`/usr/hdp/current/hbase-master/bin/hbase-daemon.sh stop rest`

#### Pig with Hbase
1. Must create Hbase table ahead of time (set up through the shell)
2. each relation has a unique key as the first column
3. USING clause allows you to STORE clause into an HBase table
4. Hbase is transactional on rows
5. ImportTsv tool from HDFS to Hbase

import user's table from HDFS to Hbase

- get into the interactive shell of hbase`hbase shell`, using `list` to list existing tables of this instance
- `create 'users', 'userinfo'`  to create a table 'users' with column family 'userinfo'
- `exit` to get out
-  Run the  pig program `pig 'hbase.pig'`
- `scan 'users'` to take a look what's in it
- `disable 'users'` first to disable a table before drop it `drop 'users'`

#### Cassandra (Greek can tell the future)
A distributed database with no single point of failure. 
- no master node at all, unlike HBase
- Data model is similar to BigTable/HBase
- non-relational, has a limited CQL query language
- CAP Theorem (consistency, availability, partition-tolerance: easily split up and distributed)
Cassandra favors availability over consistency: eventual consistent; **tunable consistency**

- Replicate Cassandra to another ring that is used for analytics

**CQL**
1. NO JOINS (de-normalized data)
2. All queries must be on some primary key
3. CQLSH can be used on the command line to create tables etc
4. All tables must be in a keyspace

**Cassandar + Spark**
- DataStax(free) offers a Spark-Cassandra connector
- Allows read and write Cassandra tables as DataFrames


#### MongoDB
- Document-based data model: any json data could be insert into MongoDB
- No real schema is enforced (no single key, lots of flexibility)
- Databases -> Collections -> Documents
- Single-master
- Maintains backup copies of your database instance
- A majority of the servers in your set must agree on the primary (must be odd numbers of servers)
To solve this, could set up an 'arbiter' node, but only one
- Replicas only address durability, not your ability to scale
- Sharding: multiple replica sets for "big data"

#### 54. Database choice consideration
1. Integration consideration. (e.g. connecting to existing parts)
2. Scaling requirements (How much data? future growth? transaction rate?)
3. Support consideration (in-house expert? security issue? paid professional support?)
4. Budget considerations (mostly open source, cost of servers and support)
5. CAP considerations (2 out of 3, which one can you give up? availability/consistency/partition-tolerance)


### Section 7. Query Data interactively
#### Drill
#### Phoenix
#### Presto


### Cluster Management

#### YARN (Yet Another Resource Negociator)

#### Tez

#### Mesos

#### Oozie (Burmese for elephant keeper)
A system for running & scheduling Hadoop tasks.
A multi-stage Hadoop job to chain together MapReduce, Hive, Pig, sqoop etc tasks
through an XML file 

###### Workflow (a Directed Acyclic Gaph of actions)
-  start & end node
-  fork node to kick off multiple tasks

*Steps to set up a workflow in Oozie*
1. Make sure each action works on its own
2. Make a directory in HDFS
3. Create **workflow.xml** and place it in your HDFS folder
4. Create **job.properties** defining variable used in workflow.xml
5. Add connector and restart Oozie
6. Run a workflow
`oozie job --oozie http://localhost:11000/oozie -config /home/admin/job.properties -run`
7. Monitor progress at `http://127.0.0.1:11000/oozie`

Oozie Coordinators
1. schedules workflow execution
2. launches workflows based on a given start time and frequency
3. wait for required input data to become available
4. run in exactly the same way as a workflow

Oozie bundles
1. new in Oozie 3.0
2. A bundle is a collection of coordinators that can be managed together


#### Zeppelin
A notebook interface to your data, e.g. iPython notebook
1. interactively run scripts/code against your data
2. interleave with nicely formatted notes
3. share notebooks with others on your cluster

Spark integration (Cassandra, Hive, HBase, Flink, R, Python, PostgreSQL, etc...)
1. execute SQL queries directly against SparkSQL
2. Query results maybe visualized in charts and graphs
 

#### Hue




