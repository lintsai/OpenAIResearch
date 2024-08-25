from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

openai.api_key = "你的API密鑰"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    prompt = data.get("prompt")
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # 使用新的模型名稱
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    reply = response['choices'][0]['message']['content']
    return jsonify(reply)

if __name__ == '__main__':
    app.run(debug=True)