# organizr
Organise documents (currently PDF files) based on subject / theme

Embeddings of PDF files are generated, page by page, and then combined into a total embedding for that document.

Based on these embeddings, the documents are clustered -- currently using KMeans, with a configurable k -- and an HTML document is created as an categorized index of the PDF documents.

For each category, a single PDF document is picked as a representative for that category, by calculating the cosine similarity with the cluster centroid. The reason is that the categories are unnamed (unknown) and any document near the centroid should be a good approximation of the cluster topic.

This seems to work reasonably well, but it is possible to modify the setup:
* by picking different embedding models,
* by clustering by other algorithms than KMeans -- such as hierarchical clustering or density-based clustering

## How-to setup
Short how-to setup for running
```
➜  python3.12 -m venv env
➜  source env/bin/activate
➜  python3 -m pip install -r requirements.txt
```

## How-to run
How-to run this over PDF documents in ~/Documents. An index.html will be created in ~/Documents.
```
➜  python3 Main.py ~/Documents
```

Document embeddings are cached (based on path to PDF document) in a local sub-directory 'embedding-cache', so that a second run will load embeddings from the cache instead of re-running the embedding process.
I got some botched embeddings, possibly due to problems with the PDF files, which may result in "empty" cache-files. 
In order to remove these "empty" cached embeddings I can use (but this is not a necessity):
```
➜  find ./embedding-cache -maxdepth 1 -type f -size 136c -exec rm -f {} +
```

