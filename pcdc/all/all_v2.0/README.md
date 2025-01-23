# Release notes for all_v2.0

This version was used for the first round of a large backlog of modeling changes that affected several dictionaries—all tied to pcdc_v2.0.

Added concepts:
>[Subject Characteristics].[CONSORTIUM]

>[Subject Characteristics].[DISEASE_GROUP]

>[Time Period]

>[Time Period].[HONEST_BROKER_SUBJECT_ID]

>[Time Period].[SUBMITTER_ID]

>[Time Period].[PARENT_SUBMITTER_ID]

>[Time Period].[TIME_PERIOD_TYPE]

>[Time Period].[TIME_PERIOD_TYPE].[Disease Phase]

>[Time Period].[TIME_PERIOD_TYPE].[Course]

>[Time Period].[DISEASE_PHASE]

>[Time Period].[COURSE]

>[Time Period].[TIME_PERIOD_NUMBER]

>[Time Period].[YEAR_AT_START]

>[Time Period].[AGE_AT_START]

>[Time Period].[AGE_AT_END]

>[Off Protocol Therapy Or Study].[HONEST_BROKER_SUBJECT_ID]

>[Off Protocol Therapy Or Study].[TIME_PERIOD_SUBMITTER_ID]

>[Demographics].[HONEST_BROKER_SUBJECT_ID]

>[Medical History].[HONEST_BROKER_SUBJECT_ID]

>[Survival Characteristics].[HONEST_BROKER_SUBJECT_ID]

>[Survival Characteristics].[CAUSE_OF_DEATH].[Unrelated to Disease or Treatment]

>[Vitals And Anthropometrics].[HONEST_BROKER_SUBJECT_ID]

>[Laboratory Test].[HONEST_BROKER_SUBJECT_ID]

>[Diagnosis].[HONEST_BROKER_SUBJECT_ID]

>[Diagnosis].[TIME_PERIOD_SUBMITTER_ID]

>[Diagnosis].[DIAGNOSIS_BASIS]

>[Disease Site Assessment]

>[Disease Site Assessment].[HONEST_BROKER_SUBJECT_ID]

>[Disease Site Assessment].[AGE_AT_SITE_ASSESSMENT]

>[Disease Site Assessment].[TIME_PERIOD_SUBMITTER_ID]

>[Disease Site Assessment].[SITE].[Mediastinum]

>[Radiation Therapy].[HONEST_BROKER_SUBJECT_ID]

>[Stem Cell Transplant].[HONEST_BROKER_SUBJECT_ID]

>[Stem Cell Transplant].[TIME_PERIOD_SUBMITTER_ID]

>[Stem Cell Transplant].[SCT_TYPE].[Autologous, Single]

>[Stem Cell Transplant].[SCT_TYPE].[Autologous, Tandem]

>[Minimal Residual Disease].[HONEST_BROKER_SUBJECT_ID]

>[Minimal Residual Disease].[METHOD].[Flow Cytometry, Different-From-Normal]

>[Adverse Events].[HONEST_BROKER_SUBJECT_ID]

>[Adverse Events].[TIME_PERIOD_SUBMITTER_ID]

>[Adverse Events].[AGE_AT_AE_RESOLVED]

>[Adverse Events].[ADVERSE_EVENT]

>[Adverse Events].[GRADE_SYSTEM]

>[Adverse Events].[GRADE_SYSTEM_VERSION]

>[Adverse Events].[AE_CODE_SYSTEM].[SNOMED]

>[Adverse Events].[AE_CODE_SYSTEM].[ICD]

>[Adverse Events].[INTERVENTION_STATUS]

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

>[Off Protocol Therapy/Study].[DISEASE_PHASE]

>[Off Protocol Therapy/Study].[DISEASE_PHASE_NUMBER]

>[Off Protocol Therapy/Study].[COURSE]

>[Off Protocol Therapy/Study].[COURSE_NUMBER]

>[Vitals].[DISEASE_PHASE]

>[Vitals].[DISEASE_PHASE_NUMBER]

>[Vitals].[COURSE]

