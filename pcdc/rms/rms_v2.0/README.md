# Release notes for rms_v2.0

This version was used for the first round of a large backlog of modeling changes that affected several dictionaries—all tied to pcdc_v2.0.

Added concepts:
>[Subject Characteristics].[CONSORTIUM]

>[Subject Characteristics].[DISEASE_GROUP]

>[Subject Characteristics].[DATA_CONTRIBUTOR_ID].[COG]

>[Subject Characteristics].[DATA_CONTRIBUTOR_ID].[EpSSG]

>[Subject Characteristics].[DATA_CONTRIBUTOR_ID].[CWS]

>[Subject Characteristics].[DATA_CONTRIBUTOR_ID].[MMT]

>[Subject Characteristics].[DATA_CONTRIBUTOR_ID].[STSC]

>[Subject Characteristics].[STUDY_ID].[ARST0331]

>[Subject Characteristics].[STUDY_ID].[ARST0431]

>[Subject Characteristics].[STUDY_ID].[ARST0531]

>[Subject Characteristics].[STUDY_ID].[ARST08P1]

>[Subject Characteristics].[STUDY_ID].[D9602]

>[Subject Characteristics].[STUDY_ID].[D9802]

>[Subject Characteristics].[STUDY_ID].[D9803]

>[Subject Characteristics].[STUDY_ID].[RMS2005]

>[Subject Characteristics].[STUDY_ID].[MTS2008]

>[Subject Characteristics].[STUDY_ID].[ICG RMS96]

>[Subject Characteristics].[STUDY_ID].[RMS 4.99]

>[Subject Characteristics].[STUDY_ID].[CWS-IV-2002]

>[Subject Characteristics].[STUDY_ID].[CWS2002P]

>[Subject Characteristics].[STUDY_ID].[CWS91]

>[Subject Characteristics].[STUDY_ID].[CWS96]

>[Subject Characteristics].[STUDY_ID].[MMT95]

>[Subject Characteristics].[TREATMENT_ARM].[ARST0331:Regimen I]

>[Subject Characteristics].[TREATMENT_ARM].[ARST0331:Regimen II]

>[Subject Characteristics].[TREATMENT_ARM].[ARST0431:High Risk Rhabdomyosarcoma]

>[Subject Characteristics].[TREATMENT_ARM].[ARST0531:Arm I (Chemotherapy, Radiotherapy)]

>[Subject Characteristics].[TREATMENT_ARM].[ARST0531:Arm II (Chemotherapy, Radiotherapy)]

>[Subject Characteristics].[TREATMENT_ARM].[ARST08P1:Group 1 (Chemotherapy, Radiation Therapy, Cixutumumab)]

>[Subject Characteristics].[TREATMENT_ARM].[D9602:Subgroup A]

>[Subject Characteristics].[TREATMENT_ARM].[D9602:Subgroup B]

>[Subject Characteristics].[TREATMENT_ARM].[D9802]

>[Subject Characteristics].[TREATMENT_ARM].[D9803]

>[Subject Characteristics].[TREATMENT_ARM].[RMS2005]

>[Subject Characteristics].[TREATMENT_ARM].[MTS2008]

>[Subject Characteristics].[TREATMENT_ARM].[ICG RMS96]

>[Subject Characteristics].[TREATMENT_ARM].[RMS 4.99]

>[Subject Characteristics].[TREATMENT_ARM].[CWS-IV-2002]

>[Subject Characteristics].[TREATMENT_ARM].[CWS2002P:LR]

>[Subject Characteristics].[TREATMENT_ARM].[CWS2002P:SR]

>[Subject Characteristics].[TREATMENT_ARM].[CWS2002P:HR]

>[Subject Characteristics].[TREATMENT_ARM].[CWS2002P:VHR]

>[Subject Characteristics].[TREATMENT_ARM].[CWS91]

>[Subject Characteristics].[TREATMENT_ARM].[CWS96:High Dose Therapy (HDT)]

>[Subject Characteristics].[TREATMENT_ARM].[CWS96:Oral Maintenance Therapy (OMT)]

>[Subject Characteristics].[TREATMENT_ARM].[MMT95]

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

