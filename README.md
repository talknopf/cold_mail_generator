# Cold Mail generator

This is a Flask application that generates a cold email using the ```davinci text 003``` model. 
The email is generated based on a target URL and an origin URL provided by the user.

## Prerequisites
Before running the application, make sure you have the following installed:
- Python 3
- Flask
- OpenAI Python library
- requests library
- BeautifulSoup library

## Installation
1. Clone the repository or download the code files.
2. Install the required libraries using the following command:
```bash
pip install -r requirements.txt

```

## Configuration
To use the OpenAI API, you need to set your API key in the code. Replace `"YOUR_API_KEY"` with your actual OpenAI API key.

## Usage
1. Start the application by running the following command:
```bash
python ./email_api.py
```
2. Open a web browser and navigate to `http://localhost:5000`.
3. The home page will be displayed, and you can enter the target URL and origin URL in the provided input fields.
4. Click the "Generate Email" button to generate the cold email.
5. The generated email will be displayed on a new page.

Note: The target URL and origin URL should be valid URLs that contain the web content you want to use for generating the email.

## Important Notes
- This code assumes you have a basic understanding of Flask and web development.
- Make sure to handle error cases and perform input validation as needed.
- The OpenAI GPT-3.5 model is used to generate the email. You may need to have appropriate access and resources from OpenAI to use this model.

## License
[MIT License](LICENSE)