## Example
I applied 'organizr' on my PhD Thesis, including reference material I still keep in sub directories.
```
➜  organizr git:(main) ✗ source env/bin/activate
(env) ➜  organizr git:(main) ✗ python3 Main.py ~/Thesis
Embedding: ea334e91cb024779253226ab16baa303194acc59.npy <- froran-thesis.pdf
Embedding: 7d62e34f3d4858746370211e337d2850f9157344.npy <- data-index.pdf
Embedding: 96ab66463fc53602977df40d51cdf18190486a29.npy <- Cost for Long-Term Digital Preservation - 9 Months Review.pdf
Embedding: f5fa7dd0ec48a7332b7c6cec2a4883d3d06e6eec.npy <- review.pdf
Embedding: 443d90cf0ed2c73a8772b3bfce0f0c58bac49264.npy <- 20 Strauch, Andrikopoulos, Bachmann, Leymann (2013) - Migrating Application Data to the Cloud using Cloud Data Patterns.pdf
Embedding: 7c5a7234b6670150015bdae4816defe2e06183b8.npy <- 25 Rings, Caryer, Gallop, Grabowski, Kovacikova, Schulz, Stokes-Rees (2009) - Grid and Cloud Computing; Opportunities for Integration with the Next Generation Network.pdf
Embedding: 025dab0d5f98f109726fbbef7fc071cf591097bd.npy <- 11 Martens, Walterbusch, Teuteberg (2012) - Costing of Cloud Computing Services; A Total Cost of Ownership Approach.pdf
Embedding: 6760b6da4fdf21071983daded97206c51c7f8ccc.npy <- 15 Fehling, Leymann, Ruehl, Rudek, Verclas (2013) - Service Migration Patterns - Decision Support and Best Practices for the Migration of Existing Service-Based Applications to Cloud Environments.pdf
Embedding: 13d4b1b7985590d5397bd18eccb0c4ba0c765d42.npy <- 05 Wittern, Kuhlenkamp, Menzel (2012) - Cloud Service Selection Based on Variability Modeling.pdf
Embedding: fea808570cfdb720dba55059c830b45ed13ade54.npy <- 08 Menzel, Ranjan (2011) - CloudGenius; Automated Decision Support for Migrating Multi-Component Enterprise Applications to Clouds.pdf
Embedding: 41b0b7d35bacf6c1b583ad12ad8788eda0284cf6.npy <- 04 Zhang (2012) - Investigating decision support techniques for automating Cloud service selection.pdf
Embedding: 45453a73e323b255dd862c54a20e27641110f57f.npy <- 18 Hartung, Anokwa, Brunette, Lerer, Tseng, Borriello (2011) - Open Data Kit; Tools to Build Information Services for Developing Regions.pdf
Embedding: 9ef9c648630c2a62a0f2a223f8bf9172327e5b80.npy <- 03 Khajeh-Hosseini, SOmmerville, Bogaerts, Teregowda (2011) - Decision Support Tools for Cloud Migration in the Enterprise.pdf
Embedding: d23fafe99686f93de061d33bf97bbb1ca31d222c.npy <- 24 Sun, Dong, Hussain, Hussain, Chang (2014) - Cloud service selection; State-of-the-art and future research directions.pdf
Embedding: 47080843ad4a4c68a18a73d063499a36ac781559.npy <- 16 Amato, Venticinque (2014) - A Distributed Agent-based Decision Support for Cloud Brokering.pdf
Embedding: e6beeeed82c9b4ed4b01bf852ab22500b9ec1d63.npy <- 10 Toosi, Calheiros, Buyya (2014) - Interconnected Cloud Computing Environments; Challenges, Taxonomy, and Survey.pdf
Embedding: a75bc08f21c538138e7f8591b283b21aaebb086c.npy <- 07 Pearson, Benameur (2010) - Privacy, Security and Trust Issues Arising from Cloud Computing.pdf
Embedding: ec283dc433016e4e21ea8332c3448274ca9367a5.npy <- 21 Jula, Sundararajan, Othman (2014) - Cloud computing service composition; A systematic literature review.pdf
Embedding: 64cd3451e758ba44d7a035e6979f55724b28cc50.npy <- 09 Sakr, Liu, Batista, Alomari (2011) - A Survey of Large Scale Data Management Approaches in Cloud Environments.pdf
Embedding: 771b9b3af3327adeb0331b82638df40e047987a6.npy <- 13 Menzel, Ranjan, Wang, Khan, Chen (2015) - CloudGenius; A Hybrid Decision Support Method for Automating the Migration of Web Application Clusters to Public Clouds.pdf
Embedding: dbf55ce8fc88fb9ce02ec943b7aae726a4785a11.npy <- 19 Rosado, Gomez, Mellado, Fernandez-Medina (2012) - Security Analysis in the Migration to Cloud Environments.pdf
Embedding: a2c5d2a0ebf9d8e01ec8baf03e0fa20f20ae8ef4.npy <- 17 Inzinger, Nastic, Sehic, Vögler, Li, Dustdar (2014) - MADCAT; A Methodology for Architecture and Deployment of Cloud Application Topologies.pdf
Embedding: 3022a628674978abf5f4bed1d2568c90e3b38281.npy <- 22 Khediri, Zaghdoud (2015) - Survey of Uncertainty Handling in Cloud Service Discovery and Composition.pdf
Embedding: af374d242dfd15cffd1f9446bbf05ea8288b68fe.npy <- 01 Menzel, Ranjan (2012) - CloudGenius; decision support for web server cloud migration.pdf
Embedding: 3a7af72bde93c3766fb4ad035a095e5418fe04d1.npy <- 02 Marston, Li, Bandyopadhyay, Ghalsasi (2011) - Cloud Computing - The Business Perspective.pdf
Embedding: faea1c753d427af2f4badc4d6cd24155de0adf99.npy <- nn AJeh, Ellman, Keogh (2014) - A Cost Modelling System for Cloud Computing.pdf
Embedding: 14615eebef15081227210ee750b818cff62942d2.npy <- 26 Liu, Rijnboutt, Routsis et al (2013) - What challenges have to be faced when using the cloud for e-health services.pdf
Embedding: 357ad8a17aa3665dbd35d87af6eef7cdf23b04bc.npy <- 23 Müller, Han, Scheider, Versteeg (2011) - Tackling the Loss of Control; Standards-Based Conjoint Management of Security Requirements for Cloud Services.pdf
Embedding: 8ca587a33a0fb21d376868ae0470dc29c75765e3.npy <- 12 Strauch, Andrikopoulos, Bachmann, Karastoyanova, Passow, Vukojevic-Haupt (2013) - Decision Support for the Migration of the Application Database Layer to the Cloud.pdf
Embedding: 4c7819fec990a80288572c167bf2f00b1750988c.npy <- 06 Andrikopoulos, Strauch, Leymann (2013) - Decision Support for Application Migration to the Cloud - Challenges and Vision.pdf
Embedding: 2e710a380f7d0696f5907a463e97757ed1e0b6db.npy <- 14 Barker, Varghese, Thai (2015) - Cloud Services Brokerage; A Survey and Research Roadmap.pdf
Embedding: b7454504564c5f5ff8698bcc326eb79039537a8f.npy <- 21 Kulmukhametov, Becker (2014) - Content Profiling for Preservation; Improving Scale, Depth and Quality.pdf
Embedding: e3fe508c5e3fad1c2dd388550837c3ed7eeb2b4c.npy <- 03 Becker, Rauber, Heydegger, Schnasse, Thaller (2008) - A Generic XML Language for Characterising Objects to Support Digital Preservation.pdf
Embedding: bbd800ae9ce73333daa261299a9e2da9e148a461.npy <- 12 Lindley, Jackson, Aitken (2010) - A Collaborative Research Environment for Digital Preservation - The Planets Testbed.pdf
Embedding: 070e8acace24bcababf4bcc51c7867fa15bb8327.npy <- 13 Becker, Ferreira, Kraxner, Rauber, Baptista, Ramalho (2008) - Distributed Preservation Services; Integrating Planning and Actions.pdf
Embedding: 98d0f16dad58808318415232718b485a1b27d709.npy <- 14 Strodl (2010) - (Semi-)Automated digital preservation archives for small institutions and private users.pdf
Embedding: ff9f0d20772022329de454f7681e0d14c203b15b.npy <- 19 Schmidt, King, Jackson, Wilson, Steeg, Melms (2010) - A Framework for Distributed Preservation Workflows.pdf
Embedding: 41d168b66841bd9cca8191e94406f1ea06ee27ac.npy <- 17 Burda, Teuteberg (2013) - Investigating the Needs, Capabilities and Decision Making Mechanisms in Digital Preservation; Insights from a Multiple Case Study.pdf
Embedding: 8a79f99de81f0b055cc2c70a37c823f29163b1d3.npy <- 07 Neumann, Miri, Thomson, Antunes, Mayer, Beigl (2013) - Towards a Decision Support Architecture for Digital Preservation of Business Processes.pdf
Embedding: 9fe0c7e58ba34ffb9d71d28c5a47939e206c6c2c.npy <- 15 Becker, Kolar, Küng, Rauber (2007) - Preserving Interactive Multimedia Art; A Case Study in Preservation Planning.pdf
Embedding: 4038cfcdc49cf058aa960c651f0afc5f630701b5.npy <- 31 Abichandani, Prakash, Barwal, Murthy (2015) - Tool for Metadata Extraction and Content Packaging as Endorsed in OAIS Framework.pdf
incorrect startxref pointer(1)
Embedding: 5d0fa0a11cd703b39fda0a37e7f56acd743b9097.npy <- 27 Liu, Futrelle, Myers, Ridriguez, Kooper (2010) - A provenance-aware virtual sensor system using the Open Provenance Model.pdf
Embedding: a24e2f782e15a676d3a66b8a89b75e0046462621.npy <- 02 Becker, Kulovits, Rauber, Hofman (2008) - Plato; a service oriented decision support system for preservation planning.pdf
Embedding: 0c1e0fc4f87f1580661e1e55102e4b9a2e27617b.npy <- 10 Hunter, Choudhury (2006) - PANIC; an integrated approach to the preservation of composite digital objects using Semantic Web services.pdf
Embedding: 7ff0a135ef724fa34ced7963cd34b057072b268a.npy <- 30 Whyte (2007) - Report from the DCC Workshop; Legal Environment of Digital Curation.pdf
Embedding: 7bf87c6d1614a4d32f8d81315b55495dbe05db63.npy <- 24 Oltmans, van Wijngaarden (2006) - The KB e-Depot digital archiving policy.pdf
Embedding: b55d2e8dfbea667dd440ce741c3595567abd4639.npy <- 26 Auer, Salmagas, Parkinson, Bancilhon, etc (2012) - Diachronic linked data; towards long-term preservation of structured interrelated information.pdf
Embedding: b6f7f5ba6570ebd40912f312e0d04da9671586e7.npy <- 23 Graf, Huber-Mörk, Schindler, Schlarb (2013) - Duplicate detection approaches for quality assurance of document image collections.pdf
Embedding: d9dc1858a7f0ee6ab82113bfbd42560b70f2589a.npy <- 08 Hunter, Choudhury (2004) - A Semi-Automated Digital Preservation System based on Semantic Web Services.pdf
Embedding: c445e7b7b82ef64893b7e74634dd547a19d836e2.npy <- 04 Becker, Rauber (2011) - Decision criteria in digital preservation; What to measure and how.pdf
Embedding: d82b0a6c21ddc9271a5f2212fee1f15063a60cf2.npy <- 22 Anderson, Delve, Powel (2012) - The Changing Face of the History of Computing; The Role of Emulation in Protecting Our Digital Heritage.pdf
Embedding: 11df0e1afbecec51ae90b3f2c805315c0de74ccc.npy <- 32 Truex, Olsson, etc (2011) - Position Statement; Sustainable Information and Information Systems (SIIS).pdf
Embedding: 6d221156f8167d24bc4c494027792187e07dfe76.npy <- 20 Hunter, Choudhury (2005) - Semi-automated preservation and archival of scientific data using semantic grid services.pdf
Embedding: 588ecd2008a36dd4f04a0987ad4e79e5dd0613e9.npy <- 18 Strodl, Becker, Neymayer, Rauber, etc (2007) - Evaluating Preservation Strategies for Electronic Theses and Dissertations.pdf
Embedding: 8087bdfb16d436497b9725e0d4aafb1c7b9fc3e1.npy <- 16 Rauch, Pavuza, Strodl, Rauber (2005) - Evaluating Preservation Strategies for Audio and Video Files.pdf
Embedding: b88e52bdfa5a5de5fcf940f9ff0d101d6963d09e.npy <- 11 Becker, Rauber, Heydegger, Schnasse, Thaller (2008) - Systematic Characterisation of Objects in Digital Preservation; The eXtensible Characterisation Languages.pdf
Embedding: 2998b9704b1199200dc4e231bb92b503d85ba279.npy <- 09 Strodl, Becker, Rauber (2009) - Digital Preservation (chapter).pdf
Embedding: 0efe41e3ba92e9ef90de272ff0bd9aa0888e8816.npy <- 01 Ferreira, Baptista, Ramalho (2007) - An intelligent decision support system for digital preservation.pdf
Embedding: 3ce3cb599b11676616e01164d6fd1371b53727c8.npy <- 25 Rauber, Bruckner, Aschenbrenner, Witvoet, Kaiser (2002) - Uncovering Information Hidden in Web Archives; A Glimpse at Web Analysis Building on Data Warehouses.pdf
Embedding: c7da97ec0a6c2e643d3189ae0b4806fa6dc28b40.npy <- 33 Risse, Dietze, Maynard, Tahmasebi, Peters (2011) - Using Events for Content Appraisal and Selection in Web Archives.pdf
Embedding: 7f1f3ca48767f29cfa0deda04a8c68643f846360.npy <- Schoorman, Mayer, Davis (2007) An integrative model of organizational trust; past, present, and future.pdf
Embedding: ff7caee8af4a5bb95cc5ebb3586315a22d341e27.npy <- Hart, Liu (2003) Trust in the preservation of digital information.pdf
Embedding: 115a16392108fdeb6aa0f00ce2fa9188ad5c818b.npy <- (2011) Preserving digital materials.pdf
Embedding: 47eb196d3ef30ed79babc512286edc4a826200bd.npy <- Day (2008) Toward distributed infrastructures for digital preservation; the roles of collaboration and trust.pdf
Embedding: 9322916422a7f9a1cadf2e270346fa4a2bad489e.npy <- Mayer, Davis, Schoorman (1995) An integrative model of organizational trust.pdf
Embedding: d80c7724331ced8160a9e64636d48e4343e6557b.npy <- rutgers-lib-36587_PDF-1.pdf
Embedding: c565224d69d7afb61584a06dff38e961304be7e8.npy <- Ross (2012) Digital Preservation, Archival Science and Methodological Foundations for Digital Libraries.pdf
Embedding: 34644052451117d255547919ff05600951850064.npy <- Rousseau, Sitkin, Burt, Camerer (1998) Not so different after all; A cross-discipline view of trust.pdf
Embedding: 37c6fd8363573a0423036b5ed99291e22fd2d0f1.npy <- 2012-05-10 Describing the quality model.pdf
Embedding: d2aa95b52002284b509483e9a35a1fea3d4d3606.npy <- Automation of information quality evaluation in ehealth records from a preservation perspective (2012).pdf
Embedding: 9488dff1a02b363f2e495a7fb62c3f5617df2c9d.npy <- An Activity Theory Lens on Digital Preservation Challenges of Using Preservation Services (2013).pdf
Embedding: 42f9e149dcc4f86c16722e2f57d826875df4ea11.npy <- A Preservation Services Planning Decision Framework (2014).pdf
Embedding: c5701ade84903307d9eb2357e2acc5cbb8952701.npy <- ENSURE; Long term digital preservation of Health Care, Clinical Trial and Financial data (2013).pdf
Embedding: 69a55b359804d05e6fa1ff1b7b309c6fcaa6202d.npy <- Inherent Problems in Cooperative Planning for Future Access to Information (2013).pdf
Embedding: 6c7a6730a0dc807823b592c23319795ea888ae7c.npy <- 2013-10-22 On consequences information sent to cost engine.pdf
Embedding: fed04728bdf79feb02d917ac87189303c5c5bbb6.npy <- 2013-11-22 Regarding evaluations of the cost engine.pdf
Embedding: 38ecbdf54660b83a5c8922bca2514f3fed38a724.npy <- 2013-05-29 Quality-to-cost-engine-integration.pdf
Embedding: 52a15505e116bc0a3976ff6efbddaa4887184f4e.npy <- 2012-09-11 On selection of purposes.pdf
Embedding: 957e79d8f5d97c7c890a13b717429b68eb868ee8.npy <- 2012-01-12 Sketches around a preservation plan model.pdf.pdf
Embedding: ca34b498e418e31c0d57837516df7f7c57948eff.npy <- 2011-05-29 Requirements deliverable v4.pdf
Embedding: f442199a44ada0f6a5521ed8d7ffccb5022b9b0f.npy <- 2010-04-15 ENSURE - draft proposal (confidential).pdf
Embedding: 0cf4f1385827d3ed8dc1fd31837b4d7eccd75864.npy <- 2010-11-16 ENSURE (270000).pdf
Embedding: 97a5035e74d8c62b0d7983c93724affdf89034b1.npy <- Scholar Alert   digital preservation  quality fitness purpose .pdf
Embedding: 1e466366631c73727a008703192441b9af06941a.npy <- 2011-09-20 Brussels F2F Meeting minutes.pdf
Token indices sequence length is longer than the specified maximum sequence length for this model (935 > 512). Running this sequence through the model will result in indexing errors
Embedding: 85e1ad56efc78373edeb3b51c56522d889a01f6c.npy <- scientfic_report_main.pdf
Embedding: 1f47224ccdfcb9ec28916f1cfd3fad3e86b72693.npy <- D20.2.3 Activity II Scientific Report.pdf
Embedding: b6c6cb70e67208e8a8aaecab0c9f0e9116e11597.npy <- A5_Scenarios_main.pdf
Embedding: e00365fd6bd26402bd19cb3ce827f9147b852dfe.npy <- Last years A5 deliverable.pdf
Embedding: ef9c05ca8223f04b67293dc20e8b95e27a9c2348.npy <- D0.1.1a Periodic Progress_man.pdf
Embedding: ab7a93f65122757c4ad6f28eb18bcd988c9cb2f0.npy <- Cost_Claim_overview_ENSURE_2013-04-10.pdf
Embedding: 62931cb4f91a4b0dc867564729c7a6906e5b0765.npy <- Final_Report_main.pdf
Embedding: e6d06831cf02cea63c4f7d7c186077b078ec1cb7.npy <- D70.2.4 Dissemination Report.pdf
Embedding: 8dbe1f3e38e006257709f0bf81f646a6a9c84832.npy <- D70.3.2_training_main.pdf
Embedding: 2cc7ea1732d2abe365e711e26510c9345b6e68c4.npy <- D11.1.3 ENSURE High Level Architecture Document_main.pdf
Embedding: 32e29776f8989039e009d582146373dfb76e905a.npy <- flowEPA.pdf
/Users/froran/Projects/private/organizr/env/lib/python3.12/site-packages/numpy/core/fromnumeric.py:3504: RuntimeWarning: Mean of empty slice.
  return _methods._mean(a, axis=axis, dtype=dtype,
/Users/froran/Projects/private/organizr/env/lib/python3.12/site-packages/numpy/core/_methods.py:129: RuntimeWarning: invalid value encountered in scalar divide
  ret = ret.dtype.type(ret / rcount)
Ignoring bogus embedding: nan
Embedding: 0d86acb02569a9897b1d3526654ed4098b04b5bc.npy <- bibliography.pdf
*** [Warning] Could not process '/Users/froran/Thesis/data/project/Deliverables/Year 2/A2/D20.2 Scientific Report M24/bibliography.pdf'. Error: EOF marker not found
Embedding: 6834c5240ade5bdcbaab2e2dc63cf1f0b0839bdd.npy <- D20.1.b Activity II Scientific Report.pdf
Embedding: 5d5b790b3de0bf499bdf72102c5e37fff0ffd33f.npy <- architectureEPA.pdf
Ignoring bogus embedding: nan
Embedding: ab4f184e9b3bd7838916980976919303171ada6d.npy <- exampleEPA.pdf
Ignoring bogus embedding: nan
Embedding: 557eba8baa78b85b12981f4b147b70d0c44f79dc.npy <- flowEPA.pdf
Ignoring bogus embedding: nan
Embedding: a1aca6e0e2ad5129de404f2f445a8436c98db99d.npy <- flowInvestmentBank.pdf
Ignoring bogus embedding: nan
Embedding: 6997bb59f82432f8fe6c1bc6510fc392bef506db.npy <- A5_Scenarios_main.pdf
Embedding: 12678a536e0fac7cacea9c38329666a266d3f31a.npy <- D0.1.1a Periodic Progress_man.pdf
Embedding: 2f8be8d4b3762c7cf6d1851c6c1d2cb3acd568eb.npy <- maccabi_standards.pdf
Embedding: 4b6aa0619f7286758dee4bf96ef0ff4b4943996b.npy <- D70.2.1 Dissemination.PDF
Embedding: 558ec95b047c306e850fd8afd0534409cf24f38a.npy <- D60.1_M24_main.pdf
Embedding: cb4ace6e02ba4f78faae9a3e2adca7eb8e54d04a.npy <- D11.1 ENSURE High Level Architecture Document_main.pdf
Embedding: aa55fa7a0b5562eb69acfb2977495b2ad81a0c5b.npy <- flowEPA.pdf
Ignoring bogus embedding: nan
Embedding: 40498caf69599b53fe283fb7437e572131edcda9.npy <- D1.2.1 Requirements M4.PDF
Embedding: bf48248f758bf2195f0b1b6b25efb05b9b27071b.npy <- D12.1c ENSURE RequiremnetsM24 Document_main.pdf
Embedding: f4bde5d7e7e4253951495c85ae812b4ec404f34e.npy <- D30.1.1_A3_prototype_demo_main.pdf
Embedding: 17ee77cad96697c602222442e354083e63426ab6.npy <- D20.1.1_A2_prototype_demo_main.pdf
Embedding: a28eda156da9f4d121b5c666e0012c91ba6718af.npy <- D20.1.a Activity II Scientific Report.pdf
Embedding: 663f6e60d8b9de9c3a0999793051e4aff4e2c891.npy <- D70.2.1 Dissemination.PDF
Embedding: 592813aecf7581a9da7b99f79b69f9081dfb9192.npy <- D1.2.1 Requirements M4.PDF
Embedding: b086fc81857e7512fd493feda337b149562b0c4e.npy <- final_review_report_1.pdf
Embedding: 94e950f8a37d8b2fa371571e8d7bc1c516f98c5a.npy <- y1_rerview_report.pdf
Ignoring bogus embedding: nan
Embedding: 28ab5d9bce5fed8f156898fa082abbb01e746d64.npy <- 2013-02-27 d0.1.1a_periodic_progress_man.pdf
Embedding: 39dd8385e29be4c9c19331a19b28bc111af4e576.npy <- 2011-06-13 d-req_up_13june2011-v6.pdf
Embedding: 4d0b987a56648b6ee0f4858b7a73b00d0be6db10.npy <- 2013-08-12 d40.1.1_a4_prototype_demo_main.pdf
Embedding: bdae70bd4b1a35ec82364b65bbf4b492e29d7bb0.npy <- 2014-02-23 final_report_main.pdf
Embedding: cfb3bd68c304957d84a558ef8626f10ff8d886a7.npy <- 2011-08-10 ensure-leaflet-10aug2011-v4.pdf
Embedding: ec3172535673152667a521673e8425854903b5f1.npy <- 2011-02-23 ensure-wp31-architecture-draft.pdf
Embedding: f848ec1dae21d62152cc1f725e8bb7334fe59752.npy <- 2011-06-15 d1.2.1_requirements_document.pdf
Embedding: 87b0cb48cfafd19f6bcfb6dd10781401c7dd07e6.npy <- 2013-02-10 d60.1_m24_main.pdf
Embedding: 153fe1b71b13092b6116f91b8d5a663300a2eca9.npy <- 2011-04-11 techreport.pdf
Embedding: da62d7be40a0b2c09a02cac5d22154d143e1be48.npy <- 2012-01-11 sample_periodic_progress_report.pdf
Embedding: dde01aaffa7b063a1236d92bf71afded3bd04164.npy <- 2014-01-30 d70.2.4_dissemination_report.pdf
Embedding: 240fccb67df50df1cd965dba6a783c3cab8ad8d8.npy <- 2012-02-02 d60.1_m12_main.pdf
Embedding: 3d7b53b4b5b7c8a47725d861161db992683e032e.npy <- 2011-03-29 ensure-wp31-architecture-draft02.pdf
Embedding: 28731a75e532504ceb552517b4ce30b5cd06852a.npy <- 2011-04-16 requirements-projects-ltdp-uporto-16april2011.pdf
Embedding: 4591d57b023174e460019fd6082d4fe87267997c.npy <- 2012-05-30 option1-b.pdf
Embedding: 05ba641b5e91198b3f08c0d7c8327543b1616f88.npy <- 2013-02-04 d70.3_m24_main.pdf
Embedding: f0ce6239405041df853bfa0872ee6a0a4a831ec3.npy <- 2012-05-30 option1-f.pdf
Embedding: 2367831593d86b0c123882fc3cf13e5f3c4aaaa7.npy <- 2011-06-10 ensure-wp31_v.1.pdf
Embedding: 11e4ee36d358701eb70e8a18460fa0389f30b232.npy <- 2012-04-11 EC rerview_report_y1.pdf
Ignoring bogus embedding: nan
Embedding: 72606c766f1b8b7b34cba6d1ed1dffe6eab30528.npy <- 2012-05-07 leaflet_ensure_back02.pdf
Embedding: 5f1431326d0d7ba60b5bce622b7c71ec92c3c8a3.npy <- 2013-02-10 d62.2.c_m24_main.pdf
Embedding: e865a09ab451130ed77c19262451ecc14bdca9f6.npy <- 2011-04-03 requirements-projects_ltdp_uporto_3april2011.pdf
Embedding: 6034574812cc71d62a4a48cf0e090972d4b20f88.npy <- 2011-06-09 d-req_up_9june2011-v3.pdf
Embedding: 0ecc9fbde34dd946bbf734485d016ba7edf7ee5a.npy <- 2012-05-07 leaflet_ensure_back03.pdf
Embedding: eee518a577af0d423d3b4189c99d62cbe7bdac74.npy <- 2012-01-31 d12.1b_ensure_requiremnetsm12_document_main.pdf
Embedding: 916250994d48b639a799fe7d3b505a8f332d0f4a.npy <- 2011-04-03 requirements-projects_ltdp_uporto_3april2011-v2.pdf
Embedding: 1f9d67bf8fc7339389e336c4eb03a942e8eb556a.npy <- 2014-01-30 d40.2.3_scientfic_report_main.pdf
Embedding: 3379200ecef7ffb9068fb93e7a1ed32f33e5e2d6.npy <- 2011-04-12 ltu_protage_d1_1-state-of-the-art-needs-scenarios_ver_1_0.pdf
Embedding: 53faa7a8c564a53bb74537536703ce20bb65f0d6.npy <- 2013-02-04 y2_agenda.pdf
Embedding: aefde05a2bed168c5ac291bec21616d1df4c9186.npy <- 2011-01-11 cranfield_university.pdf
Embedding: 81c3bd947c42484f55a8f6a109ddf342cf4f59ba.npy <- 2011-06-10 ensure-wp31_v.2.pdf
Embedding: 11572e8ffe2423c86b126612ce7e99cb0d2e5993.npy <- 2012-12-14 en91-web.pdf
Embedding: cae687ac422c714b8253548d499fd18fdc9f7322.npy <- 2014-02-16 a5_scenarios_main1.pdf
Embedding: b35c061d5e6e5cca5da1045c1c46b809f90b8cf3.npy <- 2014-01-28 d13-1-2-standardization_summary_report.pdf
Embedding: f00fd4397b992fbcabd0d81e77f0d11247491816.npy <- 2011-11-24 news_item_feup_ensure_november2011.pdf
Embedding: 9a736725b46fe7bd4d5586aa8dcd5001c7751362.npy <- 2012-05-30 postera4.pdf
Embedding: 55d6ab898a01c1031912cf53e315591289261256.npy <- 2012-09-13 echallenges_full_paper_fraunhofer_v3.pdf
Embedding: 722f1dbe65e587c802ec96740ae05b28d2c4609d.npy <- 2011-03-23 pv09_conway_pnm.pdf
Embedding: 527a3b8f9121dc90a8782cfe4bc787ddbc995341.npy <- 2011-08-08 ensure-wp31_v.4.pdf
Embedding: eac65247743427924227b2b7d11a4a6e423a06b3.npy <- 2012-12-13 acoste_conference_2012_-_agenda-final.pdf
Embedding: 92537ae48b12a56bffff8aa3dd91041d5da81204.npy <- 2011-05-29 d-req_up_29may2011-v4.pdf
Embedding: d403f96fe5e7d3ee403ef7a2f7f90fc0869a4c39.npy <- 2014-01-21 d11.1.3_ensure_high_level_architecture_document.pdf
Embedding: 6a757ccc8e4bdd413968bf7208204598842b94f9.npy <- 2011-08-21 d62.2a_dissemination_m6_submitted.pdf
Embedding: 934cde4eef260b60240fde32138817fb3b5eb138.npy <- 2012-02-01 d40.1_a4_scientific_report_m12_.pdf
Embedding: 5b9221dc829770109cdc4a634c5904c7f65c3da8.npy <- 2011-08-05 dissemination-deliv-uporto-5august2011-w.pdf
Embedding: b4447567ed4aea868ba045c0086fc11d6a2af6f2.npy <- 2011-05-13 mac-tv-march_2011.pdf
Embedding: b9d751f8d1f33250327c3c0d1c91c453d4991759.npy <- 2014-05-11 d70.3.2_training_main_v2.pdf
Embedding: 10d1ace957cb176666eaaca4288f997937ed1336.npy <- 2014-05-11 d70.3.2_training_main.pdf
Embedding: 70fc5632b7dc1970d16d4fb15e74c43ed5730def.npy <- 2011-07-04 icmr_-_cost_modelling_for_long-term_digital_preser.pdf
Embedding: 4ea589829e0282e3007e222d965ceb6816b76adf.npy <- 2012-05-30 postera4-1.pdf
Embedding: dc4c26c248ba5b1238a434945c494428273952be.npy <- 2013-02-04 d40.1.b_a4_scientfic_report_main.pdf
Embedding: baec98ed261f28712ed54fb93b8826323b54e2bc.npy <- 2011-01-11 leonardo_offer.pdf
Embedding: 5689237505daa4b10e7b8f5a4e8a13ca30ae600f.npy <- 2011-11-06 d11.1_ensure_high_level_architecture_document_main.pdf
Embedding: 7f07a878ae752cb23d38472310d0de3dc9fe379e.npy <- 2014-05-14 d50.4.2_a5_prototype_demo_main.pdf
Embedding: dc3fa82275bd1d32ab64efd02f03506df450ad61.npy <- 2013-08-12 d30.1.2_a3_prototype_demo_main.pdf
Embedding: 031d3d9ceca0ef4db1abc46462a2e55ae800eaa6.npy <- 2014-01-23 d30.2.3_scientfic_report_main.pdf
Embedding: daeaf220681bb2f7b060a2d462dcddde9444dda9.npy <- 2011-08-16 11388132.pdf
Embedding: 39164e046499c6dd510e8d18b013e6c915abd9fc.npy <- 2011-08-05 newsl-cl-5aug2011-v3-c.pdf
Embedding: d000271d620be0b608e529b52d994aac47695739.npy <- 2012-02-14 d20.1.a_activity_ii_scientific_report.pdf
Embedding: 0b204f602e200775d9b90302bc453d9ca045a1d4.npy <- 2011-08-04 ensure-wp31_v.3.pdf
Embedding: 96e892b170c6bbae5827dd214521f3dac9e24429.npy <- 2012-05-07 leaflet_ensure_front1.pdf
Embedding: 968311561dd444fdef9e7754d82e94d4436af837.npy <- 2012-03-02 echallenges_2012_ensure_abstract_fraunhofer_v1.pdf
Embedding: a0d0fec84d724a43a7fd17de992ba40ab2f2e792.npy <- 2011-02-20 ensure_-_ga_signed_by_the_european_commisssion.pdf
Ignoring bogus embedding: nan
Embedding: ecd1e7970bef1d1f8adc0ce23dede18754332c0a.npy <- 2011-06-16 d_1.2.1_requirements-16iunie2011.pdf
Embedding: d4a29adbcc57a1e5e4281254458888dda5cc8efc.npy <- 2011-08-12 press_release_fraunhofer_ibmt_ensure_2011_08_12_german.pdf
Embedding: 0c576ba9fd28cda32afc4e4a8ce7591c6385f080.npy <- 2013-04-04 EC Review Report Year 2.pdf
Ignoring bogus embedding: nan
Embedding: 4bd2ea1ad003ad3d8c8732dbaeffde420edd1134.npy <- 2011-01-11 sap_contribution_ensure.pdf
Embedding: 30ddad7c54bc7e0dade58ea965c1bbfbdb616c5a.npy <- 2011-03-23 ensure-wp31-architecture-draft01.pdf
Embedding: 03555ffd0ba9ef03f657db36e5aa2c5107dfdd9d.npy <- 2013-08-12 a2_prototype_demo_main.pdf
Embedding: c5ac24d1372e8deb985833b047010de9d65528c8.npy <- 2012-10-10 automation_of_information_quality_evaluation_in_ehealth_records_from_a_preservation_perspective.pdf
Embedding: 84801cdb8e8d0a62a9eb4f6757560bf7e78c9045.npy <- 2011-12-22 2011_infoblatt_ensure_dt.pdf
Embedding: 8840d69edc1cdb8c49aae2246d0a1c51fc368f1e.npy <- 2013-08-15 routeplanning_qs.pdf
Embedding: ea6e55d373429f2b8755976d9e9dd71acedcdbc2.npy <- 2012-03-02 mie2012_ensure_paper_fraunhofer_ibmt.pdf
Embedding: 848c79cb8baf314bc1b42169a3ef03f509296be0.npy <- 2011-05-19 ensure-wp31-architecture-draft04.pdf
Embedding: b260d008dbadea02ff8806eaf153e562be1a4b32.npy <- 2012-04-05 mie2012_ensure_paper_fraunhofer_ibmt_final_manuscript.pdf
Embedding: da538c0ba5919528ff565cc18f9cabab5e03c321.npy <- 2012-05-07 leaflet_ensure_front02.pdf
Embedding: 23304c0aad7e3b1d35acfb53d1a78eda99f01839.npy <- 2011-05-20 d-req_up_20may2011-v4.pdf
Embedding: a9bb6030ab62fefbfd79cda50d08bf5ea1908bac.npy <- 2011-08-17 d62.2a_dissemination_m6.pdf
Embedding: bd1772260ada55e239c352bf2dd4cccd96581b2d.npy <- 2011-09-14 ensure-newsletter-september2011.pdf
Embedding: cc1f6aeea5fece0f1e47ffb7c3c98aefb291fc15.npy <- 2012-05-07 leaflet_ensure_front03.pdf
Embedding: 7daaff801678dd183414054363842207e04da7a2.npy <- 2013-02-04 d50.1.b_a5_scenarios_main.pdf
Embedding: c07cfc1c2106ebae789d67cf9167efcd7eec4980.npy <- 2011-01-11 ensure_march_10.pdf
Embedding: fb9fe30a3fd5cfa3887a1fd62d4595007e285bde.npy <- 2011-01-11 ensure_270000_2010-11-16.pdf
Embedding: db5758868e8a29134c0a1fc0d7872b25a5499d57.npy <- 2013-02-04 d30.1_scientfic_report.pdf
Embedding: 311357fd4fe0f622aa93399dff666db192b02280.npy <- 2011-03-23 scarp_b4832_atmospheric.pdf
Embedding: 5bae604be4c9cffe1495a9aafff5fcf1d65eb024.npy <- 2011-01-11 build_030310.pdf
Embedding: a764a72ebad2aeb5aa92a0419d903c9bca37ce58.npy <- 2013-08-12 d20.1.1_a2_prototype_demo_main.pdf
Embedding: 5f6b1544cfea0077aa63640d1df08d0eb5bc9c63.npy <- 2014-05-14 d20.1.3_a2_prototype_demo_main.pdf
Embedding: c5c95e11c4f2ecd01dcd25503d909199e88e9c8e.npy <- 2014-01-30 d60.2.3_exploitation_report.pdf
Embedding: 04f1255c879de6b3e5d380e390886b08cfe79654.npy <- 2012-03-06 1628_cost_modelling_leaflet.pdf
Embedding: 52e6d228a26c47068abd81d5d500ec539bb32a54.npy <- 2011-11-24 news_item_uporto_ensure_november2011.pdf
Ignoring bogus embedding: nan
Embedding: b3cd4c72f20283b3e3c9beeadacd13340f1a4a26.npy <- 2011-08-08 dissemination-deliv-uporto-8august2011-w.pdf
Embedding: 8d6479a0a04c3c710bd491176f1c4d9ecfa4d507.npy <- 2014-01-30 d60.1.c_activity_vi_summary_report.pdf
Embedding: 8326c788fa858616c6077b2f6057de25e173ae48.npy <- 2013-01-29 id_643.conservacionensayosclinicos.pdf
Embedding: fcdfa7655e548472765a60ef6d12cc9ddc623b2a.npy <- 2011-05-08 ensure_poster.pdf
Embedding: 96418282b15fde80ec04c1ea7ed798e02bee8bc0.npy <- 2013-06-03 dow_amendment1_main.pdf
Embedding: c7273ce8ac63ece487e78c096565c596d1289cbc.npy <- 2011-06-24 ensure_manufacturing-debate_poster.pdf
Embedding: a1cf81c3bbdd65ae39b9d839b58ed12e427c022b.npy <- 2011-09-09 newsl-cl-9sept2011.pdf
Embedding: f8d4fb1b867c225f6143a87bf382eb33ea33c637.npy <- 2011-09-13 a2ensure.pdf
Embedding: b5fe1b25189b964a200ff2be3884d60bd1457de4.npy <- 2013-08-12 d40.1.2_a4_prototype_demo_main.pdf
Embedding: b476919cf4f1b131388e9a0aa1bbf13f8c5741af.npy <- 2012-03-14 dtc_poster_-_portrait.pdf
Embedding: f4522ddb7dc50aa5f4fb93de53a37f6761158826.npy <- 2013-02-11 d11.1.2_ensure_high_level_architecture_document_main.pdf
Embedding: 3d6c3ff7e1e70c57212929333eeac5bbaa5aa16f.npy <- 2014-03-17 runtime-user-guide.pdf
Embedding: 8f4d7eb25e5c5382a1eef4d12d7e733b92f97212.npy <- 2011-04-27 pp_concepts_pa3.pdf
Embedding: 8d2bd569f9c01bce247693a2fb1465a4b6c437de.npy <- 2011-03-23 preservationanalysis_ieee2009.pdf
Embedding: 14e39786efe5eeb1c4d285608e7e273ec1e2694d.npy <- 2012-01-19 d62.2b_ensure_disseminationm12_document_main.pdf
Embedding: 0f493f146e2bbdbc29ccb1efd4ce23ecdcc73881.npy <- 2012-01-11 sample_scientific_report.pdf
Embedding: 439a36a41fc498a4b1fe77ffc66f32a3490c6896.npy <- 2013-02-27 d0.1.1b_periodic_progress_man.pdf
Embedding: ec2f8a509405ec4ec23d052b52d3cf15f3622bdc.npy <- 2013-06-12 user-guide.pdf
Embedding: 5cb0f2d1407164c69aff841a529752c95311d519.npy <- 2012-03-14 alhawas.pdf
Embedding: b07ef4d0605b55bdb984315010588d36825f7cf2.npy <- 2012-07-06 google_analitics_reporting.pdf
Embedding: 6eb7e108f75b413f434a6e2a789bf9cf66b3d9a7.npy <- 2011-04-12 ltu_protage_d1.2-functional-requirements-specification_-_final_version.pdf
Embedding: 216b14f6995e76b5a0b37afaeb78b74748bc1192.npy <- 2011-05-31 d-req_up_31may2011-v4.pdf
Embedding: 048a4d9147db0c0e445e9cc21584984fe1ecd5db.npy <- 2012-05-07 ensure_postera4-v3.pdf
Embedding: 564c976db8cfdb729d022fc5f1b33139f5b23959.npy <- 2011-05-18 perspectives_march-apri-lmay2011_cranfield_leading_the_way_in_costing_of_long_term_digital_data_storage.pdf
Embedding: 77ce8bf0985203d55b87a17c7b113389d76f8ab5.npy <- 2014-02-10 d20.2.3_activity_ii_scientific_report.pdf
Embedding: 0789431290b09e516802a51059c296490b0a304d.npy <- 2012-05-07 leaflet_ensure_back1.pdf
Embedding: 57ef2de2f7829d2667601372d2f8c8282f8972f5.npy <- 2014-04-22 EC Final_review_report_y3.pdf
Embedding: 905f33cba986cb87536823b1a487737d97e0806b.npy <- 2014-06-19 ensure_27000_amendment_no2_signed_by_the_ec_a.pdf
Embedding: 177b7662f5817b62e1d1e5de7a5cb2d4988b287d.npy <- 2014-01-16 ensure_270000_am_no_1.pdf
Embedding: 749608ef367786c5cd5cda88f3b05094a48e5624.npy <- 2011-03-23 ensure-wp31.pdf
Embedding: e9bd70246fa71248ebc6714aecc583f1746a2ebe.npy <- 2011-05-25 minutes_nih_workshop.pdf
Embedding: 306427c64ac4d3137e74e784155a8e57ad0decb4.npy <- 2011-04-01 ensure-wp31-architecture-draft03.pdf
Embedding: e9af4356af61c8eb4321b1348b1437cc9da7ba91.npy <- 2011-08-11 maccabifood-119723_.pdf
Embedding: 4ddbbb4eb9e9e218d001b89db6cacbec822dee46.npy <- 2012-02-08 ensure_d30.2.1_scientfic_report_main.pdf
Embedding: 83c08b4c5641fefda09d60a43d9f556ea1b2cdd8.npy <- 2011-07-05 requirements_d1.2.1a.pdf
Embedding: aa96c79eb414a9640bc64f8cdcb169bd167e6527.npy <- 2011-02-23 kickoff_wp44.pdf
Embedding: 183a30ebfc7fa87817527ced26ef3e91360a0484.npy <- 2012-06-03 ipress2011_evolving_domains_problems_and_solutions_for_ltdp_.pdf
Embedding: a2d7e57365f8292391dcf8e99d3bfa3a2275d497.npy <- 2012-12-13 paasc2012_cmchituc_pristau.pdf
Embedding: ab34c2d2ccb15f9f8a270f653b716962624b5f7a.npy <- 2013-02-06 d20.1.b_activity_ii_scientific_report.pdf
Embedding: 80f1f3736d1e708bdd2f3063943a0059198aae8d.npy <- 2013-03-13 d12.1c_ensure_requiremnetsm24_document_main.pdf
Embedding: 147172d4996297711605c038a856136e893b2488.npy <- 2014-03-06 d0.1.1c_periodic_progress_man.pdf
Embedding: 6a6675d02aaf24f8c0f3b281820d91bc3f7707cf.npy <- 2012-03-14 ensure_manufacturing-debate_poster1.pdf
Embedding: 0de125387245692029a4e0521cd673b0d51b53fa.npy <- 2011-12-13 pm_jrc_ensure_08_03_11.pdf
Embedding: b9cf7e171809a6379c644446bc10d34b54e982fa.npy <- 2011-08-16 newsl-cl-16aug2011.pdf
Embedding: c8b9d9294541bfafef9d6a5bc87d52a17b9d963a.npy <- 2011-02-20 ca_-_project_ensure_270000_partners.pdf
Embedding: 97dc37901ff7f0a3f17dd56a15af6f3633411444.npy <- 2011-07-29 dissemination-deliv-uporto-29iulie2011-v4-wiki-lnumbers2.pdf
Embedding: 1448e97cf99a300f6ee0f27643c696aa191aa9a7.npy <- 2014-02-16 a5_scenarios_main.pdf
Embedding: b3f2c770bf277792629be175a6d7e1a6c5bf4d6d.npy <- 2012-03-14 poster.pdf
Embedding: d319fd8e0deec5deb2f45fa7df9c0f2048878ed3.npy <- 2013-02-10 d61.2_m24_main.pdf
Embedding: 6b4bda90f289b6a397dd990884545559a2904e59.npy <- 2013-08-12 d30.1.1_a3_prototype_demo_main.pdf
Embedding: 17796c138a3afe3ee425483533463bc54b9b0e75.npy <- 2011-01-11 feup-chituc-presentation-for_ensure-7dec2009.pdf
Embedding: 2fe0c2038061558874a46f96233c99bdc14376d6.npy <- 2013-03-18 Berlin -Agenda.pdf
Ignoring bogus embedding: nan
Embedding: a1a819611332319eddedd9336e166ddbb82052e2.npy <- 2013-04-22 Saarbrücken - Agenda.pdf
Ignoring bogus embedding: nan
Embedding: 800dadc9253c1b44a7f92fc603c93a110a547658.npy <- 2012-05-17 Haifa - Agenda.pdf
Ignoring bogus embedding: nan
Embedding: d9bdd37660806a07d30dcbf609418ebc434fd116.npy <- 2012-10-17 eChallenges Programme.pdf
Embedding: 62bfc47c42c7d7d54d63306eb0788987a70b552d.npy <- 2012-03-12 Brüssel.pdf
Embedding: fc4fb0f896d351289b72b59775777953eec03e96.npy <- 2013-11-18 Stavanger - NOKOBIT.pdf
Ignoring bogus embedding: nan
Embedding: 3a642056ed4dad28591b39965dffeebbbbb3ae73.npy <- 2013-02-17 Haifa - Invitation.pdf
Ignoring bogus embedding: nan
Embedding: bc417b589e9c67b084647f126df04b03c4d5dcac.npy <- 2014-03-17 Porto - Program.pdf
Ignoring bogus embedding: nan
Embedding: c2ef1d9c0d54cbec39d0e3a6895d420e7bb6f932.npy <- 2013-10-28 Eindhoven - Agenda.pdf
Ignoring bogus embedding: nan
Embedding: 98934c12bc54cb5818b5cf792113eaf978ac4528.npy <- 2012-02-08 D30.2.1 A3 Scientific Report.pdf
Embedding: 3ba6b6eb40999a14b2c8187d41ce40f193ccfb52.npy <- 2012-02-02 d60.1_m12_main.pdf
Embedding: 1f06d126647e6cf7d21abba4ca25c3cdc4651dd7.npy <- 2012-02-01 D20.1.a Activity II Scientific Report.pdf
Embedding: 246505c2425cd031b99b0c60d0f785644f80e163.npy <- 2014-02-01 D20.2.3 Activity II Scientific Report.pdf
Embedding: daa31427ef84a68a3713cb48b9544b87ef131f13.npy <- 2011-08-21 d62.2a_dissemination_m6_submitted.pdf
Embedding: 569a48923ff19462b0ecb775b7e49ce30cef8259.npy <- 2011-06-15 requirements_d1.2.1a.pdf
Embedding: 8a5955e857d89c9fb093f51f5c517a37c257f21e.npy <- 2012-01-31 d12.1b_ensure_requirements12_document_main.pdf
Embedding: 2040aa14ad9c7a686fa7f6936e74a90ffbe1a597.npy <- 2012-02-14 d20.1.a_activity_ii_scientific_report.pdf
Embedding: 593eb4e2cd45dd8c6b675285b3e3fc74779c3256.npy <- 2013-02-01 D20.1.b Activity II Scientific Report.pdf
Embedding: aa5791247614786e0c7717c9e31d44d7ee81d373.npy <- 2012-02-01 d40.1_a4_scientific_report_m12.pdf
Embedding: 86c3786bce5d2f6246ff72986879287d791f6e33.npy <- 2011-11-05 d11.1_ensure_high_level_architecture_document_main.pdf
Embedding: d9b9aa81b88f4b78baac1ec36b231613559f4973.npy <- 2012-02-08 d0.1.1a_periodic_progress_man.pdf
Embedding: f2c277bb8dc699558da5d1f28f22202749dc8091.npy <- 2012-03-05 a5_scenarios_main.pdf
Embedding: 6115f7747db4950188534f2cc272c98c5bef4fc1.npy <- 2012-12-13_TR_Interview_Report_version03.pdf
Embedding: f63dde5d9f52a860a456e12e03d4544378d1af05.npy <- 2014-01-28_D20_GUI_Survey_Jan28_CSISP.pdf
Embedding: 0e816de034e7bec1ecb660342e0ff735f05dfe97.npy <- 2014-01-28_D20_GUI_Survey_Jan28_JRC.pdf
HTML generated at: /Users/froran/Thesis/index.html
(env) ➜  organizr git:(main) ✗
```

