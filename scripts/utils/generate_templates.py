import os, json, argparse, datetime, csv

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
    }
  ],

  "StudyMetadata": [
    {
      "submitter_id": "study1",
      "subjects_submitter_id": ["patient1", "patient2"],
      "study_id": "AAML0531"
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
      "allelic_ratio": "0.45",
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

def export_tsvs(sheets, subset):
    os.makedirs("contributor_bundles", exist_ok=True)

    run_date = datetime.datetime.now().strftime("%Y%m%d")
    run_folder_name = f"{run_date}_{subset}"
    run_folder = os.path.join("contributor_bundles", run_folder_name)
    os.makedirs(run_folder, exist_ok=True)

    for class_name, rows in sheets.items():
        # Skip empty classes
        if not rows:
            continue
        tsv_path = os.path.join(run_folder, f"{class_name}.tsv")
        with open(tsv_path, "w", newline="") as f:
            writer = csv.writer(f, delimiter="\t")
            for row in rows:
                writer.writerow(row)

    return run_folder

if __name__ == "__main__":
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

    # sheets[class_name] = list of rows (first row = header)
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

    export_tsvs(sheets, args.subset)