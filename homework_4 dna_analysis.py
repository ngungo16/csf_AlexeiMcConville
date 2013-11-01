# Name: Alexei McConville
# Evergreen Login: mccale19
# Computer Science Foundations
# Programming as a Way of Life
# Homework 3: DNA analysis (Part 1)

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print "You must supply a file name as an argument when running this program."
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

seq_length = 0
# Total nucleotides seen so far.
total_count = 0
# Number of G and C nucleotides seen so far.
gc_count = 0

# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a G or a C,
    if bp == 'C' or bp == 'G':
        # increment the count of gc
        gc_count = gc_count + 1


# divide the gc_count by the total_count
gc_content = float(gc_count) / total_count

# Print the answer
print 'GC-content:', gc_content

at_count = 0
for bp in seq:
    total_count = total_count + 1
    if bp == 'T' or bp == 'A':
        at_count = at_count + 1

at_content = float(at_count) / total_count
print 'AT-content:', at_content

A_count = 0
T_count = 0
G_count = 0
C_count = 0

for bp in seq:
    total_count = total_count + 1
    if bp == 'T':
        T_count = T_count + 1
    elif bp == 'A':            
        A_count = A_count + 1
    elif bp == 'C':
        C_count = C_count + 1
    elif bp == 'G':
        G_count = G_count + 1
        
print 'A_count:', A_count
print 'T_count:', T_count
print 'G_count:', G_count
print 'C_count:', C_count

sum_count = A_count + T_count + G_count + C_count
print 'Sum_count:', sum_count

print 'Total_Count:', total_count

seq_length = len(seq)
print 'Seq_Length:', seq_length

ATGC_ratio = float(A_count + T_count) / (G_count + C_count)
print "AT/GC_ratio:", ATGC_ratio

if (gc_content > 0.6):
    print 'high GC content'
if (gc_content < 0.4):
    print 'low GC content'
if (0.4 <= gc_content <= 0.6):
    print 'moderate GC content'