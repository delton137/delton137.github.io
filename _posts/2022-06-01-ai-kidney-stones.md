---
id: 311111
title: Notes on applications of AI to kidney stone disease
date: 2022-06-01
facebookcomments: true
author: Dan Elton
permalink: /2022/06/01/ai-kidney-stones/
layout: post
categories:
  - medical imaging
  - kidney stones
tags:
  - kidney stones
---


**Application \#1 -- Emergency room triage**

The prevalence of renal stone disease has been increasing so that people living in the United States have a lifetime risk of 15-20% (Hill, 2022), up from just \~4% in the 1960s. Most stones go undetected until pain emerges, which often leads sufferers to the emergency room. For patients suspected of having a urinary tract stone, CT scanning is the imaging method of choice because of its high sensitivity / specificity. The downsides of CT scanning are the radiation exposure and increased workload placed on radiologists. Anecdotal reports indicate that suspected kidney stones may consume \~10% or more of the radiologist workload, contributing to less time spent per case, fatigue, burnout, and higher error rates.

It may take a day or more before a radiologist reads the scan. If kidney stones are found, the scan may be sent to a urologist for further analysis, taking more time. However, in some hospitals a physician in the ER will look at the scan shortly after it is acquired and can easily tell if there are kidney stones and can start making diagnosis-specific treatment decisions then. The precise workflow and timings of things vary between hospitals and a survey would need to be done to get a better understanding of what is common here.

There are two applications of AI one may consider:

-   Replacing the radiologist completely, reducing radiologist workload so they can focus on more important tasks, preventing radiologist burnout, and reducing costs.

-   Triage (quick detection of severe situations like severe hydronephrosis which could cause injury to the patient if not treated in a timely fashion)

Regarding the first application, it appears very unlikely a radiologist reading the scan could be avoided because of liability concerns. The standard of care in the US is that a radiologist must read the entire scan and look for diseases beyond the clinical indication. Thus, hospitals can be held liable if things like tumors, etc that are visible in scans are not detected because standard of care wasn't followed. So, scans will need to be read eventually by a radiologist.

I asked Grace Sungwon Lee, a radiologist formerly at NIH, what she thought about emergency room triage applications. She said that the severity of a situation can already be gauged well by how much pain a patient is in (higher pain = higher priority). \["Pain" may sound subjective, but it can be gauged using a 10-point scale.\] Thus, she sees the value of this AI application for triage as very low. Additionally, she agreed that the scan would have to be read eventually, so there would be no cost savings or reduction in radiologist workload.\
\
Another radiologist said that obstruction is generally not that severe compared to other conditions common in an ER setting which would be higher targets for triage. Certainly untreated obstruction can lead to organ damage, but a 12 or 24 hour delay may not cause that big of a difference.

False positives in this situation could lead to annoyance, mis-allocation of critical resources, and to doctors turning off the AI, leading to loss of revenue. High sensitivity and specificity would be required for regulatory approval. Overall this does not seem to be a promising application for AI at this time.

