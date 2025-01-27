import logging
import sys

# Create basic logger
logger = logging.getLogger('power_monitor')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s : %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
ch.setFormatter(formatter)
logger.addHandler(ch)

# Using a multimeter, measure the voltage of the receptacle where your 9V AC transformer will plug into.
# Enter the measured value below.
GRID_VOLTAGE = 124.2

# Using a multimeter, measure the output voltage of your AC transformer. Using the value on the label is
# not ideal and will lead to greater accuracy in the calculations.
AC_TRANSFORMER_OUTPUT_VOLTAGE = 10.2

# InfluxDB Settings
db_settings = {
    'host': 'localhost',
    'port': 8086,
    'username': 'root',
    'password': 'password',
    'database': 'power_monitor'
}

# ADC pins/channels
ADC_CHANNELS = {
    'ct1_channel': 0,
    'ct2_channel': 1,
    'ct3_channel': 2,
    'ct4_channel': 3,
    'ct5_channel': 6,
    'ct6_channel': 7,
    'board_voltage_channel': 4,
    'v_sensor_channel': 5
}

# The values from running the software in "phase" mode should go below!
CT_PHASE_CORRECTION = {
    'ct1': 1,
    'ct2': 1,
    'ct3': 1,
    'ct4': 1,
    'ct5': 1,
    'ct6': 1,
}

# AFTER phase correction is completed, these values are used in the final calibration for accuracy.
# See the documentation for more information.
ACCURACY_CALIBRATION = {
    'ct1': 1,
    'ct2': 1,
    'ct3': 1,
    'ct4': 1,
    'ct5': 1,
    'ct6': 1,
    'AC': 1,
}