## Resulting clustering
As you see, there is no particular sort order. Going through this list, I find it to be thematically sound.

### Cluster 7

Representative for this cluster: ```2014-02-10 d20.2.3_activity_ii_scientific_report.pdf```
```
froran-thesis.pdf
data-index.pdf
Schoorman, Mayer, Davis (2007) An integrative model of organizational trust; past, present, and future.pdf
Mayer, Davis, Schoorman (1995) An integrative model of organizational trust.pdf
A Preservation Services Planning Decision Framework (2014).pdf
2013-10-22 On consequences information sent to cost engine.pdf
2013-11-22 Regarding evaluations of the cost engine.pdf
2013-05-29 Quality-to-cost-engine-integration.pdf
D20.2.3 Activity II Scientific Report.pdf
D20.1.b Activity II Scientific Report.pdf
D20.1.a Activity II Scientific Report.pdf
2012-02-14 d20.1.a_activity_ii_scientific_report.pdf
2014-01-30 d60.1.c_activity_vi_summary_report.pdf
2014-02-10 d20.2.3_activity_ii_scientific_report.pdf
2012-12-13 paasc2012_cmchituc_pristau.pdf
2013-02-06 d20.1.b_activity_ii_scientific_report.pdf
2012-02-01 D20.1.a Activity II Scientific Report.pdf
2014-02-01 D20.2.3 Activity II Scientific Report.pdf
2012-02-14 d20.1.a_activity_ii_scientific_report.pdf
2013-02-01 D20.1.b Activity II Scientific Report.pdf
2014-01-28_D20_GUI_Survey_Jan28_CSISP.pdf
2014-01-28_D20_GUI_Survey_Jan28_JRC.pdf
```
### Cluster 3

