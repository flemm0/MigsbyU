import streamlit as st



st.set_page_config(
    layout='wide',
    page_title='MigsbyU Portal'
)

st.title('MigsbyU Course Management Portal')


st.markdown('''
Welcome to the MigsbyU Course Management Portal. This application allows you register students, professors, and courses taught at MigsbyU. 
Through the submission forms in the [operational database page](http://localhost:8501/Operational_Database), you can generate random data, add your own, or
update existing records to reflect changes in real-life (e.g. students increase their GPA, change their address, etc.). In addition to the three aforementioned entities, 
you can also register students to take a course or assign professors to teach a course (under the takes and teaches tab).
            
Behind the scenes, new data generated (or changes made to existing data) is passed into an API call which subsequently makes changes to the underlying operational database, 
hosted with PostgreSQL. The operational database is normalized, as is the norm with OLTP databases, to reduce data redundancies and increase read/write efficiency.
The schema is depicted below:
''')


st.image('./oltp-db-schema.png')


st.markdown('''
To enable analytics on the students, professors, and courses at MigsbyU I have developed a CDC (change data capture) pipeline that captures all historical information
from the operational database and stores it in a separate OLAP database. This process begins with Debezium and Kafka, which have been set up and configured to read
changes from the OLAP database and write to a Kafka topic - one topic per table. The changes are then persisted to disk using Spark structured streaming, which reads
from the Kafka topics and writes the streaming DataFrame as a parquet file to the "data_lake". Finally, DuckDB is used as the query engine to display the results
in the frontend application. 
            
This architecture minimizes additional stress on the operational database, as the Debezium connector reads changes from PostgreSQL's write ahead log (wal) instead of 
querying the database directly. Additionally, the structured stream allows for changes made in the OLTP database to be reflected in the OLAP database as close to 
real-time as possible.
            
The OLAP databse schema contains 3 dimensions: students, professors, and courses; and a single factless fact table with the grain of one student-professor combination
per course per semester. The historical information for each of the dimensions is preserved using type 2 slowly-changing dimensions. The schema for the OLAP
database is shown below:
''')


st.image('./olap-db-schema.png')