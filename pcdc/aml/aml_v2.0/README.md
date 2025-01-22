# Release notes for aml_v2.0

This version was used for the first round of a large backlog of modeling changes that affected several dictionaries—aml tied to pcdc_v2.0.

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

>[Vitals And Anthropometrics].[HONEST_BROKER_SUBJECT_ID]

>[Function Test].[HONEST_BROKER_SUBJECT_ID]

>[Function Test].[TIME_PERIOD_SUBMITTER_ID]

>[Laboratory Test].[HONEST_BROKER_SUBJECT_ID]

>[Laboratory Test].[TIME_PERIOD_SUBMITTER_ID]

>[Diagnosis]

>[Diagnosis].[HONEST_BROKER_SUBJECT_ID]

>[Diagnosis].[AGE_AT_DIAG_ASSESSMENT]

>[Diagnosis].[TIME_PERIOD_SUBMITTER_ID]

>[Diagnosis].[DIAGNOSIS_BASIS]

>[Diagnosis].[DIAGNOSIS]

>[Diagnosis].[DIAGNOSIS].[Myeloid Sarcoma]

>[Disease Site Assessment]

>[Disease Site Assessment].[HONEST_BROKER_SUBJECT_ID]

>[Disease Site Assessment].[AGE_AT_SITE_ASSESSMENT]

>[Disease Site Assessment].[TIME_PERIOD_SUBMITTER_ID]

>[Medication].[HONEST_BROKER_SUBJECT_ID]

>[Medication].[TIME_PERIOD_SUBMITTER_ID]

>[Medication].[CATEGORY]

>[Medication].[ADMINISTRATION_STATUS]

>[Radiation Therapy].[HONEST_BROKER_SUBJECT_ID]

>[Radiation Therapy].[TIME_PERIOD_SUBMITTER_ID]

>[Transfusion Medicine Procedure].[HONEST_BROKER_SUBJECT_ID]

>[Transfusion Medicine Procedure].[TIME_PERIOD_SUBMITTER_ID]

>[Cellular Immunotherapy].[HONEST_BROKER_SUBJECT_ID]

>[Cellular Immunotherapy].[TIME_PERIOD_SUBMITTER_ID]

>[Stem Cell Transplant].[HONEST_BROKER_SUBJECT_ID]

>[Stem Cell Transplant].[TIME_PERIOD_SUBMITTER_ID]

>[Stem Cell Transplant].[SCT_TYPE].[Autologous, Single]

>[Stem Cell Transplant].[SCT_TYPE].[Autologous, Tandem]

>[Minimal Residual Disease].[HONEST_BROKER_SUBJECT_ID]

>[Minimal Residual Disease].[TIME_PERIOD_SUBMITTER_ID]

>[Minimal Residual Disease].[METHOD].[Flow Cytometry, Different-From-Normal]

>[Subject Response].[HONEST_BROKER_SUBJECT_ID]

>[Subject Response].[TIME_PERIOD_SUBMITTER_ID]

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

>[Survival Characteristics].[DISEASE_PHASE]

>[Survival Characteristics].[DISEASE_PHASE_NUMBER]

>[Survival Characteristics].[COURSE]

>[Survival Characteristics].[COURSE_NUMBER]

>[Vitals].[DISEASE_PHASE]

>[Vitals].[DISEASE_PHASE_NUMBER]

>[Vitals].[COURSE]

>[Vitals].[COURSE_NUMBER]

>[Function Test].[DISEASE_PHASE]

>[Function Test].[DISEASE_PHASE_NUMBER]

>[Function Test].[COURSE]

>[Function Test].[COURSE_NUMBER]

>[Labs].[DISEASE_PHASE]

>[Labs].[DISEASE_PHASE_NUMBER]

>[Labs].[COURSE]

>[Labs].[COURSE_NUMBER]

>[Disease Characteristics].[DISEASE_PHASE]

