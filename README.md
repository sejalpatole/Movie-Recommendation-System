# 🎬 Movie Recommendation System

An intelligent **Movie Recommendation System** built using **Python, Machine Learning, Streamlit, and TMDB API**. The application recommends movies similar to the one selected by the user using **Content-Based Filtering** and **Cosine Similarity**.

---

# 📌 Features

- 🎥 Recommend movies similar to your favorite movie
- ⭐ Displays movie posters
- 📖 Shows movie overview
- 🌟 Displays movie ratings
- 📅 Release date information
- 🎨 Attractive Streamlit UI
- ⚡ Fast recommendations using precomputed similarity matrix
- 📱 Responsive interface

---

# 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Pickle
- Requests
- TMDB API

---

# 🧠 Machine Learning Concept Used

This project uses **Content-Based Movie Recommendation**.

The recommendation engine is built using:

- Movie metadata
- Tags
- Genres
- Cast
- Crew
- Keywords

The movie features are converted into vectors and similarity is calculated using:

- **Count Vectorizer**
- **Cosine Similarity**

The system recommends the movies having the highest cosine similarity score with the selected movie.

---

# 📂 Project Structure

# 📂 Project Structure

```
Movie-Recommendation-System/
│
├── app.py                    # Alternative/Backup application 
├── app1.py                   # Main Streamlit application
├── NLPFunctions.py           # NLP preprocessing functions
├── similarities.pkl          # Cosine similarity matrix
├── data.csv                  # Intermediate dataset
├── final_data.csv            # Final processed dataset
├── tmdb_5000_movies.csv      # Original TMDB movies dataset
├── tmdb_5000_credits.csv     # Original TMDB credits dataset
├── 1. Data Preprocessing.ipynb
├── 2. Data Preparation.ipynb
├── 3. Implementation.ipynb
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Movie-Recommendation-System.git
```

Go inside the project

```bash
cd Movie-Recommendation-System
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

Run the main application

```bash
streamlit run app.py
```

Or run the alternative version

```bash
streamlit run app1.py
```

---

# 🎯 How It Works

1. User selects a movie.
2. The application finds the selected movie index.
3. Cosine similarity scores are retrieved.
4. Top similar movies are selected.
5. Movie posters are fetched from TMDB API.
6. Recommended movies are displayed with posters and details.

---


# 📊 Dataset

The project uses the TMDB Movie Dataset containing:

- Movie Title
- Genres
- Keywords
- Cast
- Crew
- Overview
- Movie ID

The dataset is preprocessed before creating the recommendation model.

---

# 📈 Recommendation Algorithm

```
Movie Selected
        │
        ▼
Find Movie Index
        │
        ▼
Retrieve Cosine Similarity Scores
        │
        ▼
Sort Scores
        │
        ▼
Top 5 Similar Movies
        │
        ▼
Fetch Posters from TMDB API
        │
        ▼
Display Recommendations
```

---

# 💻 Dependencies

```
streamlit
pandas
numpy
scikit-learn
requests
pickle
```

---

# 🚀 Future Enhancements

- User Login System
- Search by Genre
- Movie Filtering
- Favorite Movies
- Watchlist Feature
- IMDb Rating Integration
- Movie Trailers
- Recommendation History
- Dark/Light Theme Toggle
- Hybrid Recommendation System
- Collaborative Filtering
- Deploy on Streamlit Cloud

---

# 👩‍💻 Author

**Sejal Patole**

AI & Machine Learning Student

Passionate about:
- Machine Learning
- Data Science
- Python Development
- Streamlit Applications
- Artificial Intelligence

---

# ⭐ If you like this project

Give this repository a ⭐ on GitHub.

It motivates me to build more Machine Learning projects.

---

# 📜 License

This project is for educational and learning purposes.