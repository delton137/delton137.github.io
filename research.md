# Opportunistic screening with CT scans

Roughly 100 million CT scans are performed in the United States each year, and that number is growing by several percent each year. Due to time and resource constraints much potentially useful information in CT scans is currently not utilized. Fully automated AI tools can run in the background, segmenting organs and looking for abdormalities. Segmentation tools can be used to extract biomarkers which can be used for disease risk prediction. We call this paradigm "opportunistic screening". 

I have developed systems which perform automated measurements of bone mineral density (BMD) [@Elton2020], muscle area and density [@Perez2020], visceral fat [@Perez2020], liver fat [@Pickhardt2020], aortic plaque
burden [@Summers2020plaque], and pancreatic fat.[@Tallam2022Pancreas] Conditions we have considered for early detection using CT biomarkers include osteoporosis, sarcopenia, myosteatosis, liver steatosis,
diabetes, pancreatic cancer, and cardiovascular disease.

Recently I published a paper demonstrating the first deep learning based system for opportunistic cardiovascular disease risk prediction using abdominal CT [@Elton2021SPIE]. The combination of genetic factors with imaging biomarkers can also improve risk prediction and lead to the discovery of new phenotypic correlations [@Sethi2020].  

I am also interested in exploring different ways of presenting risk data to patients such as plotting patient-specific survival curves. Previous work has suggested that the way risk information is presented by a clinician to patients has an effect on how receptive they are to taking steps to proactively reduce risk. For instance, comparing with a baseline helps patients understand their relative risk (ie you are at
40% higher risk for CVD in the next 5 years compared to males of your age). The concepts of "arterial age" and "biological age" may help inform patients about their health [@Raghu2021].

# Current and future work

### Opportunistic screening {#opportunistic-screening .unnumbered}

We are curently running a biomarkers suite on 200,000 studies at Mass General Brigam as part of the Opportunistic Screening Consortium for Abdominal Radiology (OSCAR). The results generated will be used to
generate reference \"nomograms\" for different biomarkers, allowing clinicians to see how a patient compares to others in their age and gender cohort.

There are several paths forward for improving my CT-based risk prediction models such as implementing multitask learning and additive hazard modeling to output multiple follow-up intervals.[@Rod2012] I am
also interested in studying associations between genes and imaging biomarkers, which could lead to the discovery of new genes that are associated with disease risk. [@Sethi2020].

### Development of a multimodal model for chest CT report generation 

Presently we are seeing a radical change in how AI is applied in the
healthcare domain. This is the shift from single-purpose bespoke machine
learning models to general-purpose foundation models like GPT-4. Dozens
of applications of large language models (LLMs) have already been
explored. For instance, helping triage and respond to to patient portal
messages,[@Chen2024] constructing patient
timelines,[@FrattalloneLlado2024] drafting radiology reports, assisting
clinicians search through video, and transcribing ambient audio to visit
notes.[@Moor2023]

I am currently pursing two research projects along these lines. The
first is the development of a multimodal model for chest CT. Currently,
radiologists who specialize in the chest at our institution spend about
50% of their time detecting and characterizing small nodules, often
characterizing the same nodule on many follow-up scans. It is hoped that
a multimodal model may help speed this process along. We are currently
exploring the open-source LLaVa-Next model and drawing inspiration from
the Merlin CT mulitmodal foundation model developed at
Stanford.[@blankemeier_merlin2024]

### Perivascular fat attentuation to improve CVD risk prediction {#perivascular-fat-attentuation-to-improve-cvd-risk-prediction .unnumbered}

The first stage of atherosclerosis involves inflammation of the arterial
walls, which cannot be directly observed in CT
scans.[@Antonopoulos2017; @Dai2020] However, inflammation inhibits
adipogenesis, leading to small increases in the X-ray attenuation of
visceral adipose tissue around the affected arteries. Recent work shows
that measuring the attenuation of perivascular fat around coronary
arteries enhances cardiac risk prediction and may serve as a valuable
early-stage biomarker to identify patients at risk for plaque formation
and cardiovascular disease. Such patients can be put on statins or other
drugs to reduce the inflammation which may \"nip atherosclerosis in the
bud\". Whereas many studies have looked at the measurement of
perivascular fat attenuation in cardiac CT, there are few studies
exploring the use of deep learning to automate such measurements and no
studies so far which have explored opportunistic measurement of
periaortic visceral fat attenuation in abdominal CT.

