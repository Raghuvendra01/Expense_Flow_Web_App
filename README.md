# Expense Tracker

A Django-based web application for managing personal expenses and budgets. Users can register, log expenses, track their spending, set budgets, and manage their financial profile.

## Features

- **User Authentication**: Secure user registration and login system with password validation
- **Expense Management**: Add, view, and delete expenses with categories, amounts, dates, and notes
- **Budget Tracking**: Set monthly income and track available balance for spending
- **User Dashboard**: View profile, upload profile picture, and manage budget settings
- **Expense History**: View all expenses in one place with complete expense details
- **Category Organization**: Organize expenses by categories for better financial tracking

## Project Structure

```
ExpenseTracker/
├── manage.py                 # Django management script
├── db.sqlite3               # SQLite database
├── addExpense/              # App for adding and managing expenses
│   ├── models.py            # Expense model
│   ├── views.py             # Expense views
│   ├── urls.py              # Expense URL routes
│   └── migrations/
├── dashboard/               # App for user dashboard and profile
│   ├── models.py            # Profile and Budget models
│   ├── views.py             # Dashboard views
│   ├── urls.py              # Dashboard URL routes
│   └── migrations/
├── register/                # App for user registration and authentication
│   ├── models.py            # Registration models
│   ├── views.py             # Registration and login views
│   ├── urls.py              # Registration URL routes
│   └── migrations/
├── ExpenseTracker/          # Project configuration
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   ├── views.py             # Project-level views
│   ├── asgi.py              # ASGI configuration
│   └── wsgi.py              # WSGI configuration
├── templates/               # HTML templates
│   ├── index.html
│   ├── register.html
│   ├── dashboard.html
│   ├── addExpense.html
│   └── allExpense.html
├── static/                  # Static files (CSS, JavaScript)
│   └── images/
└── media/                   # User uploads
    └── profiles/            # User profile pictures
```

## Models

### User Model (Django Built-in)
- Email
- Username
- Password
- First Name
- Last Name

### Expense Model
- `user`: ForeignKey to User
- `amount`: Decimal field for expense amount
- `category`: Category of the expense
- `date`: Date of the expense
- `note`: Optional notes for the expense
- `created_at`: Timestamp when expense was created

### Profile Model
- `user`: OneToOneField to User (unique profile per user)
- `image`: Optional profile picture

### Budget Model
- `user`: OneToOneField to User (unique budget per user)
- `monthly_income`: Decimal field for monthly income
- `total_balance_to_spend`: Available balance to spend
- `updated_at`: Last update timestamp

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtual Environment (recommended)

### Steps

1. **Clone or navigate to the project directory**
   ```bash
   cd "d:\Expense Tracker (1)\ExpenseTracker"
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On macOS/Linux
   ```

3. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   Or manually install:
   ```bash
   pip install Django pillow
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open your browser and go to `http://localhost:8000`
   - Admin panel: `http://localhost:8000/admin`

## Usage

### Register
1. Navigate to the registration page
2. Enter full name, email, and password (minimum 8 characters)
3. Confirm password and submit
4. You will be redirected to login

### Login
1. Enter your email and password
2. Click login to access your dashboard

### Dashboard
- View and manage your profile
- Upload a profile picture
- Set your monthly income and budget
- View budget information

### Add Expense
1. Go to "Add Expense" section
2. Enter amount, category, date, and optional notes
3. Submit to save the expense

### View All Expenses
1. Navigate to "All Expenses"
2. View complete list of all your expenses
3. Delete expenses by clicking the delete button

### Manage Budget
1. Go to Dashboard
2. Set or update your monthly income
3. Track your available balance for spending

## URL Routes

| Route | Purpose |
|-------|---------|
| `/` | Home page |
| `/register/` | User registration |
| `/login/` | User login |
| `/dashboard/` | User dashboard |
| `/addExpense/` | Add new expense |
| `/allExpense/` | View all expenses |
| `/expense/delete/<id>/` | Delete specific expense |
| `/admin/` | Django admin panel |

## Technologies Used

- **Backend**: Django 6.0.5
- **Database**: SQLite
- **Frontend**: HTML, CSS
- **Authentication**: Django's built-in auth system
- **Media Handling**: Pillow (PIL)

## Security Notes

⚠️ **Important**: The current settings contain:
- `DEBUG = False` (good for security)
- `SECRET_KEY` is visible (should be moved to environment variables for production)
- `ALLOWED_HOSTS = ['*']` (should be restricted for production)

### Recommendations for Production:
1. Move `SECRET_KEY` to environment variables
2. Set `DEBUG = False` (already done)
3. Configure specific `ALLOWED_HOSTS`
4. Use a production database (PostgreSQL, MySQL)
5. Enable HTTPS
6. Set up proper CORS headers
7. Implement rate limiting
8. Use environment variables for sensitive data

## Development & Testing

- Run tests: `python manage.py test`
- Create migrations after model changes: `python manage.py makemigrations`
- Apply migrations: `python manage.py migrate`

## File Organization

- **Templates**: HTML files for rendering views
- **Static**: CSS, JavaScript, images (not user-uploaded)
- **Media**: User-uploaded files (profile pictures)
- **Migrations**: Database schema version control

## Troubleshooting

### Database Errors
- Delete `db.sqlite3` and run `python manage.py migrate` again

### Migration Issues
- Run `python manage.py makemigrations`
- Then `python manage.py migrate`

### Static Files Not Loading
- Run `python manage.py collectstatic`

### Profile Image Not Uploading
- Check if `media/` directory exists
- Ensure Pillow is installed: `pip install pillow`

## Future Enhancements

- [ ] Add expense filtering and search functionality
- [ ] Generate expense reports and charts
- [ ] Add recurring expenses
- [ ] Implement notifications for budget alerts
- [ ] Add export to CSV/PDF functionality
- [ ] Implement expense sharing between users
- [ ] Add mobile app support
- [ ] Implement analytics and insights

## Contributing

1. Create a new branch for your feature
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please create an issue in the project repository.

---

**Last Updated**: June 2026
**Version**: 1.0.0
**Status**: Active Development
