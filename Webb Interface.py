@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        cuisine_type = request.form['cuisine_type']

        # Generate About Us text
        about_us = generate_about_us(name, location, cuisine_type)

        # Save to database
        new_restaurant = Restaurant(name=name, location=location, cuisine_type=cuisine_type, about_us=about_us)
        db.session.add(new_restaurant)
        db.session.commit()

        return render_template('result.html', about_us=about_us)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
