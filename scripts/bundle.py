import os, json, argparse, datetime, time, export
from utils import sheets_helper, script_helper

#Examples by class
example_bank = {
  "DataContributorPersonRecord": [
    {
      "submitter_id": "dcpr1",
      "person_submitter_id": "<to be added by D4CG>",
      "honest_broker_subject_id": "HB001",
      "data_contributor_id": "COG"
    },
    {
      "submitter_id": "dcpr2",
      "person_submitter_id": "<to be added by D4CG>",
      "honest_broker_subject_id": "HB002",
      "data_contributor_id": "COG"
    },
    {
      "submitter_id": "dcpr3",
      "person_submitter_id": "<to be added by D4CG>",
      "honest_broker_subject_id": "HB003",
      "data_contributor_id": "COG"
    },
    {
      "submitter_id": "dcpr4",
      "person_submitter_id": "<to be added by D4CG>",
      "honest_broker_subject_id": "HB004",
      "data_contributor_id": "COG"
    }
  ],

  "Subject": [
    {
      "submitter_id": "patient1",
      "data_contributor_person_record_submitter_id": "dcpr1",
      "consortium": "INTERACT",
      "disease_group": "AML",
      "sex": "Female",
      "enrolled_status": "Yes",
      "age_at_enrollment": "1460"
    },
    {
      "submitter_id": "patient2",
      "data_contributor_person_record_submitter_id": "dcpr2",
      "consortium": "INTERACT",
      "disease_group": "AML",
      "sex": "Male",
      "enrolled_status": "Yes",
      "age_at_enrollment": "1825"
    },
    {
      "submitter_id": "patient3",
      "data_contributor_person_record_submitter_id": "dcpr3",
      "consortium": "HIBiSCus",
      "disease_group": "EWS",
      "sex": "Male",
      "age_at_enrollment": "4380"
    },
    {
      "submitter_id": "patient4",
      "data_contributor_person_record_submitter_id": "dcpr4",
      "consortium": "HIBiSCus",
      "disease_group": "EWS",
      "sex": "Female",
      "age_at_enrollment": "5840"
    }
  ],

  "StudyMetadata": [
    {
      "submitter_id": "study1",
      "subjects_submitter_id": ["patient1", "patient2"],
      "study_id": "AAML0531"
    },
    {
      "submitter_id": "study2",
      "subjects_submitter_id": ["patient3"],
      "study_id": "AEWS0031"
    },
    {
      "submitter_id": "study3",
      "subjects_submitter_id": ["patient4"],
      "study_id": "AEWS1031"
    }
  ],

  "StudySubgroupAssignment": [
    {
      "subjects_submitter_id": ["patient1"],
      "subgroup_type": "Treatment Arm",
      "subgroup_name": "AAML0531:Arm A HR",
      "subgroup_assignment_order": "1"
    },
    {
      "subjects_submitter_id": ["patient2"],
      "subgroup_type": "Treatment Arm",
      "subgroup_name": "AAML0531:Arm B HR",
      "subgroup_assignment_order": "1"
    },
    {
      "subjects_submitter_id": ["patient3"],
      "subgroup_type": "Treatment Arm",
      "subgroup_name": "AEWS0031:Regimen B 2W-VDC-MESNA+IFO-GCSF for metastatic or unresectable disease",
      "subgroup_assignment_order": "1",
      "age_at_subgroup_assignment": "4380"
    },
    {
      "subjects_submitter_id": ["patient4"],
      "subgroup_type": "Treatment Arm",
      "subgroup_name": "AEWS1031:Arm A >> HD-IFO/etoposide (IE) >> Interval compressed VDC-IE",
      "subgroup_assignment_order": "1",
      "age_at_subgroup_assignment": "5840"
    }
  ],

  "Timing": [
    {
      "submitter_id": "p1_timing_phase1_dx",
      "subjects_submitter_id": ["patient1"],
      "parent_submitter_id": "",
      "time_period_type": "Disease Phase",
      "disease_phase": "Initial Diagnosis",
      "course": "",
      "time_period_number": "1",
      "age_at_start": "1460",
      "year_at_start": "2014"
    },
    {
      "submitter_id": "p1_timing_course1_induction",
      "subjects_submitter_id": ["patient1"],
      "parent_submitter_id": "p1_timing_phase1_dx",
      "time_period_type": "Course",
      "disease_phase": "",
      "course": "Induction",
      "time_period_number": "1",
      "age_at_start": "1462",
      "year_at_start": "2014"
    },
    {
      "submitter_id": "p1_timing_course2_intensification",
      "subjects_submitter_id": ["patient1"],
      "parent_submitter_id": "p1_timing_phase1_dx",
      "time_period_type": "Course",
      "disease_phase": "",
      "course": "Intensification",
      "time_period_number": "1",
      "age_at_start": "1520",
      "year_at_start": "2014"
    },
    {
      "submitter_id": "p1_timing_course3_consolidation",
      "subjects_submitter_id": ["patient1"],
      "parent_submitter_id": "p1_timing_phase1_dx",
      "time_period_type": "Course",
      "disease_phase": "",
      "course": "Consolidation",
      "time_period_number": "1",
      "age_at_start": "1580",
      "year_at_start": "2014"
    },
    {
      "submitter_id": "p1_timing_phase2_relapse",
      "subjects_submitter_id": ["patient1"],
      "parent_submitter_id": "",
      "time_period_type": "Disease Phase",
      "disease_phase": "Relapse",
      "course": "",
      "time_period_number": "1",
      "age_at_start": "1820",
      "year_at_start": "2015"
    },
    {
      "submitter_id": "p1_timing_course4_relapse_induction",
      "subjects_submitter_id": ["patient1"],
      "parent_submitter_id": "p1_timing_phase2_relapse",
      "time_period_type": "Course",
      "disease_phase": "",
      "course": "Induction",
      "time_period_number": "2",
      "age_at_start": "1822",
      "year_at_start": "2015"
    },
    {
      "submitter_id": "p2_timing_phase1_dx",
      "subjects_submitter_id": ["patient2"],
      "parent_submitter_id": "",
      "time_period_type": "Disease Phase",
      "disease_phase": "Initial Diagnosis",
      "course": "",
      "time_period_number": "1",
      "age_at_start": "1825",
      "year_at_start": "2014"
    },
    {
      "submitter_id": "p2_timing_course1_induction",
      "subjects_submitter_id": ["patient2"],
      "parent_submitter_id": "p2_timing_phase1_dx",
      "time_period_type": "Course",
      "disease_phase": "",
      "course": "Induction",
      "time_period_number": "1",
      "age_at_start": "1827",
      "year_at_start": "2014"
    },
    {
      "submitter_id": "p3_timing_phase1_dx",
      "subjects_submitter_id": ["patient3"],
      "parent_submitter_id": "",
      "time_period_type": "Disease Phase",
      "disease_phase": "Initial Diagnosis",
      "course": "",
      "time_period_number": "1",
      "age_at_start": "4380",
      "year_at_start": "2016"
    },
    {
      "submitter_id": "p3_timing_course1_induction",
      "subjects_submitter_id": ["patient3"],
      "parent_submitter_id": "p3_timing_phase1_dx",
      "time_period_type": "Course",
      "disease_phase": "",
      "course": "Induction",
      "time_period_number": "1",
      "age_at_start": "4385",
      "year_at_start": "2016"
    },
    {
      "submitter_id": "p3_timing_course2_consolidation",
      "subjects_submitter_id": ["patient3"],
      "parent_submitter_id": "p3_timing_phase1_dx",
      "time_period_type": "Course",
      "disease_phase": "",
      "course": "Consolidation",
      "time_period_number": "1",
      "age_at_start": "4460",
      "year_at_start": "2016"
    },
    {
      "submitter_id": "p3_timing_course3_maintenance",
      "subjects_submitter_id": ["patient3"],
      "parent_submitter_id": "p3_timing_phase1_dx",
      "time_period_type": "Course",
      "disease_phase": "",
      "course": "Maintenance",
      "time_period_number": "1",
      "age_at_start": "4750",
      "year_at_start": "2017"
    },
    {
      "submitter_id": "p4_timing_phase1_dx",
      "subjects_submitter_id": ["patient4"],
      "parent_submitter_id": "",
      "time_period_type": "Disease Phase",
      "disease_phase": "Initial Diagnosis",
      "course": "",
      "time_period_number": "1",
      "age_at_start": "5840",
      "year_at_start": "2016"
    },
    {
      "submitter_id": "p4_timing_course1_induction",
      "subjects_submitter_id": ["patient4"],
      "parent_submitter_id": "p4_timing_phase1_dx",
      "time_period_type": "Course",
      "disease_phase": "",
      "course": "Induction",
      "time_period_number": "1",
      "age_at_start": "5845",
      "year_at_start": "2016"
    },
    {
      "submitter_id": "p4_timing_course2_consolidation",
      "subjects_submitter_id": ["patient4"],
      "parent_submitter_id": "p4_timing_phase1_dx",
      "time_period_type": "Course",
      "disease_phase": "",
      "course": "Consolidation",
      "time_period_number": "1",
      "age_at_start": "5920",
      "year_at_start": "2016"
    },
    {
      "submitter_id": "p4_timing_course3_maintenance",
      "subjects_submitter_id": ["patient4"],
      "parent_submitter_id": "p4_timing_phase1_dx",
      "time_period_type": "Course",
      "disease_phase": "",
      "course": "Maintenance",
      "time_period_number": "1",
      "age_at_start": "6200",
      "year_at_start": "2017"
    },
    {
      "submitter_id": "p4_timing_phase2_relapse",
      "subjects_submitter_id": ["patient4"],
      "parent_submitter_id": "",
      "time_period_type": "Disease Phase",
      "disease_phase": "Relapse",
      "course": "",
      "time_period_number": "1",
      "age_at_start": "6500",
      "year_at_start": "2018"
    },
    {
      "submitter_id": "p4_timing_course4_relapse_induction",
      "subjects_submitter_id": ["patient4"],
      "parent_submitter_id": "p4_timing_phase2_relapse",
      "time_period_type": "Course",
      "disease_phase": "",
      "course": "Induction",
      "time_period_number": "2",
      "age_at_start": "6505",
      "year_at_start": "2018"
    }
  ],

  "OffProtocolTherapyOrStudy": [
    {
      "subjects_submitter_id": ["patient1"],
      "timings_submitter_id": ["p1_timing_course3_consolidation"],
      "age_off": "1640",
      "off_type": "Study",
      "reason_off": "Completion of Planned Therapy"
    },
    {
      "subjects_submitter_id": ["patient2"],
      "timings_submitter_id": ["p2_timing_course1_induction"],
      "age_off": "1840",
      "off_type": "Study",
      "reason_off": "Adverse Event"
    },
    {
      "subjects_submitter_id": ["patient3"],
      "timings_submitter_id": ["p3_timing_course3_maintenance"],
      "age_off": "5020",
      "off_type": "Protocol Therapy",
      "reason_off": "Completion of Planned Therapy"
    },
    {
      "subjects_submitter_id": ["patient4"],
      "timings_submitter_id": ["p4_timing_course3_maintenance"],
      "age_off": "6300",
      "off_type": "Protocol Therapy",
      "reason_off": "Completion of Planned Therapy"
    }
  ],

  "SurvivalCharacteristics": [
    {
      "subjects_submitter_id": ["patient1"],
      "timings_submitter_id": ["p1_timing_phase2_relapse"],
      "age_at_lkss": "1840",
      "lkss": "Dead",
      "cause_of_death": "Disease Progression"
    },
    {
      "subjects_submitter_id": ["patient2"],
      "timings_submitter_id": ["p2_timing_phase1_dx"],
      "age_at_lkss": "2000",
      "lkss": "Alive",
      "cause_of_death": ""
    },
    {
      "subjects_submitter_id": ["patient3"],
      "timings_submitter_id": ["p3_timing_course3_maintenance"],
      "age_at_lkss": "5200",
      "lkss": "Alive",
      "cause_of_death": "",
      "cause_of_death_detail": ""
    },
    {
      "subjects_submitter_id": ["patient4"],
      "timings_submitter_id": ["p4_timing_phase2_relapse"],
      "age_at_lkss": "7000",
      "lkss": "Alive",
      "cause_of_death": "",
      "cause_of_death_detail": ""
    }
  ],

  "MedicalHistory": [
    {
      "subjects_submitter_id": ["patient1"],
      "medical_history_condition": "None"
    },
    {
      "subjects_submitter_id": ["patient2"],
      "medical_history_condition": "Trisomy 21"
    }
  ],

  "VitalsAndAnthropometrics": [
    {
      "subjects_submitter_id": ["patient1"],
      "timings_submitter_id": ["p1_timing_phase1_dx"],
      "age_at_measurement": "1460",
      "anthropometric_measurement_type": "Weight",
      "result_text": "",
      "result_numeric": "16.2",
      "result_unit": "kg"
    },
    {
      "subjects_submitter_id": ["patient1"],
      "timings_submitter_id": ["p1_timing_phase1_dx"],
      "age_at_measurement": "1460",
      "anthropometric_measurement_type": "Height",
      "result_text": "",
      "result_numeric": "100.3",
      "result_unit": "cm"
    },
    {
      "subjects_submitter_id": ["patient2"],
      "timings_submitter_id": ["p2_timing_phase1_dx"],
      "age_at_measurement": "1825",
      "anthropometric_measurement_type": "Weight",
      "result_text": "",
      "result_numeric": "21.8",
      "result_unit": "kg"
    },
    {
      "subjects_submitter_id": ["patient2"],
      "timings_submitter_id": ["p2_timing_phase1_dx"],
      "age_at_measurement": "1825",
      "anthropometric_measurement_type": "Height",
      "result_text": "",
      "result_numeric": "116.8",
      "result_unit": "cm"
    },
    {
      "subjects_submitter_id": ["patient3"],
      "timings_submitter_id": ["p3_timing_phase1_dx"],
      "age_at_measurement": "4380",
      "anthropometric_measurement_type": "Weight",
      "result_text": "",
      "result_numeric": "40.2",
      "result_unit": "kg"
    },
    {
      "subjects_submitter_id": ["patient3"],
      "timings_submitter_id": ["p3_timing_phase1_dx"],
      "age_at_measurement": "4380",
      "anthropometric_measurement_type": "Height",
      "result_text": "",
      "result_numeric": "145.0",
      "result_unit": "cm"
    },
    {
      "subjects_submitter_id": ["patient4"],
      "timings_submitter_id": ["p4_timing_phase1_dx"],
      "age_at_measurement": "5840",
      "anthropometric_measurement_type": "Weight",
      "result_text": "",
      "result_numeric": "55.5",
      "result_unit": "kg"
    },
    {
      "subjects_submitter_id": ["patient4"],
      "timings_submitter_id": ["p4_timing_phase1_dx"],
      "age_at_measurement": "5840",
      "anthropometric_measurement_type": "Height",
      "result_text": "",
      "result_numeric": "165.0",
      "result_unit": "cm"
    }
  ],

  "LaboratoryTest": [
    {
      "subjects_submitter_id": ["patient1"],
      "timings_submitter_id": ["p1_timing_phase1_dx"],
      "age_at_lab": "1460",
      "laboratory_test": "White Blood Cell Count",
      "laboratory_test_method": "Other",
      "laboratory_test_specimen": "Peripheral blood",
      "result_text": "",
      "result_numeric": "47000",
      "result_unit": "/uL"
    },
    {
      "subjects_submitter_id": ["patient1"],
      "timings_submitter_id": ["p1_timing_phase1_dx"],
      "age_at_lab": "1460",
      "laboratory_test": "Hemoglobin",
      "laboratory_test_method": "Other",
      "laboratory_test_specimen": "Peripheral blood",
      "result_text": "",
      "result_numeric": "7.8",
      "result_unit": "g/dL"
    },
    {
      "subjects_submitter_id": ["patient1"],
      "timings_submitter_id": ["p1_timing_phase1_dx"],
      "age_at_lab": "1460",
      "laboratory_test": "Platelet Count",
      "laboratory_test_method": "Other",
      "laboratory_test_specimen": "Peripheral blood",
      "result_text": "",
      "result_numeric": "30000",
      "result_unit": "/uL"
    },
    {
      "subjects_submitter_id": ["patient2"],
      "timings_submitter_id": ["p2_timing_phase1_dx"],
      "age_at_lab": "1825",
      "laboratory_test": "White Blood Cell Count",
      "laboratory_test_method": "Other",
      "laboratory_test_specimen": "Peripheral blood",
      "result_text": "",
      "result_numeric": "52000",
      "result_unit": "/uL"
    },
    {
      "subjects_submitter_id": ["patient2"],
      "timings_submitter_id": ["p2_timing_phase1_dx"],
      "age_at_lab": "1825",
      "laboratory_test": "Hemoglobin",
      "laboratory_test_method": "Other",
      "laboratory_test_specimen": "Peripheral blood",
      "result_text": "",
      "result_numeric": "8.2",
      "result_unit": "g/dL"
    },
    {
      "subjects_submitter_id": ["patient2"],
      "timings_submitter_id": ["p2_timing_phase1_dx"],
      "age_at_lab": "1825",
      "laboratory_test": "Platelet Count",
      "laboratory_test_method": "Other",
      "laboratory_test_specimen": "Peripheral blood",
      "result_text": "",
      "result_numeric": "25000",
      "result_unit": "/uL"
    },
    {
      "subjects_submitter_id": ["patient3"],
      "timings_submitter_id": ["p3_timing_phase1_dx"],
      "age_at_lab": "4380",
      "laboratory_test": "Alkaline Phophatase",
      "laboratory_test_method": "Other",
      "laboratory_test_specimen": "Peripheral blood",
      "result_text": "",
      "result_numeric": "280",
      "result_unit": "U/L"
    },
    {
      "subjects_submitter_id": ["patient3"],
      "timings_submitter_id": ["p3_timing_phase1_dx"],
      "age_at_lab": "4380",
      "laboratory_test": "LDH",
      "laboratory_test_method": "Other",
      "laboratory_test_specimen": "Peripheral blood",
      "result_text": "",
      "result_numeric": "450",
      "result_unit": "U/L"
    },
    {
      "subjects_submitter_id": ["patient4"],
      "timings_submitter_id": ["p4_timing_phase1_dx"],
      "age_at_lab": "5840",
      "laboratory_test": "ESR",
      "laboratory_test_method": "Other",
      "laboratory_test_specimen": "Peripheral blood",
      "result_text": "",
      "result_numeric": "35",
      "result_unit": "mm/h"
    },
    {
      "subjects_submitter_id": ["patient4"],
      "timings_submitter_id": ["p4_timing_phase1_dx"],
      "age_at_lab": "5840",
      "laboratory_test": "LDH",
      "laboratory_test_method": "Other",
      "laboratory_test_specimen": "Peripheral blood",
      "result_text": "",
      "result_numeric": "480",
      "result_unit": "U/L"
    }
  ],

  "GeneticAnalysis": [
    {
      "subjects_submitter_id": ["patient1"],
      "timings_submitter_id": ["p1_timing_phase1_dx"],
      "age_at_genetic_analysis": "1460",
      "genetic_analysis_method": "Sequencing, NGS, NOS",
      "genetic_analysis_status": "Present",
      "alteration": "NM_002520.6(NPM1):c.860_863dupTCTG",
      "alteration_type": "Duplication",
      "gene": "NPM1",
      "hgvs_coding": "NM_001355006.1:c.860_863dup",
      "allelic_ratio": "0.45"
    },
    {
      "subjects_submitter_id": ["patient2"],
      "timings_submitter_id": ["p2_timing_phase1_dx"],
      "age_at_genetic_analysis": "1825",
      "genetic_analysis_method": "Cytogenetics, Karyotyping",
      "genetic_analysis_status": "Present",
      "alteration": "t(9;11)(p22;q23)",
      "alteration_type": "Translocation",
      "chromosome": "11",
      "iscn": "46,XY,t(9;11)(p22;q23)",
      "independent_aberrations": "No",
      "cells_in_metaphase": "20"
    },
    {
      "subjects_submitter_id": ["patient2"],
      "timings_submitter_id": ["p2_timing_phase1_dx"],
      "age_at_genetic_analysis": "1825",
      "genetic_analysis_method": "FISH",
      "genetic_analysis_status": "Present",
      "alteration": "KMT2A-MLLT3 fusion",
      "alteration_type": "Rearrangement",
      "alteration_effect": "Gene Fusion",
      "chromosome": "11",
      "gene": "KMT2A",
      "gene_fusion_partner": "MLLT3"
    },
    {
      "subjects_submitter_id": ["patient3"],
      "timings_submitter_id": ["p3_timing_phase1_dx"],
      "age_at_genetic_analysis": "4385",
      "genetic_analysis_method": "FISH",
      "genetic_analysis_status": "Present",
      "alteration": "EWSR1-FLI1",
      "alteration_type": "Rearrangement",
      "alteration_effect": "Gene Fusion",
      "chromosome": "22",
      "gene": "EWSR1",
      "gene_fusion_partner": "FLI1"
    },
    {
      "subjects_submitter_id": ["patient4"],
      "timings_submitter_id": ["p4_timing_phase1_dx"],
      "age_at_genetic_analysis": "5845",
      "genetic_analysis_method": "FISH",
      "genetic_analysis_status": "Present",
      "alteration": "12q Gain",
      "alteration_type": "Unknown",
      "alteration_effect": "Gain",
      "chromosome": "12",
      "gene": "",
      "gene_fusion_partner": ""
    }
  ],

  "Biospecimen": [
    {
      "subjects_submitter_id": ["patient1"],
      "biospecimen_container_type": "Cryovial",
      "biospecimen_media": "Not Reported",
      "biospecimen_type": "Bone marrow aspirate",
      "current_qty_unit": "vial",
      "current_qty_value": "2"
    },
    {
      "subjects_submitter_id": ["patient2"],
      "biospecimen_container_type": "Cryovial",
      "biospecimen_media": "Not Reported",
      "biospecimen_type": "Peripheral blood",
      "current_qty_unit": "vial",
      "current_qty_value": "1"
    },
    {
      "subjects_submitter_id": ["patient3"],
      "biospecimen_container_type": "Cryovial",
      "biospecimen_media": "Not Reported",
      "biospecimen_type": "Tumor tissue",
      "current_qty_unit": "vial",
      "current_qty_value": "3"
    },
    {
      "subjects_submitter_id": ["patient4"],
      "biospecimen_container_type": "Cryovial",
      "biospecimen_media": "Not Reported",
      "biospecimen_type": "Tumor tissue",
      "current_qty_unit": "vial",
      "current_qty_value": "2"
    }
  ],

  "FunctionTest": [
    {
      "subjects_submitter_id": ["patient1"],
      "timings_submitter_id": ["p1_timing_phase1_dx"],
      "age_at_function_test": "1458",
      "function_test": "Echocardiogram",
      "functional_measurement_type": "Ejection Fraction",
      "result_numeric": "60",
      "result_unit": "%"
    },
    {
      "subjects_submitter_id": ["patient2"],
      "timings_submitter_id": ["p2_timing_phase1_dx"],
      "age_at_function_test": "1823",
      "function_test": "Echocardiogram",
      "functional_measurement_type": "Ejection Fraction",
      "result_numeric": "65",
      "result_unit": "%"
    }
  ],

  "Diagnosis": [
    {
      "subjects_submitter_id": ["patient1"],
      "timings_submitter_id": ["p1_timing_phase1_dx"],
      "age_at_diag_assessment": "1460",
      "diagnosis_basis": "Integrated",
      "diagnosis": "WHO >> Version 4 >> Acute Myelomonocytic Leukemia"
    },
    {
      "subjects_submitter_id": ["patient2"],
      "timings_submitter_id": ["p2_timing_phase1_dx"],
      "age_at_diag_assessment": "1825",
      "diagnosis_basis": "Integrated",
      "diagnosis": "WHO >> Version 4 >> Acute Monoblastic/Monocytic Leukemia"
    },
    {
      "subjects_submitter_id": ["patient3"],
      "timings_submitter_id": ["p3_timing_phase1_dx"],
      "age_at_diag_assessment": "4380",
      "diagnosis_basis": "Integrated",
      "diagnosis": "Ewing Sarcoma"
    },
    {
      "subjects_submitter_id": ["patient4"],
      "timings_submitter_id": ["p4_timing_phase1_dx"],
      "age_at_diag_assessment": "5840",
      "diagnosis_basis": "Integrated",
      "diagnosis": "Ewing Sarcoma"
    },
    {
      "subjects_submitter_id": ["patient4"],
      "timings_submitter_id": ["p4_timing_phase2_relapse"],
      "age_at_diag_assessment": "6500",
      "diagnosis_basis": "Integrated",
      "diagnosis": "Ewing Sarcoma"
    }
  ],

  "DiseaseSiteAssessment": [
    {
      "subjects_submitter_id": ["patient1"],
      "timings_submitter_id": ["p1_timing_phase1_dx"],
      "age_at_disease_site_assessment": "1460",
      "detection_method": "Bone marrow aspirate",
      "disease_site": "Bone marrow"
    },
    {
      "subjects_submitter_id": ["patient2"],
      "timings_submitter_id": ["p2_timing_phase1_dx"],
      "age_at_disease_site_assessment": "1825",
      "detection_method": "Bone marrow aspirate",
      "disease_site": "Bone marrow"
    },
    {
      "subjects_submitter_id": ["patient3"],
      "timings_submitter_id": ["p3_timing_phase1_dx"],
      "age_at_disease_site_assessment": "4380",
      "detection_method": "Radiographic imaging",
      "disease_site": "Pelvic bone",
      "tumor_state": "Primary",
      "laterality": "Unilateral",
      "diameter1": "100",
      "diameter1_unit": "mm",
      "diameter1_axis": "base",
      "diameter2": "80",
      "diameter2_unit": "mm",
      "diameter2_axis": "height",
      "diameter3": "70",
      "diameter3_unit": "mm",
      "diameter3_axis": "height",
      "skip_lesions": "No",
      "fracture_at_site": "No",
      "joint_involvement": "No"
    },
    {
      "subjects_submitter_id": ["patient3"],
      "timings_submitter_id": ["p3_timing_phase1_dx"],
      "age_at_disease_site_assessment": "4380",
      "detection_method": "Radiographic imaging",
      "disease_site": "Lung",
      "tumor_state": "Metastatic",
      "laterality": "Bilateral",
      "diameter1": "15",
      "diameter1_unit": "mm",
      "diameter1_axis": "base",
      "diameter2": "12",
      "diameter2_unit": "mm",
      "diameter2_axis": "height",
      "diameter3": "10",
      "diameter3_unit": "mm",
      "diameter3_axis": "height",
      "skip_lesions": "No",
      "fracture_at_site": "No",
      "joint_involvement": "No"
    },
    {
      "subjects_submitter_id": ["patient4"],
      "timings_submitter_id": ["p4_timing_phase1_dx"],
      "age_at_disease_site_assessment": "5840",
      "detection_method": "Radiographic imaging",
      "disease_site": "Femur",
      "tumor_state": "Primary",
      "laterality": "Unilateral",
      "diameter1": "80",
      "diameter1_unit": "mm",
      "diameter1_axis": "base",
      "diameter2": "60",
      "diameter2_unit": "mm",
      "diameter2_axis": "height",
      "diameter3": "50",
      "diameter3_unit": "mm",
      "diameter3_axis": "height",
      "skip_lesions": "No",
      "fracture_at_site": "Yes",
      "joint_involvement": "Yes"
    },
    {
      "subjects_submitter_id": ["patient4"],
      "timings_submitter_id": ["p4_timing_phase2_relapse"],
      "age_at_disease_site_assessment": "6500",
      "detection_method": "Radiographic imaging",
      "disease_site": "Femur",
      "tumor_state": "Relapsed",
      "laterality": "Unilateral",
      "diameter1": "35",
      "diameter1_unit": "mm",
      "diameter1_axis": "base",
      "diameter2": "25",
      "diameter2_unit": "mm",
      "diameter2_axis": "height",
      "diameter3": "20",
      "diameter3_unit": "mm",
      "diameter3_axis": "height",
      "skip_lesions": "Yes",
      "fracture_at_site": "Yes",
      "joint_involvement": "Yes"
    }
  ],

  "SurgicalProcedures": [
    {
      "subjects_submitter_id": ["patient3"],
      "timings_submitter_id": ["p3_timing_phase1_dx"],
      "procedure_class": "Surgery",
      "procedure": "Internal Hemipelvectomy",
      "procedure_site": "Pelvis",
      "laterality": "Unilateral",
      "margins": "R0 - Complete Resection, Negative Margins",
      "procedure_extent": "Complete Resection"
    },
    {
      "subjects_submitter_id": ["patient4"],
      "timings_submitter_id": ["p4_timing_phase1_dx"],
      "procedure_class": "Limb Salvage",
      "procedure": "Rotationplasty",
      "procedure_site": "Femur",
      "laterality": "Unilateral",
      "margins": "R0 - Complete Resection, Negative Margins",
      "procedure_extent": "Gross Total"
    }
  ],

  "Medication": [
    {
      "subjects_submitter_id": ["patient1"],
      "timings_submitter_id": ["p1_timing_course1_induction"],
      "age_at_medication_start": "1462",
      "age_at_medication_end": "1502",
      "route": "Systemic",
      "medication": "Cytarabine",
      "number_doses": "20",
      "medication_dose_administered": "100",
      "medication_dose_intended": "100",
      "medication_dose_unit": "mg/m2"
    },
    {
      "subjects_submitter_id": ["patient1"],
      "timings_submitter_id": ["p1_timing_course1_induction"],
      "age_at_medication_start": "1462",
      "age_at_medication_end": "1465",
      "route": "Systemic",
      "medication": "Daunorubicin",
      "number_doses": "3",
      "medication_dose_administered": "60",
      "medication_dose_intended": "60",
      "medication_dose_unit": "mg/m2"
    },
    {
      "subjects_submitter_id": ["patient1"],
      "timings_submitter_id": ["p1_timing_course1_induction"],
      "age_at_medication_start": "1462",
      "age_at_medication_end": "1467",
      "route": "Systemic",
      "medication": "Etoposide",
      "number_doses": "5",
      "medication_dose_administered": "100",
      "medication_dose_intended": "100",
      "medication_dose_unit": "mg/m2"
    },
    {
      "subjects_submitter_id": ["patient1"],
      "timings_submitter_id": ["p1_timing_course2_intensification"],
      "age_at_medication_start": "1520",
      "age_at_medication_end": "1560",
      "route": "Systemic",
      "medication": "High-dose Cytarabine",
      "number_doses": "8",
      "medication_dose_administered": "3000",
      "medication_dose_intended": "3000",
      "medication_dose_unit": "mg/m2"
    },
    {
      "subjects_submitter_id": ["patient1"],
      "timings_submitter_id": ["p1_timing_course3_consolidation"],
      "age_at_medication_start": "1580",
      "age_at_medication_end": "1640",
      "route": "Systemic",
      "medication": "Cytarabine",
      "number_doses": "8",
      "medication_dose_administered": "1000",
      "medication_dose_intended": "1000",
      "medication_dose_unit": "mg/m2"
    },
    {
      "subjects_submitter_id": ["patient1"],
      "timings_submitter_id": ["p1_timing_course4_relapse_induction"],
      "age_at_medication_start": "1822",
      "age_at_medication_end": "1840",
      "medication_category": "Chemotherapy",
      "route": "Systemic",
      "medication": "FLAG-IDA regimen",
      "number_doses": "6",
      "medication_dose_intended": "900",
      "medication_dose_administered": "450",
      "medication_dose_unit": "mg/m2"
    },
    {
      "subjects_submitter_id": ["patient2"],
      "timings_submitter_id": ["p2_timing_course1_induction"],
      "age_at_medication_start": "1827",
      "age_at_medication_end": "1860",
      "route": "Systemic",
      "medication": "Cytarabine",
      "number_doses": "20",
      "medication_dose_administered": "100",
      "medication_dose_intended": "100",
      "medication_dose_unit": "mg/m2"
    },
    {
      "subjects_submitter_id": ["patient2"],
      "timings_submitter_id": ["p2_timing_course1_induction"],
      "age_at_medication_start": "1827",
      "age_at_medication_end": "1830",
      "route": "Systemic",
      "medication": "Daunorubicin",
      "number_doses": "3",
      "medication_dose_administered": "60",
      "medication_dose_intended": "60",
      "medication_dose_unit": "mg/m2"
    },
    {
      "subjects_submitter_id": ["patient2"],
      "timings_submitter_id": ["p2_timing_course1_induction"],
      "age_at_medication_start": "1827",
      "age_at_medication_end": "1831",
      "route": "Systemic",
      "medication": "Etoposide",
      "number_doses": "5",
      "medication_dose_administered": "100",
      "medication_dose_intended": "100",
      "medication_dose_unit": "mg/m2"
    },
    {
      "subjects_submitter_id": ["patient2"],
      "timings_submitter_id": ["p2_timing_course1_induction"],
      "age_at_medication_start": "1830",
      "age_at_medication_end": "1830",
      "route": "Systemic",
      "medication": "Gemtuzumab ozogamicin",
      "number_doses": "1",
      "medication_dose_administered": "3",
      "medication_dose_intended": "3",
      "medication_dose_unit": "mg/m2"
    },
    {
      "subjects_submitter_id": ["patient3"],
      "timings_submitter_id": ["p3_timing_course1_induction"],
      "age_at_medication_start": "4385",
      "age_at_medication_end": "4420",
      "route": "Systemic",
      "medication": "Vincristine",
      "number_doses": "8",
      "medication_dose_administered": "1.5",
      "medication_dose_intended": "1.5",
      "medication_dose_unit": "mg/m2"
    },
    {
      "subjects_submitter_id": ["patient3"],
      "timings_submitter_id": ["p3_timing_course1_induction"],
      "age_at_medication_start": "4385",
      "age_at_medication_end": "4420",
      "route": "Systemic",
      "medication": "Doxorubicin",
      "number_doses": "4",
      "medication_dose_administered": "75",
      "medication_dose_intended": "75",
      "medication_dose_unit": "mg/m2"
    },
    {
      "subjects_submitter_id": ["patient3"],
      "timings_submitter_id": ["p3_timing_course1_induction"],
      "age_at_medication_start": "4385",
      "age_at_medication_end": "4420",
      "route": "Systemic",
      "medication": "Cyclophosphamide",
      "number_doses": "4",
      "medication_dose_administered": "1200",
      "medication_dose_intended": "1200",
      "medication_dose_unit": "mg/m2"
    },
    {
      "subjects_submitter_id": ["patient3"],
      "timings_submitter_id": ["p3_timing_course2_consolidation"],
      "age_at_medication_start": "4460",
      "age_at_medication_end": "4520",
      "route": "Systemic",
      "medication": "Ifosfamide",
      "number_doses": "5",
      "medication_dose_administered": "1800",
      "medication_dose_intended": "1800",
      "medication_dose_unit": "mg/m2"
    },
    {
      "subjects_submitter_id": ["patient3"],
      "timings_submitter_id": ["p3_timing_course2_consolidation"],
      "age_at_medication_start": "4460",
      "age_at_medication_end": "4520",
      "route": "Systemic",
      "medication": "Etoposide",
      "number_doses": "5",
      "medication_dose_administered": "100",
      "medication_dose_intended": "100",
      "medication_dose_unit": "mg/m2"
    },
    {
      "subjects_submitter_id": ["patient4"],
      "timings_submitter_id": ["p4_timing_course1_induction"],
      "age_at_medication_start": "5845",
      "age_at_medication_end": "5880",
      "route": "Systemic",
      "medication": "Vincristine",
      "number_doses": "8",
      "medication_dose_administered": "1.5",
      "medication_dose_intended": "1.5",
      "medication_dose_unit": "mg/m2"
    },
    {
      "subjects_submitter_id": ["patient4"],
      "timings_submitter_id": ["p4_timing_course1_induction"],
      "age_at_medication_start": "5845",
      "age_at_medication_end": "5880",
      "route": "Systemic",
      "medication": "Doxorubicin",
      "number_doses": "4",
      "medication_dose_administered": "75",
      "medication_dose_intended": "75",
      "medication_dose_unit": "mg/m2"
    },
    {
      "subjects_submitter_id": ["patient4"],
      "timings_submitter_id": ["p4_timing_course1_induction"],
      "age_at_medication_start": "5845",
      "age_at_medication_end": "5880",
      "route": "Systemic",
      "medication": "Cyclophosphamide",
      "number_doses": "4",
      "medication_dose_administered": "1200",
      "medication_dose_intended": "1200",
      "medication_dose_unit": "mg/m2"
    },
    {
      "subjects_submitter_id": ["patient4"],
      "timings_submitter_id": ["p4_timing_course2_consolidation"],
      "age_at_medication_start": "5920",
      "age_at_medication_end": "5980",
      "route": "Systemic",
      "medication": "Ifosfamide",
      "number_doses": "5",
      "medication_dose_administered": "1800",
      "medication_dose_intended": "1800",
      "medication_dose_unit": "mg/m2"
    },
    {
      "subjects_submitter_id": ["patient4"],
      "timings_submitter_id": ["p4_timing_course2_consolidation"],
      "age_at_medication_start": "5920",
      "age_at_medication_end": "5980",
      "route": "Systemic",
      "medication": "Etoposide",
      "number_doses": "5",
      "medication_dose_administered": "100",
      "medication_dose_intended": "100",
      "medication_dose_unit": "mg/m2"
    }
  ],

  "RadiationTherapy": [
    {
      "subjects_submitter_id": ["patient1"],
      "timings_submitter_id": ["p1_timing_phase2_relapse"],
      "age_at_rt_start": "1830",
      "age_at_rt_end": "1835",
      "rt_site": "Cranium",
      "rt_dose": "1800",
      "rt_dose_unit": "cGy"
    },
    {
      "subjects_submitter_id": ["patient3"],
      "timings_submitter_id": ["p3_timing_course2_consolidation"],
      "age_at_rt_start": "4465",
      "age_at_rt_end": "4500",
      "rt_site": "Primary tumor site",
      "rt_dose": "5580",
      "rt_dose_unit": "cGy",
      "rt_data_source": "Protocol form"
    },
    {
      "subjects_submitter_id": ["patient4"],
      "timings_submitter_id": ["p4_timing_course2_consolidation"],
      "age_at_rt_start": "5925",
      "age_at_rt_end": "5960",
      "rt_site": "Primary tumor site",
      "rt_dose": "4500",
      "rt_dose_unit": "cGy",
      "rt_data_source": "Protocol form"
    }
  ],

  "StemCellTransplant": [
    {
      "subjects_submitter_id": ["patient2"],
      "timings_submitter_id": ["p2_timing_phase1_dx"],
      "age_at_sct": "1950",
      "sct_type": "Allogeneic",
      "stem_cell_source": "Bone marrow",
      "donor_relationship": "Biologically Unrelated",
      "hla_match": "Match",
      "number_hla": "10",
      "number_matches": "10",
      "hla_a_result": "Both Alleles Matched",
      "hla_b_result": "Both Alleles Matched",
      "hla_c_result": "Both Alleles Matched",
      "hla_drb1_result": "Both Alleles Matched",
      "hla_dq_result": "Both Alleles Matched",
      "conditioning_type": "Myeloablative",
      "prior_tbi": "No"
    }
  ],

  "TransfusionMedicineProcedure": [
    {
      "subjects_submitter_id": ["patient1"],
      "timings_submitter_id": ["p1_timing_phase1_dx"],
      "age_at_tmp_start": "1461",
      "tmp_type": "Simple Transfusion",
      "product": "RBC"
    },
    {
      "subjects_submitter_id": ["patient2"],
      "timings_submitter_id": ["p2_timing_phase1_dx"],
      "age_at_tmp_start": "1826",
      "tmp_type": "Simple Transfusion",
      "product": "Platelets"
    }
  ],

  "CellularImmunotherapy": [
    {
      "age_at_cimt_start": "1960",
      "timings_submitter_id": ["p2_timing_phase1_dx"],
      "cimt_type": "Donor lymphocyte infusion"
    }
  ],

  "SubjectResponse": [
    {
      "subjects_submitter_id": ["patient1"],
      "timings_submitter_id": ["p1_timing_course1_induction"],
      "age_at_response": "1502",
      "response_category": "Overall Response",
      "response": "System NOS >> Complete Response",
      "bm_pct_blasts_at_response": "2",
      "bm_analysis_method_at_response": "Morphology",
      "anc_at_response": "600",
      "anc_threshold_at_response": "Yes",
      "platelet_count_at_response": "60000",
      "platelet_threshold_at_response": "No"
    },
    {
      "subjects_submitter_id": ["patient2"],
      "timings_submitter_id": ["p2_timing_course1_induction"],
      "age_at_response": "1840",
      "response_category": "Overall Response",
      "response": "System NOS >> Non-Response",
      "bm_pct_blasts_at_response": "15",
      "bm_analysis_method_at_response": "Morphology",
      "anc_at_response": "300",
      "anc_threshold_at_response": "No",
      "platelet_count_at_response": "40000",
      "platelet_threshold_at_response": "Yes"
    },
    {
      "subjects_submitter_id": ["patient3"],
      "timings_submitter_id": ["p3_timing_course1_induction"],
      "age_at_response": "4420",
      "response_category": "Overall Response",
      "response": "System NOS >> Complete Response",
      "response_system": "RECIST",
      "response_system_version": "1.1"
    },
    {
      "subjects_submitter_id": ["patient4"],
      "timings_submitter_id": ["p4_timing_course1_induction"],
      "age_at_response": "5880",
      "response_category": "Overall Response",
      "response": "System NOS >> Partial Response",
      "response_system": "RECIST",
      "response_system_version": "1.1"
    }
  ],

  "MinimalResidualDisease": [
    {
      "subjects_submitter_id": ["patient1"],
      "timings_submitter_id": ["p1_timing_course1_induction"],
      "age_at_mrd_assessment": "1480",
      "mrd_method": "Flow Cytometry, Different-From-Normal",
      "result_numeric": "2.0",
      "result_unit": "%",
      "sensitivity": "0.1",
      "mrd_specimen": "Bone marrow aspirate",
      "molecular_markers": ""
    },
    {
      "subjects_submitter_id": ["patient1"],
      "timings_submitter_id": ["p1_timing_course1_induction"],
      "age_at_mrd_assessment": "1502",
      "mrd_method": "Flow Cytometry, Different-From-Normal",
      "result_text": "",
      "result_numeric": "0.05",
      "result_unit": "%",
      "sensitivity": "0.01",
      "mrd_specimen": "Bone marrow aspirate",
      "molecular_markers": ""
    },
    {
      "subjects_submitter_id": ["patient1"],
      "timings_submitter_id": ["p1_timing_phase2_relapse"],
      "age_at_mrd_assessment": "1820",
      "mrd_method": "Flow Cytometry, Different-From-Normal",
      "result_text": "",
      "result_numeric": "25.0",
      "result_unit": "%",
      "sensitivity": "0.1",
      "mrd_specimen": "Bone marrow aspirate",
      "molecular_markers": ""
    },
    {
      "subjects_submitter_id": ["patient2"],
      "timings_submitter_id": ["p2_timing_course1_induction"],
      "age_at_mrd_assessment": "1835",
      "mrd_method": "Flow Cytometry, Leukemia-Associated Immunophenotypes",
      "result_text": "",
      "result_numeric": "0.5",
      "result_unit": "%",
      "sensitivity": "0.1",
      "mrd_specimen": "Bone marrow aspirate",
      "molecular_markers": "KMT2A-rearranged clone"
    }
  ],

  "AdverseEvents": [
    {
      "subjects_submitter_id": ["patient1"],
      "timings_submitter_id": ["p1_timing_course4_relapse_induction"],
      "age_at_ae": "1835",
      "age_at_ae_resolved": "1840",
      "adverse_event": "Sepsis",
      "ae_code": "10039906",
      "ae_code_system": "MedDRA",
      "ae_grade": "5",
      "outcome": "Death",
      "icu": "Yes",
      "supportive_medication": "Other",
      "intervention_status": "Therapy discontinued",
      "intervention": "Other",
      "ae_pathogen": "Pseudomonas aeruginosa",
      "ae_pathogen_confirmation": "Culture",
      "gvhd_acuity": "",
      "gvhd_organ": ""
    },
    {
      "subjects_submitter_id": ["patient2"],
      "timings_submitter_id": ["p2_timing_course1_induction"],
      "age_at_ae": "1835",
      "age_at_ae_resolved": "1900",
      "adverse_event": "Hepatic veno-occlusive disease",
      "ae_code": "10019939",
      "ae_code_system": "MedDRA",
      "ae_grade": "4",
      "outcome": "Resolved with sequelae",
      "icu": "Yes",
      "supportive_medication": "Other",
      "intervention_status": "Therapy interrupted",
      "intervention": "Other",
      "ae_pathogen": "",
      "ae_pathogen_confirmation": "",
      "gvhd_acuity": "",
      "gvhd_organ": ""
    }
  ],

  "SecondMalignantNeoplasm": [
    {
      "subjects_submitter_id": ["patient3"],
      "age_at_smn_diagnosis": "4900",
      "smn_type": "Secondary Malignancy, NOS",
      "smn_site": "Bone marrow",
      "smn_basis_dx": "Integrated"
    }
  ],

  "Immunohistochemistry": [
    {
      "subjects_submitter_id": ["patient3"],
      "timings_submitter_id": ["p3_timing_phase1_dx"],
      "markers": "CD99/Cell Surface Antigen O13/Cell Surface Antigen HBA-71",
      "result_numeric": "90",
      "result_unit": ""
    },
    {
      "subjects_submitter_id": ["patient4"],
      "timings_submitter_id": ["p4_timing_phase1_dx"],
      "markers": "FLI-1",
      "result_numeric": "85",
      "result_unit": ""
    }
  ],

  "DiseaseCharacteristics": [
    {
      "subjects_submitter_id": ["patient3"],
      "timings_submitter_id": ["p3_timing_phase1_dx"],
      "age_at_assessment": "4380",
      "performance_score": "Lansky >> 80"
    },
    {
      "subjects_submitter_id": ["patient4"],
      "timings_submitter_id": ["p4_timing_phase1_dx"],
      "age_at_assessment": "5840",
      "performance_score": "Karnofsky >> 90"
    }
  ]
}

