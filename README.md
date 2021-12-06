# Saarthi-Backend

Only name and id attributes are accepted/stored presently. 

## Requirement 1 - Not Done
When the endpoint: GET http://localhost:8080/api/external-books?name=:nameOfABook is requested, your application should query the Ice And Fire API and use the data received to respond with JSON.

## Requirement 2 
### Create - Done
When the endpoint: POST http://localhost:8080/api/v1/books is requested with the following data: name, isbn, authors, country, number_of_page, publisher, release_date a book should be created in the local database.

### Read - Done but it's not searchable
When the endpoint: GET http://localhost:8080/api/v1/books is requested, your solution will return a list of books from the local database using the following response:{"status_code": 200,"status": "success","data": [{"id": 1,"name": "A Game of Thrones","isbn": "978-0553103540","authors": ["George R. R. Martin"],"number_of_pages": 694,"publisher": "Bantam Books","country": "United States", ... }

The Books API should be searchable by name (string), country (string), publisher (string) and release date (year, integer).

### Update - Done
When the endpoint: PATCH http://localhost:8080/api/v1/books/:id is requested with any form data such as name, isbn, database should be updated.

Alternative endpoint: POST http://localhost:8080/api/v1/books/:id/update

### Delete - Done
When the endpoint: DELETE http://localhost:8080/api/v1/books/:id is requested with a specific :id in the URL, where :id is a placeholder variable for an integer (for example 1), the specific book should be deleted from the database and the following response will be returned:{"status_code": 200,"status": "success","message": "The book My First Book was deleted successfully","data": []}

An alternative endpoint for deleting a book could be: POST http://localhost:8080/api/v1/books/:id/delete

### Show - Not Done
When the endpoint: GET http://localhost:8080/api/v1/books/:id is requested, return JSON containing record.

## Evaluation Instruction
When evaluating the submitted solution, we will put attention on the following:
- Fully functional solution: we will test the API endpoints and see if they return the expected results based on the provided input. **Not Done**
- Make sure to have things well documented in the README, so we can easily set up the project and test it. **Done**
- Good code design: we put special attention to the design of the code. Make sure your code is clean and readable, it complies with the SOLID design principles and makes use of design patterns where it makes sense. 
- Tested code: don’t forget to write your tests before submitting. You may use Python’s Unittest module or any third party testing framework like Nose or PyTest. **Not Done**
- Code Coverage: Make sure to submit the code coverage for the assignment, a code coverage would mean 95% or more. **Many corner cases have not been tested**
- Benchmark: Benchmark the APIs for various load and stress scenarios. **Not Done**

## Bonus
Show the results in the browser using Angular or React frameworks in code highlighted JSON format. **Not Done**
Automated scripts to deploy. **Not Done**

# To Run Locally
This project has only been tested on Ubuntu 20.04. 

```bash
alias pmpy=python manage.py
pip install -r requirements.txt
pmpy migrate
pmpy runserver
```

# To Setup and Run on PythonAnywhere
Clone this repository on a bash terminal on PythonAnywhere, create a web app, edit configuration file.

# To Test

Install Postman on your system and send requests to `http://localhost:8000/v1/...` (if you're running locally, else use PythonAnywhere URLs). The port number 8000 is the default port that the Django project runs on. 

Please end your URLs with a slash otherwise there may be an error.