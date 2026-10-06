# RateWise – Feedback Management Platform

RateWise is a Django-based feedback management platform that allows users to create customizable feedback forms, collect ratings and comments, and analyze submitted feedback through an interactive analytics dashboard.

## Features

- User registration and authentication
- Create customizable feedback forms
- Dynamically add questions while creating a form
- Add custom fields to feedback forms
- Share forms through unique form links
- Collect ratings, email addresses, comments, and additional field responses
- Prevent duplicate feedback submissions for the same form and email
- Edit and delete created forms
- View submitted responses
- Calculate overall average ratings
- Calculate question-wise average ratings
- Visualize question ratings using charts
- Filter comments based on rating
- Analyze textual feedback using AI-based sentiment analysis
- Classify feedback as Positive, Negative, or Neutral

## Tech Stack

### Backend
- Python
- Django

### Frontend
- HTML
- CSS
- JavaScript
- Chart.js

### Database
- MySQL
- PyMySQL

### AI / Machine Learning
- Hugging Face Transformers
- RoBERTa Sentiment Analysis Model
- `cardiffnlp/twitter-roberta-base-sentiment-latest`

## Project Structure

```text
feedback_gen/
│
├── feedback/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── sentiment.py
│   └── ...
│
├── login/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── feedback_gen/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/
│   ├── feedback/
│   ├── home.html
│   ├── dashboard.html
│   ├── login.html
│   └── register.html
│
├── static/
│   └── images/
│
├── manage.py
└── requirements.txt
