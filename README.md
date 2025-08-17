# 🎬 Movie Recommendation System

A microservices-based Movie Recommendation System that combines **Collaborative Filtering** and **Content-Based Filtering** to deliver personalized movie suggestions.

## 🚀 Features
- Developed recommendation engine using **Collaborative & Content-Based Filtering**
- Built Django-based **RESTful microservices** (User, Rating, Recommender)
- Improved API modularity and reduced response time by **20%**
- Responsive frontend with **HTML, CSS, JavaScript** for real-time interaction
- Integrated **user and rating data** for dynamic recommendations
- Wrote **unit tests** and validated recommendation logic for accuracy
- Documented APIs and architecture for maintainability & scaling

## 🛠️ Tech Stack
- **Backend:** Django, Python
- **Frontend:** HTML, CSS, JavaScript
- **Database:** PostgreSQL / MySQL
- **Architecture:** Microservices
- **Testing:** Pytest

## 📂 Project Structure
movie-recommender/
├── user_service/        # Handles user registration & profiles
├── rating_service/      # Manages user ratings
├── recommender_service/ # Generates recommendations
├── frontend/            # HTML, CSS, JS UI
├── tests/               # Unit tests
└── docs/                # Documentation

## ⚡ Getting Started
1. Clone the repo  
   git clone https://github.com/your-username/movie-recommender.git  

2. Navigate to project directory  
   cd movie-recommender  

3. Set up virtual environment  
   python -m venv venv  
   source venv/bin/activate  

4. Install dependencies  
   pip install -r requirements.txt  

5. Run services (example for user_service)  
   cd user_service  
   python manage.py runserver  

6. Access frontend in browser  

## ✅ Future Enhancements
- Deploy microservices using **Docker & Render**
- Implement **CI/CD pipelines** with GitHub Actions
- Add **content-based NLP features** for improved recommendations
- Integrate with **React.js frontend** for better UI/UX

## 📄 License
This project is licensed under the MIT License.