\[Side note: a more promising direction for reducing radiologist workload might be improved decision-making around whether a CT scan is required in the first place. A [2012 study](https://www.birpublications.org/doi/full/10.1259/bjr/62994625) found that among patients with suspected kidney stones who received a CT scan, only 57.5% of men and 27.5% of women actually had a stone. Of course, some of these patients may have other conditions that are best diagnosed with CT, so this doesn't mean that eg \~70% of the CT scans for women were not a good idea or a waste of resources. The general point here is that improving decision making which diagnostic tests to order (CT scans, x-ray, blood tests) appears to be a general area where there is a lot of room for improvement.\]

**Application \#2 -- AI to improve treatment decision making**

Once stones are detected treatment decisions must be made. There are several different ways of treating kidney stones:

-   **Minimal treatment** - for very small stones, drugs may be given to manage pain with the expectation that the stones will pass on their own. The patient may be asked to drink lots of water and try to catch the stone in a sieve so its composition can be analyzed.

-   **Medications and/or diet changes** may be prescribed to attempt to dissolve the stones and increase the chance of spontaneous passage. (see AUA [treatment guidelines](https://www.auajournals.org/doi/full/10.1016/j.juro.2014.05.006))

    -   This is appropriate for smaller stones and uric acid stones, which can be dissolved by medications. Determination of whether a stone is uric acid may be performed via blood tests or dual energy CT. A rough determination of whether a stone is uric or not can also be made from a conventional CT scan.

-   **percutaneous nephrolithotomy** (PNL)

    -   This is a type of surgery that is expensive and carries some risk of complications. With staghorn stones, complications are common, occurring in 32-42% of patients.

-   **shock wave lithotripsy** (SWL)

    -   This involves focusing sound waves on the stone while the patient is under anesthetic. If successful, the stone will be broken into smaller pieces which will pass out of the body. SWL carries a lower risk of complications than PWL but fails in 5 -- 20% of cases (Massoud et. al. 2014). Thus, there is a lot of interest in predicting if SWL will be successful.

-   **Uretoscopy** (URS)

    -   Uretoscopy is done by inserting a catheter up the ureter. It is equipped with a laser to blast the stone or using a small grabber to grab the stone and may or not involve stent placement as well. How easy this is to do depends on the size of the stone and its location.

The *UpToDate* software, which is widely used in many hospitals in the US, provides [this flowchart](https://www.uptodate.com/contents/image/print?imageKey=NEPH%2F131581) to assist in deciding which type of treatment is most appropriate:

(this is a high-level overview, *UpToDate* provides many more details in a [long document](https://www.uptodate.com/contents/kidney-stones-in-adults-surgical-management-of-kidney-and-ureteral-stones/print). )

AI may be useful for improving decision making, leading to better outcomes, fewer patient visits, lower risk to patients, and cost savings for insurers.

There has already been much work in this area attempting to create flow charts like the one shown in *UpToDate*. For instance, many stone grading systems have been developed in the hope that the stone grade will be highly correlated with the risk of side effects in PNL or the success of SWL or lather ureteroscopy. Studies show these grading systems are only weakly predictive of whether there will be complications during surgery. A study that looked at three scoring systems found AUCs of 0.635, 0.678, and 0.743 for predicting the success of PNL for staghorn stones (Sfoungaristos et al. 2015).

A 2018 study by Cui et al. published in 2018 looked at 20 variables across N=607 cases that might be associated with the success of SWL. These variables included stone volume, mean HU, and entropy of the HU. Using these variables, a model was developed with an AUC of 0.63, which is considered poor predictive accuracy.

A further study (Cui et al., 2019) used several clinical variables and CT texture variables to fit a LASSO regression model (a modified form of linear regression). A random forest model did just slightly better (AUCs of 0.67 and 0.65 respectively). The study concluded that the CT texture featuers "did not increase the predictive ability of the model." They state "Our results suggest there is not enough current understanding of the important predictive factors for SWL efficacy to be able to produce a useful model to aid clinical decision making for which cases are most suitable for SWL treatment" In univariate analysis, the variables with the greatest predictive power were age and stone volume followed by major axis length. It makes sense that volume/diameter and HU have a strong positive correlation with how difficult it is for a stone to break. They obtained an AUC of 0.66 without the CTTA variables and 0.64 with the CCTA variables included.

Either volume or length are already commonly used in clinical decision making, thus the added value of adding additional variables via an AI system seem low. Other important variables are skin-to-surface distance and the maximum or average brightness of the stone. Again, these variables are relatively easy to measure and are already used. An AI tool could speed up the processing time here by populating the report with these measurements, however.

Thus, predicting whether complications will occur during surgery or whether shockwave lithotripsy will be successful appears to be very challenging.

**Application \#3 -- fast and easy volume measurement**

The superiority of volume measurements over linear measurements is a common theme in radiology. For instance, volume measurements are superior in determining stroke severity and [detecting abnormally large livers](https://pubs.rsna.org/doi/10.1148/radiol.2021210531). However, volume measurements are rarely done because they are much more time consuming. For measuring the volume of strokes, [Spectra has shown time savings with semi-automated volume measurement](https://medical.sectra.com/resources/time-savings-using-the-sectra-volume-measurement-tool/).

With volume measurement it is easier to tell if a stone is growing or shrinking. A 10% increase in diameter leads to a 33% increase in volume, which is easier to detect with noisy measurements. Whether a stone is growing or shrinking is very useful to know when determining if dietary and/or drug interventions are working.

There is a lot of work showing that volume measurement is superior to linear measurement.\
\
Selby et al note "On multivariate analysis, only total stone volume was an independent predictor of symptomatic events (HR, 1.35 per quartile; P = .01)"\
\
M. G. Selby et al. "[Quantification of Asymptomatic Kidney Stone Burden by Computed Tomography for Predicting Future Symptomatic Stone Events](https://www.goldjournal.net/article/S0090-4295(14)00964-9/fulltext)", *Urology* **85**, 45--50 (2015).

Other references to look into:\
\
Patel, Sutchin R.et al "[Automated Renal Stone Volume Measurement by Noncontrast Computerized Tomography Is More Reproducible Than Manual Linear Size Measurement](https://doi.org/10.1016/j.juro.2011.07.091)." *Journal of Urology* 186, no. 6 (December 2011): 2275--79.

Patel, Sutchin R., et al . "[Automated Volumetric Assessment by Noncontrast Computed Tomography in the Surveillance of Nephrolithiasis](https://doi.org/10.1016/j.urology.2012.03.009)." *Urology* 80, no. 1 (July 2012): 27--31.

Bandi G, Meiners RJ, Pickhardt PJ, Nakada SY. Stone measurement by volumetric three-dimensional computed tomography for predicting the outcome after extracorporeal shock wave litho-tripsy. *BJU Int.* 2009;103:524--528.

Vuruskan, Ediz, Okan Dilek, Kadir Karkin, Umut Unal, Lokman Ayhan, and Nevzat Can Sener. "Volume Should Be Used Instead of Diameter for Kidney Stones between 10 and 20 Mm to Determine the Type of Surgery and Increase Success." *Urolithiasis* 50, no. 2 (April 2022): 215--21. https://doi.org/10.1007/s00240-022-01305-6.

Yoshida S, Hayashi T, Ikeda J, et al. Role of volume and attenuation value histogram of urinary stone on noncontrast helical computed tomography as predictor of fragility by extracorporeal shock wave lithotripsy. *Urology.* 2006;68:33--37.

One paper disagrees that volume gives little added benefit over diameter for predicting passage:\
Patel, Parth M., et al "[Axial Diameter Is Superior to Volumetric Measurement in Predicting Ureteral Stone Passage.](https://doi.org/10.1097/UPJ.0000000000000242)" *Urology Practice* 8, no. 5 (September 2021): 571--75.

It seems clear both patients and radiologists would benefit from an easy-to-use tool that measured volume. (Whether they would use it is another story -- some education may be required as well.) However, it is worth noting that some radiologists already have access to an equivalent volume measuring tool, for instance tools in the Vitrea suite (Vital Images, Canon) exist for measuring plaque volume which are equally as useful for measuring kidney stone volume. Additionally, some PACS viewing software, such as Paxera, already have one click segmentation tools which come close to what is required.

In order to be adopted, volume measurement must be very low friction, ideally two clicks (one click on the tool and one click on the stone). Then, with a third click the volume measurement may be automatically entered into the report.

Volume measurement is technically very easy to do. It is very easy to write code so that a radiologist can click on a stone and it is segmented, using a region growing algorithm to segment out to a certain predefined threshold, like 100 HU. This algorithm can be tweaked to take into account the slice thickness and compensate somewhat for partial volume averaging effects.

The challenging part is seamlessly integrating the volume measurement tool into a PACS viewer and reporting software. This application is really something for the makers of PACS viewers to implement, in my opinion. A standalone application seems unlikely to succeed here.

**Application \#4 -- opportunistic detection of small stones that might otherwise be missed**

Radiologist sensitivity and specificity for detecting stones overall is quite high (\~97%). However, there is some evidence that radiologists sometimes miss tiny stones or decide not to report them.

Currently, most stones are not found until symptoms emerge. CT scans taken for other indications can result in pre-symptomatic stones being detected so medical management can begin earlier than it would otherwise.

An early detection of a small stone could alert a person that they are a "stone former" so they can start lifestyle interventions to prevent kidney stone pain later. Passing a kidney stone is consistently ranked as one of the most painful experiences that people experience during their life, with some arguing the degree of pain is significantly (ie 10x or 100x) higher than other more common painful experiences. Thus, preventing kidney stone pain should be viewed as greatly improving patient wellbeing. There are also cost savings for insurers.

There are several unknowns here:\
\-- how many tiny stones pass spontaneously with little or no symptoms?\
\-- how many tiny stones regress (dissolve) with little or no symptoms?\
\-- how many tiny stones grow and cause symptoms? Related: how to what degree are tiny stones predictive of future symptomatic stone disease?

Boyce el al. (20101) found that 7.8% of adult patients undergoing CT colonography had asymptomatic stones. Studies on the prevalence of asymptomatic kidney stones among potential renal donors find a similar number (Platt et al. 1997). The percentage of adult patients with asymptomatic stones is close to the lifestime risk for symptomatic kidney stones, suggesting a strong correlation between asymptomatic stones and developing symptoms later in life. However, Boyce et al. found that only 10% of patients with asymptomatic stones were later recorded as having symptoms over a follow-up interval that extended to a maximum of 10 years.

**Application \#5 -- determining uric vs non-uric acid stones**

(need to look into this more)

Zhang et al. 2017 look at how well uric acid vs non-uric acid stones can be identified with texture features.

Jendeberg et al. 2021 claim by using the HU density and a texture feature they can distinguish uric and non uric-acid stones with accuracy comparable to DECT.

Jendeberg, J. et al. "[Prediction of spontaneous ureteral stone passage: Automated 3D-measurements perform equal to radiologists, and linear measurements equal to volumetric](https://link.springer.com/article/10.1007/s00330-017-5242-9)", *European Radiology* **28**, 2474--2483 (2018).

Zhang, G.-M.-Y., et al. "[Uric acid versus non-uric acid urinary stones: differentiation with single energy CT texture analysis".](https://www.clinicalradiologyonline.net/article/S0009-9260(18)30169-7/fulltext) *Clinical Radiology*. **73**(9), 792-799. 2018

**Notes on StoneChecker**

**[StoneChecker](https://www.imagingbiometrics.com/what-we-offer/product-services/ib-stonechecker/)** is an FDA approved image analysis tool offered by Imaging Biometrics LLC. StoneChecker uses the [TexRAD software package](http://www.texrad.com/) sold by Feedback PLC to compute CT based texture analysis ("CCTA") features. For FDA approval, reports online say that "use validation" was done at two clinical sites in Oxford, UK and Beijing, China.

A demo of the tool is available online. The tool has many severe shortcomings which make it unlikely to be very useful in real-world settings.

Several studies on the utility of the measurements done by this product have been published. On *Imaging Biometrics*' website, they identify three "key StoneChecker publications". These papers are a biased sample from the academic literature, since they don't mention Cui et al (2019) which found the StoneChecker texture features were not useful. The first paper (Cui et al, 2017) analyzed seven stones of varying composition (3 uric acid, 2 calcium oxalate, and 2 cystine) ex-vivo. They measured the number of acoustic shocks required to fragment each stone and found that stone volume, average stone HU, and the entropy of the stone HU were all positively correlated with the number of shocks required to a statistically significant degree (note: after correcting for multiple comparisons the significance goes away.)

**References**

Boyce, Cody J., Perry J. Pickhardt, Edward M. Lawrence, David H. Kim, and Richard J. Bruce. "[Prevalence of Urolithiasis in Asymptomatic Adults: Objective Determination Using Low Dose Noncontrast Computerized Tomography.](https://doi.org/10.1016/j.juro.2009.11.047)" *Journal of Urology* **183**, *3* 1017--21, 2010.

Cui, Helen W., et al. "[Predicting Shockwave Lithotripsy Outcome for Urolithiasis Using Clinical and Stone Computed Tomography Texture Analysis Variables](https://www.nature.com/articles/s41598-019-51026-x)." *Scientific Reports*, **9**, no. 1, p. 14674. 2019.

Cui, H. W. et al. "[PD08-04 WHICH STONES WILL FAIL SHOCKWAVE LITHOTRIPSY TREATMENT? ANALYSIS OF PATIENT AND STONE FACTORS IN A PREDICTIVE MODEL](https://www.auajournals.org/doi/10.1016/j.juro.2018.02.450)." *Journal of Urology (Supplement)*, **199**, no. 4S, 2018.

Cui, H. W. et al. "[CT Texture Analysis of Ex Vivo Renal Stones Predicts Ease of Fragmentation with Shockwave Lithotripsy](https://www.liebertpub.com/doi/10.1089/end.2017.0084)". *Journal of Endourology*, 31(7), 694--700. 2017.

Hill, Alexander J., et al. "[Incidence of Kidney Stones in the United States: The Continuous National Health and Nutrition Examination Survey](https://doi.org/10.1097/JU.0000000000002331)." *Journal of Urology*, **207** (4), Apr. 2022, pp. 851--56. This papers study used 2007-2010 NHANES data and estimated that "19% of men and 9% of women will be diagnosed with a kidney stone by the age of 70".

Jendeberg, J. et al. "[Single-Energy CT Predicts Uric Acid Stones with Accuracy Comparable to Dual-Energy CT---Prospective Validation of a Quantitative Method.](https://link.springer.com/article/10.1007/s00330-021-07713-3)" *European Radiology* **31**, no. 8 : 5980--89. (2021)

Massoud, A. M. et al. "[The success of extracorporeal shock-wave lithotripsy based on the stone-attenuation value from non-contrast computed tomography](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4434685)." *Arab journal of urology* vol. **12**,2 (2014)

Patel, Sutchin R., et al. "[Automated Renal Stone Volume Measurement by Noncontrast Computerized Tomography Is More Reproducible Than Manual Linear Size Measurement.](https://www.auajournals.org/doi/10.1016/j.juro.2012.03.015)" *Journal of Urology* **186**, (6) 2275--79 (2011)

Platt, J F, J H Ellis, M Korobkin, and K Reige. "[Helical CT Evaluation of Potential Kidney Donors: Findings in 154 Subjects](https://doi.org/10.2214/ajr.169.5.9353451)." *American Journal of Roentgenology* 169, no. 5 (November 1997): 1325--30.

R. P. Reimer, J. Salem, M. Merkt, K. Sonnabend, S. Lennartz, D. Zopfs, A. Heidenreich, D. Maintz, S. Haneder, and N. G. Hokamp, Size and volume of kidney stones in computed tomography: Influence of acquisition techniques and image reconstruction parameters, European Journal of Radiology **132**, 109267 (2020).

R. J. Kampa, K. R. Ghani, S. Wahed, U. Patel, and K. M. Anson, Size Matters: A Survey of How Urinary-Tract Stones are Measured in the UK, Journal of Endourology 19, 856--860 (2005).

S. Lai, B. "Comparing different kidney stone scoring systems for predicting percutaneous nephrolithotomy outcomes: A multicenter retrospective cohort study", *International Journal of Surgery* **81**, 55--60 (2020).

Sfoungaristos, S., Gofrit, et al. "Percutaneous nephrolithotomy for staghorn stones: Which nomogram can better predict postoperative outcomes?" *World Journal of Urology*, **34**(8), 1163--1168. (2015).
