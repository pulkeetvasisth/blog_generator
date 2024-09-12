from flask import Flask, request, render_template
import os
import google.generativeai as genai
import markdown  # Import markdown module

genai.configure(api_key="AIzaSyBceE5cBHfv3BLen-knd0cIX4_vgtJa46A")

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
)

chat_session = model.start_chat(history=[])

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    user_prompt = request.form['prompt']
    style = request.form['style']
    language = request.form['language']
    prompt = f"make a blog on {user_prompt} in a {style} way in {language} language"
    
    # Generate content using model
    response = model.generate_content(prompt, stream=True)
    markdown_text = ""
    
    # Collect chunks of text from the response
    for chunk in response:
        markdown_text += chunk.text

    # Convert markdown to HTML
    html_content = markdown.markdown(markdown_text)

    return render_template("index.html", text=html_content)

@app.route('/')
def form():
    return render_template('index.html')  # This renders the HTML form

if __name__ == '__main__':
    app.run(debug=True)
