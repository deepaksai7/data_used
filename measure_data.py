import subprocess
import psutil
from psutil._common import bytes2human
from timeloop import Timeloop
from datetime import timedelta

tl = Timeloop()

@tl.job(interval=timedelta(seconds=1200))
def network_data():
    x=psutil.net_io_counters(pernic=True)
    data_sent=x['wlp2s0'][0]  
    data_received=x['wlp2s0'][1]
    total_data=x['wlp2s0'][0]+x['wlp2s0'][1]
    message="Data used till now "+bytes2human(total_data)
    subprocess.Popen(['notify-send', message])

if __name__ == "__main__":
    tl.start(block=True)

#here wlp2s0 is the interface name. Your's may be different. You can with typing "ifconfig" in terminal
