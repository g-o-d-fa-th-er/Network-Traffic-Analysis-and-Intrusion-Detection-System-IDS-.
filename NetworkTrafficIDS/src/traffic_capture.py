import os

def capture_traffic():
    capture_file = 'data/capture.pcap'
    # Capture traffic for 10 seconds on interface 7 (Wi-Fi)
    os.system(f"tshark -i 7 -a duration:10 -w {capture_file}")
    return capture_file
