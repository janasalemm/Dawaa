# Dawaa – Medication Organizer Web App

**Dawaa** is a simple and useful web application that helps users manage and organize their medication schedules. It allows users to add medicines, specify how many times per day to take them, and write the exact times for each dose.

## Features

- Arabic user interface with clear design.
- Add new medicines with name, dose frequency, and specific times.
- Display all medications in a clear and organized table.
- Styled user interface using custom CSS.

## Technologies Used

- Python
- Flask
- SQLite
- HTML (Jinja Templates)
- CSS

## How to Run the App

1. Make sure Flask is installed:
   ```bash
   pip install flask
   ```

2. Run the application:
   ```bash
   flask run
   ```

3. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

4. To access the site from another device (e.g., iPad), run:
   ```bash
   flask run --host=0.0.0.0
   ```
   Then open:
   ```
   http://<your-computer-IP>:5000
   ```

## Project Structure

```
dawaa/
├── app.py
├── dawaa.db         ← created automatically
├── static/
│   └── style.css     ← for custom styling
├── templates/
│   ├── layout.html
│   ├── index.html
│   └── add.html
├── README.md
```

## Notes

- You can expand this project by adding notifications, login system, or email reminders.
- This project fulfills the CS50 Final Project requirements with a clean and functional design.

---

## Created with passion for CS50
