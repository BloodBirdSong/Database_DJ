### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?

  PostgreSQL is a powerful, open-source object-relational database management system. It is known for its robustness, scalability, and extensibility.

- What is the difference between SQL and PostgreSQL?

  SQL is a language for working with relational databases, and it is implemented by various database systems, including PostgreSQL. PostgreSQL, on the other hand, is a specific database system that uses SQL as its query language but also provides many additional features and capabilities beyond the SQL standard.

- In `psql`, how do you connect to a database?
  psql -U username -d database_name -h host -p port

- What is the difference between `HAVING` and `WHERE`?

The WHERE clause is used to filter rows from a table before any grouping.

The HAVING clause is used to filter the result set after grouping.

- What is the difference between an `INNER` and `OUTER` join?

An INNER JOIN returns only the rows that have matching values in both tables.

The specific type of OUTER JOIN determines which table's rows are included even if they have no matches.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?

A LEFT OUTER JOIN returns all rows from the first table and the matching rows from the second table. If there are no matches in the second table, NULL values are used for columns from the second table in the result set.

A RIGHT OUTER JOIN returns all rows from the second table and the matching rows from the first table. If there are no matches in the first table, NULL values are used for columns from the first table in the result set. 

- What is an ORM? What do they do?
The primary purpose of an ORM is to bridge the gap between the object-oriented world of the application and the relational world of the database.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
AJAX:
  AJAX requests are made from the client-side, typically within a web browser, using JavaScript
  AJAX is commonly used for making asynchronous requests from a web page to fetch data or interact with APIs without requiring a full page reload.

requests:
  Server-side requests are initiated and handled by the server where your application is hosted.
  Server-side libraries like requests are used when the server needs to interact with external services, APIs, or other servers.



- What is CSRF? What is the purpose of the CSRF token?
  CSRF is a security vulnerability where attackers trick users into performing unauthorized actions on a different website where the user is authenticated. CSRF tokens are used to prevent these attacks by ensuring that requests made to a web application are legitimate and originate from the same site where the user is logged in. 

- What is the purpose of `form.hidden_tag()`?
  In web development using frameworks like Flask and other Python-based frameworks, form.hidden_tag() is a function typically used to generate a hidden form field that contains a CSRF (Cross-Site Request Forgery) token. This token is an essential security measure to protect against CSRF attacks.