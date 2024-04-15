from flask import Flask, make_response, jsonify, render_template, redirect, request, jsonify
import motor_interface

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


# # Define a route to listen for POST requests for motor control
@app.route('/set-mode', methods=['POST'])
def set_mode():
    motor_interface.send_motor_command(motor_interface.Command.MANUAL, "")
    return redirect("/remote_control.html")
#     requested_mode = request.get_json().get('mode', None)
#     if requested_mode in ['autonomous', 'manual']:
#         control_mode = requested_mode
#         if requested_mode == 'manual':
#             driver.stop()  # Stop all motions when switching to remote control
#         return jsonify({'status': 'Mode set to ' + requested_mode}), 200
#     return jsonify({'error': 'Invalid mode requested'}), 400

@app.route('/motor-control', methods=['POST'])
def motor_control():
    motor_interface.send_motor_command(motor_interface.Command.LEFT, "")
    return redirect("/remote_control.html")
#     if control_mode != 'manual':
#         return jsonify({'error': 'Robot is not in remote control mode'}), 403

#     data = request.get_json()
#     direction = data.get('direction')
#     speed = data.get('speed', 0.2)  # Default speed
    
#     # Call the appropriate MotorDriver method based on the direction
#     if direction == 'up':
#         driver.forward(speed)
#         print(driver)
#     elif direction == 'down':
#         driver.backward(speed)
#         print(driver)
#     elif direction == 'left':
#         driver.left(speed)
#         print(driver)
#     elif direction == 'right':
#         driver.right(speed)
#         print(driver)
#     else:
#         return jsonify({'error': 'Invalid direction'}), 400

#     return jsonify({'status': 'Motor command executed'}), 200


if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)