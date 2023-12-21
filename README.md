# GradeGrind - Intelligent Student Task Manager

My final project for the CS50x course, and introduction to computer science by Harvard University

## Overview

EduTasker is an innovative web application tailored for students, designed to streamline task management and enhance academic productivity. This platform facilitates efficient scheduling and organization of academic tasks and assignments.

## Features

- **Task Creation and Management:** Add, update, and track tasks with ease.
- **Categorization:** Sort tasks by subjects or custom categories.
- **User Authentication:** Personalized experience with secure account creation and login.
- **Responsive Design:** Optimized for both desktop and mobile devices, ensuring accessibility anytime, anywhere.

## Technology Stack

- **Front-End:** HTML, CSS, JavaScript
- **Back-End:** Python with Flask
- **Database:** SQLite for the MVP, with a possibility of scaling to MySQL later
- **Other Tools:** SQLAlchemy, Flask-Migrate for database migrations

## Installation and Setup

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Setting Up a Virtual Environment

Create and activate a virtual environment:
```bash
  python3 -m venv venv
  source venv/bin/activate # On Windows, use `venv\Scripts\activate`
```

# Installing Dependencies

Install the required Python packages:

```bash
  Copy code
  pip install -r requirements.txt
```

# Database Initialization

Set up and migrate the database:

```bash
  flask db init
  flask db migrate
  flask db upgrade
```

# Running the Application

Launch EduTasker locally:

```bash
  python run.py
  Access the app at http://localhost:5000 in your web browser.
```

# Contributing

Contributions to GradeGrind are welcome! Please fork the repository and submit pull requests with your proposed changes.

# License

EduTasker is open-source software licensed under the MIT License - see the LICENSE file for details.

# Author

Lucas Larsson
Acknowledgments
Special thanks to the CS50 course team for the inspiration and foundational knowledge.
