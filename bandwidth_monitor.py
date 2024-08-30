import psutil
import time
import matplotlib.pyplot as plt


def monitor_bandwidth(interval=1, duration=60):
    timestamps = []
    bytes_sent = []
    bytes_recv = []

    for _ in range(int(duration / interval)):
        stats = psutil.net_io_counters()
        timestamps.append(time.time())
        bytes_sent.append(stats.bytes_sent)
        bytes_recv.append(stats.bytes_recv)
        time.sleep(interval)

    plt.plot(timestamps, bytes_sent, label='Bytes Sent')
    plt.plot(timestamps, bytes_recv, label='Bytes Received')
    plt.xlabel('Time')
    plt.ylabel('Bytes')
    plt.legend()
    plt.show()


monitor_bandwidth()
