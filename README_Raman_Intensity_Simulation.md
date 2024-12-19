# Raman Data Analysis - README

This repository contains a Python script for generating Raman intensity data with wavelength-dependent polarizability. The script simulates the intensity of Raman-scattered light for various laser wavelengths, taking into account the molecular polarizability, resonance effects, and experimental parameters.

## Features

- **Raman Intensity Simulation**: Computes Raman intensity across a range of wavenumbers (100 cm⁻¹ to 3000 cm⁻¹).
- **Wavelength-Dependent Polarizability**: Includes the effects of laser and resonance wavelengths on molecular polarizability.
- **Customizable Parameters**:
  - Laser wavelengths
  - Resonance wavelength
  - Laser power and beam area
  - Molecular concentration
  - Detector efficiency
  - Proportionality constant
- **Data Output**: Saves the generated Raman intensity data to an Excel file (`Raman_Intensity_With_Polarizability.xlsx`).

## Requirements

- Python 3.x
- Required Libraries:
  - numpy
  - pandas
  - openpyxl (for Excel file output)

Install dependencies with:
```bash
pip install numpy pandas openpyxl
```

## Usage

1. Clone this repository or download the script.
2. Run the script using Python:
   ```bash
   python Raman_C.py
   ```
3. The script generates an Excel file named `Raman_Intensity_With_Polarizability.xlsx` containing simulated data.

## Parameters

Modify the following parameters in the script to customize the simulation:
- `num_samples`: Number of wavenumber samples.
- `wavenumber_min` and `wavenumber_max`: Range of wavenumbers (cm⁻¹).
- `laser_wavelengths`: List of laser wavelengths (in cm).
- `resonance_wavelength`: Resonance wavelength (in cm).
- `laser_power`: Power of the laser (in W).
- `beam_area`: Laser beam area (in cm²).
- `molecular_concentration`: Concentration of molecules (molecules/cm³).
- `efficiency`: Efficiency of the detector.
- `proportionality_C`: Proportionality constant for polarizability.

## Output

The output is an Excel file with columns:
- `Wavenumber (cm⁻¹)`
- `Intensity (λ = <laser wavelength> nm)` for each specified laser wavelength.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

Shahram Moradi

For questions or suggestions, contact Shahram at [GitHub Repository](https://github.com/ShahramPhotonics).


