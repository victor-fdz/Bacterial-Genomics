# Problem 2: RNA-seq analysis 🧬
In this repository you will find some scripts💻 that I used to solve different problems that my group phased when trying to solve a problem🔎 in the context of the subject **Bacterial Genomics**🔬. 
All of them are **python** scripts that use famous packages⚙️ such as *matplotlib*, *pandas*, *numpy*.

## 📁 `Plotting`
- 📄 `Locus_tag_filtered_results.txt`: locus tags for each gene that has been defined as differentially expressed in our data (previously filtering⌨️ made).
- 📄 `Stenotrophomonas_maltophilia_K279a_ASM7248v1_genomic.g2d.COG`: COG (Clusters of Orthologous Genes) terms for each gene of the reference S. maltophilia K279a genome.
- 💻 `COGs.py`: script that uses the COG terms for our DEGs.
- 📄 `DEGs_with_COGs.csv`: csv output file with each DEG and its COG term.
- 🎨 `plot1.txt`: SVs in the reference genome.
- 🎨 `plot2.txt`: high density 📈 zone of SVs.
- 🎨 `plot3.txt`: high density zone zoomed, with SVs types labeled. 

## 📁 `COG terms`
- 📄 `Locus_tag_filtered_results.txt`: locus tags for each gene that has been defined as differentially expressed in our data (previously filtering⌨️ made).
- 📄 `Stenotrophomonas_maltophilia_K279a_ASM7248v1_genomic.g2d.COG`: COG (Clusters of Orthologous Genes) terms for each gene of the reference S. maltophilia K279a genome.
- 💻 `COGs.py`: script that uses the COG terms for our DEGs.
- 📄 `DEGs_with_COGs.csv`: csv output file with each DEG and its COG term. 




  
The script generates 3 plots, whose examples are also in the folder: 


## 2. Plotting Venn Diagrams of Private/Shared SVs among Animal Genetic Pools (📁 `Venn_Diagrams`)

In this second case I'm comparing animal genetic pools 🧬. After calling the SVs, I made comparisons of 2 pools, but I wanted to do bigger comparisons (between >2 pools at the same time). That's why I created `Venn_Plot.R` ⌨️, an R script that takes as arguments pairs of files: 
- 📄 `SVs.txt`: example random file with SVs that has the number of alleles for 2 pools (initial comparison). 
- 📄 `stats.txt`: example random file with the number of statistically significant SVs in this initial comparison.

The script permits a **naive visualisation of how many SVs are private and how many are shared between genetic pools**. It is actually coded to give 10 arguments (5 pairs), but can be easily modified 🔧 to reduce the number of pools to be compared. 

A plot example is also available (🎨 `Venn_Diagram.txt`). 

Although I didn't use **ggplot2** here, the plotting package had a similar usage, so having previous knowledge was really useful.

## 3. Using Numpy/Pandas to Store/Visualize VCF data  (📁 `np_pd_VCF`)

In this final case I wanted to better visualize my VCF files, so I applied these 2 packages that we used in the last practical sessions. The example of the session was really useful 💡, because I had never used this type of packages before in Python. 

The script `VCF_df.py` ⌨️ takes a VCF file, which in this case is the same randomly generated as in the first analysis (📄 `SVs.txt`) and converts its data into a dataframe. How is visualized in a Jupyter Notebook is shown in 🎨 `screenshot_df.png`.
