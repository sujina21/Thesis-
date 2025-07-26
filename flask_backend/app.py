import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load vectorizer
with open('tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Load services dataframe
services_df = pd.read_pickle('services_df.pkl')


from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/user/recommend', methods=['POST'])
def recommend():
    print(" ========>  Received request for recommendations")
    data = request.get_json()

    user_searches = data['searchHistory']
    user_purchases = [p['serviceName'] for p in data['purchaseHistory']]
    
    # Build user profile text (same logic as your Colab build_user_profile)
    profile_text = " ".join(user_searches) + " " + " ".join(user_purchases)
    
    # Transform using loaded vectorizer
    user_vec = vectorizer.transform([profile_text])
    
    # Transform service descriptions again (if not saved pre-transformed)
    service_vecs = vectorizer.transform(services_df['description'])
    
    # Calculate similarity
    sim_scores = cosine_similarity(user_vec, service_vecs)[0]
    
    # Get top recommendations
    service_indices = sim_scores.argsort()[::-1]
    top_services = services_df.iloc[service_indices][:10]
    top_services = top_services.copy()
    top_services['similarity'] = sim_scores[service_indices][:10]
    
    # Convert to JSON serializable
    result = top_services[['serviceId', 'title', 'serviceType', 'similarity']].to_dict(orient='records')
    return jsonify({"data": result})

if __name__ == '__main__':
    app.run(debug=True)
