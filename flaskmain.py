from flask import Flask, jsonify
import host
app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(host.tat())

if __name__ == '__main__':
    host.main()
    app.run(debug=True)