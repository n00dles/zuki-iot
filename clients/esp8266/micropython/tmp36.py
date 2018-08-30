import machine
adc = machine.ADC(0)
voltage = (((adc.read() *3.3)/1024)-0.5)*100

