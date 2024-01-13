# Import necessary modules
from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from quickstart import client
from flask_cors import cross_origin
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

load_dotenv()

# Create Flask app


print(client.api_key)

# Define the route for the homepage
@app.route('/')
def index():
    return render_template('i2.html')

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


# Define the route for handling user input and providing responses
@app.route('/get_response_sum_up', methods=['POST'])
def get_response_sum_up():
    user_input = request.form['user_input']

    # Use OpenAI's GPT model for summarization
    response = client.chat.completions.create(
    model="GPT35TURBO16K",
    messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": 'find key words in this text : ' + user_input},],

)


    try:
        response_content =response.choices[0].message.content
        return jsonify({'response': response_content})
    except TypeError as e:
        print(f"Error: {e}")
        return jsonify({'response': 'Error in processing the response'})





# Run the app if the script is executed
if __name__ == '__main__':
    app.run(debug=True,port=1710)