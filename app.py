from flask import Flask, make_response, jsonify, render_template, redirect

app = Flask(__name__, static_url_path="")

@app.route('/', methods=['GET'])
def root():
    return redirect('/home')

@app.route('/home', methods=['GET'])
def home_page():
    return render_template('index.html')

@app.errorhandler(404)
def not_found(error):
    """ 404 page route.

    get:
        description: Endpoint to return a not found 404 page.
        responses: Returns 404 object.
    """
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)