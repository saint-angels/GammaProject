"""
This program sends 10 random values between 0.0 and 1.0 to the /filter address,
waiting for 1 seconds between each value.
"""
import argparse
import random
import time

from pythonosc import osc_message_builder
from pythonosc import udp_client


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="127.0.0.1",
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=9000,
      help="The port the OSC server is listening on")
  args = parser.parse_args()

  client = udp_client.SimpleUDPClient(args.ip, args.port)

  while 1:
    r = lambda: random.randint(0,255)
    s = '#%02X%02X%02X' % (r(),r(),r())
    #HEX
    #client.send_message("/", s)
    #RGB
    client.send_message("/", "\t" + str(random.uniform(0,1)) + "\t" + str(random.uniform(0,1)) + "\t" + str(random.uniform(0,1)))
    time.sleep(1)