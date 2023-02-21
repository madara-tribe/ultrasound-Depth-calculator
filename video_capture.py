import cv2
from ultrasound_Sensor import SensorDist
import time

def sensor_dist(sensor):
    distance = sensor.getDistance()
    time.sleep(0.1)
    return distance

def run_camera(opt, hyp):
    sensor = SensorDist(hyp)
    cap = cv2.VideoCapture(0)
    i = 0 
    while True:
        ret, frame = cap.read()
        i+=1
        if i%opt.per_frames==0:
            distance = sensor_dist(sensor)
            texts = 'Distance: {} [cm/s]'.format(str(distance))
            cv2.putText(frame, texts, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, [225, 255, 255], thickness=2)
            frame = cv2.resize(frame, (500, 500))
            cv2.imshow('camera', frame)
            #print("{:.0f}cm".format(distance))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    del sensor
