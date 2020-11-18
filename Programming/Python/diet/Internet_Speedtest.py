import tk
import speedtest as st
top = tk.__doc__

speed_test = st.Speedtest()
speed_test.get_best_server()

# Get ping (miliseconds)
ping = speed_test.results.ping
# Perform download and upload speed tests (bits per second)
download = speed_test.download()
upload = speed_test.upload()

# Convert download and upload speeds to megabits per second
download_mbs = round(download / (10**6), 2)
upload_mbs = round(upload / (10**6), 2)

print(download_mbs, upload_mbs)
top.mainloop()