Representative for this cluster: ```Cost for Long-Term Digital Preservation - 9 Months Review.pdf```
```
Cost for Long-Term Digital Preservation - 9 Months Review.pdf
Cost_Claim_overview_ENSURE_2013-04-10.pdf
2011-01-11 cranfield_university.pdf
2012-12-13 acoste_conference_2012_-_agenda-final.pdf
2011-07-04 icmr_-_cost_modelling_for_long-term_digital_preser.pdf
2012-03-14 dtc_poster_-_portrait.pdf
2012-03-14 alhawas.pdf
2012-03-14 poster.pdf
2011-01-11 feup-chituc-presentation-for_ensure-7dec2009.pdf
```
### Cluster 14

Representative for this cluster: ```(2011) Preserving digital materials.pdf```
```
review.pdf
14 Strodl (2010) - (Semi-)Automated digital preservation archives for small institutions and private users.pdf
17 Burda, Teuteberg (2013) - Investigating the Needs, Capabilities and Decision Making Mechanisms in Digital Preservation; Insights from a Multiple Case Study.pdf
30 Whyte (2007) - Report from the DCC Workshop; Legal Environment of Digital Curation.pdf
24 Oltmans, van Wijngaarden (2006) - The KB e-Depot digital archiving policy.pdf
22 Anderson, Delve, Powel (2012) - The Changing Face of the History of Computing; The Role of Emulation in Protecting Our Digital Heritage.pdf
32 Truex, Olsson, etc (2011) - Position Statement; Sustainable Information and Information Systems (SIIS).pdf
09 Strodl, Becker, Rauber (2009) - Digital Preservation (chapter).pdf
Hart, Liu (2003) Trust in the preservation of digital information.pdf
(2011) Preserving digital materials.pdf
Day (2008) Toward distributed infrastructures for digital preservation; the roles of collaboration and trust.pdf
rutgers-lib-36587_PDF-1.pdf
Ross (2012) Digital Preservation, Archival Science and Methodological Foundations for Digital Libraries.pdf
An Activity Theory Lens on Digital Preservation Challenges of Using Preservation Services (2013).pdf
Inherent Problems in Cooperative Planning for Future Access to Information (2013).pdf
Scholar Alert digital preservation quality fitness purpose .pdf
2011-04-12 ltu_protage_d1_1-state-of-the-art-needs-scenarios_ver_1_0.pdf
2011-03-23 scarp_b4832_atmospheric.pdf
2011-03-23 preservationanalysis_ieee2009.pdf
2012-06-03 ipress2011_evolving_domains_problems_and_solutions_for_ltdp_.pdf
```
### Cluster 18

