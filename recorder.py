


import threading
import time


class Recorder():

    is_recording_flag = threading.Event()
    recording_initial_time = 0
    recording_id = 0
    # def __init__(self):


    def start_recording(self, recording_id):
        self.recording_id = recording_id
        self.is_recording_flag.set()
        self.recording_initial_time = int(time.time())
        threading.Thread(target=self.recording_function).start()

    def stop_recording(self):     
        self.is_recording_flag.clear()

    def recording_function(self):

        while True:
            print('recording')
            if( not self.is_recording_flag.is_set()):
                break

    def get_recording_time_in_seconds(self):
        recording_time = int(time.time()) - self.recording_initial_time 
        return recording_time
    
