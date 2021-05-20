# Akvelon_python_internship_3_Gadel_Khairutdinov

Django rest and Fibonacci 

I named the project "Wolf of Wall Street"

My main task in the first assignment was to create a personal finance management tool for financial planning. Create a REST API to store information about users and transactions for 3 days
I did what I could

Django REST:
![изображение](https://user-images.githubusercontent.com/81361783/118975492-bba26f00-b97c-11eb-9e45-9ba43728a40a.png)

  To add records to the database, you will need to go along the path: api / v1 / Wolf / create /
  ![изображение](https://user-images.githubusercontent.com/81361783/118975615-dd035b00-b97c-11eb-88a3-eced7e2214e2.png)


  to view all entries: http://127.0.0.1:8000/api/v1/Wolf/all /
  ![изображение](https://user-images.githubusercontent.com/81361783/118975732-fa382980-b97c-11eb-9d08-ead43f59678f.png)


  to view and edit a record, you will need to go to: http://127.0.0.1:8000/api/v1/Wolf/detail/<int: pk>/ '- where (<int: pk> /) is the ID of the record
  ![изображение](https://user-images.githubusercontent.com/81361783/118976060-42efe280-b97d-11eb-84a2-fb249f30a025.png)


  that is, it should look like this: http://127.0.0.1:8000/api/v1/Wolf/detail/1
  
  
Fibonacci:
My next task was to make a console application where I could find a number from the Fibonacci list
I am not very familiar with traditional python algorithms, but as it turned out, this is not difficult.

The algorithm is in WolfOfWallStAPP/Wolf/utils.py
![изображение](https://user-images.githubusercontent.com/81361783/118976230-792d6200-b97d-11eb-9a00-5f7ee91afff9.png)


the user is required to enter a number to define the list
and then the number you need to find
