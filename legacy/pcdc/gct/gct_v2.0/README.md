# Release notes for gct_v2.0

This version was used for the first round of a large backlog of modeling changes that affected several dictionaries—all tied to pcdc_v2.0.

Added concepts:
>[Subject Characteristics].[CONSORTIUM]

>[Subject Characteristics].[DISEASE_GROUP]

>[Subject Characteristics].[TREATMENT_ARM].[TE09:BEP (Cisplatin)]

>[Subject Characteristics].[TREATMENT_ARM].[TE09:CEP (Carboplatin)]

>[Subject Characteristics].[TREATMENT_ARM].[TE13:BEP]

>[Subject Characteristics].[TREATMENT_ARM].[TE13:BEP + GCSF]

>[Subject Characteristics].[TREATMENT_ARM].[TE13:BOP/VIP]

>[Subject Characteristics].[TREATMENT_ARM].[TE13:BOP/VIP + GCSF]

>[Subject Characteristics].[TREATMENT_ARM].[TE20:BEP 3 Cycle/3 Day]

>[Subject Characteristics].[TREATMENT_ARM].[TE20:BEP 3 Cycle/5 Day]

>[Subject Characteristics].[TREATMENT_ARM].[TE20:BEP 3 Cycle/Selected 3 Day]

>[Subject Characteristics].[TREATMENT_ARM].[TE20:BEP 4 Cycle/3 Day]

>[Subject Characteristics].[TREATMENT_ARM].[TE20:BEP 4 Cycle/5 Day]

>[Subject Characteristics].[TREATMENT_ARM].[TE20:BEP 4 Cycle/Selected 3 Day]

>[Time Period]

>[Time Period].[HONEST_BROKER_SUBJECT_ID]

>[Time Period].[SUBMITTER_ID]

>[Time Period].[PARENT_SUBMITTER_ID]

>[Time Period].[TIME_PERIOD_TYPE]

>[Time Period].[TIME_PERIOD_NUMBER]

>[Time Period].[YEAR_AT_START]

>[Time Period].[AGE_AT_START]

>[Demographics].[HONEST_BROKER_SUBJECT_ID]

>[Medical History].[HONEST_BROKER_SUBJECT_ID]

>[Survival Characteristics].[HONEST_BROKER_SUBJECT_ID]

>[Survival Characteristics].[TIME_PERIOD_SUBMITTER_ID]

>[Vitals And Anthropometrics].[HONEST_BROKER_SUBJECT_ID]

>[Vitals And Anthropometrics].[TIME_PERIOD_SUBMITTER_ID]

>[Laboratory Test].[HONEST_BROKER_SUBJECT_ID]

>[Laboratory Test].[TIME_PERIOD_SUBMITTER_ID]

>[Laboratory Test].[TEST].[Cytology Malignant Cells]

>[Laboratory Test].[SPECIMEN].[Pleural Fluid]

>[Laboratory Test].[RESULT]

>[Molecular Analysis].[HONEST_BROKER_SUBJECT_ID]

>[Molecular Analysis].[TIME_PERIOD_SUBMITTER_ID]

>[Immunohistochemistry].[HONEST_BROKER_SUBJECT_ID]

>[Immunohistochemistry].[TIME_PERIOD_SUBMITTER_ID]

>[Diagnosis].[HONEST_BROKER_SUBJECT_ID]

>[Diagnosis].[MORPH_CODE_SYSTEM]

>[Staging].[HONEST_BROKER_SUBJECT_ID]

>[Staging].[TIME_PERIOD_SUBMITTER_ID]

>[Disease Site Assessment].[HONEST_BROKER_SUBJECT_ID]

>[Disease Site Assessment].[TIME_PERIOD_SUBMITTER_ID]

>[Disease Characteristics].[HONEST_BROKER_SUBJECT_ID]

>[Disease Characteristics].[TIME_PERIOD_SUBMITTER_ID]

>[Medication].[HONEST_BROKER_SUBJECT_ID]

>[Medication].[TIME_PERIOD_SUBMITTER_ID]

>[Medication].[CATEGORY]

>[Radiation Therapy].[HONEST_BROKER_SUBJECT_ID]

>[Radiation Therapy].[TIME_PERIOD_SUBMITTER_ID]

>[Biopsy And Surgical Procedures].[HONEST_BROKER_SUBJECT_ID]

>[Biopsy And Surgical Procedures].[TIME_PERIOD_SUBMITTER_ID]

