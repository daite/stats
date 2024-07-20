import numpy as np
import matplotlib.pyplot as plt
import imageio

# Function to roll dice
def roll_dice(n):
    return np.random.randint(1, 7, n)

# Function to simulate Law of Large Numbers
def simulate_lln(max_n):
    sample_sizes = np.arange(2, max_n + 1)
    dice_rolls = roll_dice(max_n)
    sample_means = [np.mean(dice_rolls[:n]) for n in sample_sizes]
    return sample_sizes, sample_means

# Settings
max_n = 5000
sample_sizes, sample_means = simulate_lln(max_n)

# Create frames for the GIF
frames = []
for i in range(2, max_n, 10):
    fig, ax = plt.subplots()
    ax.plot(sample_sizes[:i], sample_means[:i], label='Sample Mean')
    ax.axhline(y=3.5, color='r', linestyle='-', label='Population Mean')
    ax.set_xlabel('Sample Size (n)')
    ax.set_ylabel('Sample Mean')
    ax.set_title('Law of Large Numbers Simulation')
    ax.legend()
    
    # Save frame
    plt.savefig('frame.png')
    frames.append(imageio.imread('frame.png'))
    plt.close(fig)

# Save frames as GIF
imageio.mimsave('lln_simulation.gif', frames, duration=0.1)