>[Disease Characteristics].[DISEASE_PHASE_NUMBER]

>[Myeloid Sarcoma Involvement]

>[Total Dose].[DISEASE_PHASE]

>[Total Dose].[DISEASE_PHASE_NUMBER]

>[Total Dose].[COURSE]

>[Total Dose].[COURSE_NUMBER]

>[Radiation Therapy].[DISEASE_PHASE]

>[Radiation Therapy].[DISEASE_PHASE_NUMBER]

>[Radiation Therapy].[COURSE]

>[Radiation Therapy].[COURSE_NUMBER]

>[Transfusion Medicine Procedure].[DISEASE_PHASE]

>[Transfusion Medicine Procedure].[DISEASE_PHASE_NUMBER]

>[Transfusion Medicine Procedure].[COURSE]

>[Transfusion Medicine Procedure].[COURSE_NUMBER]

>[Cellular Immunotherapy].[DISEASE_PHASE]

>[Cellular Immunotherapy].[DISEASE_PHASE_NUMBER]

>[Cellular Immunotherapy].[COURSE]

>[Cellular Immunotherapy].[COURSE_NUMBER]

>[Concomitant Medication]

>[Stem Cell Transplant].[DISEASE_PHASE]

>[Stem Cell Transplant].[DISEASE_PHASE_NUMBER]

>[Stem Cell Transplant].[COURSE]

>[Stem Cell Transplant].[COURSE_NUMBER]

>[Minimal Residual Disease].[DISEASE_PHASE]

>[Minimal Residual Disease].[DISEASE_PHASE_NUMBER]

>[Minimal Residual Disease].[COURSE]

>[Minimal Residual Disease].[COURSE_NUMBER]

>[Secondary Malignant Neoplasm].[DISEASE_PHASE]

>[Secondary Malignant Neoplasm].[DISEASE_PHASE_NUMBER]

>[Secondary Malignant Neoplasm].[COURSE]

>[Secondary Malignant Neoplasm].[COURSE_NUMBER]


Modified Concepts:
>[aml_v1.7].[Disease Phase Timing].[DISEASE_PHASE_NUMBER] skos:exactMatch [aml_v2.0].[Time Period].[TIME_PERIOD_NUMBER]

>[aml_v1.7].[Disease Phase Timing].[AGE_AT_DISEASE_PHASE] skos:exactMatch [aml_v2.0].[Time Period].[AGE_AT_START]

>[aml_v1.7].[Disease Phase Timing].[YEAR_AT_DISEASE_PHASE] skos:exactMatch [aml_v2.0].[Time Period].[YEAR_AT_START]

>[aml_v1.7].[Course Timing].[COURSE_NUMBER] skos:exactMatch [aml_v2.0].[Time Period].[TIME_PERIOD_NUMBER]

>[aml_v1.7].[Course Timing].[AGE_AT_COURSE_START] skos:exactMatch [aml_v2.0].[Time Period].[AGE_AT_START]

>[aml_v1.7].[Course Timing].[AGE_AT_COURSE_END] skos:exactMatch [aml_v2.0].[Time Period].[AGE_AT_END]

>[aml_v1.7].[Course Timing].[AGE_AT_COURSE_ANC_500] skos:exactMatch [aml_v2.0].[Time Period].[AGE_AT_COURSE_ANC_500]

>[aml_v1.7].[Off Protocol Therapy/Study] skos:exactMatch [aml_v2.0].[Off Protocol Therapy Or Study]

>[aml_v1.7].[Vitals] skos:exactMatch [aml_v2.0].[Vitals And Anthropometrics]

>[aml_v1.7].[Vitals].[AGE_AT_VITALS] skos:exactMatch [aml_v2.0].[Vitals And Anthropometrics].[AGE_AT_MEASUREMENT]

>[aml_v1.7].[Vitals].[VITALS_TEST] skos:exactMatch [aml_v2.0].[Vitals And Anthropometrics].[MEASUREMENT_TYPE]

