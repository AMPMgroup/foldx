import sys
import subprocess
import os

def get_mutation_input():
    while True:
        wt_residue = input("Enter the WT residue: ").strip().upper()
        if wt_residue.lower() == "quit":
            sys.exit()
        if not wt_residue.isalpha():
            print(f"Invalid WT residue '{wt_residue}'. Please fill it again.")
            continue

        while True:
            chain = input("Enter the chain: ").strip().upper()
            if chain.lower() == "quit":
                sys.exit()
            if not chain.isalpha():
                print(f"Invalid chain '{chain}'. Please fill it again.")
                continue
            break
        
        while True:
            residue_number = input("Enter the residue number: ").strip()
            if residue_number.lower() == "quit":
                sys.exit()
            if not residue_number.isdigit():
                print(f"Residue number '{residue_number}' is not in the correct format. Please fill it again.")
                continue
            break

        while True: 
            mutant_residue = input("Enter the mutant residue: ").strip()
            if mutant_residue.lower() == "quit":
                sys.exit()
            if not mutant_residue.isalpha():
                print(f"Invalid mutant residue '{mutant_residue}'. Please fill it again.")
                continue
            break

        if mutant_residue.islower() and mutant_residue in ['a', 'd', 'h', 'c', 'n']:
            mutant_residue = mutant_residue.lower()
        else:
            mutant_residue = mutant_residue.upper()

        mutation = (wt_residue, chain, residue_number, mutant_residue)
        return mutation  # Return the mutation value

def save_config_file(positions, pdb_name, pdb_dir):
    config_path = input("Enter the output directory: ")
    if not config_path:
        config_path = "."

    # Create the directory if it doesn't exist
    os.makedirs(config_path, exist_ok=True)

    with open(os.path.join(config_path, "config_PS.cfg"), "w") as file:
        file.write("command=PositionScan\n")
        file.write(f"pdb={pdb_name}.pdb\n")
        file.write(f"pdb-dir={pdb_dir}\n")
        file.write("positions=" + ','.join(positions))

    return config_path

def apply_mutations(mutations):
    # Perform the mutations
    for mutation in mutations:
        residue, chain, residue_number, mutant_residue = mutation[:1], mutation[1], mutation[2:-1], mutation[-1:]
        # Your mutation logic goes here
        print(f"Performing mutation: {residue}{residue_number}{chain} -> {mutant_residue}")

# Provide instructions to the customer
print("To obtain the energy differences in the binding of an antibody-antigen (Ab-Ag) complex due to a specific mutation at a particular position (e.g., Ala to Ser),")
print("you can employ the following instructions:")
print("1. Enter the PDB name.")
print("2. Enter the PDB directory.")
print("3. Enter the mutation positions in the following format:")
print("   - WT residue: Enter the wild-type residue (A->Z).")
print("   - Chain: Enter the chain identifier (A->Z).")
print("   - Residue number: Enter the residue number (1->9).")
print("   - Mutant residue: Enter the mutant residue (a->Z).")
print("     The format for specifying mutants is for example LC43a (residue, chain, number, mutation),")
print("     where the mutant residue can have the following options:")
print("     + a: 20 amino acids")
print("     + d: 24 amino acids (includes phosphorylated Tyr, Ser and Thr and hydroxyl Proline)")
print("     + h: {'GLY', 'ALA', 'LEU', 'VAL', 'ILE', 'THR', 'SER', 'CYS', 'MET', 'LYS', 'TRP', 'TYR', 'PHE', 'HIS'}")
print("     + c: {'ARG', 'LYS', 'GLU', 'ASP', 'HIS'}")
print("     + p: {'ARG', 'LYS', 'GLU', 'ASP', 'HIS', 'TRP', 'TYR', 'THR', 'SER', 'GLN', 'ASN'}")
print("     + n: 4 bases (mutates any base to the other three and itself)")
print("     + Or any amino acid in one-letter code, e.g., LC43G")
print("   - Repeat step 3 to add more mutation positions.")
print("4. Enter the output directory where you want to save the results.")

# Add a separate paragraph for the 'quit' option
print("5. If you type 'quit' at any time, the program will stop immediately.")
print("   The program will not proceed to the next step and will exit.")
print("   Make sure to save your progress before typing 'quit'.")

print("6. The program will generate a configuration file named 'config_PS.cfg' and execute the FoldX program.")

# Get the pdb name from the customer
pdb_name = input("Enter the PDB name: ").strip()
if pdb_name.lower() == "quit":
    sys.exit()

# Get the pdb directory from the customer
pdb_dir = input("Enter the PDB directory: ").strip()
if pdb_dir.lower() == "quit":
    sys.exit()

# List to store the positions
positions = []

# Get position input from the customer
while True:
    mutation = get_mutation_input()

    # Check if the customer wants to quit
    if mutation == ("quit",):
        sys.exit()

    # Add the validated mutation to the list
    positions.append(''.join(mutation))

    # Ask if the customer wants to add more positions
    add_more = input("Do you want to add more positions? (y/n): ")
    if add_more.lower() != 'y':
        break

# Save the positions and other information to the config file
config_path = save_config_file(positions, pdb_name, pdb_dir)

# Apply the mutations
apply_mutations(positions)

# Run FoldX command
subprocess.run(["/home/lucianhu/FoldX/foldx_20231231", "-f", f"{config_path}/config_PS.cfg"], cwd=config_path)


