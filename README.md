# Computational quantification of palmar hyperlinearity and prediction of filaggrin mutation status from palmar images  

## About

Palmar hyperlinearity is associated with the presence of a loss-of-function mutation in the filaggrin gene (FLG). Loss-of-function mutations in FLG are the strongest genetic risk factor for atopic dermatitis (AD).  Determining palmar hyperlinearity status may thus be useful in clinic and in cohort studies of AD. We created a simple tool to quantify palmar hyperlinearity to overcome current issues where: studies use different definitions of palmar hyperlinearity, there is inter-observer variation, and classifying many images can be time consuming.


### Running Locally

The code is applied to directories of images, separated by filaggrin mutation status. The paths can be changed to calculate hyperlinearity scores for given images, with results output in a csv file.

### Explanation of files
hyperlinearity_scores_plus_external_ls.ipynb : part 1 extracts thenar hyperlinearity and palmar hyperlinearity scores for directories of images. For individual images, the section entitled (Fig S5) can be used - change the file names to your file and hyperlinearity scores will be generated.
\\

Supplementary Figures S1-6.docx : supplementary files for research paper 
Supplementary Tables S1-3.docx : supplementary tables for research paper 
age_analysis_fig_s4_ls.ipynb : notebook for analysis in research paper looking at differences in hyperlinearity by age group
fig_s3_cliical_computational_comparison.ipynb: notebook for generating figure S3 in research paper
predict_flg_status_ls.ipynb: notebook for predicting filaggrin status from images from research paper
utils_flg4.py: utils

### Project Data
 531 individuals with atopic dermatitis (from Tower Hamlets Eczema Assessment (THEA)  palmar image dataset)
 72 non-atopic individuals




### Acknowledgements
LS is an NIHR Academic Clinical Fellow and the study was funded by a Barts Charity grant for investigation in atopic dermatitis (Grant ref MGU0568).  The THEA study is funded by Barts Charity (Grant ref MGU0376).  
