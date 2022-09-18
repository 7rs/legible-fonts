from configurator.glyphs.trans import TransformOption


class IosevkaExtended:
    ALL = TransformOption(scaling=0.83, x_movement=1, before_width=498, after_width=500)
    # Scaling:  500 / 600       = 0.83 (0.833...)
    # Width:    600 * 0.83      = 498
    # Movement: (500 - 498) / 2 = 1


class BIZUDGothic:
    HALF_WIDTH_KATAKANA = TransformOption(scaling=0.44, x_movement=25, y_movement=44, before_width=451, after_width=500)
    # Scaling:    800 / 1802       = 0.44 (0.443...)
    # Width:      1024 * 0.44      = 451  (450.56)
    # X Movement: (500 - 451) / 2  = 25   (24.5)
    # Y Movement: 100 * 0.44       = 44

    FULL_WIDTH_HIRAGANA = TransformOption(
        scaling=0.39, x_movement=101, y_movement=39, before_width=799, after_width=1000
    )
    # Scaling:    800 / 2048       = 0.39 (0.443...)
    # Width:      2048 * 0.39      = 799  (798.72)
    # X Movement: (1000 - 799) / 2 = 101  (100.5)
    # Y Movement: 100 * 0.39       = 39

    FULL_WIDTH_LATIN = TransformOption(scaling=0.44, x_movement=50, y_movement=22, before_width=901, after_width=1000)
    # Scaling:    800 / 1802       = 0.44 (0.443...)
    # Width:      2048 * 0.44      = 901  (901.2)
    # X Movement: (1000 - 901) / 2 = 50   (49.5)
    # Y Movement: 51 * 0.44        = 22   (22.44)

    FULL_SIZE_GLYPHS = TransformOption(scaling=0.39, x_movement=101, y_movement=78, before_width=799, after_width=1000)
    # Scaling:    800 / 2048       = 0.39 (0.390...)
    # Width:      2048 * 0.39      = 799  (798.72)
    # X Movement: (1000 - 799) / 2 = 101  (100.5)
    # Y Movement: 200 * 0.39       = 78


class NotoEmoji:
    ALL = TransformOption(scaling=0.38, x_movement=6, before_width=988, after_width=1000)
    # Height: 1740 + 340 = 2080
    # Width:  2600 - 100 = 2500
    # 2500 x 2080
    # ---
    # Scaling:    1000 / 2600      = 0.38 (0.384...)
    # Width:      2600 * 0.38      = 988
    # X Movement: (1000 - 988) / 2 = 6
