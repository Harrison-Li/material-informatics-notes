# Lennard-Jones potential plot
import numpy as np
import matplotlib.pyplot as plt

# Use default font for Latin text
plt.rcParams["font.family"] = "DejaVu Sans"

# Parameters for LJ potential
epsilon = 1.0
sigma = 1.0

# Distance range
r = np.linspace(0, 3.0, 500)

# Lennard-Jones potential
V = 4 * epsilon * ((sigma / r)**12 - (sigma / r)**6)
# Mark the repulsive and attraction region
r_min = 2**(1/6) * sigma

# Plot
plt.figure()
plt.plot(r, V, color='black', label='V(r)')
plt.axvspan(r[0], r_min, alpha=0.2, color='red', label='Repulsive')
plt.axvspan(r_min, r[-1], alpha=0.2, color='blue', label='Attractive')
plt.axvline(r_min, linestyle='--', color='gray')
plt.axhline(0, linestyle='-', color='black', linewidth=0.8)

plt.xlabel("Distance r")
plt.ylim(-1.5, 2)
plt.xlim(0.5, 3)
plt.ylabel("Lennard-Jones Potential V(r)")
plt.title("Lennard-Jones Potential")
plt.legend()
plt.show()



# Create a Morse Potential figure for me
# Parameters for Morse potential
D_e = 1.0  # Depth of the potential well
r_e = 1.0  # Equilibrium distance
a = 2.0    # Width of the potential well

# Morse potential formula
V_morse = D_e * (np.exp(-2 * a * (r - r_e)) - 2 * np.exp(-a * (r - r_e)))

# Plot Morse Potential
plt.figure()
plt.plot(r, V_morse, color='black', label='Morse V(r)')
plt.axvspan(r[0], r_e, alpha=0.2, color='red', label='Repulsive')
plt.axvspan(r_e, r[-1], alpha=0.2, color='blue', label='Attractive')
plt.axvline(r_e, linestyle='--', color='gray')
plt.axhline(0, linestyle='-', color='black', linewidth=0.8)

plt.xlabel("Distance r")
plt.ylim(-1.5, 10)
plt.xlim(0, 3)
plt.ylabel("Morse Potential V(r)")
plt.title("Morse Potential")
plt.legend()
plt.show()


# Buckingham potential
def buckingham_potential(r, A, B, C):
    """
    V(r) = A * exp(-B * r) - C / r^6
    """
    return A * np.exp(-B * r) - C / r**6

# Example Parameters (Generic units)
A = 1.5e5  # Repulsive strength
B = 3.8    # Repulsive range parameter
C = 500.0  # Attractive constant

# Generate distance (r) values
# We start above 0 to avoid the singularity at r=0
r = np.linspace(1.2, 5.0, 500)
v_r = buckingham_potential(r, A, B, C)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(r, v_r, label='Buckingham Potential', color='blue', linewidth=2)

# Add a horizontal line at V=0 for reference
plt.axhline(0, color='black', linestyle='--', linewidth=1)

# Set limits to see the potential well clearly
plt.ylim(-200, 400)
plt.xlim(1.2, 5.0)

# Labels and title
plt.xlabel('Distance (r)', fontsize=12)
plt.ylabel('Potential Energy V(r)', fontsize=12)
plt.title('Buckingham Potential Plot', fontsize=14)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

plt.show()