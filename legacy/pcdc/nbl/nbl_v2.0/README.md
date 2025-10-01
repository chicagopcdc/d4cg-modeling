# Release notes for nbl_v2.0

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

>[Time Period].[DISEASE_PHASE]

>[Time Period].[TIME_PERIOD_NUMBER]

>[Time Period].[YEAR_AT_START]

>[Time Period].[AGE_AT_START]

>[Demographics].[HONEST_BROKER_SUBJECT_ID]

>[Survival Characteristics].[HONEST_BROKER_SUBJECT_ID]

>[Survival Characteristics].[TIME_PERIOD_SUBMITTER_ID]

>[Laboratory Test].[HONEST_BROKER_SUBJECT_ID]

>[Laboratory Test].[TIME_PERIOD_SUBMITTER_ID]

>[Molecular Analysis].[HONEST_BROKER_SUBJECT_ID]

>[Molecular Analysis].[TIME_PERIOD_SUBMITTER_ID]

>[Diagnosis].[HONEST_BROKER_SUBJECT_ID]

>[Diagnosis].[TIME_PERIOD_SUBMITTER_ID]

>[Diagnosis].[DIAGNOSIS_BASIS]

>[Diagnosis].[DIAGNOSIS]

>[Staging].[HONEST_BROKER_SUBJECT_ID]

>[Staging].[TIME_PERIOD_SUBMITTER_ID]

>[Disease Site Assessment].[HONEST_BROKER_SUBJECT_ID]

>[Disease Site Assessment].[TIME_PERIOD_SUBMITTER_ID]

>[Disease Characteristics].[HONEST_BROKER_SUBJECT_ID]

>[Disease Characteristics].[TIME_PERIOD_SUBMITTER_ID]

>[Subsequent Malignant Neoplasm].[HONEST_BROKER_SUBJECT_ID]

>[Subsequent Malignant Neoplasm].[TIME_PERIOD_SUBMITTER_ID]

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

>[Labs].[DISEASE_PHASE]

>[Labs].[DISEASE_PHASE_NUMBER]

>[Molecular Analysis].[DISEASE_PHASE]

>[Molecular Analysis].[DISEASE_PHASE_NUMBER]

>[Histology].[DISEASE_PHASE]

>[Histology].[DISEASE_PHASE_NUMBER]

>[Staging].[DISEASE_PHASE]

>[Staging].[DISEASE_PHASE_NUMBER]

>[Tumor Assessment].[DISEASE_PHASE]

>[Tumor Assessment].[DISEASE_PHASE_NUMBER]

>[Disease Characteristics].[DISEASE_PHASE]

>[Disease Characteristics].[DISEASE_PHASE_NUMBER]

>[Subsequent Malignant Neoplasm].[DISEASE_PHASE]

>[Subsequent Malignant Neoplasm].[DISEASE_PHASE_NUMBER]


Modified Concepts:
>[nbl_v1.1].[Disease Phase Timing].[DISEASE_PHASE] skos:exactMatch [nbl_v2.0].[Time Period].[DISEASE_PHASE]

>[nbl_v1.1].[Disease Phase Timing].[DISEASE_PHASE_NUMBER] skos:exactMatch [nbl_v2.0].[Time Period].[TIME_PERIOD_NUMBER]

>[nbl_v1.1].[Disease Phase Timing].[AGE_AT_DISEASE_PHASE] skos:exactMatch [nbl_v2.0].[Time Period].[AGE_AT_START]

>[nbl_v1.1].[Disease Phase Timing].[YEAR_AT_DISEASE_PHASE] skos:exactMatch [nbl_v2.0].[Time Period].[YEAR_AT_START]

>[nbl_v1.1].[Labs] skos:exactMatch [nbl_v2.0].[Laboratory Test]

>[nbl_v1.1].[Labs].[LAB_TEST] skos:exactMatch [nbl_v2.0].[Laboratory Test].[TEST]

>[nbl_v1.1].[Labs].[LAB_RESULT_NUMERIC] skos:exactMatch [nbl_v2.0].[Laboratory Test].[RESULT_NUMERIC]

>[nbl_v1.1].[Histology] skos:exactMatch [nbl_v2.0].[Diagnosis]

>[nbl_v1.1].[Histology].[AGE_AT_HIST_ASSESSMENT] skos:exactMatch [nbl_v2.0].[Diagnosis].[AGE_AT_DIAG_ASSESSMENT]

>[nbl_v1.1].[Histology].[HISTOLOGY] skos:exactMatch [nbl_v2.0].[Diagnosis].[DIAGNOSIS]

>[nbl_v1.1].[Histology].[HISTOLOGY_INPC] skos:exactMatch [nbl_v2.0].[Diagnosis].[REVISED_INPC]

>[nbl_v1.1].[Tumor Assessment] skos:exactMatch [nbl_v2.0].[Disease Site Assessment]

>[nbl_v1.1].[Tumor Assessment].[AGE_AT_TUMOR_ASSESSMENT] skos:exactMatch [nbl_v2.0].[Disease Site Assessment].[AGE_AT_DISEASE_SITE_ASSESSMENT]

>[nbl_v1.1].[Tumor Assessment].[TUMOR_STATE] skos:exactMatch [nbl_v2.0].[Disease Site Assessment].[STATUS]

>[nbl_v1.1].[Tumor Assessment].[TUMOR_CLASSIFICATION] skos:exactMatch [nbl_v2.0].[Disease Site Assessment].[CLASSIFICATION]

>[nbl_v1.1].[Tumor Assessment].[TUMOR_SITE] skos:exactMatch [nbl_v2.0].[Disease Site Assessment].[SITE]

>[nbl_v1.1].[Secondary Malignant Neoplasm] skos:exactMatch [nbl_v2.0].[Subsequent Malignant Neoplasm]

>[nbl_v1.1].[Secondary Malignant Neoplasm].[SMN_MORPH_SNO] skos:broadMatch [nbl_v2.0].[Subsequent Malignant Neoplasm].[MORPH_CODE]

>[nbl_v1.1].[Secondary Malignant Neoplasm].[SMN_MORPH_ICDO] skos:broadMatch [nbl_v2.0].[Subsequent Malignant Neoplasm].[MORPH_CODE]

>[nbl_v1.1].[Secondary Malignant Neoplasm].[SMN_MORPH_TXT] skos:exactMatch [nbl_v2.0].[Subsequent Malignant Neoplasm].[MORPH_CODE_DISPLAY]

>[nbl_v1.1].[Secondary Malignant Neoplasm].[SMN_TOP_SNO] skos:broadMatch [nbl_v2.0].[Subsequent Malignant Neoplasm].[TOP_CODE]

>[nbl_v1.1].[Secondary Malignant Neoplasm].[SMN_TOP_ICDO] skos:broadMatch [nbl_v2.0].[Subsequent Malignant Neoplasm].[TOP_CODE]

>[nbl_v1.1].[Secondary Malignant Neoplasm].[SMN_TOP_TXT] skos:exactMatch [nbl_v2.0].[Subsequent Malignant Neoplasm].[TOP_CODE_DISPLAY]
