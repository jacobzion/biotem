from flask import Flask, request, jsonify
import openai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

openai.api_key = "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"  # Use free-tier key

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
