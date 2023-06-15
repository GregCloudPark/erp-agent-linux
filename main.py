
import json
import threading
from flask import Flask, request
from flask_cors import CORS

from recorder import Recorder

app = Flask(__name__) 
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


recorder = Recorder()

@app.route('/record', methods=['POST'])
def recording():
    body_data = request.get_json()
    is_audio_only = body_data.get('is_audio_only') or False # bool
    recording_id = body_data.get('recording_id') or '' # uuid
    action = body_data.get('action') or '' # 'start' or 'stop'
    phone_number = body_data.get('phone_number') or '' # 'start' or 'stop'
    meet_url = body_data['meet_url'] or '' 
    print('recording_id')


    if(action == ''):
        return json.dumps({'retorno':'Informe o campo action: "start" ou "stop"'}), 409
    
    if(recording_id == ''):
        return json.dumps({'retorno':'Informe o campo recording_id'}), 409

    if(is_audio_only and phone_number == ''):
        return json.dumps({'retorno':'Para gravar somente audio, informe o campo phone_number'}), 409

    if action == 'stop':
        recorder.stop_recording()
        print('parou de gravar')
        return json.dumps({'status': 'resting'}), 200 
    else:
        recorder.start_recording(recording_id=recording_id)
        print('começou a gravar')
        return json.dumps({'status': 'recording', 'recording_id': recording_id}), 200 



@app.route('/recordingTime', methods=['GET'])
def recording_time():

    if recorder.is_recording_flag.is_set():
        recording_time = recorder.get_recording_time_in_seconds()
        return json.dumps({
            'recording_id': recorder.recording_id,
            'recording_time_in_seconds': recording_time,
            'status': 'recording'
        }), 200
    else:
        return json.dumps({
            'recording_time_in_seconds': 0,
            'status': 'resting'
        }), 200

  


if __name__ == '__main__':

    # Start the Flask server
    app.run(port=5000, debug=True)


