# bespoke-restapi2 usage

Using the desired requests from Postman:

*Returns an error if 'key' does not exist in the database (db)

POST and PUT methods require a JSON object in the body with the updated values in the format:

```
{
  'name': (string),
  'sweetness': (int)
}
```

##### GET*

Returns a specified entry from the db

127.0.0.1:5000/fruits/name

ex. 127.0.0.1:5000/fruits/Apple

##### POST*

Updates and returns the updated entry

127.0.0.1:5000/fruits/name

##### PUT

Creates or updates the entry and returns the new entry

127.0.0.1:5000/fruits/name


##### DELETE*

Deletes the entry and returns the deleted item + deleted status

127.0.0.1:5000/fruits/name

