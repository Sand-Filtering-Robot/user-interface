# user-interface 

-- Running the app --
* Install requirements with "pip install -r requirements.txt"
* Run the app with "python app.py"
* Default runs on localhost:5000

-- Adding routes
* In app.py
    Add route decorator: @app.route('/path/to/handle', methods=['GET', 'POST', ...])
    Then add function underneath: def handler_function(): ...
    Return a redirect('/path/to/redirect') or a render_template('html_template_to_render.html')