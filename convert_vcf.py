from .slice_fasta import slice_fasta
import vcfIO

def convert_vcf(vcf_filepath:str, reference_filepath:str, start:int, stop:int) -> dict:
    
    """Takes input VCF and reference fasta as well as start and stop positions and outputs a multifasta of these positions converted"""
    
    reference = slice_fasta(reference_filepath, start, stop)
    
    vcf_lines = vcfIO.read(vcf_filepath, start, stop)
    
    for base_index in range(0, len(start, stop)):
        
        