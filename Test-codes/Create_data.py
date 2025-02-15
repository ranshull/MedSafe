# import pandas as pd
# import pubchempy as pcp

# # Load the CSV file
# input_file = "Drug_data\Atenolol_response.csv"  # Replace with your actual filename
# df = pd.read_csv(input_file)

# # Initialize a list to store fetched data
# drug_data = []

# # Function to fetch drug info
# def get_compound_info(drug_name):
#     try:
#         compound = pcp.get_compounds(drug_name, 'name')[0]  # Fetch by drug name
#         return {
#             "DBID2": drug_name,
#             "SMILES": compound.isomeric_smiles,
#             "Molecular Formula": compound.molecular_formula,
#             "Molecular Weight": compound.molecular_weight,
#             "IUPAC Name": compound.iupac_name
#         }
#     except (IndexError, Exception):
#         return {
#             "DBID2": drug_name,
#             "SMILES": None,
#             "Molecular Formula": None,
#             "Molecular Weight": None,
#             "IUPAC Name": None
#         }

# # Loop through each DBID2 and fetch information
# for drug_id in df["dbid2"].unique():  # Use unique values to avoid redundancy
#     drug_info = get_compound_info(drug_id)
#     drug_data.append(drug_info)

# # Convert to DataFrame
# output_df = pd.DataFrame(drug_data)

# # Save to CSV
# output_df.to_csv("Model_Dataset.csv", index=False)

# print("Data fetching complete. Saved as Model_Dataset.csv")

# # ------------------------------------------------------------------------------------------------------------------
# # this one works

import pandas as pd
import pubchempy as pcp

# Load the CSV file
input_file = "Drug_data\Atenolol_response.csv"  # Replace with your actual filename
df = pd.read_csv(input_file)

# Get the first 500 unique drug IDs from 'dbid2'
drug_ids = df["dbid2"].dropna().unique()[:500]  

# Initialize a list to store fetched data
drug_data = []

# Function to fetch drug info
def get_compound_info(drug_name):
    try:
        compound = pcp.get_compounds(drug_name, 'name')[0]  # Fetch by drug name

        # Check if all values are present
        if compound.isomeric_smiles and compound.molecular_formula and compound.molecular_weight and compound.iupac_name:
            return {
                # "DBID2": drug_name,
                # "SMILES": compound.isomeric_smiles,
                # "Molecular Formula": compound.molecular_formula,
                # "Molecular Weight": compound.molecular_weight,
                # "IUPAC Name": compound.iupac_name
                "DBID2": drug_name,
                "SMILES": compound.isomeric_smiles,
                "Molecular Formula": compound.molecular_formula,
                "Molecular Weight": compound.molecular_weight,
                "IUPAC Name": compound.iupac_name,
                "logP": properties.get("XLogP", None),
                "Polar Surface Area": properties.get("TPSA", None),
                "H-bond Donors": properties.get("HBondDonorCount", None),
                "H-bond Acceptors": properties.get("HBondAcceptorCount", None),
                "Rotatable Bonds": properties.get("RotatableBondCount", None)
            }
    except (IndexError, Exception):
        return None  # Skip if not found or any error occurs

# Loop through drug IDs and fetch information
for drug_id in drug_ids:
    drug_info = get_compound_info(drug_id)
    if drug_info:  # Add only if all values are present
        drug_data.append(drug_info)

# Convert to DataFrame
output_df = pd.DataFrame(drug_data)

# Save to CSV
output_df.to_csv("Model_Dataset.csv", index=False)

print(f"Data fetching complete. Saved {len(output_df)} records in Model_Dataset.csv")


# new faster program
