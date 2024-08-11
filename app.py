# from flask import Flask, request, jsonify
# from anime import recommend_anime, anime_data, cosine_sim

# app = Flask(__name__)

# @app.route('/recommend-anime', methods=['POST'])
# def recommend():
#     try:
#         data = request.json
#         print(f"Received data: {data}")  # Debugging statement to print received data
#         titles = data.get('titles')
#         print(f"Extracted titles: {titles}")  # Debugging statement to print extracted titles
#         num_recommendations = data.get('num_recommendations', 8)
#         print(f"Number of recommendations: {num_recommendations}")  # Debugging statement

#         if not titles:
#             print("No titles provided")
#             return jsonify({"error": "No titles provided"}), 400

#         final_indices = recommend_anime(
#             titles, cosine_sim, anime_data, num_recommendations
#         )
#         print(f"Final indices: {final_indices}")  # Debugging statement

#         if not final_indices:
#             print("No recommendations found")
#             return jsonify({"error": "No recommendations found"}), 404

#         recommended_codes = anime_data.iloc[final_indices]['code'].tolist()
#         print(f"Recommended codes: {recommended_codes}")  # Debugging statement
        
#         response = {
#             "codes": recommended_codes
#         }
#         return jsonify(response)
#     except Exception as e:
#         print(f"Error processing request: {e}")
#         return jsonify({"error": "Internal server error", "message": str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS
from anime import recommend_anime, anime_data, cosine_sim

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

@app.route('/recommend-anime', methods=['POST'])
def recommend():
    try:
        data = request.json
        print(f"Received data: {data}")  # Debugging statement to print received data
        titles = data.get('titles')
        print(f"Extracted titles: {titles}")  # Debugging statement to print extracted titles
        num_recommendations = data.get('num_recommendations', 10)
        print(f"Number of recommendations: {num_recommendations}")  # Debugging statement

        if not titles:
            print("No titles provided")
            return jsonify({"error": "No titles provided"}), 400

        final_indices = recommend_anime(
            titles, cosine_sim, anime_data, num_recommendations
        )
        print(f"Final indices: {final_indices}")  # Debugging statement

        if not final_indices:
            print("No recommendations found")
            return jsonify({"error": "No recommendations found"}), 404

        recommended_codes = anime_data.iloc[final_indices]['show_titles'].tolist()
        print(f"Recommended codes: {recommended_codes}")  # Debugging statement
        
        response = {
            "codes": recommended_codes
        }
        return jsonify(response)
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"error": "Internal server error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
