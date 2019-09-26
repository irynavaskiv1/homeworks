
import pyowm

city = input('What city you are interested: ')
name = input('Tell me your name, please:  ')
owm = pyowm.OWM('746a74688b8215746bb43e716dd38854')

observation = owm.weather_at_place(city)
w = observation.get_weather()
temperature = w.get_temperature('celsius')['temp']

print("Hello,  " + name + " the temperature in  " + city + " is " +
      str(temperature) + " for the Celsius. Also, the state of the sky is "
      + w.get_detailed_status() + ". Have a nice day!")
