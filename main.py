import sys
from api_comms import *

filename = sys.argv[1]


audio_url = upload(filename)
save_transcript(audio_url, filename)