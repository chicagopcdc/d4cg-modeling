# d4cg-modeling

This repo contains the various data models / dictionaries created and maintained by the D4CG Data Standards and Modeling (DSM) team. As shown below, each model has 4 associated files:

- **README.md** - a release note identifying the changes
- **mappings.txt** - a list of computable mappings that can be used to migrate data from its previous format into the new format  
- **.json** - a json representation of the concepts
- **.tsv** - a tabular representation of the concepts



```
├── README.md
├── pcdc
│   ├── all
│   │   ├── all_v1.0
│   │   │   ├── README.md
│   │   │   ├── all_v1.0.json
│   │   │   ├── all_v1.0.tsv
│   │   │   └── mappings.txt
│   │   └── all_v1.1
│   │       ├── README.md
│   │       ├── all_v1.1.json
│   │       ├── all_v1.1.tsv
│   │       └── mappings.txt
│   ├── aml
│   │   ├── aml_v1.0
│   │   │   ├── README.md
│   │   │   ├── aml_v1.0.json
│   │   │   ├── aml_v1.0.tsv
│   │   │   └── mappings.txt
  
  ...snipped for brevity...

│   └── rms
│       ├── rms_legacy
│       │   └── rms_legacy.xlsx
│       └── rms_v1.0
│           ├── README.md
│           ├── mappings.txt
│           ├── rms_v1.0.json
│           └── rms_v1.0.tsv
└── predict
    └── md_v1.0
        ├── README.md
        ├── mappings.txt
        ├── md_v1.0.json
        └── md_v1.0.tsv
```
