from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction

def line():
    print("_________________________________________________________________________________________________________")


seq_str = input("Paste your DNA sequence here: ").upper()
dna = Seq(seq_str.strip())  

line()

print("!!! DNA ANALYSIS REPORT WITH BIOPYTHON !!!")

line()

print("complementary DNA Sequence : " , dna.complement())

line()

print("Reverse Complimentary DNA Sequence : " , dna.reverse_complement())

line()

print("Converted RNA Sequence : " , dna.transcribe())

line()

print(" A - T - G - C COUNT's : ")
print("A : " , dna.count("A"))
print("T : " , dna.count("T"))
print("G : " , dna.count("G"))
print("C : " , dna.count("C"))

line()

print("Converted Protein : " , dna.translate())

line()

gc_content = gc_fraction(dna) * 100         
print("GC Content : " , gc_content)
print("AC Content : " , 100-gc_content)


line()


motif = dna.find("CGT")

print("Motif CGT found at :  ", motif)

line()

print("DNA ANALYSIS REPORT WITH BIOPYTHON CONDUCTED SUCCESSFULLY")