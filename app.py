from flask import Flask, render_template, request

app = Flask(__name__)

def get_pins():
    pins = [
        {
            'image': '/static/images/paws.jpg',
            'caption': 'Paws',
            'avatar': '/static/images/android_boy.jpg',
            'name': 'Dwayne Stewart',
            'category': 'Latte Art'
        },

        {
            'image': '/static/images/paws.jpg',
            'caption': 'Paws',
            'avatar': '/static/images/android_boy.jpg',
            'name': 'Dwayne Stewart',
            'category': 'Latte Art'
        },

        {
            'image': '/static/images/pretty.jpg',
            'caption': "Is this a swan? Whatever - it's pretty!",
            'avatar': '/static/images/woman_italy.jpg',
            'name': 'Nuria Cohen',
            'category': 'Love My Latte'
        },
        {
            'image': '/static/images/paws.jpg',
            'caption': 'Paws',
            'avatar': '/static/images/android_boy.jpg',
            'name': 'Dwayne Stewart',
            'category': 'Latte Art'
        },

        {
            'image': '/static/images/paws.jpg',
            'caption': 'Paws',
            'avatar': '/static/images/android_boy.jpg',
            'name': 'Dwayne Stewart',
            'category': 'Latte Art'
        },

        {
            'image': '/static/images/pretty.jpg',
            'caption': "Is this a swan? Whatever - it's pretty!",
            'avatar': '/static/images/woman_italy.jpg',
            'name': 'Nuria Cohen',
            'category': 'Love My Latte'
        },
        {
            'image': '/static/images/paws.jpg',
            'caption': 'Paws',
            'avatar': '/static/images/android_boy.jpg',
            'name': 'Dwayne Stewart',
            'category': 'Latte Art'
        },

        {
            'image': '/static/images/paws.jpg',
            'caption': 'Paws',
            'avatar': '/static/images/android_boy.jpg',
            'name': 'Dwayne Stewart',
            'category': 'Latte Art'
        },

        {
            'image': '/static/images/pretty.jpg',
            'caption': "Is this a swan? Whatever - it's pretty!",
            'avatar': '/static/images/woman_italy.jpg',
            'name': 'Nuria Cohen',
            'category': 'Love My Latte'
        },
        {
            'image': '/static/images/paws.jpg',
            'caption': 'Paws',
            'avatar': '/static/images/android_boy.jpg',
            'name': 'Dwayne Stewart',
            'category': 'Latte Art'
        },

        {
            'image': '/static/images/paws.jpg',
            'caption': 'Paws',
            'avatar': '/static/images/android_boy.jpg',
            'name': 'Dwayne Stewart',
            'category': 'Latte Art'
        },

        {
            'image': '/static/images/pretty.jpg',
            'caption': "Is this a swan? Whatever - it's pretty!",
            'avatar': '/static/images/woman_italy.jpg',
            'name': 'Nuria Cohen',
            'category': 'Love My Latte'
        },
        {
            'image': '/static/images/paws.jpg',
            'caption': 'Paws',
            'avatar': '/static/images/android_boy.jpg',
            'name': 'Dwayne Stewart',
            'category': 'Latte Art'
        },

        {
            'image': '/static/images/paws.jpg',
            'caption': 'Paws',
            'avatar': '/static/images/android_boy.jpg',
            'name': 'Dwayne Stewart',
            'category': 'Latte Art'
        },

        {
            'image': '/static/images/pretty.jpg',
            'caption': "Is this a swan? Whatever - it's pretty!",
            'avatar': '/static/images/woman_italy.jpg',
            'name': 'Nuria Cohen',
            'category': 'Love My Latte'
        },
        {
            'image': '/static/images/paws.jpg',
            'caption': 'Paws',
            'avatar': '/static/images/android_boy.jpg',
            'name': 'Dwayne Stewart',
            'category': 'Latte Art'
        },

        {
            'image': '/static/images/paws.jpg',
            'caption': 'Paws',
            'avatar': '/static/images/android_boy.jpg',
            'name': 'Dwayne Stewart',
            'category': 'Latte Art'
        },

        {
            'image': '/static/images/pretty.jpg',
            'caption': "Is this a swan? Whatever - it's pretty!",
            'avatar': '/static/images/woman_italy.jpg',
            'name': 'Nuria Cohen',
            'category': 'Love My Latte'
        },
        {
            'image': '/static/images/paws.jpg',
            'caption': 'Paws',
            'avatar': '/static/images/android_boy.jpg',
            'name': 'Dwayne Stewart',
            'category': 'Latte Art'
        },

        {
            'image': '/static/images/paws.jpg',
            'caption': 'Paws',
            'avatar': '/static/images/android_boy.jpg',
            'name': 'Dwayne Stewart',
            'category': 'Latte Art'
        },

        {
            'image': '/static/images/pretty.jpg',
            'caption': "Is this a swan? Whatever - it's pretty!",
            'avatar': '/static/images/woman_italy.jpg',
            'name': 'Nuria Cohen',
            'category': 'Love My Latte'
        },
        {
            'image': '/static/images/paws.jpg',
            'caption': 'Paws',
            'avatar': '/static/images/android_boy.jpg',
            'name': 'Dwayne Stewart',
            'category': 'Latte Art'
        },
        
        {
            'image': '/static/images/paws.jpg',
            'caption': 'Paws',
            'avatar': '/static/images/android_boy.jpg',
            'name': 'Dwayne Stewart',
            'category': 'Latte Art'
        },

        {
            'image': '/static/images/pretty.jpg',
            'caption': "Is this a swan? Whatever - it's pretty!",
            'avatar': '/static/images/woman_italy.jpg',
            'name': 'Nuria Cohen',
            'category': 'Love My Latte'
        },
    ]
    return pins

@app.route('/')
def index():
    pins = get_pins()
    print pins
    total_pins = len(pins)
    name = "guest"
    return render_template('index.html', name=name, pins=pins, total_pins=total_pins )

# filtering pins by name in the app (should use template loop to get pins filtered on flask app)
# @app.route('/<name>')
# def index_name(name):
#     lower_name = name.lower()
#     filtered_pins = []
#     pins = get_pins()
#     for pin in pins:
#         print pin
#         if (pin["name"].lower()).startswith(lower_name):
#             print pin["name"]
#             filtered_pins.append(pin)
#     print filtered_pins
#     return render_template('index.html', name=name, pins=filtered_pins)


# filtering pins by name in the template (should use the templates's own loop to filter pins)
# @app.route('/<name>')
# def index_name(name):
#     lower_name = name.lower()
#     pins = get_pins()
#     return render_template('index.html', name=lower_name, pins=pins)


# search bar (should use temaplate's loop to get pins filtered on flask app)
@app.route('/search', methods=['POST'])
def my_search():
    print request.form
    term = request.form.getlist('term')
    lower_term = term[0].lower()
    print lower_term
    pins = get_pins()
    filtered_pins = []
    for pin in pins:
        if lower_term in pin["category"].lower() or lower_term in pin["caption"].lower():
            filtered_pins.append(pin)
    return render_template('search.html', name="guest", pins=filtered_pins )

if __name__=='__main__':
    app.run(debug=True)
