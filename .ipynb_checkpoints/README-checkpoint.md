# Sparkify Song Data Warehouse

### Developer Details

> Name: Darren Foley
> Email: <darren.foley@ucdconnect.ie>


### Project High Level Summary

<p>This project involves the creation of an analytical (OLAP) database to meet reporting requirements for Sparkify, a startup streaming service provider. Until now, sparkify did not have a convenient way to create reports on how users interact their platform. The project contains three parts;  
</p>

1. Backend Design: Postgres database schema
2. ETL Design: python/SQL pipeline
3. Frontend Design: Python dashbpard/Report on user behaviour


### Design Overview

*1. Backend Design*

<p>The database of choice was a PostgreSQL instance (v9.5.23) deployed on a single core, 4GB Ubuntu Virtual Machine (v16.04.7 LTS).</p>

<p>A star schema configuration was chosen to improve read performance of the reports. There were 4 dimension tables and 1 fact table.</p>

Fact tables 
> SongPlayFact

Dimension tables
> UserDim
> SongDim
> ArtistDim
> TimeDim

Diagrams

![ Conceptual Diagram !](/home/workspace/images/conceptual)

![ Logical Diagram !](/home/workspace/images/logical)

![ Physical Diagram !](/home/workspace/images/physical)




*2. ETL Design*

<p>The ETL pipeline heavily utilises the psycopg2 package for interacting with the postgres database. Its used to wrap the SQL statements and provide an easy way to parameterize the queries so that are more extensible. Pandas was used for data manipulation/filtering. Embedded SQL statements were used to insert data into the database tables. </p>

![ ETL Diagram !](/home/workspace/images/etl_design)



*3. Front End Design*

<p>A report on user behaviour was created as a proof of concept to demonstrate the utility of new data warehouse.</p>