>[Vitals].[COURSE_NUMBER]

>[Histology].[DISEASE_PHASE]

>[Histology].[DISEASE_PHASE_NUMBER]

>[Histology].[COURSE]

>[Histology].[COURSE_NUMBER]

>[Disease Characteristics].[DISEASE_PHASE]

>[Disease Characteristics].[DISEASE_PHASE_NUMBER]


Modified Concepts:
>[all_v1.1].[Disease Phase Timing].[DISEASE_PHASE_NUMBER] skos:exactMatch [all_v2.0].[Time Period].[TIME_PERIOD_NUMBER]

>[all_v1.1].[Disease Phase Timing].[AGE_AT_DISEASE_PHASE] skos:exactMatch [all_v2.0].[Time Period].[AGE_AT_START]

>[all_v1.1].[Disease Phase Timing].[YEAR_AT_DISEASE_PHASE] skos:exactMatch [all_v2.0].[Time Period].[YEAR_AT_START]

>[all_v1.1].[Course Timing].[COURSE_NUMBER] skos:exactMatch [all_v2.0].[Time Period].[TIME_PERIOD_NUMBER]

>[all_v1.1].[Course Timing].[AGE_AT_COURSE_START] skos:exactMatch [all_v2.0].[Time Period].[AGE_AT_START]

>[all_v1.1].[Course Timing].[AGE_AT_COURSE_END] skos:exactMatch [all_v2.0].[Time Period].[AGE_AT_END]

>[all_v1.1].[Off Protocol Therapy/Study] skos:exactMatch [all_v2.0].[Off Protocol Therapy Or Study]

>[all_v1.1].[Survival Characteristics].[CAUSE_OF_DEATH_DETAIL].[Infection] skos:exactMatch [all_v2.0].[Survival Characteristics].[CAUSE_OF_DEATH_DETAIL].[Infection, NOS]

>[all_v1.1].[Vitals] skos:exactMatch [all_v2.0].[Vitals And Anthropometrics]

>[all_v1.1].[Vitals].[AGE_AT_VITALS] skos:exactMatch [all_v2.0].[Vitals And Anthropometrics].[AGE_AT_MEASUREMENT]

>[all_v1.1].[Vitals].[VITALS_TEST] skos:exactMatch [all_v2.0].[Vitals And Anthropometrics].[MEASUREMENT_TYPE]

>[all_v1.1].[Vitals].[VITALS_RESULT] skos:exactMatch [all_v2.0].[Vitals And Anthropometrics].[RESULT_TEXT]

>[all_v1.1].[Vitals].[VITALS_RESULT_NUMERIC] skos:exactMatch [all_v2.0].[Vitals And Anthropometrics].[RESULT_NUMERIC]

>[all_v1.1].[Vitals].[VITALS_RESULT_UNIT] skos:exactMatch [all_v2.0].[Vitals And Anthropometrics].[RESULT_UNIT]

>[all_v1.1].[Labs] skos:exactMatch [all_v2.0].[Laboratory Test]

>[all_v1.1].[Labs].[LAB_CATEGORY] skos:exactMatch [all_v2.0].[Laboratory Test].[CATEGORY]

>[all_v1.1].[Labs].[LAB_TEST] skos:exactMatch [all_v2.0].[Laboratory Test].[TEST]

>[all_v1.1].[Labs].[LAB_SPEC_TYPE] skos:exactMatch [all_v2.0].[Laboratory Test].[SPECIMEN]

>[all_v1.1].[Labs].[LAB_METHOD] skos:exactMatch [all_v2.0].[Laboratory Test].[METHOD]

>[all_v1.1].[Labs].[LAB_RESULT] skos:exactMatch [all_v2.0].[Laboratory Test].[RESULT_TEXT]

>[all_v1.1].[Labs].[LAB_RESULT_NUMERIC] skos:exactMatch [all_v2.0].[Laboratory Test].[RESULT_NUMERIC]

>[all_v1.1].[Labs].[LAB_RESULT_UNIT] skos:exactMatch [all_v2.0].[Laboratory Test].[RESULT_UNIT]

