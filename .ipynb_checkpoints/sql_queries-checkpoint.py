# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS SongPlayFact;"
user_table_drop = "DROP TABLE IF EXISTS UserDim;"
song_table_drop = "DROP TABLE IF EXISTS SongDim;"
artist_table_drop = "DROP TABLE IF EXISTS ArtistDim;"
time_table_drop = "DROP TABLE IF EXISTS TimeDim;"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS SongPlayFact (
    songplay_id int, 
    start_time varchar(50), 
    user_id int,  
    level varchar(5), 
    song_id varchar(50), 
    artist_id varchar(50),  
    session_id int, 
    location varchar(200), 
    user_agent varchar(255)
    );
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS UserDim (
    user_id int,
    first_name varchar(100),
    last_name varchar(100),
    gender varchar(5),
    level varchar(5)
    );
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS SongDim (
    song_id varchar(50), 
    title varchar(100), 
    artist_id varchar(50), 
    year int, 
    duration decimal(8,5)
    );
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS ArtistDim (
    artist_id varchar(50),
    name varchar(100),
    location varchar(100),
    latitude DECIMAL(10,8), 
    longitude DECIMAL(11,8)
    );
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS TimeDim (
    start_time varchar(50), 
    hour varchar(50), 
    day varchar(50), 
    week varchar(50), 
    month varchar(50), 
    year varchar(50), 
    weekday varchar(50)
    );
""")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
    INSERT INTO SongDim (
    song_id, 
    title, 
    artist_id, 
    year, 
    duration
    )
    VALUES (%s, %s, %s, %s, %s)
    """)

artist_table_insert = ("""
    INSERT INTO ArtistDim (
    artist_id,
    name,
    location,
    latitude, 
    longitude
    )
    VALUES (%s, %s, %s, %s, %s)
""")

time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]