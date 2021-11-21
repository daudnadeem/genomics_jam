# genomics_jam

Genomics Jam is a project to extract specific gene sequence data from Big Data public repository such as the 1000 genomes project.
At it's core it is a tool to convert Variant Call Format (VCF) files to fasta files while at the same time extracting specific features of interest.
It is a data mining project that allows non-computational users to interact with large data sets.

## The Data

The project is initially being developed with the idea of extracting the HLA and inter-genic regions from the 1000 genomes dataset.

A summary of the 1000 genomes project can be found here:

https://www.internationalgenome.org/about

The data we are interested in is a fully phased chromosome 6 data set available from the 1000 genomes project,
This data is stored as a VCF file. The publically available data can be downloaded from here:

ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/ALL.chr6.phase3_shapeit2_mvncall_integrated_v5b.20130502.genotypes.vcf.gz
ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/ALL.chr6.phase3_shapeit2_mvncall_integrated_v5b.20130502.genotypes.vcf.tbi

Additionally in order to interact with the data a reference is also needed. The url of this reference is specified in the VCF file itself but a link for this case is included here:

ftp://ftp.1000genomes.ebi.ac.uk//vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz

This data includes vcf and fasta format files descriptions of which can be found here:

 * https://www.internationalgenome.org/wiki/Analysis/vcf4.0/
 * https://en.wikipedia.org/wiki/FASTA_format

Fasta particularly is a very standard and widely used file format with a wide array of parsers. There are parsers for VCF however I think the issue that they all have is that they are designed to parse the entire file which would require a huge amount of compute resource and storage space. We are designing a system to download specific components of the data and convert them to fasta format.
