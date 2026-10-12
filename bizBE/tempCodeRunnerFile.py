
# Ensure Flask is installed in your environment


# Ensure Flask is installed in your environment before running this script


from flask import Flask, make_response, jsonify # type: ignore


app = Flask(__name__)

businesses = [
    {
        'id': 1,
        'name': 'Rabbani',
        'town': 'Dhaka',
        'rating': 4.5,
        'reviews': []
    },
    {
        'id': 2,
        'name': 'Al Barakha',
        'town': 'Dhaka',
        'rating': 4.5,
        'reviews': []
    },
    {
        'id': 3,
        'name': 'Shaheen',
        'town': 'Dhaka',
        'rating': 4.5,
        'reviews': []
    }
]  # Initialize a list to store businesses

#this is a welcome route
@app.route('/',methods=['GET'])
def index():
    return make_response("Welcome to bizBE!", 200)

@app.route('/api/v1.0/businesses', methods=['GET'])
def show_all_businesses():
    return make_response(jsonify(businesses), 200)

#fetch a specific data
@app.route('/api/v1.0/businesses/<int:biz_id>', methods=['GET'])
def show_one_business(biz_id):
    data_to_return = [
        business for business in businesses
        if business['id'] == biz_id
    ]

    return make_response(jsonify(data_to_return[0]), 200)
    #if data_to_return:
        #return make_response(jsonify(data_to_return[0]), 200)
    #else:
        #return make_response(jsonify({"error": "Business not found"}), 404)

    # for biz in businesses:
    #     if biz['id'] == biz_id:
    #         return make_response(jsonify(biz), 200)
    #     else:
    #         return make_response(jsonify({"error": "Business not found"}), 404)

@app.route('/api/v1.0/businesses', methods=['POST'])
def add_business():
    next_id = businesses ['-id']+ 1

    new_business = {
        'id': next_id,
        'name': request.form['name'],
        'town': request.form['town'],
        'rating': request.corm['rating'],
        'reviews': []
    }

    businesses.append(new_business)

    return make_response(jsonify(new_business), 201)
   

if __name__ == '__main__':
    app.run(debug=True)