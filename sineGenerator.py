import math
PI = 22/7
print('To generate your sine table values, follow the following guidlines\n')
print('You are required to supply the following data\n')
print(' minDCVoltage ==> minimum DC voltage expected at the SPWM H-bridge\n')
print(' maxDCVoltage ==> maximum DC voltage expected at the SPWM H-bridge\n')
print(' voltageResolution ==> Voltage incremet steps')
print(' maxDutyCycle ==> The maximum duty cycle of your PWM genrator')
print(' samples ==> The number of samples per half wave (180 degrees) for each row')
print(' You output will be generated to a file "sine.h" in the same folder this program executes\n')
input(" press enter to continue...\n")
print('----------------------------------------------------------------------------------------------')
minDCValue = float(input("Minimum DC Voltage:"))
maxDCValue = float(input("Maximum DC Voltage:"))
voltageResolution = float(input("Voltage Resolution:"))
maxDutyCycle = float(input("Maximum Duty Cycle value of PWM generator:"))
samples = int(input("Number of samples per 1/2 wave:"))
result = 0
count= 0
peakIncrement = (maxDutyCycle / maxDCValue) * voltageResolution
pos = (minDCValue * peakIncrement) / voltageResolution



file = open('sine.h','w')
file.write('#ifndef  SINE_H\n#define SINE_H\n')
file.write('const uint16_t sineArray[] = {\n')
percent = 0
while pos < maxDutyCycle:
    percent = round((pos / maxDutyCycle) * 100,1)
    file.write('//')
    file.write(str(percent))
    file.write('%\n')
    for i in range(samples):
        result = round(math.sin((i * PI)/samples) * pos)
        file.write(str(result))
        file.write(', ')
        count+=1
    file.write('\n')
    pos +=peakIncrement

file.write('\n};\n')
file.write('#endif')
file.close()
print(str(count)+' generated')
input('If done press enter to exit...')
