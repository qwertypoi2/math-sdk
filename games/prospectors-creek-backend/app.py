cat << 'EOF' > app.py
from flask import Flask, jsonify
from logic import SlotMachine

app = Flask(__name__)
game_engine = SlotMachine()

@app.route('/api/v1/spin', methods=['GET'])
def spin():
    try:
        result = game_engine.play_round()
        return jsonify({"status": "success", "data": result}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
EOF