using Random, Statistics, GLM, DataFrames, Plots

# Seed for reproducibility
Random.seed!(1234)

# Number of students
n_students = 50

# Generate math scores (randomly between 50 and 100)
math_scores = rand(50:100, n_students)

# Generate science scores with some correlation to math scores
science_scores = math_scores .+ rand(-10:10, n_students)

# Create a DataFrame
df = DataFrame(math_scores=math_scores, science_scores=science_scores)

# Perform linear regression
model = lm(@formula(science_scores ~ math_scores), df)

# Calculate Pearson correlation coefficient
correlation = cor(math_scores, science_scores)

# Determine correlation strength
function correlation_strength(r)
    abs_r = abs(r)
    if abs_r < 0.3
        return "Weak"
    elseif abs_r < 0.5
        return "Moderate"
    elseif abs_r < 0.7
        return "Strong"
    else
        return "Very Strong"
    end
end

strength = correlation_strength(correlation)

# Print the correlation coefficient and strength
println("Pearson correlation coefficient: ", correlation)
println("Correlation strength: ", strength)

# Scatter plot with regression line
p = scatter(math_scores, science_scores, xlabel="Math Scores", ylabel="Science Scores",
        title="Scatter Plot of Math and Science Scores", legend=false)
plot!(math_scores, predict(model), color=:red, label="Regression Line")

# Annotate the plot with the Pearson correlation coefficient and strength
annotate!(60, 90, text("Pearson correlation: $(round(correlation, digits=2))\nStrength: $strength", :left, 12, "blue"))

# Show the plot
# plot!()
display(p)
readline()
