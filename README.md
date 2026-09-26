# Manar – Client Management Desktop Application

A desktop application developed with **Python, PyQt5, and SQLite** to manage client information through a graphical user interface. The application provides account registration and login, client registration, record management, and a searchable client database.

## Features

* **User Authentication**

  * Create a user account.
  * Log in with a username and password.
  * Check account credentials before accessing the application.

* **Client Management**

  * Add new clients and store their personal information.
  * Import and display client profile pictures.
  * Record identity card numbers, phone numbers, ages, rooms, services, dates, and notes.
  * Update existing client records.
  * Delete client records.

* **Search**

  * Search for clients by name, ID, or phone number.
  * Display matching records in a table.

* **Dashboard**

  * View the total number of registered clients.
  * Track client records through a progress bar and LCD display.

* **Database**

  * Store user accounts and client information in an SQLite database.
  * Automatically create the database tables when the application starts.

## Technologies Used

| Technology        | Purpose                          |
| ----------------- | -------------------------------- |
| Python            | Application development          |
| PyQt5             | Desktop graphical user interface |
| Qt Designer       | Interface design (`.ui` file)    |
| SQLite            | Local database                   |
| EasyGUI           | File selection dialogs           |
| PyAutoGUI         | Alert dialogs                    |
| Python `datetime` | Date management                  |

## Project Structure

```text
Manar/
│
├── main.py
├── wassim.ui
├── Data.db
│
├── images/
│   └── ...
│
└── README.md
```

**Note:** `main.py` 

### 1. Clone the repository

```bash
git clone https://github.com/USERNAME/REPOSITORY.git
```

Replace `USERNAME` and `REPOSITORY` with your GitHub account and repository name.

### 2. Navigate to the project folder

```bash
cd REPOSITORY
```

### 3. Install the dependencies

Make sure Python is installed, then run:

```bash
pip install PyQt5 easygui pyautogui
```

SQLite and the other standard Python modules used by the application are included with Python.

### 4. Run the application

```bash
python main.py
```

Make sure the `wassim.ui` interface file and the required image assets are in their expected locations.

## Database

The application uses SQLite with two main tables:

* **users:** Stores user IDs, usernames, and passwords.
* **client:** Stores client IDs, registration dates, profile picture paths, personal information, room and service details, dates, and notes.

The database is local to the application, so the records are stored on the computer where it runs.

## Screenshots

Add screenshots of your application here to demonstrate its interface and main features.

For example:

```markdown
![Login Screen](screenshots/login.png)
![Dashboard](screenshots/dashboard.png)
![Client Management](screenshots/clients.png)
```

## Security Notice

This is a local desktop application. The current implementation stores passwords directly in the SQLite database. For production use, password hashing, parameterized SQL queries, and appropriate database backup and access controls should be implemented.

## License

Add your chosen license here before publishing the project. If you intend to keep the source code private or restrict redistribution, choose a license that reflects those requirements.