def get_class_slots_for_subset(schema, class_name, subset):
    sclass = schema["classes"][class_name]
    slots = []
    slot_usage = sclass.get("slot_usage", {})
    for slot_name, su in slot_usage.items():
        # If the slot_usage has no in_subset restriction, include it.
        in_subset = su.get("in_subset")
        if not in_subset or subset in in_subset:
            slots.append(slot_name)
    return slots


contributor_folders_ids = {
    "aml": "1SogX_kEW72JFnVPH68y5sud4HEV2sVyD",
    "cns": "1lKLZsKTbjoWHsLLTchDAWmHZtWziHf7Q",
    "ews": "1eHHJQNs-aZNl3lFbL6zmWdNfVrvzAixD",
    "fa": "1NsTD-JrK2aFbLjeJzmCW1QJFjVvlm_xd",
    "gct": "1CT1MPgXAAGnRb4zLXv04032rSKU2zHp2",
    "hl": "1ia51Bx5zfC2Ck1oOSSW2DbOLKp85YMHb",
    "lt": "1xr9SlpdQN_ySOEuxjIgNUoRYkbYmdx8i",
    "nbl": "1AD77bnMOA6_VQFiVqzSyA6oVL5U8zQ-v",
    "npc": "1ftN0k7T9kbTPQEt6zj1ewdmzNbQW6yy_",
    "nrsts": "1JTIdsB3ThHbNEAiHBTVL79a-GfH2hpjw",
    "os": "18TFe1Ro7Nczm9wK0UazP6Qazw5R58ziq",
    "pre": "1_T9ZMTCCziRlCgN6ZNnZgqrqZ75XPBtI",
    "rb": "1YUy8ic1GqvMR-GNLSilya5rYorlccxum",
    "rms": "1t9hNDCCXy9cFVuMa3j9-h2goIk_ES5Bd"
}


