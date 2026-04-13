### Observation Note – Git History ###

# Merge Commit

The commit graph shows branching and merging (e.g., Merge pull request #2 from vardannikhilphd/feature-visualisation).
All individual commits from the feature branch are preserved (src/visualize_data.py added, visual plots added).
History is detailed and transparent, but looks more complex.
Best when you want to trace the full development process step by step.

# Squash Merge

All commits from the feature branch are collapsed into a single commit on main.
History looks linear — no branching structure is shown.
Easier to read, but loses granular commit details (you won’t see each file addition separately).
Best when you want a clean, concise history without intermediate steps.

# Missing Value Strategy 

For this project, missing numeric values are handled using median imputation to reduce the effect of extreme 
values. 

# Visualisation Plan

We will generate plots to study score variation and environmental conditions. 