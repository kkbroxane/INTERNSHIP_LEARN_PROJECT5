# INTERNSHIP LEARN PROJECT 5

  - [Part 1 shortcut](#part-1-getting-started)
  - [Part 2 shortcut](#part-2-dive-in-my-project)

## Description:

Development of an AI Chatbot specialized in real estate.

### Technologies used:

- [Django](https://docs.djangoproject.com/en/5.2/)
- [Python](https://docs.python.org/3/),
- [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/),
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript).

# PART 1: Getting started

## Setup environment

Run :

```bash
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Next, navigate to the `project3` repository. Optional in this case, but for the sake of taking precautions, run :

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

Now, run the website :

```bash
$ python manage.py runserver
```

# PART 2: Dive in my project

## Features of my website

### User System

* **Login**: Users can securely log into their accounts.
* **Register**: New users can create an account.
* **Logout**: Users can safely log out.
* **User Roles**: User can have *student* or *teacher* role

### Home Page

* **Top Bar**: Displays the site name and authentication buttons (Login/Register or Logout). If the user is logged in, their username is shown.
* **Sidebar**: Quick navigation with links to *Home*, *Profile* (and *Create New Course* for teachers).
* **Lesson Carousel**: Highlights available lessons in a scrollable view.
* **Browse All**: “View All” button that shows all lessons available.

### Profile Page

* **User Information**: Displays username, email, and optional profile picture (with the ability to update the picture).
* **Course Tracking**: Lists on-going courses and completed courses.

### Course Page

* **Course Details**: Each course has a cover image, title and author.
* **Chapters**: Courses are divided into structured chapters for easier navigation and learning.

### Course Creation (Teacher Only)

* **Admin Access**: Only teachers (admins) can create new courses.
* **Course Builder**: Allows teachers to add a course cover, title, author, and chapters.
