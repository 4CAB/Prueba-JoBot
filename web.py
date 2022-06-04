from flask import Flask, request
import json

TOKEN = "5231646387:AAG1qWow9zgkit_TWtEV1Q_zEPdw7dBIVvw"

app = Flask(__name__)

@app.route('/' + "5231646387:AAG1qWow9zgkit_TWtEV1Q_zEPdw7dBIVvw", methods=['POST'])
def webhook():
    json_string = request.stream.read().decode('utf-8')
    update = Update.de_json(json.loads(json_string), bot)
    dp.process_update(update)
    return 'ok', 200

if __name__ == '__main__':
    app.run()