>[Stem Cell Transplant].[HONEST_BROKER_SUBJECT_ID]

>[Stem Cell Transplant].[TIME_PERIOD_SUBMITTER_ID]

>[Subject Response].[HONEST_BROKER_SUBJECT_ID]

>[Subject Response].[TIME_PERIOD_SUBMITTER_ID]

>[Adverse Events].[HONEST_BROKER_SUBJECT_ID]

>[Adverse Events].[TIME_PERIOD_SUBMITTER_ID]








>[Adverse Events].[AGE_AT_AE_RESOLVED]

>[Adverse Events].[AE_CODE_SYSTEM].[SNOMED]

>[Adverse Events].[AE_CODE_SYSTEM].[ICD]

>[Subsequent Malignant Neoplasm].[HONEST_BROKER_SUBJECT_ID]

>[Subsequent Malignant Neoplasm].[MORPH_CODE_SYSTEM]

>[Subsequent Malignant Neoplasm].[MORPH_CODE_SYSTEM_VERSION]

>[Subsequent Malignant Neoplasm].[TOP_CODE_SYSTEM]

>[Subsequent Malignant Neoplasm].[TOP_CODE_SYSTEM_VERSION]

Removed concepts:
>[Subject Identifier]

>[Subject Identifier].[PCDC_SUBJECT_ID]

>[Disease Phase Timing]

>[Survival Characteristics].[DISEASE_PHASE]

>[Survival Characteristics].[DISEASE_PHASE_NUMBER]

>[Vitals].[DISEASE_PHASE]

>[Vitals].[DISEASE_PHASE_NUMBER]

>[Labs].[DISEASE_PHASE]

>[Labs].[DISEASE_PHASE_NUMBER]

>[Cytology]

>[Molecular Analysis].[DISEASE_PHASE]

>[Molecular Analysis].[DISEASE_PHASE_NUMBER]

>[Immunohistochemistry].[DISEASE_PHASE]

>[Immunohistochemistry].[DISEASE_PHASE_NUMBER]

>[Histology].[DISEASE_PHASE]

>[Histology].[DISEASE_PHASE_NUMBER]

>[Staging].[DISEASE_PHASE]

>[Staging].[DISEASE_PHASE_NUMBER]

>[Staging].[STAGE_SYSTEM]

>[Tumor Assessment].[DISEASE_PHASE]

>[Tumor Assessment].[DISEASE_PHASE_NUMBER]

>[Disease Characteristics].[DISEASE_PHASE]

>[Disease Characteristics].[DISEASE_PHASE_NUMBER]

>[Growing Teratoma Syndrome]

>[Total Dose].[DISEASE_PHASE]

>[Total Dose].[DISEASE_PHASE_NUMBER]

>[Concomitant Medications].[DISEASE_PHASE]

>[Concomitant Medications].[DISEASE_PHASE_NUMBER]

>[Radiation Therapy].[DISEASE_PHASE]

>[Radiation Therapy].[DISEASE_PHASE_NUMBER]

>[Biopsy/Surgical Procedures].[DISEASE_PHASE]

>[Biopsy/Surgical Procedures].[DISEASE_PHASE_NUMBER]

>[Stem Cell Transplant].[DISEASE_PHASE]

>[Stem Cell Transplant].[DISEASE_PHASE_NUMBER]

>[Concomitant Medication]

>[Subject Response].[DISEASE_PHASE]

>[Subject Response].[DISEASE_PHASE_NUMBER]

>[Adverse Events].[DISEASE_PHASE]

>[Adverse Events].[DISEASE_PHASE_NUMBER]







>[Secondary Malignant Neoplasm].[DISEASE_PHASE]

>[Secondary Malignant Neoplasm].[DISEASE_PHASE_NUMBER]

>[Secondary Malignant Neoplasm].[COURSE]

>[Secondary Malignant Neoplasm].[COURSE_NUMBER]


Modified Concepts:
>[gct_v1.2].[Disease Phase Timing].[DISEASE_PHASE] skos:exactMatch [gct_v2.0].[Time Period].[DISEASE_PHASE]

>[gct_v1.2].[Disease Phase Timing].[DISEASE_PHASE_NUMBER] skos:exactMatch [gct_v2.0].[Time Period].[TIME_PERIOD_NUMBER]

>[gct_v1.2].[Disease Phase Timing].[AGE_AT_DISEASE_PHASE] skos:exactMatch [gct_v2.0].[Time Period].[AGE_AT_START]