>[aml_v1.7].[Vitals].[VITALS_RESULT] skos:exactMatch [aml_v2.0].[Vitals And Anthropometrics].[RESULT_TEXT]

>[aml_v1.7].[Vitals].[VITALS_RESULT_NUMERIC] skos:exactMatch [aml_v2.0].[Vitals And Anthropometrics].[RESULT_NUMERIC]

>[aml_v1.7].[Vitals].[VITALS_RESULT_UNIT] skos:exactMatch [aml_v2.0].[Vitals And Anthropometrics].[RESULT_UNIT]

>[aml_v1.7].[Function Test].[FUNCTION_CATEGORY] skos:exactMatch [aml_v2.0].[Function Test].[TEST]

>[aml_v1.7].[Function Test].[FUNCTION_TEST] skos:exactMatch [aml_v2.0].[Function Test].[MEASUREMENT_TYPE]

>[aml_v1.7].[Function Test].[FUNCTION_RESULT] skos:exactMatch [aml_v2.0].[Function Test].[RESULT_TEXT]

>[aml_v1.7].[Function Test].[FUNCTION_RESULT_NUMERIC] skos:exactMatch [aml_v2.0].[Function Test].[RESULT_NUMERIC]

>[aml_v1.7].[Function Test].[FUNCTION_RESULT_UNIT] skos:exactMatch [aml_v2.0].[Function Test].[RESULT_UNIT]

>[aml_v1.7].[Labs] skos:exactMatch [aml_v2.0].[Laboratory Test]

>[aml_v1.7].[Labs].[LAB_CATEGORY] skos:exactMatch [aml_v2.0].[Laboratory Test].[CATEGORY]

>[aml_v1.7].[Labs].[LAB_TEST] skos:exactMatch [aml_v2.0].[Laboratory Test].[TEST]

>[aml_v1.7].[Labs].[LAB_SPEC_TYPE] skos:exactMatch [aml_v2.0].[Laboratory Test].[SPECIMEN]

>[aml_v1.7].[Labs].[LAB_METHOD] skos:exactMatch [aml_v2.0].[Laboratory Test].[METHOD]

>[aml_v1.7].[Labs].[LAB_RESULT] skos:exactMatch [aml_v2.0].[Laboratory Test].[RESULT_TEXT]

>[aml_v1.7].[Labs].[LAB_RESULT_NUMERIC] skos:exactMatch [aml_v2.0].[Laboratory Test].[RESULT_NUMERIC]

>[aml_v1.7].[Labs].[LAB_RESULT_UNIT] skos:exactMatch [aml_v2.0].[Laboratory Test].[RESULT_UNIT]

>[aml_v1.7].[Disease Characteristics].[FAB_TYPE].[M0] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[M0]

>[aml_v1.7].[Disease Characteristics].[FAB_TYPE].[M1] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[M1]

>[aml_v1.7].[Disease Characteristics].[FAB_TYPE].[M2] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[M2]

>[aml_v1.7].[Disease Characteristics].[FAB_TYPE].[M3] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[M3]

>[aml_v1.7].[Disease Characteristics].[FAB_TYPE].[M3 Variant] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[M3 Variant]

>[aml_v1.7].[Disease Characteristics].[FAB_TYPE].[M4] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[M4]

>[aml_v1.7].[Disease Characteristics].[FAB_TYPE].[M4eo] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[M4eo]

>[aml_v1.7].[Disease Characteristics].[FAB_TYPE].[M5] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[M5]

>[aml_v1.7].[Disease Characteristics].[FAB_TYPE].[M6] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[M6]

>[aml_v1.7].[Disease Characteristics].[FAB_TYPE].[M7] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[M7]

>[aml_v1.7].[Disease Characteristics].[FAB_TYPE].[AML, NOS] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[AML, NOS]

