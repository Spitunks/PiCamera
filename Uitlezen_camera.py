from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.exposure_mode = 'antishake'
camera.resolution = (595, 842)
#camera.rotation = 180
camera.start_preview()
sleep(5)
camera.capture('D:/tlooy/Documents/Tuur/School Tuur/Ku_Leuven/3ICT/bachelorproef/Dobot/image.jpg')
camera.stop_preview()