>[gct_v1.2].[Disease Phase Timing].[YEAR_AT_DISEASE_PHASE] skos:exactMatch [gct_v2.0].[Time Period].[YEAR_AT_START]

>[gct_v1.2].[Medical History].[MEDICAL_HISTORY] skos:exactMatch [gct_v2.0].[Medical History].[CONDITION]

>[gct_v1.2].[Medical History].[MEDICAL_HISTORY_STATUS] skos:exactMatch [gct_v2.0].[Medical History].[CONDITION_STATUS]

>[gct_v1.2].[Vitals] skos:exactMatch [gct_v2.0].[Vitals And Anthropometrics]

>[gct_v1.2].[Vitals].[AGE_AT_VITALS] skos:exactMatch [gct_v2.0].[Vitals And Anthropometrics].[AGE_AT_MEASUREMENT]

>[gct_v1.2].[Vitals].[VITALS_TEST] skos:exactMatch [gct_v2.0].[Vitals And Anthropometrics].[MEASUREMENT_TYPE]

>[gct_v1.2].[Vitals].[VITALS_RESULT] skos:exactMatch [gct_v2.0].[Vitals And Anthropometrics].[RESULT_TEXT]

>[gct_v1.2].[Vitals].[VITALS_RESULT_NUMERIC] skos:exactMatch [gct_v2.0].[Vitals And Anthropometrics].[RESULT_NUMERIC]

>[gct_v1.2].[Vitals].[VITALS_RESULT_UNIT] skos:exactMatch [gct_v2.0].[Vitals And Anthropometrics].[RESULT_UNIT]

>[gct_v1.2].[Labs] skos:exactMatch [gct_v2.0].[Laboratory Test]

>[gct_v1.2].[Labs].[LAB_CATEGORY] skos:exactMatch [gct_v2.0].[Laboratory Test].[CATEGORY]

>[gct_v1.2].[Labs].[LAB_TEST] skos:exactMatch [gct_v2.0].[Laboratory Test].[TEST]

>[gct_v1.2].[Labs].[LAB_SPEC_TYPE] skos:exactMatch [gct_v2.0].[Laboratory Test].[SPECIMEN]

>[gct_v1.2].[Labs].[LAB_METHOD] skos:exactMatch [gct_v2.0].[Laboratory Test].[METHOD]

>[gct_v1.2].[Labs].[LAB_RESULT] skos:exactMatch [gct_v2.0].[Laboratory Test].[RESULT_TEXT]

>[gct_v1.2].[Labs].[LAB_RESULT_NUMERIC] skos:exactMatch [gct_v2.0].[Laboratory Test].[RESULT_NUMERIC]

>[gct_v1.2].[Labs].[LAB_RESULT_UNIT] skos:exactMatch [gct_v2.0].[Laboratory Test].[RESULT_UNIT]

>[gct_v1.2].[Labs].[LAB_SEQ_METHOD] skos:exactMatch [gct_v2.0].[Laboratory Test].[SEQ_METHOD]

>[gct_v1.2].[Cytology].[MALIGNANT_CELLS].[Present] skos:broadMatch [gct_v2.0].[Laboratory Test].[TEST].[Cytology Malignant Cells]

>[gct_v1.2].[Cytology].[MALIGNANT_CELLS].[Present] skos:broadMatch [gct_v2.0].[Laboratory Test].[RESULT].[Present]

>[gct_v1.2].[Cytology].[MALIGNANT_CELLS].[Absent] skos:broadMatch [gct_v2.0].[Laboratory Test].[RESULT].[Absent]

>[gct_v1.2].[Cytology].[CYTOLOGY_SPEC_TYPE] skos:exactMatch [gct_v2.0].[Laboratory Test].[SPECIMEN]

>[gct_v1.2].[Immunohistochemistry].[IHC_TEST] skos:exactMatch [gct_v2.0].[Immunohistochemistry].[MARKERS]

>[gct_v1.2].[Immunohistochemistry].[IHC_RESULT] skos:exactMatch [gct_v2.0].[Immunohistochemistry].[RESULT_TEXT]

>[gct_v1.2].[Immunohistochemistry].[IHC_RESULT_NUMERIC] skos:exactMatch [gct_v2.0].[Immunohistochemistry].[RESULT_NUMERIC]

>[gct_v1.2].[Histology] skos:exactMatch [gct_v2.0].[Diagnosis]

>[gct_v1.2].[Histology].[AGE_AT_HIST_ASSESSMENT] skos:exactMatch [gct_v2.0].[Diagnosis].[AGE_AT_DIAG_ASSESSMENT]