>[aml_v1.7].[Disease Characteristics].[WHO_AML].[AML, Not Otherwise Specified] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[AML, NOS]

>[aml_v1.7].[Disease Characteristics].[WHO_AML].[WHO >> Version 4 >> AML with t(8;21)(q22;q22.1); RUNX1-RUNX1T1] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[WHO >> Version 4 >> AML with t(8;21)(q22;q22.1); RUNX1-RUNX1T1]

>[aml_v1.7].[Disease Characteristics].[WHO_AML].[WHO >> Version 4 >> AML with inv(16)(p13.1q22) or t(16;16)(p13.1;q22); CBFB-MYH11] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[WHO >> Version 4 >> AML with inv(16)(p13.1q22) or t(16;16)(p13.1;q22); CBFB-MYH11]

>[aml_v1.7].[Disease Characteristics].[WHO_AML].[WHO >> Version 4 >> APL with PML-RARA] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[WHO >> Version 4 >> APL with PML-RARA]

>[aml_v1.7].[Disease Characteristics].[WHO_AML].[WHO >> Version 4 >> AML with t(9;11)(p21.3;q23.3); KMT2A-MLLT3] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[WHO >> Version 4 >> AML with t(9;11)(p21.3;q23.3); KMT2A-MLLT3]

>[aml_v1.7].[Disease Characteristics].[WHO_AML].[WHO >> Version 5 >> AML with KMT2A Rearrangement] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[WHO >> Version 5 >> AML with KMT2A Rearrangement]

>[aml_v1.7].[Disease Characteristics].[WHO_AML].[WHO >> Version 4 >> AML with t(6;9)(p23;q34.1);DEK-NUP214] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[WHO >> Version 4 >> AML with t(6;9)(p23;q34.1);DEK-NUP214]

>[aml_v1.7].[Disease Characteristics].[WHO_AML].[WHO >> Version 4 >> AML with inv(3)(q21.3q26.2) or t(3;3)(q21.3;q26.2); GATA2, MECOM] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[WHO >> Version 4 >> AML with inv(3)(q21.3q26.2) or t(3;3)(q21.3;q26.2); GATA2, MECOM]

>[aml_v1.7].[Disease Characteristics].[WHO_AML].[WHO >> Version 4 >> AML (megakaryoblastic) with t(1;22)(p13.3;q13.3); RBM15-MKL1] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[WHO >> Version 4 >> AML (megakaryoblastic) with t(1;22)(p13.3;q13.3); RBM15-MKL1]

>[aml_v1.7].[Disease Characteristics].[WHO_AML].[WHO >> Version 4 >> Provisional Entity: AML with BCR-ABL1] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[WHO >> Version 4 >> Provisional Entity: AML with BCR-ABL1]

>[aml_v1.7].[Disease Characteristics].[WHO_AML].[WHO >> Version 4 >> AML with Mutated NPM1] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[WHO >> Version 4 >> AML with Mutated NPM1]

>[aml_v1.7].[Disease Characteristics].[WHO_AML].[WHO >> Version 4 >> AML with Biallelic Mutations of CEBPA] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[WHO >> Version 4 >> AML with Biallelic Mutations of CEBPA]

>[aml_v1.7].[Disease Characteristics].[WHO_AML].[WHO >> Version 4 >> Provisional Entity: AML with Mutated RUNX1] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[WHO >> Version 4 >> Provisional Entity: AML with Mutated RUNX1]

>[aml_v1.7].[Disease Characteristics].[WHO_AML].[WHO >> Version 4 >> AML with Myelodysplasia-related Changes] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[WHO >> Version 4 >> AML with Myelodysplasia-related Changes]

>[aml_v1.7].[Disease Characteristics].[WHO_AML].[WHO >> Version 4 >> Therapy-Related Myeloid Neoplasms] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[WHO >> Version 4 >> Therapy-Related Myeloid Neoplasms]

