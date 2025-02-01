import pandas as pd
import pyshark
import socket
import struct

def ip_to_int(ip):
    return struct.unpack("!I", socket.inet_aton(ip))[0]

def protocol_to_int(protocol):
    protocol_map = {
        'TCP': 6,
        'UDP': 17,
        # Add more protocols if needed
    }
    return protocol_map.get(protocol, 0)  # Default to 0 if the protocol is not found

def extract_features(capture_file):
    cap = pyshark.FileCapture(capture_file)
    features = []
    
    for packet in cap:
        if hasattr(packet, 'ip'):
            feature = {
                'src_ip': ip_to_int(packet.ip.src),
                'dst_ip': ip_to_int(packet.ip.dst),
                'protocol': protocol_to_int(packet.transport_layer),
                'length': int(packet.length),
                'label': 0  # Assign a default label (e.g., 0 for normal traffic)
            }
            features.append(feature)
    
    if not features:
        print("No packets captured.")
    
    return pd.DataFrame(features)
