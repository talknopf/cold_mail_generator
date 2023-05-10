from flask import Flask, render_template, request
import openai
import requests
from bs4 import BeautifulSoup


# Set up the OpenAI API key and model
openai.api_key = "YOUR_API_KEY"
model_engine = "text-davinci-003"


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
    prompt = f"Generate an intro email from an SDR of a professional services company named 2bcloud to a potential customer. \
    it should describe the services 2bcloud can offer which are found here:{service_text}. \
    The customer's webpage content is here: {target_text} \
    The email should demonstrate the fact we researched the customer and we can help augment the internal teams"
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
    app.run(debug=True)