import openai

# Function to generate "About Us" section
def generate_about_us(name, location, cuisine_type, history, ambiance, special_features):
    prompt = f"""
    Write an 'About Us' section for a restaurant named {name}, located in {location}, serving {cuisine_type} cuisine.
    The restaurant has the following history: {history}. The ambiance is described as {ambiance}. 
    Some unique features of the restaurant are: {special_features}.
    Make the description engaging and marketing-friendly.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a marketing expert for restaurants."},
            {"role": "user", "content": prompt}
        ]
    )
    
    about_us_text = response.choices[0].message['content']
    return about_us_text

# Function to generate full restaurant description
def generate_restaurant_description(name, location, cuisine_type, ambiance, special_features):
    prompt = f"""
    Create a full restaurant description for {name}, located in {location}, serving {cuisine_type} cuisine.
    The ambiance is described as {ambiance}, and the restaurant features: {special_features}.
    Make the description appealing and detailed for potential customers.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a restaurant marketing expert."},
            {"role": "user", "content": prompt}
        ]
    )
    
    description_text = response.choices[0].message['content']
    return description_text
