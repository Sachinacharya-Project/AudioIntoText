from speech_recognition import Recognizer, AudioFile
from pydub import AudioSegment
def converter(data):
    src = data
    destination = str(data).split('.')[0]+'.wav'
    sound = AudioSegment.from_mp3(src)
    sound.export(destination, format='wav')
    return destination

def start(data):
    if data.endswith('.wav'):
        data = converter(data)
    else:
        print("Need Conversion")
    r = Recognizer()
    with AudioFile(data) as source:
        audio = r.listen(source)
        print("Status: Working\r", end="")
        query = r.recognize_google(audio)
        file = open("{}.txt".format(data.split('.')[0]), 'w')
        file.write(query)
        file.close()
        print(query)
if __name__ == '__main__':
    data = input("Enter AudioFile Name: ")
    start(data)