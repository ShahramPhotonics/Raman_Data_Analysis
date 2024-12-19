# Raman Laser Intensity Dependence Analysis - README

This Python script calculates and visualizes the dependence of Raman intensity on laser intensity for different Raman shifts (wavenumbers). The script also incorporates resonance effects and wavelength-dependent polarizability to simulate Raman intensity behavior.

## Features

- **Raman Intensity Simulation**: Computes Raman intensity for varying laser intensities and wavenumbers.
- **Customizable Parameters**:
  - Laser wavelength
  - Range of laser intensities
  - Wavenumbers (Raman shifts)
  - Proportionality constant
- **Visualization**: Generates plots of Raman intensity vs laser intensity for different Raman shifts.
- **Data Output**: Saves the calculated Raman intensity data to an Excel file (`raman_laser_intensity.xlsx`).

## Requirements

- Python 3.x
- Required Libraries:
  - numpy
  - pandas
  - matplotlib
  - openpyxl (for saving Excel files)

Install dependencies with:
```bash
pip install numpy pandas matplotlib openpyxl
```

## Usage

1. Clone this repository or download the script.
2. Modify the parameters in the script to suit your analysis (optional).
3. Run the script using Python:
   ```bash
   python Raman_Laser_Depend.py
   ```
4. The script generates:
   - An Excel file named `raman_laser_intensity.xlsx` containing simulated data.
   - A plot visualizing Raman intensity vs laser intensity for various wavenumbers.

## Parameters

- `wavenumbers`: Raman shifts in cm⁻¹ (e.g., 500 to 3000 cm⁻¹).
- `laser_wavelength`: Wavelength of the laser (in cm).
- `laser_intensity_range`: Range of laser power values (e.g., 0.1 to 1.0 W/cm²).
- `proportionality_C`: Proportionality constant for polarizability calculation.

## Output

1. **Excel File**: Contains columns for laser intensities and corresponding Raman intensities for each wavenumber.
2. **Plot**: Visualizes the relationship between laser intensity and Raman intensity across multiple wavenumbers.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

Shahram Moradi

For any questions or suggestions, contact Shahram at [GitHub Repository](https://github.com/ShahramPhotonics).

