from flask import Flask, render_template, request
import openai
import requests
from bs4 import BeautifulSoup
import os

# Set up the OpenAI API key and model
openai.api_key = os.getenv('OPENAI_API_KEY', 'missing')
model_engine = "text-davinci-003"

# setup variable listener port, deafault is 80
service_port = os.getenv('SERVICE_PORT', 80)

app = Flask(__name__)

# Define the home page route
@app.route('/')
def home():
    return render_template('index.html')

# Define the email generator route
@app.route('/generate-email', methods=['POST'])
def generate_email():
    # Get the target URL from the form input
    target_url = request.form.get('target_url')
    origin_url = request.form.get('origin_url')

    # Fetch the web content and extract the human-readable text
    response = requests.get(origin_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    service_text = soup.get_text()

    # Fetch the web content and extract the human-readable text
    response = requests.get(target_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    target_text = soup.get_text()

    # Generate the cold email using the OpenAI GPT-3.5 model
    prompt = f"Generate an intro email from a company providing serices as described here:{service_text}. \
    the intro email should demonstrate value to this to the company we can read of here: {target_text} \
    That will be our customer"
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=512,
        n=1,
        stop=None,
        temperature=0.5,
    )
    print(completions)
    # Extract the generated email from the OpenAI response
    # email = completions.choices[0].text.strip()
    email = completions.choices[0].text.strip()

    print(email)

    # Render the email on a new page
    return render_template('email.html', email=email)


# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=service_port)