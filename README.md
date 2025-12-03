# d4cg-modeling

This repo archives the schemas and dictionaries created and maintained by the D4CG Data Standards and Modeling (DSM) team. 

# Ancitipated workflow
Since most of D4CG's external subject matter experts are typically not data scientists, the D4CG Data Standards and Modeling (DSM) team uses tabular data dictionaries on Google Sheets for consensus data modeling. These three Python scripts facilitate the process of detecting changes from those data dictionaries (sync.py), updating the appropriate schema (update.py), and exporting fresh tabular data dictionaries out to the Google Sheeets locations (export.py). Details on each process are described below: 

## sync.py
This script parses in a data dictionary from Google Sheets and compares it to its designated schema. If there are any changes detected, proposed updates are saved into a task file.

## update.py
This script makes the updates in the task file mentioned above to the appropriate schema.

## export.py
This script creates a fresh tabular data dictionary for the designated disease group (subset) from the updated schema and exports it to its Google Sheets location.
