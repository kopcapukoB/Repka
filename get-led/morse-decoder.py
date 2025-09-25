import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

leds = [24, 22, 23, 27, 17, 25, 12, 16]
button = 13
up = 9
down = 10

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(button, GPIO.IN)
GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)
GPIO.cleanup

s_t = 0.5
p_t = s_t * 2
l_t = s_t * 3
space_t = s_t * 5
GPIO.output(leds, 0)
print('===========================')
print('Morse-decoder. Version 1.0.')
print('===========================')
print('Press the button 13 to send a message')
print('Press the button 9 to increase the tick duration')
print('Press the button 10 to decrase the tick duration')

def point():
    print('. ', end='')
    time.sleep(s_t)
    GPIO.output(leds, 1)
    time.sleep(s_t)
    GPIO.output(leds, 0)

def dash():
    print('... ', end = '')
    time.sleep(s_t)
    GPIO.output(leds, 1)
    time.sleep(l_t)
    GPIO.output(leds, 0)

def pred():
    print('()', end = '')
    time.sleep(p_t)

def space():
    print('  ', end = '')
    time.sleep(space_t)

while True:
    if GPIO.input(up):
        print('Tick = ', end = '')
        s_t = s_t + 0.1
        print(s_t)
        time.sleep(1.0)
    if GPIO.input(down) and s_t > 0.1:
        print('Tick = ', end = '')
        s_t = s_t - 0.1
        print(s_t)
        time.sleep(1.0)
    if GPIO.input(button):
        print('')
        print('Write your message:')
        mes = input()
        for i in range(len(mes)):
            pred()
            if mes[i] == ' ':
                space()
            if mes[i] == 'a':
                point()
                dash()
            if mes[i] == 'b':
                dash()
                point()
                point()
                point()
            if mes[i] == 'c':
                dash()
                point()
                dash()
                point()
            if mes[i] == 'd':
                dash()
                point()
                point()
            if mes[i] == 'e':
                point()
            if mes[i] == 'f':
                point()
                point()
                dash()
                point()
            if mes[i] == 'g':
                dash()
                dash()
                point()
            if mes[i] == 'h':
                point()
                point()
                point()
                point()
            if mes[i] == 'i':
                point()
                point()
            if mes[i] == 'j':
                point()
                dash()
                dash()
                dash()
            if mes[i] == 'k':
                dash()
                point()
                dash()
            if mes[i] == 'l':
                point()
                dash()
                point()
                point()
            if mes[i] == 'm':
                dash()
                dash()
            if mes[i] == 'n':
                point()
                dash()
            if mes[i] == 'o':
                dash()
                dash()
                dash()
            if mes[i] == 'p':
                point()
                dash()
                dash()
                point()
            if mes[i] == 'q':
                dash()
                dash()
                point()
                dash()
            if mes[i] == 'r':
                point()
                dash()
                point()
            if mes[i] == 's':
                point()
                point()
                point()
            if mes[i] == 't':
                dash()
            if mes[i] == 'u':
                point()
                point()
                dash()
            if mes[i] == 'v':
                dash()
                dash()
                dash()
                point()
            if mes[i] == 'w':
                point()
                dash()
                dash()
            if mes[i] == 'x':
                dash()
                point()
                point()
                dash()
            if mes[i] == 'y':
                dash()
                point()
                dash()
                dash()
            if mes[i] == 'z':
                dash()
                dash()
                point()
                point()
            if mes[i] == '0':
                dash()
                dash()
                dash()
                dash()
                dash()
            if mes[i] == '1':
                point()
                dash()
                dash()
                dash()
                dash()
            if mes[i] == '2':
                point()
                point()
                dash()
                dash()
                dash()
            if mes[i] == '3':
                point()
                point()
                point()
                dash()
                dash()
            if mes[i] == '4':
                point()
                point()
                point()
                point()
                dash()
            if mes[i] == '5':
                point()
                point()
                point()
                point()
                point()
            if mes[i] == '6':
                dash()
                point()
                point()
                point()
                point()
            if mes[i] == '7':
                dash()
                dash()
                point()
                point()
                point()
            if mes[i] == '8':
                dash()
                dash()
                dash()
                point()
                point()
            if mes[i] == '9':
                dash()
                dash()
                dash()
                dash()
                point()
        print('')
        print('Your message has been sent.')