Representative for this cluster: ```19 Rosado, Gomez, Mellado, Fernandez-Medina (2012) - Security Analysis in the Migration to Cloud Environments.pdf```
```
20 Strauch, Andrikopoulos, Bachmann, Leymann (2013) - Migrating Application Data to the Cloud using Cloud Data Patterns.pdf
15 Fehling, Leymann, Ruehl, Rudek, Verclas (2013) - Service Migration Patterns - Decision Support and Best Practices for the Migration of Existing Service-Based Applications to Cloud Environments.pdf
03 Khajeh-Hosseini, SOmmerville, Bogaerts, Teregowda (2011) - Decision Support Tools for Cloud Migration in the Enterprise.pdf
19 Rosado, Gomez, Mellado, Fernandez-Medina (2012) - Security Analysis in the Migration to Cloud Environments.pdf
02 Marston, Li, Bandyopadhyay, Ghalsasi (2011) - Cloud Computing - The Business Perspective.pdf
26 Liu, Rijnboutt, Routsis et al (2013) - What challenges have to be faced when using the cloud for e-health services.pdf
23 Müller, Han, Scheider, Versteeg (2011) - Tackling the Loss of Control; Standards-Based Conjoint Management of Security Requirements for Cloud Services.pdf
12 Strauch, Andrikopoulos, Bachmann, Karastoyanova, Passow, Vukojevic-Haupt (2013) - Decision Support for the Migration of the Application Database Layer to the Cloud.pdf
```
### Cluster 21

