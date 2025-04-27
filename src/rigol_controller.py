import pyvisa
import numpy as np

# Parameters
fs = 1.25e8  # Sampling rate (125 MHz)
device_address = '' # Example: 'USB0::0x1AB1::0x0642::DG5A123456789::INSTR'
# Load the waveform data
waveform = np.loadtxt("waveform.csv", delimiter=",")
waveform_points = ",".join(map(str, waveform))

# Initialize the VISA resource manager
rm = pyvisa.ResourceManager()

# Check connection:
print(rm.list_resources())

# Connect to the device
instrument = rm.open_resource(device_address)

# Reset the device
instrument.write('*RST')

# Set the sampling rate
instrument.write(f'C1:SRATE {fs}')  # Set the sampling rate to 125 MHz

# Upload the waveform
instrument.write(f'C1:ARB:DATA {waveform_points}')

# Set the output mode to arbitrary waveform
instrument.write('C1:BSWV WVTP,ARB')

# Enable output on channel 1
instrument.write('C1:OUTP ON')

# Close the connection
instrument.close()