# Ordinary Least Squares, OLS
using Random
using Plots
using Statistics  # Import Statistics module for mean function

# Step 1: Generate Simulated Data
Random.seed!(0)  # Set seed for reproducibility
x = [70, 80, 90, 60, 85]  # Korean scores
true_slope = 0.5
true_intercept = 50
noise = randn(length(x)) .* 5  # Random noise
y = true_intercept .+ true_slope .* x .+ noise  # English scores with noise

# Step 2: Calculate Regression Coefficients (Least Squares Method)
# Mean of x and y
x_mean = mean(x)
y_mean = mean(y)

# Calculate slope (b)
b = sum((x .- x_mean) .* (y .- y_mean)) / sum((x .- x_mean) .^ 2)

# Calculate intercept (a)
a = y_mean - b * x_mean

# Step 3: Calculate Predicted Values
y_pred = a .+ b .* x

# Step 4: Calculate Residuals
residuals = y .- y_pred

# Step 5: Plot Results in a 1x2 Grid
# Define the layout for the grid
p1 = plot(x, y, seriestype = :scatter, label = "Actual Data", color = :blue, marker = :circle, size = (600, 300), xlabel = "Korean Scores", ylabel = "English Scores")
plot!(p1, x, y_pred, label = "Regression Line: y = $(round(a, digits=2)) + $(round(b, digits=2))x", color = :red)

# Plot residuals
p2 = plot(x, residuals, seriestype = :scatter, label = "Residuals", color = :green, marker = :cross, size = (600, 300), xlabel = "Korean Scores", ylabel = "Residuals")
hline!(p2, [0], color = :black, linestyle = :dash, label = "Zero Residual Line")

# Create a 1x2 grid layout
plot(p1, p2, layout = (1, 2))

# Print the coefficients and residuals
println("Intercept (a): ", round(a, digits=2))
println("Slope (b): ", round(b, digits=2))
println("Residuals: ", residuals)