Representative for this cluster: ```08 Menzel, Ranjan (2011) - CloudGenius; Automated Decision Support for Migrating Multi-Component Enterprise Applications to Clouds.pdf```
```
25 Rings, Caryer, Gallop, Grabowski, Kovacikova, Schulz, Stokes-Rees (2009) - Grid and Cloud Computing; Opportunities for Integration with the Next Generation Network.pdf
05 Wittern, Kuhlenkamp, Menzel (2012) - Cloud Service Selection Based on Variability Modeling.pdf
08 Menzel, Ranjan (2011) - CloudGenius; Automated Decision Support for Migrating Multi-Component Enterprise Applications to Clouds.pdf
24 Sun, Dong, Hussain, Hussain, Chang (2014) - Cloud service selection; State-of-the-art and future research directions.pdf
16 Amato, Venticinque (2014) - A Distributed Agent-based Decision Support for Cloud Brokering.pdf
21 Jula, Sundararajan, Othman (2014) - Cloud computing service composition; A systematic literature review.pdf
13 Menzel, Ranjan, Wang, Khan, Chen (2015) - CloudGenius; A Hybrid Decision Support Method for Automating the Migration of Web Application Clusters to Public Clouds.pdf
17 Inzinger, Nastic, Sehic, Vögler, Li, Dustdar (2014) - MADCAT; A Methodology for Architecture and Deployment of Cloud Application Topologies.pdf
22 Khediri, Zaghdoud (2015) - Survey of Uncertainty Handling in Cloud Service Discovery and Composition.pdf
01 Menzel, Ranjan (2012) - CloudGenius; decision support for web server cloud migration.pdf
06 Andrikopoulos, Strauch, Leymann (2013) - Decision Support for Application Migration to the Cloud - Challenges and Vision.pdf
```
### Cluster 6

