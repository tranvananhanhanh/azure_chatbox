# Import necessary modules
from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from quickstart import client
from flask_cors import cross_origin
from flask import Flask, render_template, request
from voice import text_to_speech




# Load environment variables
load_dotenv()


# Create Flask app
app = Flask(__name__)


# Print the OpenAI API key for debugging purposes
print(client.api_key)

# Define the route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Define the route for handling user input and providing responses
@app.route('/get_response', methods=['POST'])
def get_response():
    # Get user input from the form
    user_input = request.form['user_input']

    # Use OpenAI's Chat API for completions
    response = client.chat.completions.create(
        model="GPT35TURBO16K",
        messages=[
            {"role": "system", "content": "bạn là giáo viên toán"},
            {"role": "user", "content": user_input},
        ]
    
    )
    print(response.choices[0].message.content)
    # Check the console output for the structure of the response
   

    try:
        # Access the content based on the new structure
        response_content =response.choices[0].message.content
        return jsonify({'response': str(response_content)}) 
    except TypeError as e:
        # Handle the error and provide a meaningful response
        print(f"Error: {e}")
        return jsonify({'response': 'Error in processing the response'})

cross_origin()
@app.route('/text_to_speech', methods=['POST', 'GET'])
def text_to_speech_route():
    if request.method == 'POST':
        text = request.form['speech']
        gender = 'male'
        rate = 200
        volum = 0.1
        text_to_speech(text, gender, rate, volum)
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'error', 'message': 'Invalid request method'})

# Run the app if the script is executed
if __name__ == '__main__':
    app.run(debug=True,port=1700)
