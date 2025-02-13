# lunch-place
Lunch Place API
This is the backend of a restaurant management system for managing daily menus, employees, and restaurants. The system includes JWT-based authentication, creating and uploading menus, managing employees, and getting the current day’s menu and results.

Before you begin, make sure you have Python 3+, Docker, Docker Compose, and PostgreSQL installed on your system.

Step-by-step Setup
Clone the repository:

git clone https://github.com/VolodymyrSemchysyn/lunch-place
cd lunch-place
Install the project dependencies with Poetry:

poetry install
Set up the PostgreSQL database:

Create a PostgreSQL database and configure your DATABASES settings in settings.py. After configuring, run migrations:

Running with Docker
Ensure Docker is installed.

Build the Docker image:

docker-compose build
Start the Docker containers:

docker-compose up
Once the containers are up, the app will be accessible at http://localhost:8000/.

Authentication
Create a user via /api/user/register/.
Get the access token via /api/user/token/. Use the token in the Authorization header for all subsequent requests.
API Endpoints
1. Restaurant Endpoints
GET /api/restaurants/ - List all restaurants.
POST /api/restaurants/ - Create a new restaurant.
PUT /api/restaurants/{id}/ - Update an existing restaurant.
DELETE /api/restaurants/{id}/ - Delete a restaurant.
2. Menu Endpoints
GET /api/menus/ - Get all menus.
POST /api/menus/ - Upload a new menu for the current day.
GET /api/menus/today/ - Get the menu for the current day.
DELETE /api/menus/{id}/ - Delete a menu.
3. Employee Endpoints
POST /api/employees/ - Create a new employee.
GET /api/employees/ - Get all employees.
4. Voting Endpoints
POST /api/votes/ - Vote for a menu.
GET /api/votes/results/ - Get the results (e.g., vote counts) for the current day.
Tests
You can run tests using the following command:

poetry run pytest
Tests are located in the tests/ folder and test the functionality of the API, including:

User authentication and token generation.
Restaurant creation and deletion.
Menu upload and retrieval.
Employee creation.
Voting and results tracking.
