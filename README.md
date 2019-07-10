# QUIZZY API USAGE
This is the setup and expected behaviour of the Quizzy API.

## Setup 
Quizzy's API was built with MongoDB in mind, to get the API working, you should replace the empty string value for the `mongoURI` variable in app.py.  After that, you can start the API by running `flask run` in the same directory.


## Get a quiz
By accessing the `/quiz/<QUIZID>` endpoint with a GET request, you should receive a 200 OK status code along with a JSON payload in the following format:

```
{
    "name": "Superhero knowledge quiz",
    "questions": [
        {
            "answer": "28",
            "options": [
                "22",
                "24",
                "26",
                "28"
            ],
            "question": "How old is batman?"
        },
        [...]
    ]
}

```

## Upload a quiz
You should make a POST request to `/create` with a JSON payload in the same format as the above. It will return the created quiz's id with status code 201 CREATED.

```
{
    "_id": "5d24066b5cf35981d16d4dc3"
}

``` 

