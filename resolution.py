from boxshape import BoxShape


################################################################################
###### IMPORTANT --- Names for Common Screen Resolutions
################################################################################
###### Full HD ----- 1920 x 1080
###### Ultra-Wide -- 5120 x 1440
################################################################################


FULL_HD_MODE = 'f'
ULTRA_WIDE_MODE = 'u'


# [1] FULL_HD_READ
FULL_HD_READ_X = 557
FULL_HD_READ_Y = 1032
FULL_HD_READ_WIDTH = 42
FULL_HD_READ_HEIGHT = 23
FULL_HD_READ_BOX_SHAPE = BoxShape(
    FULL_HD_READ_X, 
    FULL_HD_READ_Y, 
    FULL_HD_READ_WIDTH, 
    FULL_HD_READ_HEIGHT)

# [2] FULL_HD_WRITE
FULL_HD_WRITE_X = 675
FULL_HD_WRITE_Y = 948
FULL_HD_WRITE_WIDTH = 125
FULL_HD_WRITE_HEIGHT = 49
FULL_HD_WRITE_BOX_SHAPE = BoxShape(
    FULL_HD_WRITE_X, 
    FULL_HD_WRITE_Y, 
    FULL_HD_WRITE_WIDTH, 
    FULL_HD_WRITE_HEIGHT)


# [3] ULTRA_WIDE_READ
ULTRA_WIDE_READ_X = 2020
ULTRA_WIDE_READ_Y = 1375
ULTRA_WIDE_READ_WIDTH = 74
ULTRA_WIDE_READ_HEIGHT = 25
ULTRA_WIDE_READ_BOX_SHAPE = BoxShape(
    ULTRA_WIDE_READ_X, 
    ULTRA_WIDE_READ_Y, 
    ULTRA_WIDE_READ_WIDTH, 
    ULTRA_WIDE_READ_HEIGHT)

# [4] ULTRA_WIDE_WRITE
ULTRA_WIDE_WRITE_X = 2150
ULTRA_WIDE_WRITE_Y = 1250
ULTRA_WIDE_WRITE_WIDTH = 200
ULTRA_WIDE_WRITE_HEIGHT = 70
ULTRA_WIDE_WRITE_BOX_SHAPE = BoxShape(
    ULTRA_WIDE_WRITE_X, 
    ULTRA_WIDE_WRITE_Y, 
    ULTRA_WIDE_WRITE_WIDTH, 
    ULTRA_WIDE_WRITE_HEIGHT)


# Dictionary mapping modes to their configurations
RESOLUTION_CONFIG = {
    FULL_HD_MODE: {
        "read_box": FULL_HD_READ_BOX_SHAPE,
        "write_box": FULL_HD_WRITE_BOX_SHAPE,
        "resolution": (1920, 1080),
    },
    ULTRA_WIDE_MODE: {
        "read_box": ULTRA_WIDE_READ_BOX_SHAPE,
        "write_box": ULTRA_WIDE_WRITE_BOX_SHAPE,
        "resolution": (5120, 1440),
    },
}

