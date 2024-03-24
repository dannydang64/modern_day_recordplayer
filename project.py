import serial
import pygame
import time
import queue
from pynput import keyboard

# Replace '/dev/cu.usbmodemXXXX' with the appropriate serial port of your Arduino
arduino_port = 'COM3'
baud_rate = 9600

daqueue = queue.Queue()
pygame.mixer.init()
pygame.mixer.set_num_channels(20)

class AudioPlayer:
    def __init__(self, file_path, num):
        self.file_path = file_path
        self.is_playing = False
        self.chaNum = num

    def activate(self):
        if not self.is_playing:
            channel = pygame.mixer.Channel(self.chaNum)
            channel.play(pygame.mixer.Sound(self.file_path), loops=-1)

            self.is_playing = True
        else:
            channel.stop()
            self.is_playing = False


sound1 = AudioPlayer('C:\\Users\\dangd\\Downloads\\kiss-[AudioTrimmer.com] (1).mp3', 1)
sound2 = AudioPlayer('C:\\Users\\dangd\\OneDrive\\Desktop\\build\BeatDrop-trimmed.mp3', 2)
sound3 = AudioPlayer('C:\\Users\\dangd\\OneDrive\\Desktop\\build\\stillwooz.mp3', 3)
sound4 = AudioPlayer('C:\\Users\\dangd\\OneDrive\\Desktop\\build\\IMG_0 (8).mp3', 4)
sound5 = AudioPlayer('C:\\Users\\dangd\\OneDrive\\Desktop\\build\\IMG_0 (9).mp3', 5)
sound6 = AudioPlayer('C:\\Users\\dangd\\OneDrive\\Desktop\\build\\edmdrums.mp3', 6)
sound7 = AudioPlayer('C:\\Users\\dangd\\OneDrive\\Desktop\\build\\Nujabes Drums (Farrel)-[AudioTrimmer.com].mp3', 7)
sound8 = AudioPlayer('C:\\Users\\dangd\\OneDrive\\Desktop\\build\yenastraw.mp3', 8 )
sound9 = AudioPlayer('C:\\Users\\dangd\\OneDrive\\Desktop\\build\Buildup-trimmed.mp3', 9)
sound10 = AudioPlayer('C:\\Users\\dangd\\OneDrive\\Desktop\\build\EDM Vocals-[AudioTrimmer.com].mp3', 10)
sound11 = AudioPlayer('C:\\Users\\dangd\\OneDrive\\Desktop\\build\\IMG_0 (15).mp3', 11)
sound12 = AudioPlayer('C:\\Users\\dangd\\OneDrive\\Desktop\\build\\IMG_0 (16).mp3', 12)
sound14 = AudioPlayer('C:\\Users\\dangd\\OneDrive\\Desktop\\build\\hotandcold.mp3',14)
time = 0

def play_mp3(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
def increment():
    global time
    time = time + 1
    if(time == 5):
        time = 1
    print(time)
try:
    # Connect to Arduino
    arduino = serial.Serial(arduino_port, baud_rate, timeout=1)

    while True:
        # Read serial data from Arduino
        data = arduino.readline().decode().strip()
        print(data)
        if data == 'd36c3704': 
            increment()
            daqueue.put('0')
            print('0')
        elif data == '99043904': 
            increment()
            daqueue.put('1')
            print('1')
        elif data == 'b19b3804': 
            increment()
            daqueue.put('2')
            print('2')
        elif data == '74093704': 
            increment()
            daqueue.put('3')
            print('3')
        elif data == 'b34a3804': 
            increment()
            daqueue.put('14')
            print('14')
        elif data == 'd2943904': 
            increment()
            daqueue.put('5')
            print('5')
        elif data == '2be63804': 
            increment()
            daqueue.put('6')
            print('6')
        elif data == '59043904': 
            increment()
            daqueue.put('7')
            print('7')
        elif data == '2f6f3804': 
            increment()
            daqueue.put('8')
            print('8')
        elif data == 'decd3704': 
            increment()
            daqueue.put('9')
            print('9')
        elif data == 'b5843804': 
            increment()
            daqueue.put('a')
            print('a')
        else:
            increment()

        if (time == 1 and daqueue.qsize() > 0):
            val = daqueue.get()
            if(val == '0'):
                #sound0.activate()
                print('sound')
            elif(val == '1'):
                sound1.activate()
            elif(val == '2'):
                sound2.activate()
            elif(val == '3'):
                sound3.activate()
            elif(val == '14'):
                sound14.activate()
            elif(val == '5'):
                sound5.activate()
            elif(val == '6'):
                sound6.activate()
            elif(val == '7'):
                sound7.activate()
            elif(val == '8'):
                sound8.activate()
            elif(val == '9'):
                sound9.activate()
            elif(val == 'a'):
                sound10.activate()
            elif(val == 'b'):
                sound11.activate()
            elif(val == 'c'):
                sound12.activate()
            
                

except serial.SerialException as e:
    print("Error: Failed to connect to Arduino.")