from flask import Flask, request, render_template
from Database_setup import db, setup_database, Restaurant
from Text_Generation import generate_about_us, generate_restaurant_description

app = Flask(__name__)
setup_database(app)

# Route for generating the "About Us" section
@app.route('/about_us', methods=['GET', 'POST'])
def about_us():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        cuisine_type = request.form['cuisine_type']
        history = request.form.get('history', '')
        ambiance = request.form.get('ambiance', '')
        special_features = request.form.get('special_features', '')

        # Generate About Us text
        about_us = generate_about_us(name, location, cuisine_type, history, ambiance, special_features)

        # Save to database
        new_restaurant = Restaurant(name=name, location=location, cuisine_type=cuisine_type, about_us=about_us)
        db.session.add(new_restaurant)
        db.session.commit()

        return render_template('Results.html', about_us=about_us)
    
    return render_template('about_us.html')

# Route for generating the restaurant description
@app.route('/description', methods=['GET', 'POST'])
def description():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        cuisine_type = request.form['cuisine_type']
        ambiance = request.form.get('ambiance', '')
        special_features = request.form.get('special_features', '')

        # Generate restaurant description
        description = generate_restaurant_description(name, location, cuisine_type, ambiance, special_features)

        # Save to database
        new_restaurant = Restaurant(name=name, location=location, cuisine_type=cuisine_type, description=description)
        db.session.add(new_restaurant)
        db.session.commit()

        return render_template('Results.html', description=description)
    
    return render_template('description.html')

if __name__ == '__main__':
    app.run(debug=True)
