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
        'message': 'You are doing great, human! 😁',
        'description': 'This is a sample API for demonstration purposes.'
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
