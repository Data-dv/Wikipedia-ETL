# Wikipedia-ETL

## Overwiew
In this project, I assumed the role of a data engineer for an EdTech StartUp in Lagos, Nigeria. I built a simple and robust data pipeline that extracts the information about the largest universities in the world by country from Wikipedia page, transforms and cleans the data, and then stores it in a database necessary for the use-case scenarios. Different tools, programming language and libraries was used to ensure the data is properly formated and inserted into the databases used, such as PostgreSQL and MySQL. A virtual enivronment and docker was used for local development of the data pipeline and deployment. Once the extracted data is transformed, cleaned and stored, a data visualization tool like Metabase was connected to create interactive charts and graphs giving visuals to business problems. Additionally, the stored data was analyzed using SQL queries on PgAdmin to extract meaningful insights and informations. These analyses, combined with the visualizations, will help generate actionable insights to enhance the goal of the EdTech company. The project focuses on building a scalable and reproducible system, ensuring that the process can be easily replicated. This end-to-end pipeline will provide valuable experience in data engineering, processing, visualization, and analysis.

## Objectives
- Provide Recommendations: The processed data will be utilized by the EdTech StartUp to offer personalized recommendations to clients.
- Enhance Decision-Making: Generate actionable insights that can guide the EdTEch StartUp in her investment strategies and actions.
- Streamline Data Management: Employ a robust architecture that ensures data consistency and ease of access for analysis and visualization.
- Design a Versatile Workflow: Create a streamlined workflow that can be seamlessly executed both within Docker containers and in a local environment.

## Data Source
- Wikipedia Page: [Wikipedia Page](https://en.wikipedia.org/wiki/List_of_largest_universities)

## Extracted Fields
- Country: The name of the country the university is situated.
- University: The name of the University
- Founded: The year the university was founded
- Type: The type of university
- Enrollment: The total popultion of student
- Link: The university website

## Architecture Diagram
