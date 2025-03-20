from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# OpenAI API Key (Replace with your key)
openai.api_key = "your_openai_api_key"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    # AI response using OpenAI (ChatGPT)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You're an IT support bot for Jweconstructs.com."},
                  {"role": "user", "content": user_message}]
    )

    bot_reply = response["choices"][0]["message"]["content"]
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