>[gct_v1.2].[Histology].[HIST_ASSESSMENT_REVIEW] skos:exactMatch [gct_v2.0].[Diagnosis].[REVIEW_SOURCE]

>[gct_v1.2].[Histology].[HISTOLOGY] skos:exactMatch [gct_v2.0].[Diagnosis].[DIAGNOSIS]

>[gct_v1.2].[Histology].[HISTOLOGY_RESULT] skos:exactMatch [gct_v2.0].[Diagnosis].[RESULT_TEXT]

>[gct_v1.2].[Histology].[HISTOLOGY_RESULT_NUMERIC] skos:exactMatch [gct_v2.0].[Diagnosis].[RESULT_NUMERIC]

>[gct_v1.2].[Histology].[HISTOLOGY_RESULT_UNIT] skos:exactMatch [gct_v2.0].[Diagnosis].[RESULT_UNIT]

>[gct_v1.2].[Histology].[HIST_ICD_O_MORPH] skos:exactMatch [gct_v2.0].[Diagnosis].[MORPH_CODE]

>[gct_v1.2].[Histology].[HISTOLOGY_GRADE] skos:exactMatch [gct_v2.0].[Diagnosis].[GRADE]

>[gct_v1.2].[Staging].[STAGE].[Stage I] skos:exactMatch [gct_v2.0].Staging].[STAGE].[FIGO, Stage I]

>[gct_v1.2].[Staging].[STAGE].[Stage II] skos:exactMatch [gct_v2.0].Staging].[STAGE].[FIGO, Stage II]

>[gct_v1.2].[Staging].[STAGE].[Stage III] skos:exactMatch [gct_v2.0].Staging].[STAGE].[FIGO, Stage III]

>[gct_v1.2].[Staging].[STAGE].[Stage IV] skos:exactMatch [gct_v2.0].Staging].[STAGE].[FIGO, Stage IV]

>[gct_v1.2].[Staging].[STAGE].[Stage I] skos:exactMatch [gct_v2.0].Staging].[STAGE].[COG, Stage I]

>[gct_v1.2].[Staging].[STAGE].[Stage II] skos:exactMatch [gct_v2.0].Staging].[STAGE].[COG, Stage II]

>[gct_v1.2].[Staging].[STAGE].[Stage III] skos:exactMatch [gct_v2.0].Staging].[STAGE].[COG, Stage III]

>[gct_v1.2].[Staging].[STAGE].[Stage IV] skos:exactMatch [gct_v2.0].Staging].[STAGE].[COG, Stage IV]

>[gct_v1.2].[Staging].[STAGE].[Stage 0] skos:exactMatch [gct_v2.0].Staging].[STAGE].[AJCC, Stage 0]

>[gct_v1.2].[Staging].[STAGE].[Stage I] skos:exactMatch [gct_v2.0].Staging].[STAGE].[AJCC, Stage I]

>[gct_v1.2].[Staging].[STAGE].[Stage IA] skos:exactMatch [gct_v2.0].Staging].[STAGE].[AJCC, Stage IA]

>[gct_v1.2].[Staging].[STAGE].[Stage IB] skos:exactMatch [gct_v2.0].Staging].[STAGE].[AJCC, Stage IB]

>[gct_v1.2].[Staging].[STAGE].[Stage IS] skos:exactMatch [gct_v2.0].Staging].[STAGE].[AJCC, Stage IS]

>[gct_v1.2].[Staging].[STAGE].[Stage II] skos:exactMatch [gct_v2.0].Staging].[STAGE].[AJCC, Stage II]

>[gct_v1.2].[Staging].[STAGE].[Stage IIA] skos:exactMatch [gct_v2.0].Staging].[STAGE].[AJCC, Stage IIA]

>[gct_v1.2].[Staging].[STAGE].[Stage IIB] skos:exactMatch [gct_v2.0].Staging].[STAGE].[AJCC, Stage IIB]

>[gct_v1.2].[Staging].[STAGE].[Stage IIC] skos:exactMatch [gct_v2.0].Staging].[STAGE].[AJCC, Stage IIC]

>[gct_v1.2].[Staging].[STAGE].[Stage III] skos:exactMatch [gct_v2.0].Staging].[STAGE].[AJCC, Stage III]

>[gct_v1.2].[Staging].[STAGE].[Stage IIIA] skos:exactMatch [gct_v2.0].Staging].[STAGE].[AJCC, Stage IIIA]

