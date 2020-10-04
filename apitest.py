#!/usr/bin/env python3
from samplebase import SampleBase
import math
import requests


class APITest(SampleBase):
    def __init__(self, *args, **kwargs):
        super(APITest, self).__init__(*args, **kwargs)

    def run(self):
        offset_canvas = self.matrix.CreateFrameCanvas()

        while True:
            data = requests.get('http://192.168.1.62:5000/map/1/data').json()

            for x in range(self.matrix.width):
                for y in range(self.matrix.height):
                    offset_canvas.SetPixel(x, y, data['pixel_data'][x][y][0], data['pixel_data'][x][y][1], data['pixel_data'][x][y][2])

            offset_canvas = self.matrix.SwapOnVSync(offset_canvas)

            self.usleep(8 * 10000)

# Main function
if __name__ == "__main__":
    api_test = APITest()
    if (not api_test.process()):
        api_test.print_help()
