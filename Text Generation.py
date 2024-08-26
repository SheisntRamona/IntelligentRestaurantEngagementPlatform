def generate_about_us(name, location, cuisine_type):
    prompt = f"Write an 'About Us' section for a restaurant named {name}, located in {location}, serving {cuisine_type} cuisine."
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a marketing expert for restaurants."},
            {"role": "user", "content": prompt}
        ]
    )
    
    about_us_text = response.choices[0].message['content']
    return about_us_text
