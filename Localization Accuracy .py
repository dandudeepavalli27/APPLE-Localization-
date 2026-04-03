# SESSION 35 – Localization Accuracy Check

# Step 1: Input values
error = 0.08      # pose error in meters
threshold = 0.1   # acceptable error

# Step 2: Check accuracy
if error < threshold:
    print("Accurate Localization")
else:
    print("Localization Error High")

print("\nProgram Executed Successfully")
