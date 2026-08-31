# '/api/v1/details'
# '/api/v1/healthz'

from flask import Flask, jsonify
import datetime, socket, os

app = Flask(__name__)

@app.route('/api/v1/details', methods=['GET'])
def get_details():
    details = {
        'hostname': socket.gethostname(),
        'timestamp': datetime.datetime.now().strftime("%I:%M:%S %p on %B %d, %Y"),
        'version': '1.0.0',
        'message': 'You are doing great, human! 😁👍',
        'description': 'This is a simple Flask application that provides two API endpoints: /api/v1/details and /api/v1/healthz. The /api/v1/details endpoint returns information about the server, including the hostname, current timestamp, version, and a motivational message. The /api/v1/healthz endpoint returns the health status of the application along with the current timestamp.'
    }
    return jsonify(details)

@app.route('/api/v1/healthz', methods=['GET'])
def health_check():
    health_status = {
        'status': 'healthy',
        'timestamp': datetime.datetime.now().strftime("%I:%M%S %p on %B %d, %Y")
    }
    return jsonify(health_status), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT', 5000))
