# Request Log Analysis Tool

Request Log Analysis Tool is a simple script to analyze and process data from a database into a log file. The database
used is a fictional news stored in PostgresSQL. The news database contains the tables articles, authors, and log. The
tool creates a log file that contains the top 3 most viewed articles, most popular authors ordered by article views, and
 dates where errors exceed 1% of total views.

## Requirements

* Python 2.7
* PostgreSQL version >=7.4 <=10
* psycopg2 (pip install psycopg2)

## Installation
1. [Download](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) the news database
 sql file
2. Clone the GitHub repository and use Python to run the script.
  ```
  $ git clone https://github.com/nicholsont/log_tool.git
  ```

## Usage
How to run Request Log Analysis Tool

1. Import news database into PostgreSQL
  ```
  $ psql news < PATH/TO/newsdata.sql
  ```
2. Check for proper install
  ```
  $ psql news

  news=> \dt
  ```
3. Run log tool
  ```
  $ cd log_tool
  $ python log_tool.py
  ```
You can see a sample output of the logfile [here](request_log.txt)

## License
Please refer to the [License](LICENSE.md)