>[Survival Characteristics].[HONEST_BROKER_SUBJECT_ID]

>[Molecular Analysis].[HONEST_BROKER_SUBJECT_ID]

>[Diagnosis].[HONEST_BROKER_SUBJECT_ID]

>[Diagnosis].[DIAGNOSIS_BASIS]

>[Staging].[HONEST_BROKER_SUBJECT_ID]

>[Disease Site Assessment].[HONEST_BROKER_SUBJECT_ID]

>[Disease Site Assessment].[DIAMETER1_UNIT]

>[Disease Site Assessment].[DIAMETER2_UNIT]

>[Disease Site Assessment].[DIAMETER3_UNIT]

>[Radiation Therapy].[HONEST_BROKER_SUBJECT_ID]

>[Biopsy And Surgical Procedures].[HONEST_BROKER_SUBJECT_ID]

>[Biopsy And Surgical Procedures].[TIME_PERIOD_SUBMITTER_ID]

>[Subject Response].[HONEST_BROKER_SUBJECT_ID]





>[Subsequent Malignant Neoplasm].[HONEST_BROKER_SUBJECT_ID]

>[Subsequent Malignant Neoplasm].[MORPH_CODE_SYSTEM]

>[Subsequent Malignant Neoplasm].[MORPH_CODE_SYSTEM_VERSION]

>[Subsequent Malignant Neoplasm].[TOP_CODE_SYSTEM]

>[Subsequent Malignant Neoplasm].[TOP_CODE_SYSTEM_VERSION]

Removed concepts:
>[Subject Identifier]

>[Subject Identifier].[PCDC_SUBJECT_ID]

>[Disease Phase Timing]

>[Course Timing]

>[Biopsy And Surgical Procedures].[DISEASE_PHASE]

>[Biopsy And Surgical Procedures].[DISEASE_PHASE_NUMBER]






>[Secondary Malignant Neoplasm].[DISEASE_PHASE]

>[Secondary Malignant Neoplasm].[DISEASE_PHASE_NUMBER]

>[Secondary Malignant Neoplasm].[COURSE]

>[Secondary Malignant Neoplasm].[COURSE_NUMBER]


Modified Concepts:
>[rms_v1.0].[Disease Phase Timing].[DISEASE_PHASE] skos:exactMatch [rms_v2.0].[Time Period].[DISEASE_PHASE]

>[rms_v1.0].[Course Timing].[COURSE] skos:exactMatch [rms_v2.0].[Time Period].[COURSE]

>[rms_v1.0].[Disease Phase Timing].[DISEASE_PHASE_NUMBER] skos:broadMatch [rms_v2.0].[Time Period].[TIME_PERIOD_NUMBER]

>[rms_v1.0].[Disease Phase Timing].[AGE_AT_DISEASE_PHASE] skos:broadMatch [rms_v2.0].[Time Period].[AGE_AT_START]

>[rms_v1.0].[Disease Phase Timing].[YEAR_AT_DISEASE_PHASE] skos:exactMatch [rms_v2.0].[Time Period].[YEAR_AT_START]

>[rms_v1.0].[Course Timing].[COURSE_NUMBER] skos:broadMatch [rms_v2.0].[Time Period].[TIME_PERIOD_NUMBER]

>[rms_v1.0].[Course Timing].[AGE_AT_COURSE_START] skos:broadMatch [rms_v2.0].[Time Period].[AGE_AT_START]

>[rms_v1.0].[Course Timing].[AGE_AT_COURSE_END] skos:exactMatch [rms_v2.0].[Time Period].[AGE_AT_END]

>[rms_v1.0].[Histology] skos:exactMatch [rms_v2.0].[Diagnosis]

>[rms_v1.0].[Histology].[AGE_AT_HIST_ASSESSMENT] skos:exactMatch [rms_v2.0].[Diagnosis].[AGE_AT_DIAG_ASSESSMENT]

>[rms_v1.0].[Histology].[HISTOLOGY] skos:exactMatch [rms_v2.0].[Diagnosis].[DIAGNOSIS]

>[rms_v1.0].[Staging].[IRS_GROUP] skos:exactMatch [rms_v2.0].[Staging].[GROUP]

