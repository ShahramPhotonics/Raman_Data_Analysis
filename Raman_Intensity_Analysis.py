import numpy as np
import pandas as pd

# Function to calculate Raman Intensity
def generate_raman_data(wavenumbers, laser_intensities, laser_wavelength, proportionality_C=1e-40, resonance_wavelength=900e-7):
    c = 3e10  # Speed of light in cm/s
    results = {}

    for wavenumber in wavenumbers:
        # Calculate shifted laser wavelength due to Raman shift
        laser_wavelength_shifted = laser_wavelength - (1 / wavenumber) * 1e-7  # Convert cm^-1 to cm shift

        # Resonance-dependent Delta Alpha calculation
        delta_alpha = proportionality_C * (1 / laser_wavelength_shifted**2) * (1 / (resonance_wavelength**2 - laser_wavelength_shifted**2))

        # Laser frequency
        laser_frequency = c / laser_wavelength_shifted

        # Raman Intensity Calculation
        raman_intensity = (8 * np.pi**4 / (45 * c**4)) * laser_frequency**4 * delta_alpha**2 * laser_intensities
        results[wavenumber] = raman_intensity

    return results

# Parameters
wavenumbers = np.arange(500, 3001, 500)  # Wavenumbers: 500 cm^-1 to 3000 cm^-1
laser_intensities = np.linspace(0.1, 5, 50)  # Laser intensities: 0.1 W to 5 W
laser_wavelength = 785e-7  # Laser wavelength in cm
resonance_wavelength = 900e-7  # Resonance wavelength in cm

# Generate Raman Intensity Data
data = generate_raman_data(wavenumbers, laser_intensities, laser_wavelength, resonance_wavelength=resonance_wavelength)

# Save Data to Excel
df = pd.DataFrame(data, index=laser_intensities)
df.index.name = "Laser Intensity (W)"
df.columns.name = "Raman Shift (cm^-1)"
output_file = "raman_intensity_data_updated.xlsx"
df.to_excel(output_file)
print(f"Data successfully saved to {output_file}")
