import streamlit as st
import pandas as pd
import pickle
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.title("🎬 Movie Recommender")

    st.markdown("---")

    st.write("### 📊 Project Information")

    st.write("**Dataset**")
    st.write("TMDB 5000 Movies")

    st.write("**Algorithm**")
    st.write("Cosine Similarity")

    st.write("**Language**")
    st.write("Python")

    st.write("**Framework**")
    st.write("Streamlit")

    st.markdown("---")

    st.success("Machine Learning Project")

# =====================================================
# CUSTOM CSS
# =====================================================
st.markdown("""
<style>

/* =====================================================
GENERAL
===================================================== */

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

header{
    visibility:hidden;
}

.stApp{
    background:linear-gradient(135deg,#0B0B0B,#151515,#1F1F1F);
}

/* =====================================================
TEXT
===================================================== */

html,
body{
    color:white;
}

h1,h2,h3,h4,h5,h6{
    color:white !important;
}

p{
    color:#DDDDDD !important;
}

label{
    color:white !important;
}

.stMarkdown{
    color:white !important;
}

/* =====================================================
HERO
===================================================== */

.hero{

    background:linear-gradient(135deg,#E50914,#7B0000);

    padding:60px;

    border-radius:25px;

    text-align:center;

    margin-bottom:40px;

    box-shadow:0 8px 25px rgba(0,0,0,.45);

}

.hero h1{

    font-size:58px;

    color:white !important;

}

.hero h3{

    color:#EEEEEE !important;

}

.hero p{

    color:#DDDDDD !important;

    font-size:18px;

}

/* =====================================================
SECTION TITLE
===================================================== */

.section-title{

    font-size:34px;

    font-weight:bold;

    color:white !important;

}

/* =====================================================
METRICS
===================================================== */

[data-testid="stMetric"]{

    background:#1F1F1F;

    border-radius:18px;

    padding:18px;

    border:1px solid #333333;

}

/* =====================================================
CARD
===================================================== */

.card{

    background:#1F1F1F;

    padding:25px;

    border-radius:18px;

    border:1px solid #333333;

    box-shadow:0 5px 15px rgba(0,0,0,.35);

}

/* =====================================================
SELECTBOX
===================================================== */

div[data-baseweb="select"]{

    background:#2A2A2A;

    color:white;

    border-radius:10px;

}

/* =====================================================
BUTTON
===================================================== */

.stButton > button{

    width:100%;

    height:55px;

    border:none;

    border-radius:12px;

    background:linear-gradient(90deg,#E50914,#B20710);

    color:white;

    font-size:18px;

    font-weight:bold;

}

.stButton > button:hover{

    background:linear-gradient(90deg,#FF3030,#E50914);

}

/* =====================================================
MOVIE CARD
===================================================== */

.movie-card{

    background:#202020;

    color:white !important;

    padding:20px;

    border-radius:15px;

    border-left:6px solid #E50914;

    margin-bottom:20px;

    box-shadow:0 5px 15px rgba(0,0,0,.35);

}

.movie-card h2,
.movie-card h3{

    color:white !important;

}

.movie-card p{

    color:#DDDDDD !important;

}

/* =====================================================
SIDEBAR
===================================================== */

[data-testid="stSidebar"]{

    background:#141414;

}

[data-testid="stSidebar"] *{

    color:white !important;

}

/* =====================================================
SUCCESS
===================================================== */

[data-testid="stAlert"]{

    border-radius:12px;

}

/* =====================================================
FOOTER
===================================================== */

.footer{

    text-align:center;

    color:#BBBBBB;

    margin-top:50px;

    padding:25px;

}

/* =====================================================
HR
===================================================== */

hr{

    border:1px solid #333333;

}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HERO SECTION
# =====================================================

st.markdown("""

<div class="hero">

<h1>🎬 Movie Recommendation System</h1>

<h3>Discover Your Next Favorite Movie</h3>

<p>

Get personalized movie recommendations using
Machine Learning and Cosine Similarity.

</p>

</div>

""", unsafe_allow_html=True)

# =====================================================
# LOAD DATASET
# =====================================================

df = pd.read_csv("final_data.csv")

# =====================================================
# ABOUT PROJECT
# =====================================================

st.markdown("## 🎥 About This Project")

st.info("""
This Movie Recommendation System uses **Natural Language Processing (NLP)** and
**Cosine Similarity** to recommend movies based on content such as genres,
keywords, cast, crew, and overview.

Select a movie from the dropdown below to discover five similar movies.
""")

# =====================================================
# DASHBOARD
# =====================================================

st.markdown("<h2 class='section-title'>📊 Dashboard</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="🎬 Total Movies",
        value=len(df)
    )

with col2:
    st.metric(
        label="🤖 AI Model",
        value="Cosine Similarity"
    )

with col3:
    st.metric(
        label="⭐ Recommendations",
        value="Top 5"
    )

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# MOVIE RECOMMENDATION PANEL
# =====================================================

st.markdown("""
<div class="card">

<h2 style="color:white;">🎥 Find Your Next Movie</h2>

<p style="color:#CFCFCF; font-size:17px;">

Search for a movie you've already watched and our recommendation
engine will suggest five similar movies that you might enjoy.

</p>

</div>

""", unsafe_allow_html=True)

# =====================================================
# MOVIE LIST
# =====================================================

movie_names = sorted(df["title"].unique())

st.markdown(
    "<h3 style='color:white;'>🎬 Search Movie</h3>",
    unsafe_allow_html=True
)

selected_movie = st.selectbox(
    "",
    movie_names,
    label_visibility="collapsed"
)

recommend = st.button(
    "✨ Recommend Movies",
    use_container_width=True,
    key="recommend_button"
)

# =====================================================
# GENERATE SIMILARITY MATRIX (ONLY ONCE)
# =====================================================

if not os.path.exists("similarities.pkl"):

    with st.spinner("Generating recommendation model..."):

        cv = CountVectorizer(
            max_features=10000,
            stop_words="english"
        )

        dtm = cv.fit_transform(df["tags"])

        similarities = cosine_similarity(dtm)

        pickle.dump(
            similarities,
            open("similarities.pkl", "wb")
        )

# =====================================================
# HELPER FUNCTIONS
# =====================================================

def get_movie_index(movie_name):

    for i in df.index:

        if movie_name == df.loc[i, "title"]:

            return i

    return -1


def get_movie_name(index):

    if index >= len(df):

        return ""

    return df.loc[index, "title"]

# =====================================================
# RECOMMENDATION ENGINE
# =====================================================

if recommend:

    with st.spinner("Finding similar movies for you... 🍿"):

        similarities = pickle.load(open("similarities.pkl", "rb"))

        movie_index = get_movie_index(selected_movie)

        if movie_index == -1:

            st.error("Movie not found!")

        else:

            similarity_scores = list(enumerate(similarities[movie_index]))

            similarity_scores = sorted(
                similarity_scores,
                key=lambda x: x[1],
                reverse=True
            )

            # Progress Bar
            progress = st.progress(0)

            for i in range(100):
                progress.progress(i + 1)

            progress.empty()

            st.success(f"Recommendations based on **{selected_movie}** 🍿")

            st.markdown(f"""
### 📌 Recommendation Summary

🎬 **Selected Movie:** {selected_movie}

🤖 **Recommendation Algorithm:** Cosine Similarity

📊 **Movies Recommended:** 5
""")

            st.markdown(
                "<h2 style='color:white;'>🎬 Recommended Movies</h2>",
                unsafe_allow_html=True
            )

            recommendations = similarity_scores[1:6]

            col1, col2 = st.columns(2)

            for idx, movie in enumerate(recommendations):

                movie_name = get_movie_name(movie[0])

                card = f"""
<div class="movie-card">

<h3>🎬 {movie_name}</h3>

<p style="color:#E50914;font-weight:bold;">
⭐ Recommendation #{idx+1}
</p>

<p style="color:#DDDDDD;">
Recommended because it shares similar genres, cast, crew and storyline with your selected movie.
</p>

</div>
"""

                if idx % 2 == 0:
                    with col1:
                        st.markdown(card, unsafe_allow_html=True)
                else:
                    with col2:
                        st.markdown(card, unsafe_allow_html=True)


st.markdown("---")

st.markdown("""

<div class="footer">

<h2>🎬 Movie Recommendation System</h2>

<p>

Developed using

Python • Streamlit • NLP • Scikit-Learn • Cosine Similarity

</p>

<p>

Made with ❤️ by Sejal Patole

</p>

</div>

""", unsafe_allow_html=True)

# python -m streamlit run app1.py