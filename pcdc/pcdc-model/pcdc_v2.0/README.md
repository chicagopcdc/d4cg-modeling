# Release notes for pcdc_v2.0

This version includes data migration 1 changes for all dictionaries that currently have live data in the PCDC:

|Consortium|Disease Group|Data Dictionary|
|---|---|---|
|INTERACT|AML|aml_v2.0|
|MaGIC|GCT|gct_v2.0|
|NODAL|HL|hl_v2.0|
|INRG|NBL|nbl_v2.0|
|INSTRuCT|RMS|rms_v2.0|
|INSTRuCT|NRSTS|nrsts_v2.0|

Additional disease groups who are still in the process of contribution or modeling will be handled separately.

Almost all of these changes are either renamed fields (1:1), or are related to the PCDC-wide move to using reference time periods rather than duplicated disease phases and treatment courses.

Changes that still require consortia feedback and approval, and which are not reflected in this version, include:
- The restructured molecular/genetics table.
- Expanding the diagnosis table to include medical history.
- The restructure radiation therapy table.
- And a handful of other isolated changes that require more discussion.
