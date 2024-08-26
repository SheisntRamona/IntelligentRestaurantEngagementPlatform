import openai

# Initialize the OpenAI API client
openai.api_key = 'your_openai_api_key'

def generate_about_us_section(restaurant_name, cuisine_type, location, unique_features):
    """
    Generates an "About Us" section for a restaurant.
    
    Parameters:
    - restaurant_name: Name of the restaurant
    - cuisine_type: Type of cuisine the restaurant serves
    - location: Location of the restaurant
    - unique_features: Any unique features or selling points of the restaurant
    
    Returns:
    - A generated "About Us" section text.
    """
    
    prompt = (
        f"Write a brief 'About Us' section for a restaurant named {restaurant_name} that serves {cuisine_type} cuisine. "
        f"The restaurant is located in {location}. "
        f"Some of its unique features include {unique_features}. "
        "Make it engaging and suitable for marketing purposes."
    )
    
    response = openai.Completion.create(
        engine="text-davinci-003",  # or another engine of your choice
        prompt=prompt,
        max_tokens=150,  # Adjust the length as needed
        n=1,
        stop=None,
        temperature=0.7  # Adjust creativity level
    )
    
    about_us_text = response.choices[0].text.strip()
    return about_us_text

# Example usage
restaurant_name = "Sunset Bistro"
cuisine_type = "Mediterranean"
location = "Santa Monica, California"
unique_features = "a beautiful ocean view, locally-sourced ingredients, and a cozy atmosphere"

about_us_section = generate_about_us_section(restaurant_name, cuisine_type, location, unique_features)

print("Generated About Us Section:")
print(about_us_section)
