# %%
import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1.25e8  # Sampling rate
Ts = 5e-6    # Duration of a symbol
chirpRate = 2e13
carrierFreq = 1e7

# Time vector
num_samples = int(round(fs * Ts))
timeLine = np.arange(num_samples) / fs

# Signal generation
xSignal = np.real(np.exp(1j * 2 * np.pi * (carrierFreq * timeLine + chirpRate * timeLine ** 2 / 2)))

# Scaling
ppAmp = 0.9
bias = 3.5
xSignal = bias + xSignal * ppAmp / 2

# %%
"""Prepare csv"""
# Normalize to the range [0, 1] for the Rigol DG5352
xSignal_normalized = (xSignal - np.min(xSignal)) / (np.max(xSignal) - np.min(xSignal))

# Save the waveform to a file
np.savetxt("waveform.csv", xSignal_normalized, delimiter=",")
# %%

# Optional: Plot the signal
plt.plot(timeLine, xSignal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Generated Signal')
plt.show()
# %%