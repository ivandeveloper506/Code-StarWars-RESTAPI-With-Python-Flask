# How to reset your migrations?

Sometimes the migration folder can get messed up, its really hard to fix some of the issues and, since we are still in development, it makes sense to reset the entire database and migrations.

## To reset the migrations carefully follow this commands:

> Warning: your data will be lost

1. In the terminal, stop server typing: `Ctrl + C`      
2. Delete the entire migrations folder.
3. Delete the database: `mysql -u root -e "DROP DATABASE example";`
4. Create the database again: `mysql -u root -e "CREATE DATABASE example";`
5. Initiallize the migrations again: `pipenv run init;`
5. Create the migration files again: `pipenv run migrate;`
7. Apply the migration files into your database: `pipenv run upgrade;`
8. Init the server: `pipenv run start;`