>[all_v1.1].[Histology] skos:exactMatch [all_v2.0].[Diagnosis]

>[all_v1.1].[Histology].[AGE_AT_HIST_ASSESSMENT] skos:exactMatch [all_v2.0].[Diagnosis].[AGE_AT_DIAG_ASSESSMENT]

>[all_v1.1].[Disease Characteristics].[ALL_TYPE] skos:exactMatch [all_v2.0].[Diagnosis].[DIAGNOSIS]

>[all_v1.1].[Disease Characteristics].[CNS_DISEASE_STATUS].[CNS1] skos:exactMatch [all_v2.0].[Diagnosis].[DIAGNOSIS].[CNS1]

>[all_v1.1].[Disease Characteristics].[CNS_DISEASE_STATUS].[CNS2] skos:exactMatch [all_v2.0].[Diagnosis].[DIAGNOSIS].[CNS2]

>[all_v1.1].[Disease Characteristics].[CNS_DISEASE_STATUS].[CNS3] skos:exactMatch [all_v2.0].[Diagnosis].[DIAGNOSIS].[CNS3]

>[all_v1.1].[Disease Characteristics].[CNS_DISEASE_STATUS].[CNS2a] skos:exactMatch [all_v2.0].[Diagnosis].[DIAGNOSIS].[CNS2a]

>[all_v1.1].[Disease Characteristics].[CNS_DISEASE_STATUS].[CNS2b] skos:exactMatch [all_v2.0].[Diagnosis].[DIAGNOSIS].[CNS2b]

>[all_v1.1].[Disease Characteristics].[CNS_DISEASE_STATUS].[CNS2c] skos:exactMatch [all_v2.0].[Diagnosis].[DIAGNOSIS].[CNS2c]

>[all_v1.1].[Disease Characteristics].[CNS_DISEASE_STATUS].[CNS3a] skos:exactMatch [all_v2.0].[Diagnosis].[DIAGNOSIS].[CNS3a]

>[all_v1.1].[Disease Characteristics].[CNS_DISEASE_STATUS].[CNS3b] skos:exactMatch [all_v2.0].[Diagnosis].[DIAGNOSIS].[CNS3b]

>[all_v1.1].[Disease Characteristics].[CNS_DISEASE_STATUS].[CNS3c] skos:exactMatch [all_v2.0].[Diagnosis].[DIAGNOSIS].[CNS3c]

>[all_v1.1].[Disease Characteristics].[CNS_DISEASE_STATUS].[Unknown] skos:exactMatch [all_v2.0].[Diagnosis].[DIAGNOSIS].[Unknown]

>[all_v1.1].[Disease Characteristics].[CNS_DISEASE_STATUS].[Not Reported] skos:exactMatch [all_v2.0].[Diagnosis].[DIAGNOSIS].[Not Reported]

>[all_v1.1].[Disease Characteristics].[DISEASE_SITE] skos:exactMatch [all_v2.0].[Disease Site Assessment].[SITE]

>[all_v1.1].[Disease Characteristics].[BULK_MED_MASS] skos:exactMatch [all_v2.0].[Disease Site Assessment].[BULKY_MASS]

>[all_v1.1].[Non-Protocol Therapy].[NPT_TYPE].[Radiation Therapy] skos:closeMatch [all_v2.0].[Radiation Therapy].[PROTOCOL_RADIATION_THERAPY].[No]

>[all_v1.1].[Non-Protocol Therapy].[NPT_TIMING] skos:narrowMatch [all_v2.0].[Radiation Therapy].[NON_PROTOCOL_TIMING]

>[all_v1.1].[Radiation Therapy].[RT_SITE] skos:exactMatch [all_v2.0].[Radiation Therapy].[SITE]

>[all_v1.1].[Non-Protocol Therapy].[NPT_TYPE].[Stem Cell Transplant] skos:closeMatch [all_v2.0].[Stem Cell Transplant].[PROTOCOL_SCT].[No]

>[all_v1.1].[Non-Protocol Therapy].[NPT_TIMING] skos:narrowMatch [all_v2.0].[Stem Cell Transplant].[NON_PROTOCOL_TIMING]

