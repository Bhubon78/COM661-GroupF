
# Ensure Flask is installed in your environment


# Ensure Flask is installed in your environment before running this script


from flask import Flask, make_response, jsonify, request # type: ignore
from pymongo import MongoClient
from bson import ObjectId


app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client.bizBE
businesses = db.biz
# Use a collection named 'businesses' in the 'bizBE' database

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
    page_num,page_size =1,10
    
    if request.args.get('pn'):
        page_num = int(request.args.get('pn'))  
    
    if request.args.get('ps'):
        page_size = int(request.args.get('ps'))
    
    page_start = (page_size *(page_num-1))

    data_to_return = []

    for business in businesses.find().skip(page_start).limit(page_size):
        business['_id'] = str(business['_id']) 

        #for review in business['reviews']:
            #review['_id'] = str(review['_id'])
        
        data_to_return.append(business)

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
    next_id = businesses [-1]["id"]+ 1

    new_business = {
        'id': next_id,
        'name': request.form['name'],
        'town': request.form['town'],
        'rating': request.form['rating'],
        'reviews': []
    }

    businesses.append(new_business)

    return make_response(jsonify(new_business), 201)

# Uncomment or complete the route if needed, or remove it if unnecessary
@app.route('/api/v1.0/businesses/<int:biz_id>', methods=['PUT'])
def edit_business(biz_id):
    for business in businesses:
        if business['id'] == biz_id:
            business['name'] = request.form['name']
            business['town'] = request.form['town']
            business['rating'] = request.form['rating']

            break
        return make_response(jsonify(business), 200)
    #return make_response(jsonify({"error": "Business not found"}), 404)

@app.route('/api/v1.0/businesses/<int:biz_id>', methods=['DELETE'])
def delete_business(biz_id):
    for business in businesses:
        if business['id'] == biz_id:
            businesses.remove(business)
            break

    return make_response(jsonify({"message": "Business deleted successfully"}), 200)
    #return make_response(jsonify({"error": "Business not found"}), 404)

#============Reviews============

@app.route('/api/v1.0/businesses/<int:biz_id>/reviews', methods=['GET'])
def get_all_reviews(biz_id):
    for business in businesses:
        if business['id'] == biz_id:
            break

    return make_response(jsonify(business['reviews']), 200)
    #return make_response(jsonify({"error": "Business not found"}), 404)

@app.route('/api/v1.0/businesses/<int:biz_id>/reviews', methods=['POST'])
def add_new_review(biz_id):
    for business in businesses:
        if len(business['reviews']) == 0:
            next_review_id = 1
        else:
            next_review_id = business['reviews'][-1]['id'] + 1


        new_review = {
        'id': next_review_id,
        'username': request.form['username'],
        'comments': request.form['comments'],
        'stars': request.form['stars']
        }

        business['reviews'].append(new_review)
        break
    
    return make_response(jsonify(new_review), 201)

@app.route('/api/v1.0/businesses/<int:biz_id>/reviews/<int:rev_id>', methods=['GET'])
def fetch_one_review(biz_id, rev_id):
    for business in businesses:
        if business['id'] == biz_id:
            for review in business['reviews']:
                
                break
            break

    return make_response(jsonify(review), 200)
    #return make_response(jsonify({"error": "Business or Review not found"}), 404)

@app.route('/api/v1.0/businesses/<int:biz_id>/reviews/<int:rev_id>', methods=['PUT'])
def update_review(biz_id, rev_id):
    for business in businesses:
        if business['id'] == biz_id:
            for review in business['reviews']:
                if review['id'] == rev_id:
                    review['username'] = request.form['username']
                    review['comments'] = request.form['comments']
                    review['stars'] = request.form['stars']
                    break
            break

    return make_response(jsonify(review), 200)
    #return make_response(jsonify({"error": "Business or Review not found"}), 404)


@app.route('/api/v1.0/businesses/<int:biz_id>/reviews/<int:rev_id>', methods=['DELETE'])
def delete_review(biz_id, rev_id):
    for business in businesses:
        if business['id'] == biz_id:
            for review in business['reviews']:
                if review['id'] == rev_id:
                    business['review'].remove(review)
                   
                    break
            break

    return make_response(jsonify(review), 200)
    #return make_response(jsonify({"error": "Business or Review not found"}), 404)


if __name__ == '__main__':
    app.run(debug=True)