### New methods for validating general-purpose medical AI 

Already many people are using LLMs like Anthropic and Claude to help
with medical questions. Several powerful open source models have
appeared as well, such as medBERT.de (2024),[@Bressem2024] MedVersa
(2024),[@Zhou2024MedVersa], CancerLLM,[@Li2024] and OpenBioLLM. The FDA
still has not released guidance on how it will regulate general-purpose
medical AI ("AI doctors"). Furthermore, even if the FDA does start
regulation, this will not cover "off-label" use of general purpose AI.
Very likely the FDA process will not address the safety concerns of
specific local use-cases as well. Therefore, new forms of oversight and
validation are needed.[@Panch2022-cd] Topics of interest include
uncertainty quantification, logging and monitoring for oversight, red
teaming, and the design of 'licensing' tests for medical AI.

# Completed projects {#completed-projects .unnumbered}

### Automated bone mineral density measurement {#automated-bone-mineral-density-measurement .unnumbered}

:::: wrapfigure
r0.14

::: center
![image](vert_ex.png){width="12%"}\
Example spine segmentation.
:::
::::

A measurement of bone mineral density (BMD) can be performed by placing
an elliptical region of interest (ROI) in the trabecular space of the L1
vertebra. This is often a challenging task due to curvature of the spine
(scoliosis, kyphosis, swayback) and the presence of vertebral anomalies.
I developed an iterative-instance based approach for segmenting the
entire spine using a 3D U-Net  [@Elton2020]. The system produces very
accurate segmentations of the entire spine and labels with an average
error of 20 mm. I showed that a small improvement can be obtained by
tilting the 3D ROI so it is perpendicular to the spinal cord. The
system, which is written entirely in Python, is by some measures more
accurate than the existing C++ code for BMD measurement previously
developed in the lab at reproducing manual measurements ($r^2 = 0.729$
vs $r^2 = 0.704$).

### The effect of intravenous contrast on automated measurement tools {#the-effect-of-intravenous-contrast-on-automated-measurement-tools .unnumbered}

Completion of this project required accurately labeling of L1, L3, and
L4 vertebrae on low resolution (3-5mm) contrast CT which was challenging
due to the lack of contrast CT training data and the inherent difficulty
of partitioning vertebrae on low resolution scans. I developed an
approach which uses watershed based spine segmentation tool to extract a
cropped box around the lumbar spine and a multiclass 3D U-Net to segment
and label the 5 lumbar vertebrae and T12. After making improvements I
ran existing codes for automated muscle, fat, and BMD measurement on
1,200 matched post-contrast and non-contrast scans. We showed that these
tools yield accurate measurements on contrast CT if linear corrections
are applied [@Perez2020]. Looking forward, automated measurement in the
hip may be more consistent than the vertebral technique for a variety of
technical reasons.

### Automated plaque measurement {#automated-plaque-measurement .unnumbered}

:::: wrapfigure
r0.25

::: center
![image](aortic_plaque_example.png){width="24%"}\
Example aortic plaque segmentation.
:::
::::

Relative to measuring plaque in the heart, little work has been done on
automated measurement of plaque in the aorta and pelvic arteries. I
developed 3D U-Net based method for segmenting and quantifying aortic
plaque [@Summers2020plaque]. The method was trained with a novel loss
function that counts false positive and false negative voxels. Unlike
many prior works, the network was developed on a completely different
dataset from the dataset it was tested on, yielding a true "external
validation" of the method. On a set of 922 cases we found the method
could accurately segment plaque and accurately measure the Agatston
score for plaque severity ($r^2$ of 0.94 vs manual
measurement) [@Summers2020plaque], a major improvement over a mask-RCNN
approach developed previously the lab which suffered from a high rate of
false positives. We used the CycleGAN and UNIT image translation models
to generate synthetic non-contrast training data for this task, leading
to a small but significant improvement [@Zhu2020MICCAI; @Zhu2020MIDL].

### Liver fat and size quantification {#liver-fat-and-size-quantification .unnumbered}