>[all_v1.1].[Stem Cell Transplant].[SCT_TYPE].[Autologous] skos:exactMatch [all_v2.0].[Stem Cell Transplant].[SCT_TYPE].[Autologous, NOS]

>[all_v1.1].[Stem Cell Transplant].[SCT_SOURCE] skos:exactMatch [all_v2.0].[Stem Cell Transplant].[STEM_CELL_SOURCE]

>[all_v1.1].[Stem Cell Transplant].[SCT_DONOR_RELATIONSHIP] skos:exactMatch [all_v2.0].[Stem Cell Transplant].[DONOR_RELATIONSHIP]

>[all_v1.1].[Stem Cell Transplant].[SCT_CONDITIONING_TYPE] skos:exactMatch [all_v2.0].[Stem Cell Transplant].[CONDITIONING_TYPE]

>[all_v1.1].[Stem Cell Transplant].[SCT_TBI] skos:exactMatch [all_v2.0].[Stem Cell Transplant].[PRIOR_TBI]

>[all_v1.1].[Minimal Residual Disease].[MRD_METHOD] skos:exactMatch [all_v2.0].[Minimal Residual Disease].[METHOD]

>[all_v1.1].[Minimal Residual Disease].[MRD_METHOD].[Flow Cytometry] skos:exactMatch [all_v2.0].[Minimal Residual Disease].[METHOD].[Flow Cytometry, NOS]

>[all_v1.1].[Minimal Residual Disease].[MRD_METHOD].[Molecular Real-Time Quantitative Polymerase Chain Reaction] skos:exactMatch [all_v2.0].[Minimal Residual Disease].[METHOD].[Molecular Real-time Quantitative PCR]

>[all_v1.1].[Minimal Residual Disease].[FLOW_CYTOMETRY_TYPE].[Leukemia-Associated Immunophenotypes] skos:exactMatch [all_v2.0].[Minimal Residual Disease].[METHOD].[Flow Cytometry, Leukemia-Associated Immunophenotypes]

>[all_v1.1].[Minimal Residual Disease].[MRD_RESULT] skos:exactMatch [all_v2.0].[Minimal Residual Disease].[RESULT_TEXT]

>[all_v1.1].[Minimal Residual Disease].[MRD_RESULT_NUMERIC] skos:exactMatch [all_v2.0].[Minimal Residual Disease].[RESULT_NUMERIC]

>[all_v1.1].[Minimal Residual Disease].[MRD_RESULT_UNIT] skos:exactMatch [all_v2.0].[Minimal Residual Disease].[RESULT_UNIT]

>[all_v1.1].[Minimal Residual Disease].[MRD_SENSITIVTY] skos:exactMatch [all_v2.0].[Minimal Residual Disease].[SENSITIVITY]

>[all_v1.1].[Minimal Residual Disease].[MRD_SAMPLE_SOURCE] skos:exactMatch [all_v2.0].[Minimal Residual Disease].[SPECIMEN]

>[all_v1.1].[Adverse Events].[AE_ATTRIBUTION] skos:exactMatch [all_v2.0].[Adverse Events].[ATTRIBUTION]

>[all_v1.1].[Adverse Events].[AVN_METHOD] skos:exactMatch [all_v2.0].[Adverse Events].[DETECTION_METHOD]

>[all_v1.1].[Adverse Events].[ORTHOPEDIC_PROCEDURE] skos:exactMatch [all_v2.0].[Adverse Events].[INTERVENTION]

>[all_v1.1].[Secondary Malignant Neoplasm] skos:exactMatch [all_v2.0].[Subsequent Malignant Neoplasm]

>[all_v1.1].[Secondary Malignant Neoplasm].[SMN_ICD_O_MORPH] skos:exactMatch [all_v2.0].[Subsequent Malignant Neoplasm].[MORPH_CODE]

>[all_v1.1].[Secondary Malignant Neoplasm].[SMN_ICD_O_TOP] skos:exactMatch [all_v2.0].[Subsequent Malignant Neoplasm].[TOP_CODE]