Representative for this cluster: ```04 Zhang (2012) - Investigating decision support techniques for automating Cloud service selection.pdf```
```
11 Martens, Walterbusch, Teuteberg (2012) - Costing of Cloud Computing Services; A Total Cost of Ownership Approach.pdf
04 Zhang (2012) - Investigating decision support techniques for automating Cloud service selection.pdf
10 Toosi, Calheiros, Buyya (2014) - Interconnected Cloud Computing Environments; Challenges, Taxonomy, and Survey.pdf
09 Sakr, Liu, Batista, Alomari (2011) - A Survey of Large Scale Data Management Approaches in Cloud Environments.pdf
nn AJeh, Ellman, Keogh (2014) - A Cost Modelling System for Cloud Computing.pdf
14 Barker, Varghese, Thai (2015) - Cloud Services Brokerage; A Survey and Research Roadmap.pdf
```
### Cluster 20

Representative for this cluster: ```2013-02-27 d0.1.1a_periodic_progress_man.pdf```
```
18 Hartung, Anokwa, Brunette, Lerer, Tseng, Borriello (2011) - Open Data Kit; Tools to Build Information Services for Developing Regions.pdf
07 Pearson, Benameur (2010) - Privacy, Security and Trust Issues Arising from Cloud Computing.pdf
2012-09-11 On selection of purposes.pdf
2010-04-15 ENSURE - draft proposal (confidential).pdf
2010-11-16 ENSURE (270000).pdf
A5_Scenarios_main.pdf
Last years A5 deliverable.pdf
D0.1.1a Periodic Progress_man.pdf
Final_Report_main.pdf
A5_Scenarios_main.pdf
D0.1.1a Periodic Progress_man.pdf
maccabi_standards.pdf
final_review_report_1.pdf
2013-02-27 d0.1.1a_periodic_progress_man.pdf
2014-02-23 final_report_main.pdf
2011-08-10 ensure-leaflet-10aug2011-v4.pdf
2012-01-11 sample_periodic_progress_report.pdf
2014-02-16 a5_scenarios_main1.pdf
2014-01-28 d13-1-2-standardization_summary_report.pdf
2012-05-30 postera4.pdf
2012-05-30 postera4-1.pdf
2011-01-11 sap_contribution_ensure.pdf
2013-02-04 d50.1.b_a5_scenarios_main.pdf
2011-01-11 ensure_march_10.pdf
2011-01-11 ensure_270000_2010-11-16.pdf
2011-01-11 build_030310.pdf
2013-01-29 id_643.conservacionensayosclinicos.pdf
2013-06-03 dow_amendment1_main.pdf
2013-02-27 d0.1.1b_periodic_progress_man.pdf
2011-04-12 ltu_protage_d1.2-functional-requirements-specification_-_final_version.pdf
2012-05-07 ensure_postera4-v3.pdf
2014-04-22 EC Final_review_report_y3.pdf
2011-02-23 kickoff_wp44.pdf
2014-03-06 d0.1.1c_periodic_progress_man.pdf
2011-02-20 ca_-_project_ensure_270000_partners.pdf
2014-02-16 a5_scenarios_main.pdf
2012-10-17 eChallenges Programme.pdf
2012-02-08 d0.1.1a_periodic_progress_man.pdf
2012-03-05 a5_scenarios_main.pdf
```
### Cluster 8

Representative for this cluster: ```01 Ferreira, Baptista, Ramalho (2007) - An intelligent decision support system for digital preservation.pdf```
```
21 Kulmukhametov, Becker (2014) - Content Profiling for Preservation; Improving Scale, Depth and Quality.pdf
03 Becker, Rauber, Heydegger, Schnasse, Thaller (2008) - A Generic XML Language for Characterising Objects to Support Digital Preservation.pdf
12 Lindley, Jackson, Aitken (2010) - A Collaborative Research Environment for Digital Preservation - The Planets Testbed.pdf
13 Becker, Ferreira, Kraxner, Rauber, Baptista, Ramalho (2008) - Distributed Preservation Services; Integrating Planning and Actions.pdf
07 Neumann, Miri, Thomson, Antunes, Mayer, Beigl (2013) - Towards a Decision Support Architecture for Digital Preservation of Business Processes.pdf
15 Becker, Kolar, Küng, Rauber (2007) - Preserving Interactive Multimedia Art; A Case Study in Preservation Planning.pdf
02 Becker, Kulovits, Rauber, Hofman (2008) - Plato; a service oriented decision support system for preservation planning.pdf
10 Hunter, Choudhury (2006) - PANIC; an integrated approach to the preservation of composite digital objects using Semantic Web services.pdf
23 Graf, Huber-Mörk, Schindler, Schlarb (2013) - Duplicate detection approaches for quality assurance of document image collections.pdf
04 Becker, Rauber (2011) - Decision criteria in digital preservation; What to measure and how.pdf
18 Strodl, Becker, Neymayer, Rauber, etc (2007) - Evaluating Preservation Strategies for Electronic Theses and Dissertations.pdf
16 Rauch, Pavuza, Strodl, Rauber (2005) - Evaluating Preservation Strategies for Audio and Video Files.pdf
11 Becker, Rauber, Heydegger, Schnasse, Thaller (2008) - Systematic Characterisation of Objects in Digital Preservation; The eXtensible Characterisation Languages.pdf
01 Ferreira, Baptista, Ramalho (2007) - An intelligent decision support system for digital preservation.pdf
33 Risse, Dietze, Maynard, Tahmasebi, Peters (2011) - Using Events for Content Appraisal and Selection in Web Archives.pdf
Automation of information quality evaluation in ehealth records from a preservation perspective (2012).pdf
2011-03-23 pv09_conway_pnm.pdf
2012-10-10 automation_of_information_quality_evaluation_in_ehealth_records_from_a_preservation_perspective.pdf
```
### Cluster 9

Representative for this cluster: ```2011-11-06 d11.1_ensure_high_level_architecture_document_main.pdf```
```
19 Schmidt, King, Jackson, Wilson, Steeg, Melms (2010) - A Framework for Distributed Preservation Workflows.pdf
31 Abichandani, Prakash, Barwal, Murthy (2015) - Tool for Metadata Extraction and Content Packaging as Endorsed in OAIS Framework.pdf
27 Liu, Futrelle, Myers, Ridriguez, Kooper (2010) - A provenance-aware virtual sensor system using the Open Provenance Model.pdf
26 Auer, Salmagas, Parkinson, Bancilhon, etc (2012) - Diachronic linked data; towards long-term preservation of structured interrelated information.pdf
08 Hunter, Choudhury (2004) - A Semi-Automated Digital Preservation System based on Semantic Web Services.pdf
20 Hunter, Choudhury (2005) - Semi-automated preservation and archival of scientific data using semantic grid services.pdf
25 Rauber, Bruckner, Aschenbrenner, Witvoet, Kaiser (2002) - Uncovering Information Hidden in Web Archives; A Glimpse at Web Analysis Building on Data Warehouses.pdf
ENSURE; Long term digital preservation of Health Care, Clinical Trial and Financial data (2013).pdf
scientfic_report_main.pdf
D11.1.3 ENSURE High Level Architecture Document_main.pdf
D11.1 ENSURE High Level Architecture Document_main.pdf
2014-01-30 d40.2.3_scientfic_report_main.pdf
2014-01-21 d11.1.3_ensure_high_level_architecture_document.pdf
2012-02-01 d40.1_a4_scientific_report_m12_.pdf
2013-02-04 d40.1.b_a4_scientfic_report_main.pdf
2011-11-06 d11.1_ensure_high_level_architecture_document_main.pdf
2014-01-23 d30.2.3_scientfic_report_main.pdf
2013-02-04 d30.1_scientfic_report.pdf
2013-02-11 d11.1.2_ensure_high_level_architecture_document_main.pdf
2012-01-11 sample_scientific_report.pdf
2012-02-08 ensure_d30.2.1_scientfic_report_main.pdf
2012-02-08 D30.2.1 A3 Scientific Report.pdf
2012-02-01 d40.1_a4_scientific_report_m12.pdf
2011-11-05 d11.1_ensure_high_level_architecture_document_main.pdf
```
### Cluster 10

