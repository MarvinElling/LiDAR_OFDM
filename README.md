

### 1. **NI-VISA or PyVISA-Compatible VISA Library**
- **Why?** The `pyvisa` library requires a VISA backend to communicate with instruments.
- **What to Install?**
  - Download and install **NI-VISA** (National Instruments VISA) from [NI's website](https://www.ni.com/en-us/support/downloads/drivers/download.ni-visa.html).
  - Alternatively, you can use **Keysight IO Libraries Suite** or **TekVISA**, depending on your preference and compatibility with your system.

---

### 2. **Rigol USB Driver (if using USB connection)**
- **Why?** The Rigol DG5352 requires a USB driver for your computer to recognize it as a VISA-compatible device.
- **What to Install?**
  - Download the Rigol USB driver from the [Rigol website](https://www.rigolna.com/).
  - Install the driver and ensure the device is recognized in your system's Device Manager.

---

### 3. **Rigol UltraStation (Optional)**
- **Why?** Rigol UltraStation is Rigol's official software for creating and uploading arbitrary waveforms. While not required for Python-based control, it can be helpful for testing and manual uploads.
- **What to Install?**
  - Download Rigol UltraStation from the Rigol website.

---

### 4. **Python Environment**
- Ensure you have Python installed (preferably Python 3.7 or later).
- Install the required Python libraries:
  ```bash
  pip install pyvisa numpy
  ```

---

### 5. **Check Device Connectivity**
After installing the necessary software, verify that your computer can detect the Rigol DG5352:
- Use the `pyvisa` command to list connected devices:
  ```python
  import pyvisa
  rm = pyvisa.ResourceManager()
  print(rm.list_resources())
  ```
  This should return the VISA address of your Rigol DG5352 (e.g., `USB0::0x1AB1::0x0642::DG5A123456789::INSTR`).

