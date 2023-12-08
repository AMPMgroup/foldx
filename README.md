## FoldX - Predicting changes in protein stability caused by mutation 

### Project: “Characterizing therapeutic antibody interactions”.

#### Task 2: Write a Python code to determine the binding energy changes caused by a certain point mutation at a specific site, such as Ala->Ser. 

Reference:
https://foldxsuite.crg.eu/documentation#manual


FoldX is a software application for molecular modeling and protein design that calculates energy differences that are near to experimental values. FoldX has the ability to reduce a PDB structure, change one or more residues to new residues, analyze protein stability, protein-protein interaction energy, and much more. FoldX is commonly used to anticipate the effect of mutations on a protein's stability or on protein-protein interaction.

To obtain the energy differences in the binding of an antibody-antigen (Ab-Ag) complex due to a specific mutation at a particular position (e.g., Ala to Ser), you can employ the following instructions:
1. Enter the PDB name.
2. Enter the PDB directory: `path/to/pdb-directory`
3. Enter the mutation positions in the following format:
   - WT residue: Enter the wild-type residue (A->Z).
   - Chain: Enter the chain identifier (A->Z).
   - Residue number: Enter the residue number (1->9).
   - Mutant residue: Enter the mutant residue (a->Z).
     The format for specifying mutants is for example LC43a (residue, chain, number, mutation),
     where the mutant residue can have the following options:
     + a: 20 amino acids
     + d: 24 amino acids (includes phosphorylated Tyr, Ser and Thr and hydroxyl Proline)
     + h: {'GLY', 'ALA', 'LEU', 'VAL', 'ILE', 'THR', 'SER', 'CYS', 'MET', 'LYS', 'TRP', 'TYR', 'PHE', 'HIS'}
     + c: {'ARG', 'LYS', 'GLU', 'ASP', 'HIS'}
     + p: {'ARG', 'LYS', 'GLU', 'ASP', 'HIS', 'TRP', 'TYR', 'THR', 'SER', 'GLN', 'ASN'}
     + n: 4 bases (mutates any base to the other three and itself)
     + Or any amino acid in one-letter code, e.g., LC43G
   - Repeat step 3 to add more mutation positions.
4. Enter the output directory where you want to save the results: `path/to/output`.
5. If you type `quit` at any time, the program will stop immediately.
   The program will not proceed to the next step and will exit.
6. The program will generate a configuration file named `config_PS.cfg` and execute the `FoldX --command=PositionScan` program.

FoldX uses output-file as a tag to label different outputs from different commands in batch runs. After running `PositionScan` you'll get five files to look at:
- PS_PS.fxout
- PS_PS_scanning_output.txt
- Unrecognized_molecules.txt
- energies_14_PS.txt
- energies_5_PS.txt

If you need additional information regarding the "PositionScan" command, you may find it useful to consult the provided link
https://foldxsuite.crg.eu/command/PositionScan
