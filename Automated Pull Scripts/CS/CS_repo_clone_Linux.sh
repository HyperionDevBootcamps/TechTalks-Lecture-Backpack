#!/bin/bash
# Cloning the repository with sparse checkout
git clone --filter=blob:none --sparse https://github.com/HyperionDevBootcamps/TechTalks-Lecture-Backpack.git

# Changing directory to the cloned repository
cd TechTalks-Lecture-Backpack

# Adding the specific folders to sparse checkout
git sparse-checkout add "CyberSecurity (CS)"
git sparse-checkout add "StarterPack"
