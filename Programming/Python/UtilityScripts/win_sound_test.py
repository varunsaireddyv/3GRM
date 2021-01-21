import winsound
frequency = 9000  # Set Frequency To 2500 Hertz
duration = 500  # Set Duration To 1000 ms == 1 second
for x in range(10):
    winsound.Beep(frequency, duration)