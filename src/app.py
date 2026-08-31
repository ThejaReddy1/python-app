# '/api/v1/details'
# '/api/v1/healthz'

from flask import Flask, jsonify
import datetime, socket, os

app = Flask(__name__)

@app.route('/api/v1/info', methods=['GET'])
def get_info():
    return jsonify( {
        'hostname': socket.gethostname(),
        'timestamp': datetime.datetime.now().strftime("%I:%M:%S %p on %B %d, %Y"),
        'version': '1.0.0',
        'message': 'You are doing great, human! 😁👍',
        'description': 'This is a simple Flask application that provides information about the server and its health status. It has two endpoints: one for retrieving server details and another for checking the health of the application.',
        'deployed_on': 'kubernetes',
    }), 200

@app.route('/api/v1/healthz', methods=['GET'])
def health_check():
    return jsonify( {
        'status': 'healthy',
        'timestamp': datetime.datetime.now().strftime("%I:%M%S %p on %B %d, %Y"),
    }), 200
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT', 5000))