>[aml_v1.7].[Disease Characteristics].[WHO_AML].[WHO >> Version 4 >> AML with Minimal Differentiation] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[WHO >> Version 4 >> AML with Minimal Differentiation]

>[aml_v1.7].[Disease Characteristics].[WHO_AML].[WHO >> Version 4 >> AML without Maturation] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[WHO >> Version 4 >> AML without Maturation]

>[aml_v1.7].[Disease Characteristics].[WHO_AML].[WHO >> Version 4 >> AML with Maturation] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[WHO >> Version 4 >> AML with Maturation]

>[aml_v1.7].[Disease Characteristics].[WHO_AML].[WHO >> Version 4 >> Acute Myelomonocytic Leukemia] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[WHO >> Version 4 >> Acute Myelomonocytic Leukemia]

>[aml_v1.7].[Disease Characteristics].[WHO_AML].[WHO >> Version 4 >> Acute Monoblastic/Monocytic Leukemia] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[WHO >> Version 4 >> Acute Monoblastic/Monocytic Leukemia]

>[aml_v1.7].[Disease Characteristics].[WHO_AML].[WHO >> Version 4 >> Pure Erythroid Leukemia] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[WHO >> Version 4 >> Pure Erythroid Leukemia]

>[aml_v1.7].[Disease Characteristics].[WHO_AML].[WHO >> Version 4 >> Acute Megakaryoblastic Leukemia] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[WHO >> Version 4 >> Acute Megakaryoblastic Leukemia]

>[aml_v1.7].[Disease Characteristics].[WHO_AML].[WHO >> Version 4 >> Acute Basophilic Leukemia] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[WHO >> Version 4 >> Acute Basophilic Leukemia]

>[aml_v1.7].[Disease Characteristics].[WHO_AML].[WHO >> Version 4 >> Acute Panmyelosis with Myelofibrosis] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[WHO >> Version 4 >> Acute Panmyelosis with Myelofibrosis]

>[aml_v1.7].[Disease Characteristics].[WHO_AML].[WHO >> Version 4 >> Myeloid Sarcoma] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[WHO >> Version 4 >> Myeloid Sarcoma]

>[aml_v1.7].[Disease Characteristics].[WHO_AML].[WHO >> Version 4 >> Myeloid Proliferations Related to Down Syndrome] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[WHO >> Version 4 >> Myeloid Proliferations Related to Down Syndrome]

>[aml_v1.7].[Disease Characteristics].[WHO_AML].[WHO >> Version 4 >> Transient Abnormal Myelopoiesis (TAM)] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[WHO >> Version 4 >> Transient Abnormal Myelopoiesis (TAM)]

>[aml_v1.7].[Disease Characteristics].[WHO_AML].[WHO >> Version 4 >> Myeloid Leukemia Associated with Down Syndrome] skos:exactMatch [aml_v2.0].[Diagnosis].[WHO >> Version 4 >> Myeloid Leukemia Associated with Down Syndrome]

>[aml_v1.7].[Disease Characteristics].[CNS_DISEASE_STATUS] skos:broadMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS]

>[aml_v1.7].[Disease Characteristics].[CNS_DISEASE_STATUS].[CNS1] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[CNS1]

>[aml_v1.7].[Disease Characteristics].[CNS_DISEASE_STATUS].[CNS2] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[CNS2]

>[aml_v1.7].[Disease Characteristics].[CNS_DISEASE_STATUS].[CNS3] skos:exactMatch [aml_v2.0].[Diagnosis].[DIAGNOSIS].[CNS3]

>[aml_v1.7].[Disease Characteristics].[DETECTION_METHOD] skos:exactMatch [aml_v2.0].[Disease Site Assessment].[DETECTION_METHOD]

>[aml_v1.7].[Disease Characteristics].[DISEASE_SITE] skos:exactMatch [aml_v2.0].[Disease Site Assessment].[SITE]

