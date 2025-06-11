## Database (with sqlalchemy)

- Install the two packages `pipenv install flask-sqlalchemy flask-migrate`
- How to get the possible commands `flask db --help`
- Init migrations with `flask db init` run only once
- Create migration files with `flask db migrate -m "message"`
- Apply migration with `flask db upgrade`