#!/usr/ben/env python3
import speedtest

st = speedtest.Speedtest()

print("Finding best server...")
st.get_best_server()

print("Testing download...")
download = st.download()

print("Testing upload...")
upload = st.upload()

ping = st.results.ping

print()
print(f"Download: {download/1_000_000:.2f} Mbps")
print(f"Upload:   {upload/1_000_000:.2f} Mbps")
print(f"Ping:     {ping:.2f} ms")