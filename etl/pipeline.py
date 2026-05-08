import pandas as pd

# -----------------------------
# Load datasets
# -----------------------------
users_df = pd.read_csv("../data/users.csv")
purchases_df = pd.read_csv("../data/purchases.csv")

# -----------------------------
# Join datasets
# -----------------------------
merged_df = pd.merge(
    purchases_df,
    users_df,
    on="user_id",
    how="inner"
)

# -----------------------------
# Create age groups
# -----------------------------
def age_group(age):
    if age >= 50:
        return "G50"
    elif age >= 40:
        return "G40"
    elif age >= 30:
        return "G30"
    else:
        return "G20"

merged_df["age_group"] = merged_df["age"].apply(age_group)

# -----------------------------
# Filter high-value purchases
# -----------------------------
filtered_df = merged_df[merged_df["amount"] > 500]

# -----------------------------
# Aggregate purchase amount
# -----------------------------
result_df = filtered_df.groupby("age_group")["amount"] \
    .sum() \
    .reset_index()

# -----------------------------
# Sort results
# -----------------------------
result_df = result_df.sort_values("age_group")

# -----------------------------
# Save output
# -----------------------------
result_df.to_csv("../output/final_output.csv", index=False)

# -----------------------------
# Print as list of lists
# -----------------------------
final_output = result_df.values.tolist()

print(final_output)
