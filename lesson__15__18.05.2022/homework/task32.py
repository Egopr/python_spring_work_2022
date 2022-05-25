# todo: Написать скрипт создания базы данных(ER-модели) TestSystem
# Скрипт  create_db.py  должен создавать таблицы, индексы , констрейнты в СУБД PostgresSQL
# В задании использовать библиотеку psycopg


# Ссылка на документацию
# https://www.psycopg.org/psycopg3/docs/basic/usage.html
# Для подключения использовать пользователя и базу отличную от postgres
# Note: the module name is psycopg, not psycopg3
import psycopg


with psycopg.connect("dbname=testsysrem user=test password=0000 ") as conn:

    with conn.cursor() as cur:

        cur.execute("""
            CREATE TABLE test (
                id serial PRIMARY KEY,
                num integer,
                data text)
            """)


        cur.execute(
            "INSERT INTO test (num, data) VALUES (%s, %s)",
            (100, "abc'def"))

        cur.execute("SELECT * FROM test")
        cur.fetchone()
        # will return (1, 100, "abc'def")

        for record in cur:
            print(record)


        conn.commit()