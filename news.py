#!/usr/bin/env python
# python code for the logs problem.

import datetime
import psycopg2
DBNAME = "news"


def sql_helper(query):
    """helper function to run sql queries"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    try:
        query = c.execute(query)
        results = c.fetchall()
    except Exception:
        print "The SQL query could not be executed"
    db.close
    return results


def top_articles():
    """print the most downloaded articles"""
    query = ("select count, title from (select count(l.*) count, " +
             "a.title from log l, articles a where l.path != '/' and " +
             "'/article/' || a.slug = l.path group by path, title "
             "order by count desc) as foo limit 3")
    articles = sql_helper(query)
    print("The three most popular articles are:")
    for views, title in articles:
        print('"{}" - {:,d} views'.format(title, views))


def popular_authors():
    """print the most popular authors"""
    query = ("select auth.name, count(l.*) count " +
             "from log l join articles a on '/article/' || a.slug = l.path " +
             "left join authors auth ON a.author=auth.id " +
             "group by auth.name order by count desc")
    authors = sql_helper(query)
    print("The most downloaded authors are:")
    for author, views in authors:
        print('{} - {:,d} views'.format(author, views))


def fails():
    """find days when download errors exceeded 1 percent of the /
    total downloads for that day"""
    query = ("select d, (fail * 1.0 / (success + fail) * 1.0) * 100 pct " +
             "from (SELECT cast(time as date) d, " +
             "SUM(CASE status WHEN '200 OK' THEN 1 ELSE 0 END) " +
             "AS success, SUM(CASE status WHEN '404 NOT FOUND' " +
             "THEN 1 ELSE 0 END) AS fail " +
             "from log group by d) as foo " +
             "where (fail * 1.0 / (success + fail) * 1.0) * 100 > 1")
    fails = sql_helper(query)
    print("Days when more than 1% of downloads led to errors:")
    for date, pct in fails:
        print('{} - {:.2f}% errors'.format(date.strftime("%B %d, %Y"), pct))


if __name__ == "__main__":
    top_articles()
    print("-------------------")
    popular_authors()
    print("-------------------")
    fails()
