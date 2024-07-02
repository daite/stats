using Random
using Plots

# Function to simulate the Law of Large Numbers
function simulate_LLN(n_steps::Int, distribution::Function)
    sample_means = zeros(n_steps)  # Array to store sample means
    cumulative_sum = 0.0  # Cumulative sum of samples

    for n in 1:n_steps
        sample = distribution()  # Draw a random sample
        cumulative_sum += sample  # Update cumulative sum
        sample_means[n] = cumulative_sum / n  # Compute sample mean
    end

    return sample_means
end

# Parameters
n_steps = 10000  # Number of samples to draw
true_mean = 0.5  # True mean of the uniform distribution [0,1]
distribution = () -> rand()  # Uniform distribution

# Simulate
sample_means = simulate_LLN(n_steps, distribution)

# Plotting
plot(1:n_steps, sample_means, label="Sample Mean", xlabel="Number of Samples", ylabel="Mean", title="Law of Large Numbers Simulation")
hline!([true_mean], label="True Mean", linestyle=:dash, color=:red)

# Display the plot
display(plot)
