import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# LOAD DATASET

df = pd.read_csv(
    "data/career_recommender.csv"
)

df.fillna("", inplace=True)


# TARGET COLUMN

career_column = (
"If yes, then what is/was your first Job title in your current field of work? If not applicable, write NA.               "
)


# CREATE PROFILE

df["profile"] = (

df["What was your course in UG?"].astype(str)

+ " "

+ df[
"What is your UG specialization? Major Subject (Eg; Mathematics)"
].astype(str)

+ " "

+ df[
"What are your interests?"
].astype(str)

+ " "

+ df[
"What are your skills ? (Select multiple if necessary)"
].astype(str)

+ " "

+ df[
"If yes, please specify your certificate course title."
].astype(str)

)


# REMOVE EMPTY CAREERS

df = df[
    df[career_column]
    .astype(str)
    .str.strip()
    .str.lower()
    != "na"
]

df = df[
    df[career_column]
    .astype(str)
    .str.strip()
    != ""
]


# TFIDF

vectorizer = TfidfVectorizer(
stop_words="english"
)

vectors = vectorizer.fit_transform(
df["profile"]
)


# REASON GENERATOR

def build_reason(profile):

    profile = profile.lower()

    reasons = []

    if "python" in profile:

        reasons.append(
        "Python skills detected"
        )

    if "machine learning" in profile:

        reasons.append(
        "Machine Learning experience matched"
        )

    if "data" in profile:

        reasons.append(
        "Data analytics background found"
        )

    if "cloud" in profile:

        reasons.append(
        "Cloud knowledge identified"
        )

    if len(reasons)==0:

        reasons.append(
        "General profile similarity"
        )

    return ", ".join(reasons)



# RECOMMENDER

def recommend_career(user_text):

    user_vector = vectorizer.transform(
        [user_text]
    )

    similarity = cosine_similarity(
        user_vector,
        vectors
    )[0]

    top = similarity.argsort()[-3:][::-1]

    recommendations = []

    for idx in top:

        career = str(
        df.iloc[idx][career_column]
        ).strip()

        profile = str(
        df.iloc[idx]["profile"]
        )

        reason = build_reason(
        profile
        )

        recommendations.append({

        "career":
        career,

        "score":
        round(
        similarity[idx]*100,
        2
        ),

        "reason":
        reason

        })

    return recommendations