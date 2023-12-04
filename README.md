# Culinary Connoisseur: A Dual-Project Exploration

## Overview

Our project's narrative is a tale of adaptation and skillful application of knowledge, both from academic settings and self-initiated learning. We embarked on two separate projects within the culinary realm to demonstrate our comprehensive understanding and ability to pivot when necessary.

### Why Two Projects?

We chose to develop two projects to showcase our expertise gained in the classroom and through independent exploration. Initially, our objective was to create a Recipe Suggestions Chatbot using deep learning techniques. However, we encountered challenges that led us to reconsider our approach. To stay true to our original vision while adapting to these challenges, we decided to split our efforts into two applications:

1. *Recipe Suggestions Chatbot using API*: This chatbot generates recipe suggestions based on user-input ingredients, showcasing our proficiency in API integration and chatbot development.
2. *Cuisine Predictor*: A deep learning-based application that predicts cuisines from ingredients, illustrating our problem-solving skills and ability to apply complex concepts.

## Applications

- *Recipe Suggestions Chatbot using API*: Engage with a chatbot that provides recipe suggestions, emphasizing practical API integration and user interaction.
- *Cuisine Predictor*: Employs a deep learning model to identify the cuisine of a dish from its ingredients, showcasing advanced machine learning techniques.

## Learning Outcomes

- Mastery of API usage for dynamic data retrieval and chatbot communication.
- Deployment of deep learning models for insightful data analysis and accurate predictions.
- Flexibility in project development and dedication to the initial project proposal.

## Technologies Used

- API Communication
- Chatbot Development
- Deep Learning (Neural Networks)
- Python Programming

## Getting Started for the Cuisine Predictor

# Hosting a Streamlit App Locally

This guide will walk you through the steps to host your Streamlit app on a local server.

## Prerequisites

Before you begin, ensure that you have Streamlit installed. If not, you can install it using pip:


pip install streamlit

Ensure you also download the 'app.py' file provided in the repository along with the imported joblib files and jpegs.

## Running Streamlit App

1. **Open Terminal or Command Prompt**: Navigate to the directory where your Streamlit app `.py` file is located.

2. **Run the App**: Execute the following command to start the app:


streamlit run app.py


By default, Streamlit will start a local server, and the app will be accessible at `http://localhost:8501`

## Firewall Settings

Ensure that your firewall settings allow incoming connections on the port you're using for your Streamlit app.

For more detailed instructions and advanced configurations, refer to the [Streamlit documentation](https://docs.streamlit.io).

---

# Getting Started For Recipe Suggestions Chatbot

## Overview

This chatbot utilizes the Edamam.com API to provide recipe suggestions based on user-input ingredients. The chatbot is built using Gradio, a Python library for creating user interfaces for machine learning models.

## Requirements

Ensure you have the following packages installed:

```bash
pip install requests
pip install gradio
pip install openai
```

## API Credentials

To run the application, you'll need API credentials from Edamam.com. Obtain your API key and app ID, and replace the placeholders in the `get_recipes_from_edamam` function.

```python
api_key = 'YOUR_EDAMAM_API_KEY'
app_id = 'YOUR_EDAMAM_APP_ID'
```

Run the code and open the link provided. The Recipe Suggestions Chatbot interface should be accessible.

Enter ingredients in the provided textbox and click the "Submit" button to get recipe suggestions.

## Demo of our applications
https://youtu.be/oorUiEu5HBQ 

