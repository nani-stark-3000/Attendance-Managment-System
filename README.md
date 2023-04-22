# Attendance Management System

This program is a Flask-based web application for managing attendance in an educational institution. It allows the user to input an Excel file containing attendance data, along with the day for which the attendance is being taken, and generates an updated Excel file with the attendance data for that day.

## Installation

1. Clone this repository to your local machine.
2. Install the necessary dependencies by running the following command:
```
pip install Flask openpyxl
```
3. Run the program by executing the following command:
```
python app.py
```

## Usage

1. Once the program is running, navigate to `http://localhost:34` in your web browser.
2. Input the path of your Excel file in the `File` field.
3. Enter the day for which you want to take attendance in the `Day` field.
4. Enter the list of absentees' roll numbers in the `Absentees` field separated by a single space.
5. Click the `Submit` button to generate an updated Excel file with the attendance data.


# Detailed process

* This repo is a project of conecting excel and python.
* Actually my teacher asked me to maintain an excel sheet for attendence.
* Alredy i have list of roll numbers and names in an excel sheet. 
* If student was absent then in that row on that purticular day coloumn mark as '0' if present its '1'
* Iam least intreasted to enter 0s and 1s manually.
* so i have created this python code which takes input as 
>>Excel file path : (for example "D:\c++ attendance list.xlsx")
>>Day : (for example if its day-1 then "1")
* we have latral entries and normal students in our class so it takes list of absenties and automaticaly assign 0 for absentis and 1 for present
>>nlist = (for example 01 02 03 04)
>>llist = (for example 01 02 03 04)
* finally the same excel sheet will be re-writed.


## Contributing

Contributions to this project are welcome. To contribute, please follow these steps:

1. Fork this repository.
2. Create a new branch for your changes.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request.
