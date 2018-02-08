# python code for the logs problem
#!/usr/bin/python

import datetime
import psycopg2
DBNAME = "news"


def top_articles():
    """print the most downloaded articles"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select count, title from (select count(*) count, " +
              "substr(path, 10) title " +
              "from log where path != '/' group by path " +
              "order by count desc) as foo limit 3")
    articles = c.fetchall()
    db.close
    print("The three most popular articles are:")
    for row in articles:
        print "%s - %s views" % (row[1], '{:,d}'.format(row[0]))


def popular_authors():
    """print the most popular authors"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select auth.name, count(v.title) count " +
              "from log_v v join articles a on v.title=a.slug " +
              "left join authors auth ON a.author=auth.id " +
              "group by auth.name order by count desc")
    authors = c.fetchall()
    db.close
    print("The most downloaded authors are:")
    for row in authors:
        print "%s - %s views" % (row[0], '{:,d}'.format(row[1]))


def fails():
    """find days when download errors exceeded 1 percent of the /
    total downloads for that day"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select d, (fail * 1.0 / (success + fail) * 1.0) * 100 pct " +
              "from (SELECT cast(time as date) d, " +
              "SUM(CASE status WHEN '200 OK' THEN 1 ELSE 0 END) " +
              "AS success, SUM(CASE status WHEN '404 NOT FOUND' " +
              "THEN 1 ELSE 0 END) AS fail " +
              "from log group by d) as foo " +
              "where (fail * 1.0 / (success + fail) * 1.0) * 100 > 1")
    fails = c.fetchall()
    db.close
    print("Days when more than 1% of downloads led to errors:")
    for row in fails:
        print "%s - %.2f%% errors" % (row[0].strftime("%B %d, %Y"), row[1])


if __name__ == "__main__":
    popular_authors()
    print("-------------------")
    top_articles()
    print("-------------------")
    fails()
