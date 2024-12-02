# Release notes for nbl_v1.2

This version is a circumscribed view of the NBL dictionary that was made specifically for the inclusion of relapse and response data from the SIOPEN BEACON study.

Collaborators included: Mei Li (D4CG), Michael Watkins (D4CG), Brian Furner (D4CG), Sue Cohn (INRG), Andy Pearson (INRG), Lucas Moreno (INRG), and Wendy London (INRG).


Added concepts:
>[Subject Characteristics].[AGE_AT_ENROLLMENT]

>[Subject Characteristics].[YEAR_AT_ENROLLMENT]

>[Disease Phase Timing].[HONEST_BROKER_SUBJECT_ID]

>[Disease Phase Timing].[DISEASE_PHASE].[Relapse/Progression]

>[Course Timing]

>[Course Timing].[HONEST_BROKER_SUBJECT_ID]

>[Course Timing].[CYCLE_NUMBER]

>[Course Timing].[AGE_AT_CYCLE_START]

>[Course Timing].[AGE_AT_CYCLE_END]

>[Demographics].[HONEST_BROKER_SUBJECT_ID]

>[Survival Characteristics].[HONEST_BROKER_SUBJECT_ID]

>[Survival Characteristics].[DISEASE_PHASE].[Relapse/Progression]

>[Survival Characteristics].[CAUSE_OF_DEATH].[Secondary Malignancy]

>[Survival Characteristics].[CAUSE_OF_DEATH].[Unrelated to Disease or Treatment]

>[Tumor Assessment].[HONEST_BROKER_SUBJECT_ID]

>[Tumor Assessment].[DISEASE_PHASE].[Relapse/Progression]

>[Staging].[HONEST_BROKER_SUBJECT_ID]

>[Histology].[HONEST_BROKER_SUBJECT_ID]

>[Histology].[HISTOLOGY_GRADE].[Grade 3]

>[Labs].[HONEST_BROKER_SUBJECT_ID]

>[Labs].[DISEASE_PHASE].[Relapse/Progression]

>[nbl_v1.1].[Labs].[LAB_RESULT_NUMERIC] skos:exactMatch [nbl_v1.2].[Labs].[RESULT_NUMERIC]

>[Labs].[RESULT_UNIT]

>[Labs].[RESULT_UNIT].[U/L]

>[Labs].[RESULT_UNIT].[µg/L]

>[Molecular Analysis].[HONEST_BROKER_SUBJECT_ID]

>[Molecular Analysis].[DISEASE_PHASE].[Relapse/Progression]

>[Secondary Malignant Neoplasm].[HONEST_BROKER_SUBJECT_ID]

>[Secondary Malignant Neoplasm].[DISEASE_PHASE].[Relapse/Progression]

>[Stem Cell Transplant]

>[Stem Cell Transplant].[HONEST_BROKER_SUBJECT_ID]

>[Stem Cell Transplant].[DISEASE_PHASE]

>[Stem Cell Transplant].[DISEASE_PHASE].[Initial Diagnosis]

>[Stem Cell Transplant].[DISEASE_PHASE_NUMBER]

>[Stem Cell Transplant].[SCT_TYPE]

>[Stem Cell Transplant].[SCT_TYPE].[Autologous, Single]

>[Stem Cell Transplant].[SCT_TYPE].[Autologous, Tandem]

>[Stem Cell Transplant].[SCT_TYPE].[Unknown]

>[Stem Cell Transplant].[SCT_TYPE].[Not Reported]

>[Stem Cell Transplant].[TREATMENT_ASSIGNED]

>[Stem Cell Transplant].[TREATMENT_ASSIGNED].[Yes]

>[Stem Cell Transplant].[TREATMENT_ASSIGNED].[No]

>[Biopsy and Surgical Procedures]

>[Biopsy and Surgical Procedures].[HONEST_BROKER_SUBJECT_ID]

>[Biopsy and Surgical Procedures].[DISEASE_PHASE]

>[Biopsy and Surgical Procedures].[DISEASE_PHASE].[Initial Diagnosis]

>[Biopsy and Surgical Procedures].[DISEASE_PHASE_NUMBER]

>[Biopsy and Surgical Procedures].[PROCEDURE]

>[Biopsy and Surgical Procedures].[PROCEDURE].[Surgical Resection]

>[Biopsy and Surgical Procedures].[TREATMENT_PERFORMED]

>[Biopsy and Surgical Procedures].[TREATMENT_PERFORMED].[Yes]

>[Biopsy and Surgical Procedures].[TREATMENT_PERFORMED].[No]

>[Total Dose]

>[Total Dose].[HONEST_BROKER_SUBJECT_ID]

>[Total Dose].[DISEASE_PHASE]

>[Total Dose].[DISEASE_PHASE].[Initial Diagnosis]