Representative for this cluster: ```Rousseau, Sitkin, Burt, Camerer (1998) Not so different after all; A cross-discipline view of trust.pdf```
```
Rousseau, Sitkin, Burt, Camerer (1998) Not so different after all; A cross-discipline view of trust.pdf
```
### Cluster 0

Representative for this cluster: ```2012-05-10 Describing the quality model.pdf```
```
2012-05-10 Describing the quality model.pdf
```
### Cluster 19

Representative for this cluster: ```2012-01-12 Sketches around a preservation plan model.pdf.pdf```
```
2012-01-12 Sketches around a preservation plan model.pdf.pdf
2011-04-27 pp_concepts_pa3.pdf
```
### Cluster 1

Representative for this cluster: ```2011-06-13 d-req_up_13june2011-v6.pdf```
```
2011-05-29 Requirements deliverable v4.pdf
D1.2.1 Requirements M4.PDF
D12.1c ENSURE RequiremnetsM24 Document_main.pdf
D1.2.1 Requirements M4.PDF
2011-06-13 d-req_up_13june2011-v6.pdf
2011-06-15 d1.2.1_requirements_document.pdf
2011-04-11 techreport.pdf
2011-04-16 requirements-projects-ltdp-uporto-16april2011.pdf
2012-05-30 option1-b.pdf
2011-06-10 ensure-wp31_v.1.pdf
2011-04-03 requirements-projects_ltdp_uporto_3april2011.pdf
2011-06-09 d-req_up_9june2011-v3.pdf
2012-01-31 d12.1b_ensure_requiremnetsm12_document_main.pdf
2011-04-03 requirements-projects_ltdp_uporto_3april2011-v2.pdf
2011-05-29 d-req_up_29may2011-v4.pdf
2011-06-16 d_1.2.1_requirements-16iunie2011.pdf
2011-05-19 ensure-wp31-architecture-draft04.pdf
2011-05-20 d-req_up_20may2011-v4.pdf
2011-05-31 d-req_up_31may2011-v4.pdf
2011-05-25 minutes_nih_workshop.pdf
2011-07-05 requirements_d1.2.1a.pdf
2013-03-13 d12.1c_ensure_requiremnetsm24_document_main.pdf
2011-06-15 requirements_d1.2.1a.pdf
2012-01-31 d12.1b_ensure_requirements12_document_main.pdf
2012-12-13_TR_Interview_Report_version03.pdf
```
### Cluster 4

Representative for this cluster: ```2014-03-17 runtime-user-guide.pdf```
```
2011-09-20 Brussels F2F Meeting minutes.pdf
2012-05-30 option1-f.pdf
2013-02-04 y2_agenda.pdf
2012-12-14 en91-web.pdf
2011-05-13 mac-tv-march_2011.pdf
2014-05-11 d70.3.2_training_main_v2.pdf
2014-05-11 d70.3.2_training_main.pdf
2011-01-11 leonardo_offer.pdf
2013-08-15 routeplanning_qs.pdf
2011-09-13 a2ensure.pdf
2014-03-17 runtime-user-guide.pdf
2013-06-12 user-guide.pdf
2012-07-06 google_analitics_reporting.pdf
2011-05-18 perspectives_march-apri-lmay2011_cranfield_leading_the_way_in_costing_of_long_term_digital_data_storage.pdf
2012-03-12 Brüssel.pdf
```
### Cluster 5

Representative for this cluster: ```2013-02-10 d62.2.c_m24_main.pdf```
```
D70.2.4 Dissemination Report.pdf
D70.3.2_training_main.pdf
D70.2.1 Dissemination.PDF
D60.1_M24_main.pdf
D70.2.1 Dissemination.PDF
2013-02-10 d60.1_m24_main.pdf
2014-01-30 d70.2.4_dissemination_report.pdf
2012-02-02 d60.1_m12_main.pdf
2013-02-04 d70.3_m24_main.pdf
2013-02-10 d62.2.c_m24_main.pdf
2011-08-21 d62.2a_dissemination_m6_submitted.pdf
2011-08-05 dissemination-deliv-uporto-5august2011-w.pdf
2011-08-05 newsl-cl-5aug2011-v3-c.pdf
2011-08-17 d62.2a_dissemination_m6.pdf
2011-09-14 ensure-newsletter-september2011.pdf
2014-01-30 d60.2.3_exploitation_report.pdf
2011-08-08 dissemination-deliv-uporto-8august2011-w.pdf
2011-09-09 newsl-cl-9sept2011.pdf
2012-01-19 d62.2b_ensure_disseminationm12_document_main.pdf
2011-08-16 newsl-cl-16aug2011.pdf
2011-07-29 dissemination-deliv-uporto-29iulie2011-v4-wiki-lnumbers2.pdf
2013-02-10 d61.2_m24_main.pdf
2012-02-02 d60.1_m12_main.pdf
2011-08-21 d62.2a_dissemination_m6_submitted.pdf
```
### Cluster 2

Representative for this cluster: ```D30.1.1_A3_prototype_demo_main.pdf```
```
D30.1.1_A3_prototype_demo_main.pdf
2013-08-12 d30.1.2_a3_prototype_demo_main.pdf
2013-08-12 d30.1.1_a3_prototype_demo_main.pdf
```
### Cluster 24

Representative for this cluster: ```D20.1.1_A2_prototype_demo_main.pdf```
```
D20.1.1_A2_prototype_demo_main.pdf
2013-08-12 d40.1.1_a4_prototype_demo_main.pdf
2014-05-14 d50.4.2_a5_prototype_demo_main.pdf
2013-08-12 a2_prototype_demo_main.pdf
2013-08-12 d20.1.1_a2_prototype_demo_main.pdf
2014-05-14 d20.1.3_a2_prototype_demo_main.pdf
2013-08-12 d40.1.2_a4_prototype_demo_main.pdf
```
### Cluster 11

Representative for this cluster: ```2012-03-02 mie2012_ensure_paper_fraunhofer_ibmt.pdf```
```
2011-02-23 ensure-wp31-architecture-draft.pdf
2012-09-13 echallenges_full_paper_fraunhofer_v3.pdf
2012-03-02 echallenges_2012_ensure_abstract_fraunhofer_v1.pdf
2012-03-02 mie2012_ensure_paper_fraunhofer_ibmt.pdf
2012-04-05 mie2012_ensure_paper_fraunhofer_ibmt_final_manuscript.pdf
```
### Cluster 13

Representative for this cluster: ```2011-03-23 ensure-wp31-architecture-draft01.pdf```
```
2011-03-29 ensure-wp31-architecture-draft02.pdf
2011-06-10 ensure-wp31_v.2.pdf
2011-08-08 ensure-wp31_v.4.pdf
2011-08-04 ensure-wp31_v.3.pdf
2011-03-23 ensure-wp31-architecture-draft01.pdf
2011-03-23 ensure-wp31.pdf
2011-04-01 ensure-wp31-architecture-draft03.pdf
```
### Cluster 15

Representative for this cluster: ```2012-05-07 leaflet_ensure_back02.pdf```
```
2012-05-07 leaflet_ensure_back02.pdf
2012-05-07 leaflet_ensure_back03.pdf
2011-05-08 ensure_poster.pdf
2012-05-07 leaflet_ensure_back1.pdf
```
### Cluster 23

Representative for this cluster: ```2011-08-12 press_release_fraunhofer_ibmt_ensure_2011_08_12_german.pdf```
```
2011-11-24 news_item_feup_ensure_november2011.pdf
2011-08-12 press_release_fraunhofer_ibmt_ensure_2011_08_12_german.pdf
2011-12-22 2011_infoblatt_ensure_dt.pdf
2011-12-13 pm_jrc_ensure_08_03_11.pdf
```
### Cluster 17

Representative for this cluster: ```2011-08-11 maccabifood-119723_.pdf```
```
2011-08-16 11388132.pdf
2011-08-11 maccabifood-119723_.pdf
```
### Cluster 22

Representative for this cluster: ```2012-05-07 leaflet_ensure_front1.pdf```
```
2012-05-07 leaflet_ensure_front1.pdf
2012-05-07 leaflet_ensure_front02.pdf
2012-05-07 leaflet_ensure_front03.pdf
```
### Cluster 12

Representative for this cluster: ```2012-03-14 ensure_manufacturing-debate_poster1.pdf```
```
2012-03-06 1628_cost_modelling_leaflet.pdf
2011-06-24 ensure_manufacturing-debate_poster.pdf
2012-03-14 ensure_manufacturing-debate_poster1.pdf
```
### Cluster 16

Representative for this cluster: ```2014-01-16 ensure_270000_am_no_1.pdf```
```
2014-06-19 ensure_27000_amendment_no2_signed_by_the_ec_a.pdf
2014-01-16 ensure_270000_am_no_1.pdf
```
