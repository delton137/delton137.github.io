---
layout: page
title: Research Statement
---

*This statement describes research from my time as a Staff Scientist at NIH and as a Data Scientist at Mass General Brigham. I now work independently; some of the projects below were still in progress when I left.*

# Opportunistic screening with CT scans

Roughly 100 million CT scans are performed in the United States each year, and that number is growing by several percent each year. Due to time and resource constraints, much potentially useful information in CT scans is currently not utilized. Fully automated AI tools can run in the background, segmenting organs and looking for abnormalities. Segmentation tools can be used to extract biomarkers which can be used for disease risk prediction. We call this paradigm "opportunistic screening".

I developed systems which perform automated measurements of bone mineral density (BMD) ([Elton et al., 2020](https://doi.org/10.1117/12.2551247)), muscle area and density ([Perez et al., 2020](https://doi.org/10.1007/s00261-020-02755-5)), visceral fat ([Perez et al., 2020](https://doi.org/10.1007/s00261-020-02755-5)), liver fat ([Pickhardt et al., 2020](https://doi.org/10.2214/ajr.20.24415)), aortic plaque burden ([Summers et al., 2020](https://doi.org/10.1016/j.acra.2020.08.022)), and pancreatic fat ([Tallam et al., 2022](https://doi.org/10.1148/radiol.211914)). Conditions we considered for early detection using CT biomarkers include osteoporosis, sarcopenia, myosteatosis, liver steatosis, diabetes, pancreatic cancer, and cardiovascular disease.

I also published a paper demonstrating a deep learning system for opportunistic cardiovascular disease risk prediction using abdominal CT ([Elton et al., 2022](https://doi.org/10.1117/12.2612620)). The combination of genetic factors with imaging biomarkers can also improve risk prediction and lead to the discovery of new phenotypic correlations ([Sethi et al., 2020](https://doi.org/10.1101/2020.05.07.20094706)).

I remain interested in how risk data is presented to patients, such as plotting patient-specific survival curves. Previous work has suggested that the way risk information is presented by a clinician affects how receptive patients are to taking steps to reduce risk. For instance, comparing with a baseline helps patients understand their relative risk (i.e. you are at 40% higher risk for CVD in the next 5 years compared to males of your age). The concepts of "arterial age" and "biological age" may help inform patients about their health ([Raghu et al., 2021](https://doi.org/10.1016/j.jcmg.2021.01.008)).

# Work at Mass General Brigham

### Opportunistic screening

At Mass General Brigham I helped run a biomarkers suite on 200,000 studies as part of the Opportunistic Screening Consortium for Abdominal Radiology (OSCAR). The results were intended to generate reference "nomograms" for different biomarkers, allowing clinicians to see how a patient compares to others in their age and gender cohort.

Paths forward for improving the CT-based risk prediction models include implementing multitask learning and additive hazard modeling to output multiple follow-up intervals ([Rod et al., 2012](https://doi.org/10.1097/ede.0b013e31825fa218)). I am also interested in studying associations between genes and imaging biomarkers, which could lead to the discovery of new genes associated with disease risk ([Sethi et al., 2020](https://doi.org/10.1101/2020.05.07.20094706)).

### Development of a multimodal model for chest CT report generation

AI in healthcare has been shifting from single-purpose bespoke machine learning models to general-purpose foundation models. Dozens of applications of large language models (LLMs) have already been explored: helping triage and respond to patient portal messages ([Chen et al., 2024](https://doi.org/10.1016/s2589-7500(24)00060-8)), constructing patient timelines ([Frattallone-Llado et al., 2024](https://doi.org/10.1007/978-981-97-2238-9_25)), drafting radiology reports, assisting clinicians search through video, and transcribing ambient audio to visit notes ([Moor et al., 2023](https://doi.org/10.1038/s41586-023-05881-4)).

At Mass General Brigham I worked on a multimodal model for chest CT. Radiologists who specialize in the chest at that institution spend about 50% of their time detecting and characterizing small nodules, often characterizing the same nodule on many follow-up scans. A multimodal model may help speed this process along. That work explored the open-source LLaVA-Next model and drew inspiration from the Merlin CT multimodal foundation model developed at Stanford ([Blankemeier et al., 2024](https://doi.org/10.48550/arXiv.2406.06512)).

### Perivascular fat attenuation to improve CVD risk prediction

The first stage of atherosclerosis involves inflammation of the arterial walls, which cannot be directly observed in CT scans ([Antonopoulos et al., 2017](https://doi.org/10.1126/scitranslmed.aal2658); [Dai et al., 2020](https://doi.org/10.1016/j.ijcard.2020.06.008)). However, inflammation inhibits adipogenesis, leading to small increases in the X-ray attenuation of visceral adipose tissue around the affected arteries. Recent work shows that measuring the attenuation of perivascular fat around coronary arteries enhances cardiac risk prediction and may serve as a valuable early-stage biomarker to identify patients at risk for plaque formation and cardiovascular disease. Such patients can be put on statins or other drugs to reduce the inflammation which may "nip atherosclerosis in the bud". Whereas many studies have looked at perivascular fat attenuation in cardiac CT, there are few studies exploring the use of deep learning to automate such measurements, and no studies so far which have explored opportunistic measurement of periaortic visceral fat attenuation in abdominal CT.

### New methods for validating general-purpose medical AI

Already many people are using LLMs like Claude and ChatGPT to help with medical questions. Several powerful open-source models have appeared as well, such as medBERT.de ([Bressem et al., 2024](https://doi.org/10.1016/j.eswa.2023.121598)), MedVersa ([Zhou et al., 2024](https://doi.org/10.48550/arXiv.2405.07988)), CancerLLM ([Li et al., 2024](https://arxiv.org/abs/2406.10459)), and OpenBioLLM. The FDA still has not released guidance on how it will regulate general-purpose medical AI ("AI doctors"). Even if the FDA does start regulation, this will not cover "off-label" use of general-purpose AI. Very likely the FDA process will not address the safety concerns of specific local use-cases either. Therefore, new forms of oversight and validation are needed ([Panch et al., 2022](https://doi.org/10.1371/journal.pdig.0000040)). Topics of interest include uncertainty quantification, logging and monitoring for oversight, red teaming, and the design of "licensing" tests for medical AI.

# Completed projects

### Automated bone mineral density measurement

A measurement of bone mineral density (BMD) can be performed by placing an elliptical region of interest (ROI) in the trabecular space of the L1 vertebra. This is often a challenging task due to curvature of the spine (scoliosis, kyphosis, swayback) and the presence of vertebral anomalies. I developed an iterative-instance based approach for segmenting the entire spine using a 3D U-Net ([Elton et al., 2020](https://doi.org/10.1117/12.2551247)). The system produces very accurate segmentations of the entire spine and labels with an average error of 20 mm. I showed that a small improvement can be obtained by tilting the 3D ROI so it is perpendicular to the spinal cord. The system, which is written entirely in Python, is by some measures more accurate than the existing C++ code for BMD measurement previously developed in the lab at reproducing manual measurements (*r*² = 0.729 vs *r*² = 0.704).

### The effect of intravenous contrast on automated measurement tools

Completion of this project required accurate labeling of L1, L3, and L4 vertebrae on low-resolution (3–5 mm) contrast CT, which was challenging due to the lack of contrast CT training data and the inherent difficulty of partitioning vertebrae on low-resolution scans. I developed an approach which uses a watershed-based spine segmentation tool to extract a cropped box around the lumbar spine and a multiclass 3D U-Net to segment and label the 5 lumbar vertebrae and T12. After making improvements I ran existing codes for automated muscle, fat, and BMD measurement on 1,200 matched post-contrast and non-contrast scans. We showed that these tools yield accurate measurements on contrast CT if linear corrections are applied ([Perez et al., 2020](https://doi.org/10.1007/s00261-020-02755-5)). Looking forward, automated measurement in the hip may be more consistent than the vertebral technique for a variety of technical reasons.

### Automated plaque measurement

Relative to measuring plaque in the heart, little work has been done on automated measurement of plaque in the aorta and pelvic arteries. I developed a 3D U-Net based method for segmenting and quantifying aortic plaque ([Summers et al., 2020](https://doi.org/10.1016/j.acra.2020.08.022)). The method was trained with a novel loss function that counts false positive and false negative voxels. Unlike many prior works, the network was developed on a completely different dataset from the dataset it was tested on, yielding a true "external validation" of the method. On a set of 922 cases we found the method could accurately segment plaque and accurately measure the Agatston score for plaque severity (*r*² of 0.94 vs manual measurement), a major improvement over a mask-RCNN approach developed previously in the lab which suffered from a high rate of false positives. We used the CycleGAN and UNIT image translation models to generate synthetic non-contrast training data for this task, leading to a small but significant improvement ([Zhu et al., 2020a](https://arxiv.org/abs/2005.11384); [Zhu et al., 2020b](https://doi.org/10.1007/978-3-030-59713-9_37)).

### Liver fat and size quantification

I helped develop a deep learning model for liver segmentation and wrote code to measure the longest liver diameter on each transverse slice, reproducing a common manual measurement. On a set of 12,000 cases (≈ 9,000 patients) we showed that the average CT X-ray attenuation in the liver can be used to classify the severity of fatty liver disease, using a fat fraction measurement from an MRI proton density scan as a reference ([Pickhardt et al., 2020](https://doi.org/10.2214/ajr.20.24415)). We also showed that liver volume measurement is a much more accurate standard for diagnosing hepatomegaly than liver diameter measurement ([Perez et al., 2021](https://doi.org/10.1148/radiol.2021210531)).

### Relation of pancreas volume and radiomics features to type II diabetes

Utilizing an iterative active learning process to minimize the need for manual segmentation, I developed a pancreas segmentation model for non-contrast CT which achieves state-of-the-art for non-contrast CT (average Dice scores 0.77–0.80). The model has been run on a dataset of 9,200 patients, 2,536 of which have a diagnosis of type II diabetes. Our paper investigates how pancreas volume, surface irregularity (fractal dimension), texture, density, and fat fraction are predictive of diabetes diagnosis ([Tallam et al., 2022](https://doi.org/10.1148/radiol.211914)). Prior works on the subject used a maximum of 200 patients and most used fewer than 100 total. A future line of work is to replicate a recent paper suggesting that people with type II diabetes are more likely to have plaques in their splenic artery by using deep learning tools to automate measurements required for the study, thus enabling the study to be done on a much larger cohort ([Alexandre-Heymann et al., 2020](https://doi.org/10.1186/s12933-020-01098-1)).

### Automated lymph node detection in MRI

I created an enormous dataset containing 21,786 abdominal MRI studies for 9,343 patients with 27,918 line annotations which are linked to 11,039 doctor's reports. Natural language processing techniques were used to extract references to different types of lesions. As a first project we focused on extracting accurate references to lymph nodes ([Peng et al., 2020](https://aclanthology.org/2020.clinicalnlp-1.12)) and created a lymph node dataset which has been used for two deep learning projects so far. I helped develop registration methods to align bookmarks from T1 and DWI series onto T2 series since deep learning techniques perform best on T2 due to improved soft tissue contrast.

### Automated segmentation and analysis of liver Couinaud regions

I developed a two-stage 3D U-Net algorithm to segment the 8 Couinaud regions of the liver. We showed the ratio of liver segment volumes can be used as a biomarker for the classification of liver cirrhosis grade ([Lee et al., 2022](https://doi.org/10.1148/ryai.210268)). Getting a system with high enough accuracy on severe cirrhosis cases required additional manual segmentation using an active learning approach.

### Deployment and testing of AI tools in the radiology clinic

I worked with experts from Blackford Analysis along with Dr. Gregg Cohen to deploy AI tools from Dr. Summers' lab into the clinic at NIH. We deployed both my model for aortic plaque segmentation and the Multitask Universal Lesion Analysis Network (MULAN) ([Yan et al., 2019](https://doi.org/10.1007/978-3-030-32251-9_22)). At MGH I worked on deploying several AI projects from academic labs for extensive validation and testing which I was not at liberty to discuss. I also advised an academic team at MGH on AI system development and worked closely with researchers at NVIDIA to provide feedback on the Clara Deploy software stack, the Triton Inference Engine, and the Medical Open Network for AI (MONAI) library. We also deployed multiple tools that I helped develop which perform automated body composition analysis, as part of the Opportunistic Screening Consortium in Abdominal Radiology (OSCAR). Those tools were being run on 200,000 historical studies.

### Out-of-distribution detection and uncertainty quantification for medical AI safety

There have been several high-profile cases where medical AI systems that did well in the lab failed upon deployment, such as the system for diabetic retinopathy developed by Verily Life Sciences ([Beede et al., 2020](https://doi.org/10.1145/3313831.3376718)). The recent discovery of the double descent phenomenon in deep learning indicates that deep neural networks operate primarily through interpolation and local computations, so this lack of robustness to distributional shift is not surprising ([Elton, 2020](https://doi.org/10.1007/978-3-030-52152-3_10)). Thus, it is worthwhile to implement an additional output to AI systems which provides a warning if the system is likely to fail. The little prior work that has been done in this area is scattered through the literature, where it is variously described as "out-of-distribution detection", "outlier detection", and "applicability domain analysis". I trained two variational autoencoder models in this vein — one to detect incorrect organ segmentations and another to detect anomalous chest X-ray images. I have also worked on a conformal method for uncertainty quantification that can be used with binary classifiers ([Angelopoulos et al., 2024](https://doi.org/10.1101/2024.02.09.24302543)). Instead of outputting just two outputs ('yes', 'no') a third category of 'uncertain' is introduced. Using rigorous statistical methods, thresholds can be determined so the rate of false positives and false negatives is controlled.

# References

- Alexandre-Heymann, L., Barral, M., Dohan, A., and Larger, E. 2020. "Patients with Type 2 Diabetes Present with Multiple Anomalies of the Pancreatic Arterial Tree on Abdominal Computed Tomography." *Cardiovascular Diabetology* 19 (1). [https://doi.org/10.1186/s12933-020-01098-1](https://doi.org/10.1186/s12933-020-01098-1)

- Angelopoulos, A. N., Pomerantz, S., Do, S., Bates, S., Bridge, C. P., Elton, D. C., Lev, M. H., González, R. G., Jordan, M. I., and Malik, J. 2024. "Conformal Triage for Medical Imaging AI Deployment." [https://doi.org/10.1101/2024.02.09.24302543](https://doi.org/10.1101/2024.02.09.24302543)

- Antonopoulos, A. S., et al. 2017. "Detecting Human Coronary Inflammation by Imaging Perivascular Fat." *Science Translational Medicine* 9 (398). [https://doi.org/10.1126/scitranslmed.aal2658](https://doi.org/10.1126/scitranslmed.aal2658)

- Beede, E., et al. 2020. "A Human-Centered Evaluation of a Deep Learning System Deployed in Clinics for the Detection of Diabetic Retinopathy." In *Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems*. [https://doi.org/10.1145/3313831.3376718](https://doi.org/10.1145/3313831.3376718)

- Blankemeier, L., et al. 2024. "Merlin: A Vision Language Foundation Model for 3D Computed Tomography." [https://doi.org/10.48550/arXiv.2406.06512](https://doi.org/10.48550/arXiv.2406.06512)

- Bressem, K. K., et al. 2024. "medBERT.de: A Comprehensive German BERT Model for the Medical Domain." *Expert Systems with Applications* 237: 121598. [https://doi.org/10.1016/j.eswa.2023.121598](https://doi.org/10.1016/j.eswa.2023.121598)

- Chen, S., et al. 2024. "The Effect of Using a Large Language Model to Respond to Patient Messages." *The Lancet Digital Health* 6 (6): e379–81. [https://doi.org/10.1016/s2589-7500(24)00060-8](https://doi.org/10.1016/s2589-7500(24)00060-8)

- Dai, X., Yu, L., Lu, Z., Shen, C., Tao, X., and Zhang, J. 2020. "Serial Change of Perivascular Fat Attenuation Index After Statin Treatment." *International Journal of Cardiology* 319: 144–49. [https://doi.org/10.1016/j.ijcard.2020.06.008](https://doi.org/10.1016/j.ijcard.2020.06.008)

- Elton, D. C. 2020. "Self-Explaining AI as an Alternative to Interpretable AI." In *Artificial General Intelligence*, 95–106. [https://doi.org/10.1007/978-3-030-52152-3_10](https://doi.org/10.1007/978-3-030-52152-3_10)

- Elton, D. C., Chen, A., Pickhardt, P. J., and Summers, R. M. 2022. "Cardiovascular disease and all-cause mortality risk prediction from abdominal CT using deep learning." In *Medical Imaging 2022: Computer-Aided Diagnosis*. [https://doi.org/10.1117/12.2612620](https://doi.org/10.1117/12.2612620)

- Elton, D., Sandfort, V., Pickhardt, P. J., and Summers, R. M. 2020. "Accurately Identifying Vertebral Levels in Large Datasets." In *Medical Imaging 2020: Computer-Aided Diagnosis*. [https://doi.org/10.1117/12.2551247](https://doi.org/10.1117/12.2551247)

- Frattallone-Llado, G., et al. 2024. "Using Multimodal Data to Improve Precision of Inpatient Event Timelines." In *Lecture Notes in Computer Science*, 322–34. [https://doi.org/10.1007/978-981-97-2238-9_25](https://doi.org/10.1007/978-981-97-2238-9_25)

- Lee, S., Elton, D. C., Yang, A. H., Koh, C., Kleiner, D. E., Lubner, M. G., Pickhardt, P. J., and Summers, R. M. 2022. "Fully Automated and Explainable Liver Segmental Volume Ratio and Spleen Segmentation in CT for Diagnosing Cirrhosis." *Radiology: Artificial Intelligence* 4 (5): e210268. [https://doi.org/10.1148/ryai.210268](https://doi.org/10.1148/ryai.210268)

- Li, M., Blaes, A., Johnson, S., Liu, H., Xu, H., and Zhang, R. 2024. "CancerLLM: A Large Language Model in Cancer Domain." [https://arxiv.org/abs/2406.10459](https://arxiv.org/abs/2406.10459)

- Moor, M., et al. 2023. "Foundation Models for Generalist Medical Artificial Intelligence." *Nature* 616 (7956): 259–65. [https://doi.org/10.1038/s41586-023-05881-4](https://doi.org/10.1038/s41586-023-05881-4)

- Panch, T., et al. 2022. "A Distributed Approach to the Regulation of Clinical AI." *PLOS Digital Health* 1 (5): e0000040. [https://doi.org/10.1371/journal.pdig.0000040](https://doi.org/10.1371/journal.pdig.0000040)

- Peng, Y., et al. 2020. "Automatic Recognition of Lymph Nodes from Clinical Text." In *Proceedings of the 3rd Workshop on Clinical Natural Language Processing*. [https://aclanthology.org/2020.clinicalnlp-1.12](https://aclanthology.org/2020.clinicalnlp-1.12)

- Perez, A. A., et al. 2021. "Deep Learning CT-Based Quantitative Visualization Tool for Liver Volume Estimation: Defining Normal and Hepatomegaly." *Radiology*. [https://doi.org/10.1148/radiol.2021210531](https://doi.org/10.1148/radiol.2021210531)

- Perez, A. A., Pickhardt, P. J., Elton, D. C., Sandfort, V., and Summers, R. M. 2020. "Fully Automated CT Imaging Biomarkers of Bone, Muscle, and Fat: Correcting for the Effect of Intravenous Contrast." *Abdominal Radiology*. [https://doi.org/10.1007/s00261-020-02755-5](https://doi.org/10.1007/s00261-020-02755-5)

- Pickhardt, P. J., et al. 2020. "Liver Steatosis Categorization on Contrast-Enhanced CT Using a Fully-Automated Deep Learning Volumetric Segmentation Tool." *American Journal of Roentgenology*. [https://doi.org/10.2214/ajr.20.24415](https://doi.org/10.2214/ajr.20.24415)

- Pickhardt, P. J., Graffy, P. M., Perez, A. A., Lubner, M. G., Elton, D. C., and Summers, R. M. 2021. "Opportunistic Screening at Abdominal CT: Use of Automated Body Composition Biomarkers for Added Cardiometabolic Value." *RadioGraphics* 41 (2): 524–42. [https://doi.org/10.1148/rg.2021200056](https://doi.org/10.1148/rg.2021200056)

- Raghu, V. K., Weiss, J., Hoffmann, U., Aerts, H. J. W. L., and Lu, M. T. 2021. "Deep Learning to Estimate Biological Age from Chest Radiographs." *JACC: Cardiovascular Imaging*. [https://doi.org/10.1016/j.jcmg.2021.01.008](https://doi.org/10.1016/j.jcmg.2021.01.008)

- Rod, N. H., Lange, T., Andersen, I., Marott, J. L., and Diderichsen, F. 2012. "Additive Interaction in Survival Analysis: Use of the Additive Hazards Model." *Epidemiology* 23 (5): 733–37. [https://doi.org/10.1097/ede.0b013e31825fa218](https://doi.org/10.1097/ede.0b013e31825fa218)

- Sethi, A., et al. 2020. "Calcification of Abdominal Aorta Is a High Risk Underappreciated Cardiovascular Disease Factor in a General Population." *medRxiv*. [https://doi.org/10.1101/2020.05.07.20094706](https://doi.org/10.1101/2020.05.07.20094706)

- Summers, R. M., Elton, D. C., et al. 2020. "Atherosclerotic Plaque Burden on Abdominal CT: Automated Assessment with Deep Learning on Noncontrast and Contrast-Enhanced Scans." *Academic Radiology*. [https://doi.org/10.1016/j.acra.2020.08.022](https://doi.org/10.1016/j.acra.2020.08.022)

- Tallam, H., Elton, D. C., Lee, S., Wakim, P., Pickhardt, P. J., and Summers, R. M. 2022. "Fully Automated Abdominal CT Biomarkers for Type 2 Diabetes Using Deep Learning." *Radiology* 304 (1): 85–95. [https://doi.org/10.1148/radiol.211914](https://doi.org/10.1148/radiol.211914)

- Yan, K., et al. 2019. "MULAN: Multitask Universal Lesion Analysis Network for Joint Lesion Detection, Tagging, and Segmentation." In *MICCAI 2019*. [https://doi.org/10.1007/978-3-030-32251-9_22](https://doi.org/10.1007/978-3-030-32251-9_22)

- Zhou, H.-Y., Adithan, S., Acosta, J. N., Topol, E. J., and Rajpurkar, P. 2024. "A Generalist Learner for Multifaceted Medical Image Interpretation." [https://doi.org/10.48550/arXiv.2405.07988](https://doi.org/10.48550/arXiv.2405.07988)

- Zhu, Y., Elton, D. C., Lee, S., Pickhardt, P. J., and Summers, R. M. 2020. "Image Translation by Latent Union of Subspaces for Cross-Domain Plaque Detection." In *Proceedings of the 2020 Medical Imaging with Deep Learning (MIDL) Conference*. [https://arxiv.org/abs/2005.11384](https://arxiv.org/abs/2005.11384)

- Zhu, Y., Tang, Y., Tang, Y., Elton, D. C., Lee, S., Pickhardt, P. J., and Summers, R. M. 2020. "Cross-Domain Medical Image Translation by Shared Latent Gaussian Mixture Model." In *MICCAI 2020*, 379–89. [https://doi.org/10.1007/978-3-030-59713-9_37](https://doi.org/10.1007/978-3-030-59713-9_37)
