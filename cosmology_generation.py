import numpy as np
import scipy.ndimage
import os

# Output folder: change this to your actual datapack folder
output_dir = r"C:\Users\User\Documents\GitHub\cosmology-data-pack"
os.makedirs(output_dir, exist_ok=True)

# Simulation parameters
size = 32  # grid size
smoothing_scale = 3  # Gaussian smoothing sigma

# Generate Gaussian random field
field = np.random.randn(size, size, size)

# Smooth to mimic large-scale structure coherence
field = scipy.ndimage.gaussian_filter(field, smoothing_scale)

# Calculate mean and std dev for binning
mean = np.mean(field)
std = np.std(field)
print(f"Mean: {mean}, Std: {std}")

def get_block(value):
    if value < mean - std:
        return "air"
    elif value < mean:
        return "light_blue_stained_glass"
    elif value < mean + std:
        return "lime_stained_glass"
    elif value < mean + 2*std:
        return "orange_stained_glass"
    else:
        return "red_stained_glass"

# Write mcfunction file
output_path = os.path.join(output_dir, "output.mcfunction")
with open(output_path, "w") as f:
    for x in range(size):
        for y in range(size):
            for z in range(size):
                block = get_block(field[x, y, z])
                if block != "air":
                    f.write(f"setblock ~{x} ~{y} ~{z} {block}\n")

print(f"File written: {output_path}")
