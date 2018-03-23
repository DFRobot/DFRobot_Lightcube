# Light cube Library 
This is a Library for Light cube.

## Table of Contents

* [Summary](#summary)
* [Methods](#methods)
* [History](#history)
* [Credits](#credits)

<snippet>
<content>

## Summary
This is a Library for 8X8X8 Light cube.
The hardware is FireBeetle-ESP32
The software is upyCraft

## Methods

### micropython
```python

import light_cube
/*
 * @brief Light rotation
 *
 * @param layer Select the layer to rotate.
 *
 * @param t Scan time, the shorter the time, the faster the rotation
 */
show_circle(layer,t)

/*
 * @brief Interlaced lights.
 *
 * @param t Scan time, the shorter the time, the faster the interlace
 */
show_cross(t)

/*
 * @brief Heartbeat effects
 *
 * @param t Scan time, the shorter the time, the faster the heartbeat
 */
show_heart(t)

import import lightcube_show
/*
 * @brief Light falling
 *
 * @param t Scan time, the shorter the time, the faster the falling
 */
show_fall(t)

/*
 * @brief Light cube expansion
 *
 * @param t Scan time, the shorter the time, the faster the expansion
 */
show_cube(t)

/*
 * @brief Display characters and move backwards
 *
 * @param t Scan time, the shorter the time, the faster the move
 *
 * @param data The character array,array contained in the lightcube_show library:
               num 0-9 : num_0-num_9  word A-Z: word_A-word_Z
 */
show_print(self,t,data)

```

```

## History

- data 2018-3-23
- version V0.1

## Credits

- author [Jiawei Zhang  <jiawei.zhang@dfrobot.com>]