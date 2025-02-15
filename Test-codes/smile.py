import pubchempy as pcp

def get_compound_info(compound_name):
    try:
        compound = pcp.get_compounds(compound_name, 'name')[0]  # Search by name

        # Extract required details
        compound_info = {
            "SMILES": compound.isomeric_smiles,
            "Molecular Formula": compound.molecular_formula,
            "Molecular Weight": compound.molecular_weight,
            "IUPAC Name": compound.iupac_name
        }

        return compound_info

    except IndexError:
        return "Compound not found."

# Example Usage
compound_name = "Aspirin"  # Change this to any compound name
result = get_compound_info(compound_name)
print(result)