>[gct_v1.2].[Staging].[STAGE].[Stage IIIB] skos:exactMatch [gct_v2.0].Staging].[STAGE].[AJCC, Stage IIIB]

>[gct_v1.2].[Staging].[STAGE].[Stage IIIC] skos:exactMatch [gct_v2.0].Staging].[STAGE].[AJCC, Stage IIIC]

>[gct_v1.2].[Tumor Assessment] skos:exactMatch [gct_v2.0].[Disease Site Assessment]

>[gct_v1.2].[Tumor Assessment].[AGE_AT_TUMOR_ASSESSMENT] skos:exactMatch [gct_v2.0].[Disease Site Assessment].[AGE_AT_DISEASE_SITE_ASSESSMENT]

>[gct_v1.2].[Tumor Assessment].[TUMOR_DETECTION_METHOD] skos:exactMatch [gct_v2.0].[Disease Site Assessment].[DETECTION_METHOD]

>[gct_v1.2].[Tumor Assessment].[TUMOR_CLASSIFICATION] skos:exactMatch [gct_v2.0].[Disease Site Assessment].[CLASSIFICATION]

>[gct_v1.2].[Tumor Assessment].[TUMOR_STATE] skos:exactMatch [gct_v2.0].[Disease Site Assessment].[STATE]

>[gct_v1.2].[Tumor Assessment].[TUMOR_SITE] skos:exactMatch [gct_v2.0].[Disease Site Assessment].[SITE]

>[gct_v1.2].[Tumor Assessment].[TUMOR_LATERALITY] skos:exactMatch [gct_v2.0].[Disease Site Assessment].[LATERALITY]

>[gct_v1.2].[Disease Characteristics].[IGCCC_RISK_GROUP] skos:narrowMatch [gct_v2.0].[Disease Characteristics].[RISK_GROUP]

>[gct_v1.2].[Disease Characteristics].[MAGIC_RISK_GROUP] skos:narrowMatch [gct_v2.0].[Disease Characteristics].[RISK_GROUP]

>[gct_v1.2].[Growing Teratoma Syndrome].[GTS_TREATMENT] skos:exactMatch [gct_v2.0].[Disease Characteristics].[GTS_TREATMENT]

>[gct_v1.2].[Total Dose] skos:broadMatch [gct_v2.0].[Medication]

>[gct_v1.2].[Concomitant Medications] skos:broadMatch [gct_v2.0].[Medication]

>[gct_v1.2].[Total Dose].[AGE_AT_TOTAL_DOSE_START] skos:broadMatch [gct_v2.0].[Medication].[AGE_AT_MEDICATION_START]

>[gct_v1.2].[Total Dose].[AGE_AT_TOTAL_DOSE_END] skos:broadMatch [gct_v2.0].[Medication].[AGE_AT_MEDICATION_END]

>[gct_v1.2].[Concomitant Medications].[AGE_AT_MEDICATION_START] skos:broadMatch [gct_v2.0].[Medication].[AGE_AT_MEDICATION_START]

>[gct_v1.2].[Concomitant Medications].[AGE_AT_MEDICATION_END] skos:broadMatch [gct_v2.0].[Medication].[AGE_AT_MEDICATION_END]

>[gct_v1.2].[Total Dose].[ANTINEOPLASTIC_AGENT].[Amifostine] skos:exactMatch
[gct_v2.0].[Medication].[MEDICATION].[Amifostine]

>[gct_v1.2].[Total Dose].[ANTINEOPLASTIC_AGENT].[Bleomycin] skos:exactMatch [gct_v2.0].[Medication].[MEDICATION].[Bleomycin]

>[gct_v1.2].[Total Dose].[ANTINEOPLASTIC_AGENT].[Carboplatin] skos:exactMatch [gct_v2.0].[Medication].[MEDICATION].[Carboplatin]

>[gct_v1.2].[Total Dose].[ANTINEOPLASTIC_AGENT].[Cisplatin] skos:exactMatch [gct_v2.0].[Medication].[MEDICATION].[Cisplatin]

>[gct_v1.2].[Total Dose].[ANTINEOPLASTIC_AGENT].[Cyclophosphamide] skos:exactMatch [gct_v2.0].[Medication].[MEDICATION].[Cyclophosphamide]

>[gct_v1.2].[Total Dose].[ANTINEOPLASTIC_AGENT].[Dactinomycin] skos:exactMatch [gct_v2.0].[Medication].[MEDICATION].[Dactinomycin]

