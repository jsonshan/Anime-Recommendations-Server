import requests

recommend_anime_url = 'http://127.0.0.1:5000/recommend-anime'
recommend_anime_data = {
    'titles': ["Darling in the FranXX", "One Piece", "Magi"],
    'num_recommendations': 5
}

response = requests.post(recommend_anime_url, json=recommend_anime_data)
print(f"Status code: {response.status_code}")

if response.status_code == 200:
    response_json = response.json()
    print("Response content:")
    print(f"Codes: {response_json.get('codes')}")
else:
    print(f"Error: {response.text}")
