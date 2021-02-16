## Docker Setup

To create a MySQL server and client, we will be using a tool called `docker`. We aren't going to go into the details of how it works in this module, however we do have an entire module dedicated to it soon after this one.

## Part 1

1. Ensure you have Docker Desktop installed
2. Ensure you have the `docker-setup` directory
3. Run the following command inside the directory. This will create both the client and server for us which is running on localhost.

```sh
$ docker-compose up -d
```

4. Navigate to the following URL to ensure that you can see the `Adminer` interface:

http://localhost:8080/

5. Fill in the username (`root`) and password field (`password`)
6. Select `SQL Command` on the left
7. We'll create our own database with:

```
CREATE DATABASE test;
```

7. Select `test` in the DB dropdown
8. Now we'll create our first table with:

```sql
CREATE TABLE person (
  person_id INT NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  age INT,
  PRIMARY KEY(person_id)
);
```

9. Let's alter the table by adding a new field:

```sql
ALTER TABLE person 
ADD email varchar(255);
```

---

## Part 2

1. Insert rows into the `person` table
2. Try and update some of the rows
3. Try and delete some rows you created
4. Build up a SELECT statement one part at a time and start to refine your query (use all of the keywords `SELECT, FROM, WHERE, ORDER BY, LIMIT`)

---

## Part 3

1. Start up the dev container
1. Activate a virtual env
1. Install the dependencies from `requirements.txt`
1. Run the `python_mysql_example.py` file