import streamlit as st
from keras.models import load_model
import joblib
from keras.preprocessing.sequence import pad_sequences

# Load model
model = load_model('my_model.h5')

# Load tokenizer and max length
tokenizer = joblib.load('tokenizer.joblib')
maxlen = joblib.load('preprocessing_config.joblib')['max_length']  # Ensure this is an integer

# Function to encode and pad sequences, similar to how you did during training
def preprocess_input(ingredients_list):
    # Convert list of ingredients to a string
    ingredients_text = ' '.join(ingredients_list)
    
    # Convert texts to sequences using the loaded tokenizer
    seq = tokenizer.texts_to_sequences([ingredients_text])
    
    # Pad the sequences using the loaded max length
    processed_input = pad_sequences(seq, maxlen=maxlen)
    
    return processed_input

# Function to get background image based on predicted cuisine
def get_background_image(predicted_cuisine):
    image_mapping = {
        'greek': 'greek.jpg',
        'southern_us': 'Sus.jpeg',
        'filipino': 'fil.jpg',
        'indian': "indian.jpg",
        'jamaican':"jam.jpg",
        'spanish':"span.jpg" , 
        'italian':"italian.jpg" , 
        'mexican': "mex.jpg",
        'chinese': "china.jpg", 
        'british': "bir.jpg", 
        'thai': "thai.jpg", 
        'vietnamese': "vit.jpg",
        'cajun_creole': "cc.jpg",
        'brazilian' : "bra.jpg",
        'french' : "french.jpg", 
        'japanese' : "jap.jpg",
        'irish': "irish.jpg", 
        'korean': "korean.jpg",
        'moroccan': "mo.jpg",
        'russian': "rus.jpg",
        'Unknown': 'unknown.jpg'  # Default image for unknown cuisine
    }
    return image_mapping.get(predicted_cuisine, 'unknown.jpg')

# Set the background image for the entire app
predicted_cuisine = 'Unknown'  # Default value
background_image = get_background_image(predicted_cuisine)
st.markdown(
    f"""
    <style>
        body {{
            background-image: url("{background_image}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit interface
st.title('Cuisine Predictor')

# Make the text more appealing
st.markdown(
    """
    Welcome to the Cuisine Predictor! Enter a list of ingredients below, and I'll predict the cuisine type.
    
    **Instructions:**
    - Enter ingredients separated by commas(e.g., tomato, basil, olive oil).
    - Click the 'Predict Cuisine' button to see the prediction.

    """
)
st.text('**Note:ENSURE SPELLINGS ARE CORRECT**')
# User input
input_ingredients = st.text_area('Enter ingredients separated by commas here (e.g., tomato, basil, olive oil):')


if st.button('Predict Cuisine'):
    # Convert input string to a list of ingredients
    ingredients_list = input_ingredients.split(',')
    
    # Preprocess the input
    processed_input = preprocess_input(ingredients_list)
    
    # Make prediction
    prediction = model.predict(processed_input)
    
    # Create a mapping from encoded labels to cuisine names
    # Replace with actual mapping
    cuisine_types = {6: 'greek', 16: 'southern_us', 4: 'filipino', 7: 'indian', 10: 'jamaican', 17: 'spanish', 9: 'italian', 13: 'mexican', 3: 'chinese', 1: 'british', 18: 'thai', 19: 'vietnamese', 2: 'cajun_creole', 0: 'brazilian', 5: 'french', 11: 'japanese', 8: 'irish', 12: 'korean', 14: 'moroccan', 15: 'russian'}
    
    # Get the predicted cuisine type
    predicted_cuisine = cuisine_types.get(prediction.argmax(axis=-1)[0], 'Unknown')
    st.write(f'Predicted Cuisine: {predicted_cuisine}')

    # Update background image based on predicted cuisine
    background_image = get_background_image(predicted_cuisine)
    st.image(background_image, use_column_width=True)

# Disclaimer
st.markdown(
    """
    **Disclaimer:**
    The predictions are based on the data the model was trained on and may not reflect all possible cuisine types or variations.
    The accuracy of the prediction may vary based on the input provided.
    """
)
