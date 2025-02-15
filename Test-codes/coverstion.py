# import scipy.io
# import pandas as pd
# mat = scipy.io.loadmat('"C:\Users\SUKHPAL SINGH RAWAT\Downloads\DDI_data_SR.mat"') 
# mat = {k:v for k, v in mat.items() if k[0] != '_'}
# data = pd.DataFrame({k: pd.Series(v[0]) for k, v in mat.iteritems()})
# data.to_csv("DDI.csv")
import pubchempy as pcp

def get_pubchem_id_from_name(drug_name):
    try:
        compound = pcp.get_compounds(drug_name, 'name')
        if compound:
            return compound[0].cid
        else:
            return None
    except Exception as e:
        print(f"Error fetching PubChem ID for {drug_name}: {e}")
        return None

def get_name_from_pubchem_id(pubchem_id):
    try:
        compound = pcp.Compound.from_cid(pubchem_id)
        return compound.iupac_name
    except Exception as e:
        print(f"Error fetching name for PubChem ID {pubchem_id}: {e}")
        return None

if __name__ == "__main__":
    choice = input("Enter 1 to get PubChem ID from name, 2 to get name from PubChem ID: ")
    
    if choice == "1":
        name = input("Enter drug name: ")
        pubchem_id = get_pubchem_id_from_name(name)
        print(f"PubChem ID: {pubchem_id}" if pubchem_id else "Drug not found.")
    elif choice == "2":
        pubchem_id = input("Enter PubChem ID: ")
        name = get_name_from_pubchem_id(pubchem_id)
        print(f"Drug Name: {name}" if name else "ID not found.")
    else:
        print("Invalid choice.")