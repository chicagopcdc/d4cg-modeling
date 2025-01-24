# Release notes for nrsts_v2.0

This version was used for the first round of a large backlog of modeling changes that affected several dictionaries—all tied to pcdc_v2.0.

Added concepts:
>[Subject Characteristics].[CONSORTIUM]

>[Subject Characteristics].[DISEASE_GROUP]

>[Subject Characteristics].[DATA_CONTRIBUTOR_ID].[AIEOP]

>[Subject Characteristics].[DATA_CONTRIBUTOR_ID].[COG]

>[Subject Characteristics].[DATA_CONTRIBUTOR_ID].[EpSSG]

>[Subject Characteristics].[DATA_CONTRIBUTOR_ID].[SIOP MMT]

>[Subject Characteristics].[DATA_CONTRIBUTOR_ID].[CWS]

>[Subject Characteristics].[DATA_CONTRIBUTOR_ID].[STSC]

>[Time Period]

>[Time Period].[HONEST_BROKER_SUBJECT_ID]

>[Time Period].[SUBMITTER_ID]

>[Time Period].[PARENT_SUBMITTER_ID]

>[Time Period].[TIME_PERIOD_TYPE]

>[Time Period].[TIME_PERIOD_NUMBER]

>[Time Period].[YEAR_AT_START]

>[Time Period].[AGE_AT_START]

>[Time Period].[AGE_AT_END]

>[Demographics].[HONEST_BROKER_SUBJECT_ID]

>[Medical History].[HONEST_BROKER_SUBJECT_ID]

>[Survival Characteristics].[HONEST_BROKER_SUBJECT_ID]

>[Molecular Analysis].[HONEST_BROKER_SUBJECT_ID]

>[Diagnosis].[HONEST_BROKER_SUBJECT_ID]

>[Diagnosis].[DIAGNOSIS_BASIS]

>[Disease Site Assessment].[HONEST_BROKER_SUBJECT_ID]

>[Disease Site Assessment].[DIAMETER1_UNIT]

>[Disease Site Assessment].[DIAMETER2_UNIT]

>[Disease Site Assessment].[DIAMETER3_UNIT]

>[Radiation Therapy].[HONEST_BROKER_SUBJECT_ID]

>[Biopsy And Surgical Procedures].[HONEST_BROKER_SUBJECT_ID]

>[Subject Response].[HONEST_BROKER_SUBJECT_ID]

>[Subsequent Malignant Neoplasm].[HONEST_BROKER_SUBJECT_ID]

Removed concepts:
>[Subject Identifier]

>[Subject Identifier].[PCDC_SUBJECT_ID]

>[Disease Phase Timing]

>[Course Timing]

Modified Concepts:
>[nrsts_v1.0].[Disease Phase Timing].[DISEASE_PHASE] skos:exactMatch [nrsts_v2.0].[Time Period].[DISEASE_PHASE]

>[nrsts_v1.0].[Course Timing].[COURSE] skos:exactMatch [nrsts_v2.0].[Time Period].[COURSE]

>[nrsts_v1.0].[Disease Phase Timing].[DISEASE_PHASE_NUMBER] skos:broadMatch [nrsts_v2.0].[Time Period].[TIME_PERIOD_NUMBER]

>[nrsts_v1.0].[Disease Phase Timing].[AGE_AT_DISEASE_PHASE] skos:broadMatch [nrsts_v2.0].[Time Period].[AGE_AT_START]

>[nrsts_v1.0].[Disease Phase Timing].[YEAR_AT_DISEASE_PHASE] skos:exactMatch [nrsts_v2.0].[Time Period].[YEAR_AT_START]

>[nrsts_v1.0].[Course Timing].[COURSE_NUMBER] skos:broadMatch [nrsts_v2.0].[Time Period].[TIME_PERIOD_NUMBER]

>[nrsts_v1.0].[Course Timing].[AGE_AT_COURSE_START] skos:broadMatch [nrsts_v2.0].[Time Period].[AGE_AT_START]

