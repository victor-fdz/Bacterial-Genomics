# Define the file to be processed and plotted. 
file_path = "Mutant_vs_WildType_results.txt"

# Open the file and convert it into a dataframe.
with open (file_path) as vs:
    df = pd.read_csv(vs, sep="\t")

# Logarithm transformation of the fold changes values. 
fc = [math.log2(i) for i in df["FoldChange"]]

# Start the plot.
fig,ax = plt.subplots()

n, bins, rect = plt.hist(fc, bins = 100)

# Assign colors based on bin values
for rect, bin_val in zip(rect, bins):
    if bin_val < -1:
        rect.set_facecolor('forestgreen') # Underexpressed
    elif bin_val > 1:
        rect.set_facecolor('firebrick')  # Overexpressed
    else:
        rect.set_facecolor('slateblue')   # No differential expression

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Absolute frequency')
ax.set_xlabel('log2(Fold Change)')
ax.set_title('Distribution of Fold Changes')
# Background lines:
ax.grid(color = "grey", 
        linewidth = 0.5,
        alpha = 0.5)

# Show the plot.
plt.show()