I helped develop a deep learning model for liver segmentation and wrote
code to measure the longest liver diameter on each transverse slice,
reproducing a common manual measurement. On a set of 12,000 cases
($\approx$ 9,000 patients) we showed that the average CT X-ray
attenuation in the liver can be used to classify the severity of fatty
liver disease, using a fat fraction measurement from a MRI proton
density scan as a reference [@Pickhardt2020]. We also showed that liver
volume measurement is a much more accurate standard for diagnosing
hepatomegaly than liver diameter measurement [@2021].

### Relation of pancreas volume and radiomics features to type II diabetes {#relation-of-pancreas-volume-and-radiomics-features-to-type-ii-diabetes .unnumbered}

:::: wrapfigure
r0.3

::: center
![image](pancreas_example.png){width="28%"}\
Example pancreas segmentation. A 2 mm surface erosion is shown in light
red.
:::
::::

Utilizing an iterative active learning process to minimize the need for
manual segmentation I developed a pancreas segmentation model for
non-contrast CT which achieves state-of-the art for non-contrast CT
(average Dice scores $0.77-0.80$). The model has been run on a dataset
of 9,200 patients, 2,536 of which have a diagnosis of type II diabetes.
Our paper investigates how pancreas volume, surface irregularity
(fractal dimension), texture, density, and fat fraction are predictive
of diabetes diagnosis.[@Tallam2022Pancreas] Prior works on the subject
used a maximum of 200 patients and most used $<100$ total. A future line
of work is to replicate a recent paper suggesting that people with type
II diabetes are more likely to have plaques in their splenic artery by
using deep learning tools to automate measurements required for the
study, thus enabling the study to be done on a much larger
cohort [@AlexandreHeymann2020].

### Automated lymph node detection in MRI {#automated-lymph-node-detection-in-mri .unnumbered}

I created an enormous dataset containing 21,786 abdominal MRI studies
for 9,343 patients with 27,918 line annotations which are linked to
11,039 doctor's reports. Natural language processing techniques were
used to extract references to different types of lesions. As a first
project we focused on extracting accurate references to lymph
nodes [@Peng2020] and created a lymph node dataset which has been used
for two deep learning projects so far. I helped develop registration
methods to align bookmarks from T1 and DWI series onto T2 series since
deep learning techniques perform best on T2 due to improved soft tissue
contrast.

### Automated segmentation and analysis of liver Couinaud regions  {#automated-segmentation-and-analysis-of-liver-couinaud-regions .unnumbered}

I have developed a two-stage 3D U-Net algorithm to segment the 8
Couinaud regions of the liver. We have shown the ratio of liver segment
volumes can be used as a biomarker for the classification of liver
cirrhosis grade using this system (work under review). We found that
getting a system with high enough accuracy on severe cirrhosis cases
required additional manual segmentation using an active learning
approach.[@Lee2022]

### Deployment and testing of AI tools in the radiology clinic {#deployment-and-testing-of-ai-tools-in-the-radiology-clinic .unnumbered}

I worked with experts from Blackford Analysis along with Dr. Gregg Cohen
to deploy AI tools from Dr. Summer's lab into the clinic at NIH. We
deployed both my model for aortic plaque segmentation and the Multitask
Universal Lesion Analysis Network (MULAN) [@Ke2019MULAN]. At MGH I have
worked on deploying several AI projects from academic labs for extensive
validation and testing which I am not yet at liberty to discuss. I also
advised an academic team at MGH on AI system development and worked
closely with researchers at NVIDIA to provide feedback on the Clara
Deploy software stack, the Triton Inference Engine, and the Medical Open
Network for AI (MONAI) library. More recently we have deployed multiple
tools that I helped develop which perform automated body composition
analysis, as part of the Opportunistic Screening Consortium in Abdominal
Radiology (OSCAR). We are in the process of running those tools on
200,000 historical studies.

### Out-of-distribution detection and uncertainty quantification for medical AI safety {#out-of-distribution-detection-and-uncertainty-quantification-for-medical-ai-safety .unnumbered}

