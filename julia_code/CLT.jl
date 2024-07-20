using Random
using Statistics
using Plots
using Distributions

# Function to simulate the Central Limit Theorem
function simulate_CLT(pop_mean::Float64, pop_std::Float64, sample_size::Int, num_samples::Int)
    sample_means = zeros(num_samples)  # Array to store sample means

    for i in 1:num_samples
        sample = rand(Normal(pop_mean, pop_std), sample_size)  # Draw a sample from the normal distribution
        sample_means[i] = mean(sample)  # Calculate and store the sample mean
    end

    return sample_means
end

# Parameters
pop_mean = 170.0  # Population mean (as Float64)
pop_std = 7.0  # Population standard deviation (as Float64)
sample_size = 100  # Sample size
num_samples = 10000  # Number of samples

# Simulate
sample_means = simulate_CLT(pop_mean, pop_std, sample_size, num_samples)

# Create plots
p1 = histogram(sample_means, bins=50, density=true, alpha=0.6, label="Sample Means", title="Histogram of Sample Means", xlabel="Sample Mean", ylabel="Density")

# Theoretical normal distribution plot
theoretical_mean = pop_mean
theoretical_std = pop_std / sqrt(sample_size)
x = range(minimum(sample_means), stop=maximum(sample_means), length=1000)
y = pdf.(Normal(theoretical_mean, theoretical_std), x)
p2 = plot(x, y, label="Theoretical Normal Distribution", lw=2, color=:red, title="Theoretical Normal Distribution", xlabel="Sample Mean", ylabel="Density")

# Combine plots in a 1x2 grid
plot(p1, p2, layout = (1, 2))