>[aml_v1.7].[Myeloid Sarcoma Involvement].[MYELOID_SARCOMA_SITE].[Bone] skos:exactMatch [aml_v2.0].[Disease Site Assessment].[SITE].[Bone]

>[aml_v1.7].[Myeloid Sarcoma Involvement].[MYELOID_SARCOMA_SITE].[Orbit] skos:exactMatch [aml_v2.0].[Disease Site Assessment].[SITE].[Orbit]

>[aml_v1.7].[Myeloid Sarcoma Involvement].[MYELOID_SARCOMA_SITE].[Skin] skos:exactMatch [aml_v2.0].[Disease Site Assessment].[SITE].[Skin]

>[aml_v1.7].[Myeloid Sarcoma Involvement].[MYELOID_SARCOMA].[Yes] skos:exactMatch [aml_v2.0].[Diagnosis].[WHO >> Version 4 >> Myeloid Sarcoma]

>[aml_v1.7].[Disease Characteristics].[MPAL] skos:exactMatch [aml_v2.0].[Diagnosis].[MPAL]

>[aml_v1.7].[Disease Characteristics].[MLDS] skos:exactMatch [aml_v2.0].[Diagnosis].[MLDS]

>[aml_v1.7].[Disease Characteristics].[TAM] skos:exactMatch [aml_v2.0].[Diagnosis].[TAM]

>[aml_v1.7].[Disease Characteristics].[DISEASE_SITE].[Bone Marrow] skos:exactMatch [aml_v2.0].[Disease Site Assessment].[SITE].[Bone Marrow]

>[aml_v1.7].[Disease Characteristics].[DISEASE_SITE].[Central Nervous System] skos:exactMatch [aml_v2.0].[Disease Site Assessment].[SITE].[Central Nervous System]

>[aml_v1.7].[Disease Characteristics].[DISEASE_SITE].[Testes] skos:exactMatch [aml_v2.0].[Disease Site Assessment].[SITE].[Testes]

>[aml_v1.7].[Disease Characteristics].[SITE] skos:exactMatch [aml_v2.0].[Disease Site Assessment].[SITE]

>[aml_v1.7].[Total Dose] skos:exactMatch [aml_v2.0].[Medication]

>[aml_v1.7].[Total Dose].[AGE_AT_TOTAL_DOSE_START] skos:exactMatch [aml_v2.0].[Medication].[AGE_AT_MEDICATION_START]

>[aml_v1.7].[Total Dose].[AGE_AT_TOTAL_DOSE_END] skos:exactMatch [aml_v2.0].[Medication].[AGE_AT_MEDICATION_END]

>[aml_v1.7].[Total Dose].[ANTINEOPLASTIC_AGENT] skos:exactMatch [aml_v2.0].[Medication].[MEDICATION]

>[aml_v1.7].[Radiation Therapy].[RT_SITE] skos:exactMatch [aml_v2.0].[Radiation Therapy].[SITE]

>[aml_v1.7].[Radiation Therapy].[RT_DOSE] skos:exactMatch [aml_v2.0].[Radiation Therapy].[DOSE]

>[aml_v1.7].[Radiation Therapy].[RT_UNIT] skos:exactMatch [aml_v2.0].[Radiation Therapy].[DOSE_UNIT]

>[aml_v1.7].[Transfusion Medicine Procedure].[TMP_TYPE] skos:exactMatch [aml_v2.0].[Transfusion Medicine Procedure].[TYPE]

>[aml_v1.7].[Transfusion Medicine Procedure].[TMP_PRODUCT] skos:exactMatch [aml_v2.0].[Transfusion Medicine Procedure].[PRODUCT]

>[aml_v1.7].[Cellular Immunotherapy].[CIMT_TYPE] skos:exactMatch [aml_v2.0].[Cellular Immunotherapy].[TYPE]

>[aml_v1.7].[Concomitant Medication].[MEDICATION].[Dexrazoxane] skos:exactMatch [aml_v2.0].[Medication].[MEDICATION].[Dexrazoxane]

