import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

flag = True
df = pd.read_csv("college_faq.csv")
# print('file found')
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["Question"])

while flag == True:
    user_query = input('Question: ')

    if user_query.lower() == 'quit':
        flag = False

    elif user_query:
        user_vec = vectorizer.transform([user_query])
        print(type(user_vec))
        print(user_vec)
        similarity = cosine_similarity(user_vec, X)
        best_match = similarity.argmax()
        score = similarity[0][best_match]
        print('Answer: ', df['Answers'][best_match])
    else: 
        print('How can i help you?...')