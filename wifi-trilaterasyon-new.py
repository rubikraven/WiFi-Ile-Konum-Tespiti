import math
from datetime import datetime
from scapy.all import *
from scapy.layers.dot11 import Dot11, Dot11Beacon, Dot11ProbeReq
from scipy.optimize import minimize

# Özel BSSID'nizi bu genel değerle değiştirin
your_wifi_ssid = "YOUR_WIFI_BSSID"

# Özel konum bilgilerinizi bu genel değerlerle değiştirin
apartment_x, apartment_y = 0.0, 0.0

location_AP1 = (apartment_x + 0.0001, apartment_y + 0.0001)
location_AP2 = (apartment_x - 0.0001, apartment_y - 0.0001)
location_AP3 = (apartment_x + 0.0002, apartment_y - 0.0001)

rssi_AP1 = -60
rssi_AP2 = -65
rssi_AP3 = -55

known_aps = {
    "AP1": {"location": location_AP1, "rssi": rssi_AP1},
    "AP2": {"location": location_AP2, "rssi": rssi_AP2},
    "AP3": {"location": location_AP3, "rssi": rssi_AP3},
}

min_rssi = -70

def calculate_distance(signal_strength, frequency):
    return 10 ** ((27.55 - (20 * math.log10(frequency)) + abs(signal_strength)) / 20)

def trilateration(known_aps, target_rssi):
    def distance_error(location, known_aps, target_rssi):
        error = 0
        for ap_name, ap_info in known_aps.items():
            known_location = ap_info["location"]
            known_rssi = ap_info["rssi"]
            dist = calculate_distance(known_rssi, 2400)
            target_dist = calculate_distance(target_rssi, 2400)
            error += (math.sqrt((location[0] - known_location[0]) ** 2 + (location[1] - known_location[1]) ** 2) - abs(dist - target_dist)) ** 2
        return error

    initial_location = (0, 0)
    result = minimize(distance_error, initial_location, args=(known_aps, target_rssi), method='L-BFGS-B')
    return result.x

def packet_handler(packet):
    if packet.haslayer(Dot11ProbeReq) or packet.haslayer(Dot11Beacon):
        if packet.haslayer(Dot11Elt):
            ssid = packet[Dot11Elt].info.decode("utf-8", "ignore")
        else:
            ssid = None
        mac_address = packet[Dot11].addr2
        rssi = packet.dBm_AntSignal
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        packet_type = "Beacon" if packet.haslayer(Dot11Beacon) else "Probe Request"

        if ssid != your_wifi_ssid and rssi >= min_rssi:
            estimated_location = trilateration(known_aps, rssi)
            
            # Calculate estimated distance in meters using the RSSI value
            estimated_distance = calculate_distance(rssi, 2400)
            
            print(f"[{current_time}] Type: {packet_type}, MAC: {mac_address}, RSSI: {rssi}, Location: {estimated_location}, Estimated distance: {estimated_distance:.2f} meters")

iface = "wlan1"
sniff(iface=iface, prn=packet_handler, store=False)