There have been several high-profile cases where medical AI systems that
did well in the lab failed upon deployment, such as the system for
diabetic retinopathy developed by Verily Life Sciences [@Beede2020]. The
recent discovery of the double descent phenomena in deep learning
indicates that deep neural networks operate primarily through
interpolation and local computations, so this lack of robustness to
distributional shift is not surprising  [@Elton2020AGI]. Thus, it is
worthwhile to implement an additional output to AI systems which
provides a warning if the system is likely to fail. The little prior
work that has been done in this area is scattered through the
literature, where it is variously described as "out-of-distribution
detection", "outlier detection", and "applicability domain analysis". I
trained two variational autoencoder models in this vein - one to detect
incorrect organ segmentations and another to detect anomalous chest
X-ray images. I have also worked on a conformal method for uncertainty
quantification that can be used with binary
classifiers.[@Angelopoulos2024] Instead of outputting just two outputs
('yes', 'no') a third category of 'uncertain' is introduced. Using
rigorous statistical methods, thresholds can be determined so the rate
of false positives and false negatives is controlled.


Alexandre-Heymann, Laure, Matthias Barral, Anthony Dohan, and Etienne
Larger. 2020. “Patients with Type 2 Diabetes Present with Multiple
Anomalies of the Pancreatic Arterial Tree on Abdominal Computed
Tomography: Comparison Between Patients with Type 2 Diabetes and a
Matched Control Group.” *Cardiovascular Diabetology* 19 (1).
<https://doi.org/10.1186/s12933-020-01098-1>.

Angelopoulos, Anastasios N., Stuart Pomerantz, Synho Do, Stephen Bates,
Christopher P. Bridge, Daniel C. Elton, Michael H. Lev, R. Gilberto
González, Michael I. Jordan, and Jitendra Malik. 2024. “Conformal Triage
for Medical Imaging AI Deployment,” February.
<https://doi.org/10.1101/2024.02.09.24302543>.

Antonopoulos, Alexios S., Fabio Sanna, Nikant Sabharwal, Sheena Thomas,
Evangelos K. Oikonomou, Laura Herdman, Marios Margaritis, et al. 2017.
“Detecting Human Coronary Inflammation by Imaging Perivascular Fat.”
*Science Translational Medicine* 9 (398).
<https://doi.org/10.1126/scitranslmed.aal2658>.

Beede, Emma, Elizabeth Baylor, Fred Hersch, Anna Iurchenko, Lauren
Wilcox, Paisan Ruamviboonsuk, and Laura M. Vardoulakis. 2020. “A
Human-Centered Evaluation of a Deep Learning System Deployed in Clinics
for the Detection of Diabetic Retinopathy.” In *Proceedings of the 2020
CHI Conference on Human Factors in Computing Systems*. ACM.
<https://doi.org/10.1145/3313831.3376718>.

Blankemeier, Louis, Joseph Paul Cohen, Ashwin Kumar, Dave Van Veen, Syed
Jamal Safdar Gardezi, Magdalini Paschali, Zhihong Chen, et al. 2024.
“Merlin: A Vision Language Foundation Model for 3D Computed Tomography.”
<https://doi.org/10.48550/ARXIV.2406.06512>.

Bressem, Keno K., Jens-Michalis Papaioannou, Paul Grundmann, Florian
Borchert, Lisa C. Adams, Leonhard Liu, Felix Busch, et al. 2024.
“<span class="nocase">medBERT.de</span>: A Comprehensive German BERT
Model for the Medical Domain.” *Expert Systems with Applications* 237
(March): 121598. <https://doi.org/10.1016/j.eswa.2023.121598>.

Chen, Shan, Marco Guevara, Shalini Moningi, Frank Hoebers, Hesham
Elhalawani, Benjamin H Kann, Fallon E Chipidza, et al. 2024. “The Effect
of Using a Large Language Model to Respond to Patient Messages.” *The
Lancet Digital Health* 6 (6): e379–81.
<https://doi.org/10.1016/s2589-7500(24)00060-8>.

Dai, Xu, Lihua Yu, Zhigang Lu, Chengxing Shen, Xinwei Tao, and Jiayin
Zhang. 2020. “Serial Change of Perivascular Fat Attenuation Index After
Statin Treatment: Insights from a Coronary CT Angiography Follow-up
Study.” *International Journal of Cardiology* 319 (November): 144–49.
<https://doi.org/10.1016/j.ijcard.2020.06.008>.

Elton, Daniel C. 2020. “Self-Explaining AI as an Alternative to
Interpretable AI.” In *Artificial General Intelligence*, 95–106.
Springer International Publishing.
<https://doi.org/10.1007/978-3-030-52152-3_10>.