>[gct_v1.2].[Total Dose].[ANTINEOPLASTIC_AGENT].[Etoposide] skos:exactMatch [gct_v2.0].[Medication].[MEDICATION].[Etoposide]

>[gct_v1.2].[Total Dose].[ANTINEOPLASTIC_AGENT].[Etoposide Phosphate] skos:exactMatch [gct_v2.0].[Medication].[MEDICATION].[Etoposide Phosphate]

>[gct_v1.2].[Total Dose].[ANTINEOPLASTIC_AGENT].[Gemcitabine] skos:exactMatch [gct_v2.0].[Medication].[MEDICATION].[Gemcitabine]

>[gct_v1.2].[Total Dose].[ANTINEOPLASTIC_AGENT].[Ifosfamide] skos:exactMatch [gct_v2.0].[Medication].[MEDICATION].[Ifosfamide]

>[gct_v1.2].[Total Dose].[ANTINEOPLASTIC_AGENT].[Melphalan] skos:exactMatch [gct_v2.0].[Medication].[MEDICATION].[Melphalan]

>[gct_v1.2].[Total Dose].[ANTINEOPLASTIC_AGENT].[Paclitaxel] skos:exactMatch [gct_v2.0].[Medication].[MEDICATION].[Paclitaxel]

>[gct_v1.2].[Concomitant Medications].[MEDICATION].[Sodium Thiosulfate] skos:exactMatch [gct_v2.0].[Medication].[MEDICATION].[Sodium Thiosulfate]

>[gct_v1.2].[Total Dose].[ANTINEOPLASTIC_AGENT].[Vinblastine] skos:exactMatch [gct_v2.0].[Medication].[MEDICATION].[Vinblastine]

>[gct_v1.2].[Total Dose].[ANTINEOPLASTIC_AGENT].[Vincristine] skos:exactMatch [gct_v2.0].[Medication].[MEDICATION].[Vincristine]

>[gct_v1.2].[Radiation Therapy].[RT_SITE] skos:exactMatch [gct_v2.0].[Radiation Therapy].[SITE]

>[gct_v1.2].[Radiation Therapy].[RT_DOSE] skos:exactMatch [gct_v2.0].[Radiation Therapy].[DOSE]

>[gct_v1.2].[Radiation Therapy].[RT_UNIT] skos:exactMatch [gct_v2.0].[Radiation Therapy].[DOSE_UNIT]

>[gct_v1.2].[Biopsy/Surgical Procedures] skos:exactMatch [gct_v2.0].[Biopsy And Surgical Procedures]

>[gct_v1.2].[Biopsy/Surgical Procedures].[PROCEDURE_SITE] skos:exactMatch [gct_v2.0].[Biopsy And Surgical Procedures].[SITE]

>[gct_v1.2].[Biopsy/Surgical Procedures].[PROCEDURE_LATERALITY] skos:exactMatch [gct_v2.0].[Biopsy And Surgical Procedures].[LATERALITY]

>[gct_v1.2].[Biopsy/Surgical Procedures].[PROCEDURE_EXTENT] skos:exactMatch [gct_v2.0].[Biopsy And Surgical Procedures].[EXTENT]

>[gct_v1.2].[Stem Cell Transplant].[SCT_CYCLES] skos:exactMatch [gct_v2.0].[Stem Cell Transplant].[TOTAL_CYCLES]

>[gct_v1.2].[Adverse Events].[AE_GRADE] skos:exactMatch [gct_v2.0].[Adverse Events].[GRADE]

>[gct_v1.2].[Adverse Events].[AE_ATTRIBUTION] skos:exactMatch [gct_v2.0].[Adverse Events].[ATTRIBUTION]

>[gct_v1.2].[Adverse Events].[AE_OUTCOME] skos:exactMatch [gct_v2.0].[Adverse Events].[OUTCOME]







>[gct_v1.2].[Secondary Malignant Neoplasm] skos:exactMatch [gct_v2.0].[Subsequent Malignant Neoplasm]

>[gct_v1.2].[Secondary Malignant Neoplasm].[SMN_ICD_O_MORPH] skos:exactMatch [gct_v2.0].[Subsequent Malignant Neoplasm].[MORPH_CODE]

>[gct_v1.2].[Secondary Malignant Neoplasm].[SMN_ICD_O_TOP] skos:exactMatch [gct_v2.0].[Subsequent Malignant Neoplasm].[TOP_CODE]
