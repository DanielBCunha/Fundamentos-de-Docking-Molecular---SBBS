import pandas as pd
from pathlib import Path

# Input file
INPUT_FILE = "ligands.tsv"

# Output directories
OUTPUT_DIR = Path("output")
ACTIVE_DIR = OUTPUT_DIR / "active"
INACTIVE_DIR = OUTPUT_DIR / "inactive"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Read TSV file
df = pd.read_csv(INPUT_FILE, sep="\t")

# Convert Standard Value to numeric
df["Standard Value"] = pd.to_numeric(
    df["Standard Value"], errors="coerce"
)

# Separate active and inactive compounds
active = df[df["Standard Value"] < 50]
inactive = df[df["Standard Value"] > 50]

# Export in SMILES ChEMBL_ID format
active[["Smiles", "Molecule ChEMBL ID"]].to_csv(
    OUTPUT_DIR / "actives.smi",
    sep=" ",
    index=False,
    header=False
)

inactive[["Smiles", "Molecule ChEMBL ID"]].to_csv(
    OUTPUT_DIR / "inactives.smi",
    sep=" ",
    index=False,
    header=False
)

# Print summary
print(f"Total compounds: {len(df)}")
print(f"Active compounds (<50): {len(active)}")
print(f"Inactive compounds (>50): {len(inactive)}")
print(f"Compounds with Standard Value = 50: "
      f"{len(df[df['Standard Value'] == 50])}")
print(f"\nOutput saved to: {OUTPUT_DIR.resolve()}")