Elton, Daniel C., Andy Chen, Perry J. Pickhardt, and Ronald M. Summers.
2022. “<span class="nocase">Cardiovascular disease and all-cause
mortality risk prediction from abdominal CT using deep learning</span>.”
In *Medical Imaging 2022: Computer-Aided Diagnosis*, edited by Karen
Drukker and Khan M. Iftekharuddin, 12033:120332N. International Society
for Optics; Photonics; SPIE. <https://doi.org/10.1117/12.2612620>.

Elton, Daniel, Veit Sandfort, Perry J. Pickhardt, and Ronald M. Summers.
2020. “Accurately Identifying Vertebral Levels in Large Datasets.” In
*Medical Imaging 2020: Computer-Aided Diagnosis*, edited by Horst K.
Hahn and Maciej A. Mazurowski. SPIE.
<https://doi.org/10.1117/12.2551247>.

Frattallone-Llado, Gabriel, Juyong Kim, Cheng Cheng, Diego Salazar,
Smitha Edakalavan, and Jeremy C. Weiss. 2024. “Using Multimodal Data to
Improve Precision of Inpatient Event Timelines.” In *Lecture Notes in
Computer Science*, 322–34. Springer Nature Singapore.
<https://doi.org/10.1007/978-981-97-2238-9_25>.

Lee, Sungwon, Daniel C. Elton, Alexander H. Yang, Christopher Koh, David
E. Kleiner, Meghan G. Lubner, Perry J. Pickhardt, and Ronald M. Summers.
2022. “Fully Automated and Explainable Liver Segmental Volume Ratio and
Spleen Segmentation in CT for Diagnosing Cirrhosis.” *Radiology:
Artificial Intelligence* 4 (5): e210268.
<https://doi.org/10.1148/ryai.210268>.

Li, Mingchen, Anne Blaes, Steven Johnson, Hongfang Liu, Hua Xu, and Rui
Zhang. 2024. “CancerLLM: A Large Language Model in Cancer Domain.”
arXiv. <https://arxiv.org/abs/2406.10459>.

Moor, Michael, Oishi Banerjee, Zahra Shakeri Hossein Abad, Harlan M.
Krumholz, Jure Leskovec, Eric J. Topol, and Pranav Rajpurkar. 2023.
“Foundation Models for Generalist Medical Artificial Intelligence.”
*Nature* 616 (7956): 259–65.
<https://doi.org/10.1038/s41586-023-05881-4>.

Panch, Trishan, Erin Duralde, Heather Mattie, Gopal Kotecha, Leo Anthony
Celi, Melanie Wright, and Felix Greaves. 2022. “A Distributed Approach
to the Regulation of Clinical AI.” *PLOS Digit. Health* 1 (5): e0000040.

Peng, Y., S. Lee, D. C. Elton, T. Shen, Y. Tang, Q. Chen, S. Wang, Y.
Zhu, R. M. Summers, and Z. Lu. 2020. “Automatic Recognition of Lymph
Nodes from Clinical Text.” In *Proceedings of the 3rd Workshop on
Clinical Natural Language Processing*.

Perez, Alberto A., Victoria Noe-Kim, Meghan G. Lubner, Peter M. Graffy,
John W. Garrett, Daniel C. Elton, Ronald M. Summers, and Perry J.
Pickhardt. 2021. “Deep Learning CT-Based Quantitative Visualization Tool
for Liver Volume Estimation: Defining Normal and Hepatomegaly.”
*Radiology*, October. <https://doi.org/10.1148/radiol.2021210531>.

Perez, Alberto A., Perry J. Pickhardt, Daniel C. Elton, Veit Sandfort,
and Ronald M. Summers. 2020. “Fully Automated CT Imaging Biomarkers of
Bone, Muscle, and Fat: Correcting for the Effect of Intravenous
Contrast.” *Abdominal Radiology*, September.
<https://doi.org/10.1007/s00261-020-02755-5>.

Pickhardt, Perry J., Glen M. Blake, Peter M. Graffy, Veit Sandfort,
Daniel C. Elton, Alberto A. Perez, and Ronald M. Summers. 2020. “Liver
Steatosis Categorization on Contrast-Enhanced CT Using a Fully-Automated
Deep Learning Volumetric Segmentation Tool: Evaluation in 1, 204 Heathy
Adults Using Unenhanced CT as Reference Standard.” *American Journal of
Roentgenology*, September. <https://doi.org/10.2214/ajr.20.24415>.