>[rms_v1.0].[Staging].[IRS_GROUP].[Group I] skos:exactMatch [rms_v2.0].[Staging].[GROUP].[IRS, Group I]

>[rms_v1.0].[Staging].[IRS_GROUP].[Group IIA] skos:exactMatch [rms_v2.0].[Staging].[GROUP].[IRS, Group IIA]

>[rms_v1.0].[Staging].[IRS_GROUP].[Group IIB] skos:exactMatch [rms_v2.0].[Staging].[GROUP].[IRS, Group IIB]

>[rms_v1.0].[Staging].[IRS_GROUP].[Group IIC] skos:exactMatch [rms_v2.0].[Staging].[GROUP].[IRS, Group IIC]

>[rms_v1.0].[Staging].[IRS_GROUP].[Group II, NOS] skos:exactMatch [rms_v2.0].[Staging].[GROUP].[IRS, Group II NOS]

>[rms_v1.0].[Staging].[IRS_GROUP].[Group III] skos:exactMatch [rms_v2.0].[Staging].[GROUP].[IRS, Group III]

>[rms_v1.0].[Staging].[IRS_GROUP].[Group IV] skos:exactMatch [rms_v2.0].[Staging].[GROUP].[IRS, Group IV]

>[rms_v1.0].[Tumor Assessment] skos:exactMatch [rms_v2.0].[Disease Site Assessment]

>[rms_v1.0].[Tumor Assessment].[AGE_AT_TUMOR_ASSESSMENT] skos:exactMatch [rms_v2.0].[Disease Site Assessment].[AGE_AT_DISEASE_SITE_ASSESSMENT]

>[rms_v1.0].[Tumor Assessment].[TUMOR_CLASSIFICATION] skos:exactMatch [rms_v2.0].[Disease Site Assessment].[CLASSIFICATION]

>[rms_v1.0].[Tumor Assessment].[TUMOR_SITE] skos:exactMatch [rms_v2.0].[Disease Site Assessment].[SITE]

>[rms_v1.0].[Tumor Assessment].[TUMOR_SITE_OTHER] skos:exactMatch [rms_v2.0].[Disease Site Assessment].[SITE_OTHER]


>[rms_v1.0].[Tumor Assessment].[LONGEST_DIAM_DIM1] skos:exactMatch [rms_v2.0].[Disease Site Assessment].[DIAMETER1]

>[rms_v1.0].[Tumor Assessment].[LONGEST_DIAM_DIM2] skos:exactMatch [rms_v2.0].[Disease Site Assessment].[DIAMETER2]

>[rms_v1.0].[Tumor Assessment].[LONGEST_DIAM_DIM3] skos:exactMatch [rms_v2.0].[Disease Site Assessment].[DIAMETER3]

>[rms_v1.0].[Radiation Therapy].[TUMOR_CLASSIFICATION] skos:exactMatch [rms_v2.0].[Radiation Therapy].[CLASSIFICATION]

>[rms_v1.0].[Radiation Therapy].[RT_SITE] skos:exactMatch [rms_v2.0].[Radiation Therapy].[SITE]

>[rms_v1.0].[Radiation Therapy].[RT_DOSE] skos:exactMatch [rms_v2.0].[Radiation Therapy].[DOSE]

>[rms_v1.0].[Radiation Therapy].[RT_UNIT] skos:exactMatch [rms_v2.0].[Radiation Therapy].[DOSE_UNIT]

>[rms_v1.0].[Biopsy/Surgical Procedures] skos:exactMatch [rms_v2.0].[Biopsy And Surgical Procedures]

>[rms_v1.0].[Biopsy/Surgical Procedures].[TUMOR_CLASSIFICATION] skos:exactMatch [rms_v2.0].[Biopsy And Surgical Procedures].[CLASSIFICATION]

>[rms_v1.0].[Biopsy/Surgical Procedures].[PROCEDURE_SITE] skos:exactMatch [rms_v2.0].[Biopsy And Surgical Procedures].[SITE]

>[rms_v1.0].[Secondary Malignant Neoplasm] skos:exactMatch [rms_v2.0].[Subsequent Malignant Neoplasm]