if __name__ == "__main__":
    script_helper.enforce_repo_root()
    print(
    """
    ▛▀▖▞▀▖▙▗▌   ▛▀▖▌ ▌▙ ▌▛▀▖▌  ▛▀▘
    ▌ ▌▚▄ ▌▘▌▄▄▖▙▄▘▌ ▌▌▌▌▌ ▌▌  ▙▄ 
    ▌ ▌▖ ▌▌ ▌   ▌ ▌▌ ▌▌▝▌▌ ▌▌  ▌  
    ▀▀ ▝▀ ▘ ▘   ▀▀ ▝▀ ▘ ▘▀▀ ▀▀▘▀▀▘
                    
    Use Ctrl+C to abort if needed
    ______________________________________________
    Usage: 
        python bundle.py [target_schema_path] [subset]

    Examples: 
        - python bundle.py schemas/pcdc/pcdc_v2.0 aml_v2.0-live
    ______________________________________________
    """
        ) 
    parser = argparse.ArgumentParser(
        description="Schema Utils: generate blank data sheet templates for contributor bundles"
    )
    parser.add_argument("schema", help="Path to the schema JSON file.")
    parser.add_argument("subset", help="Target subset for the templates.")
    args = parser.parse_args()

    if not os.path.exists(args.schema):
        print("ERROR: " + args.schema + " not found")
        raise SystemExit(1)

    with open(args.schema, "r") as file_in:
        schema = json.load(file_in)

    if args.subset not in schema.get("subsets", {}):
        print("ERROR: " + args.subset + " not found in: " + args.schema)
        raise SystemExit(1)
    
    disease_prefix = args.subset.split("_")[0].split("-")[0]
    folder_id = contributor_folders_ids.get(disease_prefix)

    if not folder_id:
        print("ERROR: a Drive folder ID for a " + disease_prefix + " bundle was not found in bundle.py")
        raise SystemExit(1)
    
    start = time.time()
    print('\n...compiling data sheets')
    sheets = {}
    for class_name, sclass in schema["classes"].items():
        class_in_subset = args.subset in sclass.get("in_subset", [])
        if not class_in_subset:
            continue

        # 1. Determine which slots apply in this subset
        slots = get_class_slots_for_subset(schema, class_name, args.subset)

        # If there are no slots, skip
        if not slots:
            continue

        # 2. Build rows: first row is header, rest are examples
        rows = []
        header_row = slots[:]  # copy
        rows.append(header_row)

        # 3. If we have example rows for this class, use them
        examples = example_bank.get(class_name, [])
        for ex in examples:
            # Build row values in the same column order as header
            row = [str(ex.get(slot, "")) for slot in slots]
            rows.append(row)

        sheets[class_name] = rows
    print(script_helper.elapsed_time(start))
    start = time.time()
    print('\n...writing bundle to Drive')
    title = f"{datetime.datetime.now().strftime('%Y%m%d')} {args.subset} contributor bundle"
    spreadsheet_id = sheets_helper.create_spreadsheet_from_tables(title, sheets, folder_id)
    print(f"\nBundle uploaded to the Contribution > {disease_prefix} Drive folder:")  
    print(f"    https://drive.google.com/drive/u/0/folders/{folder_id}")
    print(script_helper.elapsed_time(start))
    start = time.time()
    print('\n...adding a fresh dictionary export to the bundle')
    export.init("pcdc", disease_prefix, spreadsheet_id, args.schema, args.subset, False)
    print(script_helper.elapsed_time(start))
