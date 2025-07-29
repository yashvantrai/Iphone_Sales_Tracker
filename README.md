# Iphone_Sales_Tracker:
A python and fastapi project,
Track, manage, and analyze iPhone sales efficiently with a robust and clean RESTful API built using , Fastapi, Python, Postgresql.

#Overview:
This project is designed to help retail chains manage iPhone sales data effectively. It offers full CRUD functionality, sales insights, and data validation through a well-structured backend.

#Features:
1.Add, update, delete, and view iPhone sales.
2.View total sales, total revenue, popular models, and average price.
3.Pydantic-based input validation.
4.PostgreSQL integration with SQLAlchemy.
5.Auto-generated interactive API docs using Swagger. 

# Setup Instruction:
1.Python 3.10+
2.PostgreSQL installed and running
3.Git

#Clone the repository
https://github.com/yashvantrai/Iphone_Sales_Tracker.git.
cd iphone_sales_tracker

# Create and activate virtual environment:
python -m venv venv
venv\Scripts\activate

# Install required packages:
pip install -r requirements.txt

# Run the server:
uvicorn app.main:app --reload

# Check for Swagger UI:
http://127.0.0.1:8000/docs

# API Endpoints:
method      -     Endpoint        -      Description
GET               /sales/                List all sales
POST              /sales/                Create a new sale
GET               /sales/{sale_id}       Retrieve a sale by ID
PUT	              /sales/{sale_id}	     Update a sale by ID 
DELETE	          /sales/{sale_id}	     Delete a sale by ID
GET	              /sales/stats	         Get sales statistics

#Data Validation:
Field	   -       Type	        -        Validation Rules
customer_name	   string	             Required, non-empty
phone_model	       string	             Must be a valid iPhone model
color	           string	             Limited to specific valid colors 
purchase_date	   date	                 Format: YYYY-MM-DD
price	           decimal	             Required, must be a positive number