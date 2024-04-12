from flask import Flask, make_response, jsonify, render_template, redirect

app = Flask(__name__, static_url_path="")

@app.route('/', methods=['GET'])
def root():
    return redirect('/index.html')

@app.route('/index.html', methods=['GET'])
def home_page():
    return render_template('index.html')

@app.route('/about-us.html', methods=['GET'])
def about_us():
    return render_template('about-us.html')

@app.route('/map.html', methods=['GET'])
def map():
    return render_template('map.html')

@app.route('/remote-control.html', methods=['GET'])
def remote_control():
    return render_template('remote-control.html')

@app.route('/user-guideline.html', methods=['GET'])
def user_guideline():
    return render_template('user-guideline.html')

@app.route('/sand-es-status.html', methods=['GET'])
def status():
    return render_template('sand-es-status.html')

@app.errorhandler(404)
def not_found(error):
    """ 404 page route.

    get:
        description: Endpoint to return a not found 404 page.
        responses: Returns 404 object.
    """
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)