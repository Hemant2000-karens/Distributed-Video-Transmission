
![Logo](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/th5xamgrr6se0x5ro4g6.png)

# Distributed Video Transmission System

This repository contains the source code for a distributed video transmission system built with Django, designed to facilitate real-time video broadcasting and playback across distributed networks. The system incorporates advanced features such as clock synchronization, mutual exclusion, fault tolerance, and distributed transaction management. Utilizing Django's robust framework, the project aims to provide a seamless and scalable solution for video conferencing and streaming applications.

## Key Features

- **Clock Synchronization**: Ensure accurate timing across distributed nodes.
- **Mutual Exclusion**: Control access to shared resources.
- **Election Algorithm**: Automatic failover and fault tolerance.
- **Transparency**: Transparent server selection for seamless client experience.
- **Distributed Transaction**: Logging and timestamping for auditing and analysis.

## Technologies Used

- **Django**: Web framework for backend development.
- **Python**: Programming language for server-side logic.
- **HTML/CSS/JavaScript**: Frontend development and user interface.
- **Docker**: Containerization for easy deployment and scalability.
- **Redis**: Cache backend for efficient data storage and retrieval.

## Getting Started

### Prerequisites

- Python (version 3.9 and later)
- Django (version latest)
- Docker (version latest)
- Redis (version X.X.X)
# Installation


#### 1. Clone the repository:
    
    git clone https://github.com/Hemant-2000karens/distributed-video-transmission.git
   
#### 2. Installing the packages required:
    sudo apt install python3 python3-pip python3-dev default-libmysqlclient-dev build-essential pkg-config virtualenv
    mariadb-server

#### 3. Activating virtualenv:

    cd <Project Location>
    virtualenv venv
    source venv/bin/activate

    
#### 4. Installation of dependencies packages:

    pip install -r requirement.txt

#### 5. Making migrations and settings

Firstly, setup and turn on Mysql Server, make a new user name root and with passowrd `passowrd`, then create database named by `DistributedSystem`, then futher create tables `code` and `code`.

Now enter command in shell

    cd <Project Location>

    python manage.py makemigrations dvs_app
    python manage.py migrate

#### 6. Running the Development Server

    python manage.py runserver


## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


## Authors

- [@Hemant Kumar](https://www.github.com/Hemant2000-karens/)


## FAQ

#### Question 1

Answer 1

#### Question 2

Answer 2

