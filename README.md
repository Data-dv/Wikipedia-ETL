# Wikipedia-ETL

## Overwiew
In this project, I assumed the role of a data engineer for an EdTech StartUp in Lagos, Nigeria. I built a simple and robust data pipeline that extracts the information about the largest universities in the world by country from Wikipedia page, transforms and cleans the data, and then stores it in a database necessary for the use-case scenarios. Different tools, programming language and libraries was used to ensure the data is properly formated and inserted into the databases used, such as PostgreSQL and MySQL. A virtual enivronment and docker was used for local development of the data pipeline and deployment. Once the extracted data is transformed, cleaned and stored, a data visualization tool like Metabase was connected to create interactive charts and graphs giving visuals to business problems. Additionally, the stored data was analyzed using SQL queries on PgAdmin to extract meaningful insights and informations. These analyses, combined with the visualizations, will help generate actionable insights to enhance the goal of the EdTech company. The project focuses on building a scalable and reproducible system, ensuring that the process can be easily replicated. This end-to-end pipeline will provide valuable experience in data engineering, processing, visualization, and analysis.

## Objectives
- **Provide Recommendations**: The processed data will be utilized by the EdTech StartUp to offer personalized recommendations to clients.
- **Enhance Decision-Making**: Generate actionable insights that can guide the EdTEch StartUp in her investment strategies and actions.
- **Streamline Data Management**: Employ a robust architecture that ensures data consistency and ease of access for analysis and visualization.
- **Design a Versatile Workflow**: Create a streamlined workflow that can be seamlessly executed both within Docker containers and in a local environment.

## Data Source
- Wikipedia Page: [Wikipedia Page](https://en.wikipedia.org/wiki/List_of_largest_universities)

## Extracted Fields
- **Country**: The name of the country the university is situated.
- **University**: The name of the University
- **Founded**: The year the university was founded
- **Type**: The type of university
- **Enrollment**: The total popultion of student
- **Link**: The university website

## Architecture Diagram
![Alt text](https://github.com/Data-dv/Wikipedia-ETL/blob/4ee497590dbbb431bbc22b6b89471ea7f7d1230e/Images/Data%20Architecture.png)

## Why This Architecture
We chose this architecture for its simplicity and efficiency. Given the nature of the data, which is small and rarely changes, extensive automation and complex setups would be unnecessary and resource-intensive. Here's why we opted for this approach:

- **Simplicity**: The data is small and can be handled easily without the need for batch loading.
- **Efficiency**: Automation is not required as the data rarely changes, saving time and resources.
- **Speed**: The data can be extracted and loaded into the database within a minute.
- **Minimal Setup**: We decided against using a staging database or data lake due to the manageable size of the data. The only aspect of the data that might change is the population, which is updated every year through each university's website across different counties. This streamlined approach ensures quick and effective data processing while avoiding unnecessary complexity
- **Database Strategy (Dual Database Approach)**:
  - PostgreSQL for:
    - Complex data analysis and querying
    - Better handling of large datasets
    - Advanced analytical functions
    - Integration with BI tools like Metabase
  - MySQL for:
    - Simple, quick queries
    - Backup/redundancy
    - Different use case optimizations
    - Load balancing for read operations

## Tools Used
**Python for ETL**:
  - Python serves as the primary language for Extract, Transform, Load (ETL) processes.
  - Utilizes powerful libraries such as Pandas, requests, and pyscopg2 for data manipulation and database interaction.
  - Automates the extraction of data from source and tansfrom it into usable formats, then load the data into databases.

**Metabase for Data Visualization**:
  - Metabase is used for creating interactive and insightful data visualizations.
  - Connects seamlessly to the Postgres database to visualize data in real-time.

**Postgres for Database Management**:
  - PostgreSQL (Postgres) is the database system for storing and managing data.
  - Known for its robustness, scalability, and support for complex queries.
    
**pgAdmin for Database Management**:
  - pgAdmin is the tool for managing the Postgres database.
  - Offers a user-friendly interface for database administration tasks.
  - Facilitates tasks such as querying, data modeling, and database monitoring.

**Docker for Managing Services**:
  - Containerization: Docker puts each service (like Python scripts, Metabase, Postgres, pgAdmin) into separate boxes. For example, if you run a Python script, Docker ensures it runs the same way on any computer.
  - Consistency: Docker ensures that everything works the same on different machines. For instance, if your script needs specific tools, Docker makes sure everyone has the same tools.
  - Integration: Docker helps all services work together smoothly. If you need your script to get data from Postgres and visualize it in Metabase, Docker keeps everything connected.

## Python Dependencies
- requests
- pandas
- dotenv
- psycopg2
- logging

## Getting Started
## Running Without Docker
- Make sure you have Pgadmin and Postgres on your PC.
- Clone the repository.
