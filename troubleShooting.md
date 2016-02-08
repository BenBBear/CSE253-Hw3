
**Sat Feb  6 17:36:36 UTC 2016**

- *Errro*: Encounter "input blob unknown Error"
- *Solve*: Remove unnecessary stage in net.prototxt



**Sat Feb  6 18:14:17 UTC 2016**

- *Error*: Unable to visualize graph
- *Solve*: 
    0. install xvfb, `sudo apt-get install xvfb`
    1. add `$CAFFE_ROOT/python` to path
    2. install `sudo apt-get install graphviz`, pydot
    3. [http://stackoverflow.com/questions/15951748/pydot-and-graphviz-error-couldnt-import-dot-parser-loading-of-dot-files-will]()  this is the pydot install guide
    3. ensure no number in net name, and net must have name
    4. `xvfb-run draw_net.py input.prototxt vis.png`
