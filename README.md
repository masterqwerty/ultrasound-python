# UltraSound Python Helpers

This is a few files that should help with doing the math behind some of the UltraSound stuff.

## Usage

All the main code is in **UltraSound.py**. To import and instantiate, do this:

```python
import UltraSound

us = UltraSound.UltraSound(1, 1, 1, 1)
```

Here are the input parameters for the constructor (in order):

| Param No. | Name        | Type   | Description                            |
|-----------|-------------|--------|----------------------------------------|
| 1         | `arr_width` | number | Width of the linear array. (cm?)       |
| 2         | `freq`      | number | Carrier frequency of the device. (MHz) |
| 3         | `axial`     | number | Axial Resolution (mm)                  |
| 4         | `lateral`   | number | Lateral Resolution (mm)                |

### Functions

#### `reflect(Z1, Z2)`

Calculate the intensity of the reflected beam. Assumes a 90 degree incidence. Returns the amount reflected as well as the final intensity.

```python
us.reflect(100, 200)
```

| Param No. | Name | Type   | Description                                                       |
|-----------|------|--------|-------------------------------------------------------------------|
| 1         | `Z1` | number | Acoustic impedance of the material the beam is coming from.       |
| 2         | `Z2` | number | Acoustic impedance of the material the beam is reflecting off of. |

#### `transmit(Z1, Z2)`

Calculate the intensity of the transmitted beam. Assumes a 90 degree incidence. Returns the amount transmitted as well as the final intesnity.

```python
us.transmit(100, 200)
```

| Param No. | Name | Type   | Description                                                            |
|-----------|------|--------|------------------------------------------------------------------------|
| 1         | `Z1` | number | Acoustic impedance of the material the beam is coming from.            |
| 2         | `Z2` | number | Acoustic impedance of the material the beam is being transmitted into. |

#### `propagate(mu, z)`

Calculate the intensity of the beam after it has propagated through a material for a given distance. Returns the final intensity.

```python
us.propagate(0.9, 3)
```

| Param No. | Name | Type   | Description                                                              |
|-----------|------|--------|--------------------------------------------------------------------------|
| 1         | `mu` | number | The attenuation factor of the given material. (dB/(cm*MHz))              |
| 2         | `z`  | number | The distance that the beam is travelling inside the given material. (cm) |