>[Total Dose].[DISEASE_PHASE_NUMBER]

>[Total Dose].[REGIMEN].[GPOH Induction]

>[Total Dose].[REGIMEN].[COJEC]

>[Total Dose].[REGIMEN].[N7]

>[Total Dose].[REGIMEN].[COJEC+TVD]

>[Total Dose].[REGIMEN].[Other]

>[Total Dose].[REGIMEN_OTHER]

>[Total Dose].[ANTINEOPLASTIC_AGENT]

>[Total Dose].[ANTINEOPLASTIC_AGENT].[Dinutuximab-beta]

>[Total Dose].[ANTINEOPLASTIC_AGENT].[Crizotinib]

>[Total Dose].[ANTINEOPLASTIC_AGENT].[Lorlatinib]

>[Total Dose].[ANTINEOPLASTIC_AGENT].[MIBG]

>[Total Dose].[TREATMENT_ASSIGNED]

>[Total Dose].[TREATMENT_ASSIGNED].[Yes]

>[Total Dose].[TREATMENT_ASSIGNED].[No]

>[Radiation Therapy].[HONEST_BROKER_SUBJECT_ID]

>[Radiation Therapy].[DISEASE_PHASE]

>[Radiation Therapy].[DISEASE_PHASE].[Initial Diagnosis]

>[Radiation Therapy].[DISEASE_PHASE_NUMBER]

>[Radiation Therapy].[TREATMENT_PERFORMED]

>[Radiation Therapy].[TREATMENT_PERFORMED].[Yes]

>[Radiation Therapy].[TREATMENT_PERFORMED].[No]

>[Subject Response]

>[Subject Response].[HONEST_BROKER_SUBJECT_ID]

>[Subject Response].[DISEASE_PHASE]

>[Subject Response].[DISEASE_PHASE].[Refractory]

>[Subject Response].[DISEASE_PHASE].[Relapse/Progression]

>[Subject Response].[DISEASE_PHASE_NUMBER]

>[Subject Response].[CYCLE_NUMBER]

>[Subject Response].[RESPONSE_CATEGORY]

>[Subject Response].[RESPONSE_CATEGORY].[Overall Response]

>[Subject Response].[RESPONSE_CATEGORY].[Primary Site Response]

>[Subject Response].[RESPONSE_CATEGORY].[Bone Marrow Response]

>[Subject Response].[RESPONSE_CATEGORY].[Metastatic Soft Tissue and Bone Response]

>[Subject Response].[RESPONSE]

>[Subject Response].[RESPONSE].[RECIST, Complete Response]

>[Subject Response].[RESPONSE].[RECIST, Partial Response]

>[Subject Response].[RESPONSE].[RECIST, Stable Disease]

>[Subject Response].[RESPONSE].[RECIST, Progressive Disease]

>[Subject Response].[RESPONSE].[INRC Park 2017, Complete Response]

>[Subject Response].[RESPONSE].[INRC Park 2017, Partial Response]

>[Subject Response].[RESPONSE].[INRC Park 2017, Stable Disease]

>[Subject Response].[RESPONSE.[INRC Park 2017, Minor Response]

>[Subject Response].[RESPONSE].[INRC Park 2017, Minimal Disease]

>[Subject Response].[RESPONSE].[INRC Park 2017, Progressive Disease]

>[Subject Response].[RESPONSE].[Not Evaluable]

>[Subject Response].[RESPONSE].[Not Done]

>[Subject Response].[RESPONSE].[Unknown]

>[Subject Response].[RESPONSE].[Not Involved]

>[Subject Response].[MIBG_SCORE_TYPE]

>[Subject Response].[MIBG_SCORE_TYPE].[MIBG SIOPEN Score]

>[Subject Response].[MIBG_SCORE]

Removed concepts:
>None. However, there are many concepts not shown in this version that will persist in the full NBL dictionary.

Modified concepts:
>[nbl_v1.1].[Disease Characteristics].[MKI] skos:exactMatch [nbl_v1.2].[Histology].[MKI]

>[nbl_v1.1].[Disease Characteristics].[MKI].[Intermediate (2-4% or 100 to <200/5,000 cells)] skos:exactMatch [nbl_v1.2].[Histology].[MKI].[Intermediate (2-4% or 100 to <200/5,000 cells)]

>[nbl_v1.1].[Disease Characteristics].[MKI].[High (>4% or >200/5,000 cells)] skos:exactMatch [nbl_v1.2].[Histology].[MKI].[High (>4% or >200/5,000 cells)]

>[nbl_v1.1].[Disease Characteristics].[MKI].[Unknown] skos:exactMatch [nbl_v1.2].[Histology].[MKI].[Unknown]

>[nbl_v1.1].[Disease Characteristics].[MKI].[Not Reported] skos:exactMatch [nbl_v1.2].[Histology].[MKI].[Not Reported]
