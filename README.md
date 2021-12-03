# UltraSound Python Helpers

This is a few files that should help with doing the math behind some of the UltraSound stuff.

## Usage

All the main code is in **UltraSound.py**. To import and instantiate, do this:

```python
import UltraSound

us = UltraSound.UltraSound(1, 1, 1, 1)
```

Here are the input parameters for the constructor (in order):

| Param No. | Name                | Type   | Description                            |
|-----------|---------------------|--------|----------------------------------------|
| 1         | Array Width         | Number | Width of the linear array. (cm?)       |
| 2         | Carrier Frequency   | Number | Carrier frequency of the device. (MHz) |
| 3         | Axial Resolution    | Number | Axial Resolution (mm?)                 |
| 4         | Lateral Resolution  | Number | Lateral Resolution (mm?)               |
