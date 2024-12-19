# Raman Intensity Data Analysis - README

This Python script calculates and simulates Raman intensity data for various laser intensities and Raman shifts. It takes into account the effect of wavelength-dependent polarizability and resonance effects.

## Features

- **Raman Intensity Simulation**: Computes Raman intensity values based on given laser intensities and Raman shifts.
- **Customizable Parameters**:
  - Wavenumbers (Raman shifts)
  - Laser wavelength
  - Resonance wavelength
  - Proportionality constant
  - Range of laser intensities
- **Data Output**: Saves the calculated Raman intensity data to an Excel file (`raman_intensity_data_updated.xlsx`).

## Requirements

- Python 3.x
- Required Libraries:
  - numpy
  - pandas
  - openpyxl (for saving Excel files)

Install dependencies with:
```bash
pip install numpy pandas openpyxl
```

## Usage

1. Clone this repository or download the script.
2. Modify the parameters in the script to suit your analysis (optional).
3. Run the script using Python:
   ```bash
   python Raman_nP.py
   ```
4. The script generates an Excel file named `raman_intensity_data_updated.xlsx` with the simulated data.

## Parameters

- `wavenumbers`: Raman shifts in cm⁻¹ (e.g., 500 cm⁻¹ to 3000 cm⁻¹).
- `laser_intensities`: Range of laser power values (e.g., 0.1 W to 5 W).
- `laser_wavelength`: Wavelength of the laser (in cm).
- `resonance_wavelength`: Resonance wavelength for polarizability (in cm).
- `proportionality_C`: Proportionality constant for polarizability calculation.

## Output

The output is an Excel file with:
- Rows representing laser intensities (in W).
- Columns representing Raman shifts (in cm⁻¹).
- Raman intensity values as the cell entries.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

Shahram Moradi

For any questions or suggestions, contact Shahram at [GitHub Repository](https://github.com/ShahramPhotonics).

