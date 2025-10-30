import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def number_to_dac(self, number):
        return [int(element) for element in bin(number)[2:].zfill(8)]

    def sequential_counting_adc(self):
        number = -1
        while(GPIO.input(self.comp_gpio) == 0 and number < 255):
            number = number + 1
            GPIO.output(self.bits_gpio, R2R_ADC.number_to_dac(self, number))
            time.sleep(self.compare_time)
        reset_number = 0
        GPIO.output(self.bits_gpio, R2R_ADC.number_to_dac(self, reset_number))
        return number

    def get_sc_voltage(self):
        return float(self.dynamic_range * R2R_ADC.sequential_counting_adc(self) / 256)
    
    def successive_approximation_adc(self):
        razr = 64
        number = 128
        time.sleep(self.compare_time)
        GPIO.output(self.bits_gpio, R2R_ADC.number_to_dac(self, number))
        time.sleep(self.compare_time)
        for i in range(8):
            if GPIO.input(self.comp_gpio) == 0:
                number = number + razr
            else:
                number = number - razr
            GPIO.output(self.bits_gpio, R2R_ADC.number_to_dac(self, number))
            razr = int(razr / 2)
            time.sleep(self.compare_time)

        reset_number = 0
        GPIO.output(self.bits_gpio, R2R_ADC.number_to_dac(self, reset_number))
        return number

if __name__ == "__main__":
    dac = R2R_ADC(3.157, 0.003  , True)
    try:
        while True:
            try:
                #print(dac.sequential_counting_adc())
                voltage = dac.dynamic_range * dac.successive_approximation_adc() / 256
                print(f"Напряжение: {voltage} В\n")

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз \n")

    finally:
        dac.deinit()

    