# Project 3: AI Recommendation Logic — Tech Stack Recommender

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# 1. INPUT: Job roles dataset (acts as raw_skills.csv)
# Each role is a "document" made of its required skills
job_roles = {
    "Data Scientist": "Python SQL Machine Learning Data Analysis Statistics",
    "DevOps Engineer": "AWS Docker Kubernetes CI CD Automation Cloud",
    "Backend Developer": "Java Python SQL APIs Databases Git",
    "Cloud Architect": "AWS Cloud Computing Automation Kubernetes Security",
    "Sys Admin": "Linux Networking Automation Cloud Monitoring",
    "ML Engineer": "Python Machine Learning TensorFlow Data Structures Algorithms"
}

roles = list(job_roles.keys())
descriptions = list(job_roles.values())

# 2. Take user input (minimum 3 skills, per project requirement)
user_skills = ["Python", "Cloud Computing", "Automation"]
user_profile = " ".join(user_skills)

# 3. PROCESS: Vectorize everything into the SAME vocabulary space (TF-IDF)
documents = descriptions + [user_profile]   # last item = user vector
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# Split back out: job vectors vs user vector
job_vectors = tfidf_matrix[:-1]
user_vector = tfidf_matrix[-1]

# 4. Scoring: Cosine Similarity (angle-based, not magnitude-based)
scores = cosine_similarity(user_vector, job_vectors).flatten()

# 5. OUTPUT: Sort + Filter (Top-N list)
results = pd.DataFrame({"Role": roles, "Match Score": scores})
results = results.sort_values(by="Match Score", ascending=False).reset_index(drop=True)

top_n = 3
print("Top", top_n, "Recommended Career Paths:\n")
print(results.head(top_n).to_string(index=False))