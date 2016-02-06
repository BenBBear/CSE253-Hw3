#! /bin/bash

xvfb-run draw_net.py ./net.prototxt ./not.working.png
xvfb-run draw_net.py ./net.works.prototxt ./working.png
