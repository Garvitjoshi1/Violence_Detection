import os
root_dir = "dataset/RealLifeViolenceDataset"
violence_dir = os.path.join(root_dir, "Violence")
non_violence_dir = os.path.join(root_dir, "NonViolence")

print("Violence directory exists:", os.path.exists(violence_dir))
print("NonViolence directory exists:", os.path.exists(non_violence_dir))
