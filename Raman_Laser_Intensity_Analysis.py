import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Function to calculate Raman intensity
def raman_intensity(laser_intensity, laser_wavelength, resonance_wavelength, proportionality_C=1e-40):
    delta_alpha = proportionality_C * (1 / laser_wavelength**2) * (1 / (resonance_wavelength**2 - laser_wavelength**2))
    return delta_alpha**2 * laser_intensity

# Parameters
wavenumbers = np.arange(500, 3001, 500)  # Raman shifts: 500 to 3000 cm^-1
laser_wavelength = 785e-7  # Laser wavelength in cm
laser_intensity_range = np.linspace(0.1, 1.0, 50)  # Laser intensity range: 0.1 W/cm^2 to 1.0 W/cm^2
proportionality_C = 1e-40  # Proportionality constant

# Prepare DataFrame to save results
data = {"Laser Intensity (W/cm^2)": laser_intensity_range}
for wavenumber in wavenumbers:
    resonance_wavelength = 1 / wavenumber  # Resonance wavelength for this wavenumber
    intensities = [
        raman_intensity(laser_intensity, laser_wavelength, resonance_wavelength, proportionality_C)
        for laser_intensity in laser_intensity_range
    ]
    data[f"Raman Intensity ({wavenumber} cm^-1)"] = intensities

# Save to Excel
df = pd.DataFrame(data)
df.to_excel("raman_laser_intensity.xlsx", index=False)
print("Results saved to 'raman_laser_intensity.xlsx'.")

# Plotting
plt.figure(figsize=(10, 6))
for wavenumber in wavenumbers:
    plt.plot(
        data["Laser Intensity (W/cm^2)"],
        data[f"Raman Intensity ({wavenumber} cm^-1)"],
        label=f"{wavenumber} cm$^{{-1}}$"
    )
plt.xlabel("Laser Intensity (W/cm$^2$)")
plt.ylabel("Raman Intensity (arbitrary units)")
plt.title("Raman Intensity vs Laser Intensity for Various Wavenumbers")
plt.legend()
plt.grid(True)
plt.show()
