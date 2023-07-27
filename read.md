# Weather App

It is an application made using Python, Postgres, Flask, Marshmallow, SQLAlchemy, Blueprint and Rest API. And Deployed using Docker, Kubernetes and AWS.
The uses of tis app is to see weather report based on valid city name and it store all search result. It has Login and Registration Module too. It is using 3rd party API so after certain use API Key may expire for 24 hour.
It has its own custom APIS too to generate all user name, get the search history, get custom search of weather using google scraping and search of weather using third party API. It has CSRF Token as an authorization. 

## Table of contents (optional)

- Requirements
- Installation
- API End Points
- Website End Points
- Configuration
- Troubleshooting
- FAQ
- Maintainers


## Requirements
- Python 3.9
- Flask
- Pycharm or Sublime Text
- Postman
- Postgres SQL or SQL Lite
- Docker
- Kubernetes
- AWS


## Installation
- bcrypt==4.0.1
- beautifulsoup4==4.12.2
- bs4==0.0.1
- Flask==2.3.2
- flask-paginate==2022.1.8
- Flask-SQLAlchemy==3.0.5
- Flask-WTF==1.1.1
- marshmallow==3.20.1
- psycopg2-binary==2.9.6
- PyJWT==2.8.0
- requests==2.31.0
- SQLAlchemy==2.0.19


## API End Points
- To Generate Token
    * End Point: /api/generate_token
    * Arguments
        - Body [form-data]: email and password
- To get All Users
    * End Point: /api/get/all_users
    * Arguments
        - Headers: x-access-token
- To get current Weather from 3rd Party API
    * End Point: /api/currentWeather
    * Arguments
        - Headers: x-access-token
        - Body [form-data]: email and city_name
- To get current Weather from google Scraping (Won't store it into DB)
    * End Point: /api/customWeather
    * Arguments
        - Headers: x-access-token
        - Body [form-data]: city_name
- To get search history based on particular user
    * End Point: /api/historyWeather
    * Arguments
        - Headers: x-access-token
        - Body [form-data]: email
        

## Website End Points End Points
- To Register a new User
    * End Point: /register
- To Login using the username and Password
    * End Point: /login
- To Logout
    * End Point: /logout
- To see the Dashboard from where user can search and see search history
    * End Point: /dashboard
- To get current Weather from 3rd Party API
    * End Point: /currentWeather
- To get search history based on particular user
    * End Point: /historyWeather
    
        
    
## Configuration

1. Make sure all the required Packages are Installed
2. If database won't be created using code have to make it manully


## Troubleshooting

1. Debug the code
2. Check the Log Files
3. Check the Connections


## FAQ

**Q: What to do if API Key gets Expire?**

**A:** Again after 24 hour you will be able to use the API key.

**Q: What to use API?**

**A:** You can use API by providing valid Token.

**Q: What can I generate Token to use for API?**

**A:** To generate token use the API Endpoint - /api/generate_token


## Maintainers

- Utsab Dutta - [LinkedIn](https://www.linkedin.com/in/utsabdutta/)