>[nrsts_v1.0].[Course Timing].[AGE_AT_COURSE_END] skos:exactMatch [nrsts_v2.0].[Time Period].[AGE_AT_END]

>[nrsts_v1.0].[Medical History].[MEDICAL_HISTORY] skos:exactMatch [nrsts_v2.0].[Medical History].[CONDITION]

>[nrsts_v1.0].[Histology] skos:exactMatch [nrsts_v2.0].[Diagnosis]

>[nrsts_v1.0].[Histology].[AGE_AT_HIST_ASSESSMENT] skos:exactMatch [nrsts_v2.0].[Diagnosis].[AGE_AT_DIAG_ASSESSMENT]

>[nrsts_v1.0].[Histology].[HISTOLOGY] skos:exactMatch [nrsts_v2.0].[Diagnosis].[DIAGNOSIS]

>[nrsts_v1.0].[Tumor Assessment] skos:exactMatch [nrsts_v2.0].[Disease Site Assessment]

>[nrsts_v1.0].[Tumor Assessment].[AGE_AT_TUMOR_ASSESSMENT] skos:exactMatch [nrsts_v2.0].[Disease Site Assessment].[AGE_AT_DISEASE_SITE_ASSESSMENT]

>[nrsts_v1.0].[Tumor Assessment].[TUMOR_CLASSIFICATION] skos:exactMatch [nrsts_v2.0].[Disease Site Assessment].[CLASSIFICATION]

>[nrsts_v1.0].[Tumor Assessment].[TUMOR_SITE] skos:exactMatch [nrsts_v2.0].[Disease Site Assessment].[SITE]

>[nrsts_v1.0].[Tumor Assessment].[TUMOR_SITE_OTHER] skos:exactMatch [nrsts_v2.0].[Disease Site Assessment].[SITE_OTHER]

>[nrsts_v1.0].[Tumor Assessment].[LONGEST_DIAM_DIM1] skos:exactMatch [nrsts_v2.0].[Disease Site Assessment].[DIAMETER1]

>[nrsts_v1.0].[Tumor Assessment].[LONGEST_DIAM_DIM2] skos:exactMatch [nrsts_v2.0].[Disease Site Assessment].[DIAMETER2]

>[nrsts_v1.0].[Tumor Assessment].[LONGEST_DIAM_DIM3] skos:exactMatch [nrsts_v2.0].[Disease Site Assessment].[DIAMETER3]

>[nrsts_v1.0].[Radiation Therapy].[TUMOR_CLASSIFICATION] skos:exactMatch [nrsts_v2.0].[Radiation Therapy].[CLASSIFICATION]

>[nrsts_v1.0].[Radiation Therapy].[RT_SITE] skos:exactMatch [nrsts_v2.0].[Radiation Therapy].[SITE]

>[nrsts_v1.0].[Radiation Therapy].[RT_DOSE] skos:exactMatch [nrsts_v2.0].[Radiation Therapy].[DOSE]

>[nrsts_v1.0].[Radiation Therapy].[RT_UNIT] skos:exactMatch [nrsts_v2.0].[Radiation Therapy].[DOSE_UNIT]

>[nrsts_v1.0].[Biopsy/Surgical Procedures] skos:exactMatch [nrsts_v2.0].[Biopsy And Surgical Procedures]

>[nrsts_v1.0].[Biopsy/Surgical Procedures].[TUMOR_CLASSIFICATION] skos:exactMatch [nrsts_v2.0].[Biopsy And Surgical Procedures].[CLASSIFICATION]

>[nrsts_v1.0].[Biopsy/Surgical Procedures].[PROCEDURE_SITE] skos:exactMatch [nrsts_v2.0].[Biopsy And Surgical Procedures].[SITE]

>[nrsts_v1.0].[Secondary Malignant Neoplasm] skos:exactMatch [nrsts_v2.0].[Subsequent Malignant Neoplasm]

>[nrsts_v1.0].[Secondary Malignant Neoplasm].[SMN_SITE] skos:exactMatch [nrsts_v2.0].[Subsequent Malignant Neoplasm].[SITE]