Pickhardt, Perry J., Peter M. Graffy, Alberto A. Perez, Meghan G.
Lubner, Daniel C. Elton, and Ronald M. Summers. 2021. “Opportunistic
Screening at Abdominal CT: Use of Automated Body Composition Biomarkers
for Added Cardiometabolic Value.” *RadioGraphics* 41 (2): 524–42.
<https://doi.org/10.1148/rg.2021200056>.

Raghu, Vineet K., Jakob Weiss, Udo Hoffmann, Hugo J. W. L. Aerts, and
Michael T. Lu. 2021. “Deep Learning to Estimate Biological Age from
Chest Radiographs.” *JACC: Cardiovascular Imaging*, March.
<https://doi.org/10.1016/j.jcmg.2021.01.008>.

Rod, Naja Hulvej, Theis Lange, Ingelise Andersen, Jacob Louis Marott,
and Finn Diderichsen. 2012. “Additive Interaction in Survival Analysis:
Use of the Additive Hazards Model.” *Epidemiology* 23 (5): 733–37.
<https://doi.org/10.1097/ede.0b013e31825fa218>.

Sethi, Anurag, Leland Taylor, J Graham Ruby, Jagadish Venkataraman,
Elena Sorokin, Madeleine Cule, and Eugene Melamud. 2020. “Calcification
of Abdominal Aorta Is a High Risk Underappreciated Cardiovascular
Disease Factor in a General Population.” *medRxiv*.
<https://doi.org/10.1101/2020.05.07.20094706>.

Summers, Ronald M., Daniel C. Elton, Sungwon Lee, Yingying Zhu, Jiamin
Liu, Mohammedhadi Bagheri, Veit Sandfort, et al. 2020. “Atherosclerotic
Plaque Burden on Abdominal CT: Automated Assessment with Deep Learning
on Noncontrast and Contrast-Enhanced Scans.” *Academic Radiology*,
September. <https://doi.org/10.1016/j.acra.2020.08.022>.

Tallam, Hima, Daniel C. Elton, Sungwon Lee, Paul Wakim, Perry J.
Pickhardt, and Ronald M. Summers. 2022. “Fully Automated Abdominal CT
Biomarkers for Type 2 Diabetes Using Deep Learning.” *Radiology* 304
(1): 85–95. <https://doi.org/10.1148/radiol.211914>.

Yan, Ke, Youbao Tang, Yifan Peng, Veit Sandfort, Mohammadhadi Bagheri,
Zhiyong Lu, and Ronald M. Summers. 2019. “MULAN: Multitask Universal
Lesion Analysis Network for Joint Lesion Detection, Tagging, and
Segmentation.” In *Medical Image Computing and Computer Assisted
Intervention - MICCAI 2019 - 22nd International Conference, Shenzhen,
China, October 13-17, 2019, Proceedings, Part VI*, edited by Dinggang
Shen, Tianming Liu, Terry M. Peters, Lawrence H. Staib, Caroline Essert,
Sean Zhou, Pew-Thian Yap, and Ali R. Khan, 11769:194–202. Lecture Notes
in Computer Science. Springer.

Zhou, Hong-Yu, Subathra Adithan, Julián Nicolás Acosta, Eric J. Topol,
and Pranav Rajpurkar. 2024. “A Generalist Learner for Multifaceted
Medical Image Interpretation.” arXiv.
<https://doi.org/10.48550/ARXIV.2405.07988>.

Zhu, Yingying, Daniel C. Elton, Sungwon Lee, Perry J. Pickhardt, and
Ronald M. Summers. 2020. “Image Translation by Latent Union of Subspaces
for Cross-Domain Plaque Detection.” In *Proceedings of the 2020 Medical
Imaging with Deep Learning (MIDL) Conference*.

Zhu, Yingying, Youbao Tang, Yuxing Tang, Daniel C. Elton, Sungwon Lee,
Perry J. Pickhardt, and Ronald M. Summers. 2020. “Cross-Domain Medical
Image Translation by Shared Latent Gaussian Mixture Model.” In *Medical
Image Computing and Computer Assisted Intervention MICCAI 2020*, 379–89.
Springer International Publishing.
<https://doi.org/10.1007/978-3-030-59713-9_37>.