>[aml_v1.7].[Stem Cell Transplant].[SCT_TYPE].[Autologous] skos:exactMatch [aml_v2.0].[Stem Cell Transplant].[SCT_TYPE].[Autologous, NOS]

>[aml_v1.7].[Stem Cell Transplant].[SCT_SOURCE] skos:exactMatch [aml_v2.0].[Stem Cell Transplant].[STEM_CELL_SOURCE]

>[aml_v1.7].[Stem Cell Transplant].[SCT_DONOR_RELATIONSHIP] skos:exactMatch [aml_v2.0].[Stem Cell Transplant].[DONOR_RELATIONSHIP]

>[aml_v1.7].[Stem Cell Transplant].[SCT_CONDITIONING_TYPE] skos:exactMatch [aml_v2.0].[Stem Cell Transplant].[CONDITIONING_TYPE]

>[aml_v1.7].[Stem Cell Transplant].[SCT_TBI] skos:exactMatch [aml_v2.0].[Stem Cell Transplant].[PRIOR_TBI]

>[aml_v1.7].[Minimal Residual Disease].[MRD_METHOD] skos:exactMatch [aml_v2.0].[Minimal Residual Disease].[METHOD]

>[aml_v1.7].[Minimal Residual Disease].[MRD_METHOD].[Flow Cytometry] skos:exactMatch [aml_v2.0].[Minimal Residual Disease].[METHOD].[Flow Cytometry, NOS]

>[aml_v1.7].[Minimal Residual Disease].[MRD_METHOD].[Molecular Real-Time Quantitative Polymerase Chain Reaction] skos:exactMatch [aml_v2.0].[Minimal Residual Disease].[METHOD].[Molecular Real-time Quantitative PCR]

>[aml_v1.7].[Minimal Residual Disease].[FLOW_CYTOMETRY_TYPE].[Leukemia-Associated Immunophenotypes] skos:exactMatch [aml_v2.0].[Minimal Residual Disease].[METHOD].[Flow Cytometry, Leukemia-Associated Immunophenotypes]

>[aml_v1.7].[Minimal Residual Disease].[MRD_RESULT] skos:exactMatch [aml_v2.0].[Minimal Residual Disease].[RESULT_TEXT]

>[aml_v1.7].[Minimal Residual Disease].[MRD_RESULT_NUMERIC] skos:exactMatch [aml_v2.0].[Minimal Residual Disease].[RESULT_NUMERIC]

>[aml_v1.7].[Minimal Residual Disease].[MRD_RESULT_UNIT] skos:exactMatch [aml_v2.0].[Minimal Residual Disease].[RESULT_UNIT]

>[aml_v1.7].[Minimal Residual Disease].[MRD_SENSITIVTY] skos:exactMatch [aml_v2.0].[Minimal Residual Disease].[SENSITIVITY]

>[aml_v1.7].[Minimal Residual Disease].[MRD_SAMPLE_SOURCE] skos:exactMatch [aml_v2.0].[Minimal Residual Disease].[SPECIMEN]

>[aml_v1.7].[Minimal Residual Disease].[MRD_MOLECULAR_MARKERS] skos:exactMatch [aml_v2.0].[Minimal Residual Disease].[MOLECULAR_MARKERS]

>[aml_v1.7].[Secondary Malignant Neoplasm] skos:exactMatch [aml_v2.0].[Subsequent Malignant Neoplasm]

>[aml_v1.7].[Secondary Malignant Neoplasm].[SMN_ICD_O_MORPH] skos:exactMatch [aml_v2.0].[Subsequent Malignant Neoplasm].[MORPH_CODE]

>[aml_v1.7].[Secondary Malignant Neoplasm].[SMN_ICD_O_TOP] skos:exactMatch [aml_v2.0].[Subsequent Malignant Neoplasm].[TOP_CODE]
