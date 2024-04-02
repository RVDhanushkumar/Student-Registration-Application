# Student-Registration-Application

#Overview
This project is a Student Registration Application developed using Python. It allows users to input student information via a graphical user interface built using the Tkinter library. The entered data is stored in a SQLite database for easy retrieval and management. Additionally, the application provides functionality to generate a PDF report containing the registered student details in a tabular format.

#Features
User-friendly graphical interface for entering student information.
Storage of student data in a SQLite database for efficient management.
Generation of PDF reports containing student details in a tabular format.
Validation of input data to ensure accuracy and consistency.
Easy navigation and interaction for users of all levels.

#Technologies Used
Python 3
Tkinter: Python's de facto standard GUI (Graphical User Interface) package.
SQLite3: A lightweight, self-contained SQL database engine.
ReportLab: A Python library for creating PDF documents.
Other Python libraries: ParagraphStyle, Letter, SimpleDocTemplate, Colors, Datetime, Regular Expressions (re), os.

Installation
1.Clone the repository to your local machine:
git clone https://github.com/your_username/your_project.git

2.Navigate to the project directory:
cd your_project

3.Install the required dependencies:
pip install -r requirements.txt

#Usage
1.Run the main Python script:
python main.py
2.Use the graphical interface to input student details and interact with the application.
3.Click on the appropriate buttons to generate PDF reports or perform other actions as needed.

#Directory Structure
project/
│
├── main.py                   # Main Python script to run the application
├── database.py               # Script handling SQLite database operations
├── pdf_generator.py          # Script for generating PDF reports
├── gui/                      # Directory containing GUI-related files
│   ├── __init__.py
│   ├── main_window.py        # Main window of the application
│   └── other_gui_elements.py # Other GUI elements (buttons, labels, etc.)
├── utils/                    # Directory containing utility scripts
│   ├── __init__.py
│   └── validation.py         # Script for data validation
├── requirements.txt          # File containing list of dependencies
└── README.md                 # ReadMe file containing project information
Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to help improve this project.

#License
This project is licensed under the MIT License - see the LICENSE file for details.

#Author
R.V.Dhanush Kumar

#Acknowledgements
Special thanks to the contributors and maintainers of the libraries used in this project.
Inspired by similar projects and online tutorials.
Hat tip to anyone whose code was used as a reference.





