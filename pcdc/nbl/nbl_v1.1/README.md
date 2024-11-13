# Release notes for nbl_v1.1

This version includes additional fields in the Molecular Analysis table to accommodate a COG ALK dataset, described in this publication:

Bresler SC, Weiser DA, Huwe PJ, Park JH, Krytska K, Ryles H, Laudenslager M, Rappaport EF, Wood AC, McGrady PW, Hogarty MD, London WB, Radhakrishnan R, Lemmon MA, Mossé YP. ALK mutations confer differential oncogenic activation and sensitivity to ALK inhibition therapy in neuroblastoma. Cancer Cell. 2014 Nov 10;26(5):682-94. doi: 10.1016/j.ccell.2014.09.019. Epub 2014 Nov 10. PMID: 25517749; PMCID: PMC4269829.

This molecular data is from patients included in the following studies:

|Data Contributor|Study|
|---|---|
|COG| 0901, 0925, 09709, 321P2, 321P3, 3881, 3891, 3951, 4941, 8742, 9047, 9082, 9140, 9243, 9244, 9262, 9280, 9340, 9341, 9342, 9343, 9361, 9375, 9464, 9579, 9640, 9900, 9907, A3961, A3973, AADM01P1, AALL03B1, AAML00P2, AAML07P1, AB9804, ACCL0331, ACCL0431, ACCL05C1, ADVL0018, ADVL0122, ADVL0212, ADVL0214, ADVL0215, ADVL0414, ADVL0416, ADVL0421, ADVL0524, ADVL0525, ADVL0714, ADVL0812, ADVL0813, ADVL0821, ADVL0911, ADVL0912, ADVL0921, ADVL1412, AEPI07N1, ALTE03N1, ALTE05N1, ALTE15N2, ALTE1621, ANBL0032, ANBL00B1, ANBL00P1, ANBL00P2, ANBL00P3, ANBL02P1, ANBL0321, ANBL0322, ANBL0421, ANBL0531, ANBL0532, ANBL0621, ANBL0931, ANBL1021, ANBL1221, ANUR0631, AREN0321, AREN03B2, B003, B903, B947, B954, B973, E18, I03, N891, P9462, P9641, P9761, P9963, R9702, S31 |


Added concepts:
>[Molecular Analysis].[MOLECULAR_ABNORMALITY].[ALK Copy Number Gain]

>[Molecular Analysis].[MOLECULAR_ABNORMALITY].[ALK Copy Number Loss]

>[Molecular Analysis].[MOLECULAR_ABNORMALITY].[ALK Amplification]

>[Molecular Analysis].[COPY_NUMBER_STATUS]

>[Molecular Analysis].[COPY_NUMBER_STATUS].[Gain]

>[Molecular Analysis].[COPY_NUMBER_STATUS].[Loss]

>[Molecular Analysis].[COPY_NUMBER_STATUS].[Amplification]

>[Molecular Analysis].[COPY_NUMBER_STATUS].[No gain/loss/amplification]

>[Molecular Analysis].[COPY_NUMBER_STATUS].[Unknown]

Removed concepts:
>None

Modified concepts:
>None
