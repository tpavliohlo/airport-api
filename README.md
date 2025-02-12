# Airport Service API

DRF API that allows you to manage flight schedules, routes and orders.


### Features

* CRUD operations for airplanes, routes, airplane types, airports, flights, crew and orders.
* Authentication and authorization using JWT.
* API documentation using Swagger UI.

### Installation via GitHub

#### Prerequisites

    * Python 3.12
    * pip
    * Virtual environment (recommended)
    
#### Setup

1. Clone the repository:
    
    ```bash
    git clone https://github.com/tpavliohlo/airport-api.git

2. Create and activate a virtual environment:
    
    ```bash
    python -m venv venv
    source venv/bin/activate
    '''

3. Install dependencies:
    
    ```bash
    pip install -r requirements.txt
    ```
    
4. Apply database migrations:
    
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  Create a superuser account (or use the provided credentials: 
    `admin.user` / `1qazcde3`):

    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:

    ```bash
    python manage.py runserver
    ```
