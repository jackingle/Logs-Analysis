#!/usr/bin/env python
# Jack Ingle 9/11/2019 - added print_function to improve output
# print_function works to improve the enumerate print output
# psycopg2 allows python to communicate with the SQL server
from __future__ import print_function
import psycopg2
# List of questions to ask and answer
question1 = ("What are the most popular three articles of all time?")
question2 = ("Who are the most popular article authors of all time?")
question3 = ("On which days did more than 1% of requests lead to errors?")


def get_query_results(query):
    """
    get_query_results returns the results of an SQL query.

    get_query_results takes an SQL query as a parameter,
    executes the query and returns the results as a list of tuples.
    args:
    query - an SQL query statement to be executed.

    returns:
    A list of tuples containing the results of the query.
    """
    try:
        db = psycopg2.connect(database='news')
        cursor = db.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        db.close()
        return result
    except psycopg2.Error as e:
        print(e)
        exit(1)


def first_question(query_result):
    """
    first_question handles printing the first query by processing through
    the query results in an orderly fashion
    """
    print(query_result[1])
    for index, results in enumerate(query_result[0], 1):
        print('\t', str(index) + '.', results[0],
              '\t - ', str(results[1]), 'views')


def second_question(query_result):
    """
    second_question handles printing the first query by processing through
    the query results in an orderly fashion
    """
    print(query_result[1])
    for index, results in enumerate(query_result[0], 1):
        print("\t", str(index) + ".", results[0],
              "\t - ", str(results[1]), "views")


def third_question(query_result):
    """
    third_question handles printing the first query by processing through
    the query results in an orderly fashion
    """
    print(query_result[1])
    for index, results in enumerate(query_result[0], 1):
        print("\t", str(index) + ".", results[0],
              "\t - ", str(results[1]), "%")


query1 = """SELECT title, count(title) AS views
            FROM articles, log
            WHERE log.path=CONCAT('/article/',articles.slug)
            GROUP BY articles.title
            ORDER BY views DESC
            LIMIT 3;"""

query2 = """SELECT authors.name, count(*) as views FROM articles inner
            JOIN authors on articles.author = authors.id inner
            JOIN log ON log.path = '/article/' || articles.slug
            WHERE log.status LIKE '%200%'
            GROUP BY authors.name
            ORDER BY views DESC;"""

query3 = """SELECT * FROM (SELECT date(time),round(100.0*sum(CASE log.status
            WHEN '404 NOT FOUND'  THEN 1 ELSE 0 END)/count(log.status),3)
            AS error FROM log
            GROUP BY date(time)
            ORDER BY error DESC) AS subquery
            WHERE error > 1;"""

if __name__ == '__main__':
    """
    q1,2,3_result each store query results
    The three questions are then processed with the query results
    """
    q1_result = get_query_results(query1), question1
    q2_result = get_query_results(query2), question2
    q3_result = get_query_results(query3), question3

    first_question(q1_result)
    second_question(q2_result)
    third_question(q3_result)
