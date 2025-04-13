# Problem 2: RNA-seq analysis 🧬
In this repository you will find some scripts💻 that I used to solve💡 different issues that my group phased when trying to solve a problem🔎 in the context of the subject **Bacterial Genomics**🔬. 
All of them are **python** scripts that use famous packages⚙️ such as *matplotlib*, *pandas*, *numpy*🔧.

## 📁 `RPKMs_plotting`
- 📄 `gene_count_fpkm.txt`: FPKM values for each gene and for each replica of the experiment. It is the input.
- 💻 `RPKM_plot.py`: script that plots the distribution📈 of RPKMs in all the replicas.
- 🎨 `plt_FPKM.png`: FKPM distribution plotted. 
  
## 📁 `COG_terms`
- 📄 `Locus_tag_filtered_results.txt`: locus tags for each gene that has been defined as differentially expressed in our data (previously filtering⌨️ made). It is one of the inputs.
- 📄 `Stenotrophomonas_maltophilia_K279a_ASM7248v1_genomic.g2d.COG`: COG (Clusters of Orthologous Genes) terms for each gene of the reference S. maltophilia K279a genome. It is one of the imputs.
- 💻 `COGs.py`: script that uses the COG terms for our DEGs.
- 📄 `DEGs_with_COGs.csv`: csv output file with each DEG and its COG term. 
