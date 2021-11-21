#! /usr/bin/env python3

"""This script extract a specific region of a fasta file"""

from Bio.Seq import Seq, reverse_complement

def slice_fasta(fasta_filepath:str, start:int, end:int) -> dict:
    
    """Extracts sequence from start to end in the fasta file"""
    
    with open(fasta_filepath) as FF:
        
        cursor = 0      # Cursor tracks file being parsed
        fasta_sequence = ''
        
        for line in FF:
            
            line = line.strip()
            
            if line.startswith('>'):    # Handle ID line
                fasta_id = line
                continue
            
            for base in line:
                
                if start <= cursor < end:
                    fasta_sequence += base
                
                cursor += 1
            
            if cursor > end:
                break
    
    return {'id': fasta_id, 'sequence':fasta_sequence }

def extract_single_fasta(multi_fasta_filepath:str, fasta_header:str) -> str:
    
    if not fasta_header.startswith('>'):
        fasta_header = f'>{fasta_header}'
    
    with open(multi_fasta_filepath) as MFF:
        
        line = MFF.readline()
        
        while not line.startswith(fasta_header):
            line = MFF.readline()
        
        line = MFF.readline()
        fasta_str = ''
        
        while not line.startswith('>'):
            fasta_str += line.strip()
            line = MFF.readline()
    
    return fasta_str

def find_sequence(query:str, subject:str):
    
    if query in subject:
        return {"orientation": {"forward": True,"sense": True}, "start": subject.find(query), "length": len(query)}
    
    reverse = query[::-1]
    if reverse in subject:
        return {"orientation": {"forward": False,"sense": True}, "start": subject.find(reverse), "length": len(reverse)}
    
    sequence = Seq(query)
    complement = str(sequence.complement())
    
    if complement in subject:
        return {"orientation": {"forward": True,"sense": False}, "start": subject.find(complement), "length": len(complement)}
    
    reverse_complement = complement[::-1]
    
    if reverse_complement in subject:
        return {"orientation": {"forward": False,"sense": False}, "start": subject.find(reverse_complement), "length": len(reverse_complement)}
    
    return False