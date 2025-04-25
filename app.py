from flask import Flask, request, jsonify
import openai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

openai.api_key = openai.environ.get('OPENAI_API_KEY')  # Use free-tier key

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    question = data.get("question", "")

    prompt = f"You are a dental assistant helping with dental implants. Patient question: {question}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{ "role": "user", "content": prompt }]
    )

    answer = response['choices'][0]['message']['content']
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run()
