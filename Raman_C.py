import numpy as np
import pandas as pd

# Function to generate Raman intensity data with wavelength-dependent polarizability
def generate_raman_intensity_data(
    num_samples=500,  # Number of samples
    wavenumber_min=100,  # Minimum wavenumber (cm^-1)
    wavenumber_max=3000,  # Maximum wavenumber (cm^-1)
    laser_wavelengths=[532e-7, 785e-7, 1064e-7],  # Laser wavelengths in cm
    resonance_wavelength=900e-7,  # Resonance wavelength in cm
    laser_power=0.1,  # Laser power in W
    beam_area=1e-4,  # Laser beam area in cm²
    molecular_concentration=1e18,  # Molecules/cm³
    efficiency=0.5,  # Detector efficiency
    proportionality_C=1e-30  # Proportionality constant C
):
    # Constants
    c = 3.0e10  # Speed of light in cm/s
    pi = np.pi

    # Derived laser intensity
    I_laser = laser_power / beam_area  # Laser intensity (W/cm²)

    # Generate wavenumbers
    wavenumbers = np.linspace(wavenumber_min, wavenumber_max, num_samples)

    # Function to compute Raman intensity with wavelength-dependent polarizability
    def compute_raman_intensity(wavenumbers, laser_wavelength, resonance_wavelength):
        laser_frequency = c / laser_wavelength  # Laser frequency in Hz
        vibrational_frequency = c * wavenumbers  # Vibrational frequency in Hz

        # Polarizability dependency on laser and resonance wavelengths
        delta_alpha = proportionality_C * (1 / laser_wavelength**2) * (1 / (resonance_wavelength**2 - laser_wavelength**2))

        # Frequency difference term
        difference_term = (laser_frequency - vibrational_frequency) ** 2

        # Raman intensity calculation
        intensity = (
            (8 * pi**4 / (45 * c**4)) *
            laser_frequency**4 *
            delta_alpha**2 *
            I_laser *
            molecular_concentration *
            efficiency / 
            difference_term
        )
        return intensity

    # Prepare data
    data = {"Wavenumber (cm⁻¹)": wavenumbers}
    for laser_wavelength in laser_wavelengths:
        intensity = compute_raman_intensity(wavenumbers, laser_wavelength, resonance_wavelength)
        wavelength_nm = laser_wavelength * 1e7  # Convert to nm
        data[f"Intensity (λ = {wavelength_nm:.0f} nm)"] = intensity

    # Convert to DataFrame
    df = pd.DataFrame(data)
    return df

# Generate and save the data
data = generate_raman_intensity_data()
output_file = "Raman_Intensity_With_Polarizability.xlsx"
data.to_excel(output_file, index=False)

print(f"Raman intensity data saved to {output_file}")
