************************
Introducing the dataset
************************

This is not a text on biology, genomics or bioinformatics. But we will
be using a population genomics dataset, hence we will introduce some
necessary concepts. The text will be kept to a bare minimum with links
to further explanations (as a rule the English version of Wikipedia
is a great port of call).


Very basic genomics
===================

We will not teach you genetics and genomics here, furthermore the level of
explanation that you will find is below what you can find on Wikipedia. But we
do need to explain some basic concepts in order to make sure you know
all that is needed to understand the data.

When you were born, you received genetic material (DNA) from your parents. In
our species that means 22 pairs of *autosomes* , 1 pair of *allosomes*
and *mitochondrial* DNA. While the terminolgy might seem strange, it is actually
quite easy:

* *allosomes* are sex chromosomes. They might have different forms. You got
one X chromosome from your mother and either an X (if you are a female) or
Y (if you are a male) from your father. Females have 2 X chromosomes, males
are XY.

* *autosomes* appear in pairs: you have one from your mother and another from
your father. They have mostly the same form and size and encode similar genes.

* You also get *mitochondrial* DNA from your mother. This is a small piece
of DNA in circular form.

In this course we will only be using *autosomes*, that is the 22 pairs of
chromosomes where you got similar forms from both of your parents (actually
we will be using mosquito autosomes, but the concept is the same).

**Because this is a big-data** course, the sizes of the chromosomes are an
important topic. Here, for reference is the size of human ones (take from
Wikipedia):

==========  =============
Chromosome	Base pairs
----------  -------------
1	          249,250,621
2	          243,199,373
3	          198,022,430
4	          191,154,276
5	          180,915,260
6	          171,115,067
7	          159,138,663
8	          146,364,022
9	          141,213,431
10	        135,534,747
11	        135,006,516
12	        133,851,895
13	        115,169,878
14	        107,349,540
15	        102,531,392
16	        90,354,753
17          81,195,210
18          78,077,248
19          59,128,983
20          63,025,520
21          48,129,895
22          51,304,566
X           155,270,560
Y           59,373,566
mtDNA       16,569
**total**   3,095,693,981
==========  =============

So, we are dealing with around 3GB of information per individual. In theory
2 bits ber base is enough, remenber that we only have ACTG, but most encodings
that you see are text based (ASCII), so it is probably a byte per base
(actually two bytes as we will see).

Note the small size of the mitochondrial DNA and the difference in size between
X and Y.


Recombination
-------------

Think, for example on chromosome 3 that you received from your mother. Where
does it come from? From your grandmother or your grandfather?
It turns out that the answer is not as obvious at it seems. Autosomes do
recombine inside our cells. This means that that chromosome 3 from your mother
might be:

* Only from your grandfather
* Only from your grandmother
* Have pieces from both your grandparents

Roughly you might think that there is around one recombination event per
chromosome, say between 0 and 2.

Think a bit about the consequences here: while you have roughly half of the
genetic material from your parents, your grandparents are not equally
represented.

.. important::
  Recombination is important in terms of statistical properties of the dataset,
  take a bit of time to reflect on the data analysis consequences of
  recombination.

Finally, you might remember from school that the most common unit of
chromosome size is not the number of base pairs, but Morgans, well these
reflect exactly the recombination rate!

Single-Nucleotide Polymorphisms (SNPs)
--------------------------------------

The DNA that you receive from you mother and father is different. There are
many kinds of differences, but here we will only concentrate on arguably the
simplest one: Single-Nucleotide Polymorphisms (SNPs). A SNP is the variation
of a single base pair on the same position across the genome. For example,
look the following piece of genome in 3 different individuals:

+------------+-----------------------+
|            | Position              |
| Individual |                       |
|            | ``1 2 3 4 5 6 7 8 9`` |
+------------+-----------------------+
| 1          | ``A T C T G A T G T`` |
+------------+-----------------------+
|            | ``A A C T G A T G T`` |
+------------+-----------------------+
| 2          | ``A A C T C A T G T`` |
+------------+-----------------------+
|            | ``A A C T C A T G T`` |
+------------+-----------------------+
| 3          | ``A A C T C A T G T`` |
+------------+-----------------------+
|            | ``A A C T C A T G T`` |
+------------+-----------------------+
|            | ``1 * 3 4 * 6 7 8 9`` |
+------------+-----------------------+

Remeber that with autosomes individuals have 2 copies of the same genetic
material, hence two entries per individual.

Positions 2 and 5 are SNPs, that is, there is a mutation across the individuals
sequenced at those positions.

Individual 1 is heterozyguous at position 2, i.e. it has a different nucleotide
for the same position.

For humans, there is very little variation across the genome, roughly
1 SNP every 2000 base pairs (note to self: check the accuracy of the number).


The mosquito that transmits malaria
===================================

For most of our examples, we will use not human data but a dataset from the
mosquito that transmits malaria.

Rigorously, the *Anopheles* mosquito does not transmit malaria, but
transmits *Plasmodium*, the parasite that causes malaria.

Now that you know a bit about human genomics we can discuss mosquito
genomics. Fortunately they are very similar (if you are not a geneticist, you
would be shocked at the variation in genomic structure that can be found
in nature).

Sex in anopheles mosquitoes is similar (genomically) to humans: A X and a Y
chromosome. There is also a mitochondria. **Mosquitoes have only two pairs
of autosomes**, that purely for ease of convention are split in left and right
arms. For some weird reason they are numbered 2 and 3 (2L, 2R, 3L and 3R
with the arms) - no 1. The sizes are:

==========  ===========
Chromosome	Base pairs
----------  -----------
2R          61,545,105
3R          53,200,684
3L          41,963,435
2L          49,364,325
X           24,393,108
UNKN        42,389,979
Y           ???
mtDNA       15,363
==========  ===========

We have around 270 Mbp, one order of magnitude lower than humans. Notice
that, as with most species, we do not have a very good genome assembly
for *Anopheles*. No Y assembled (females - XX - are more important, because they
are the ones that transmit malaria) and quite a lot of unknown bits.

Now, the interesting part is that while humans have little genomic variation,
*Anopheles* mosquitoes site on the other extreme. We are probably dealing
with a SNP every 4 base pairs. When we are reduced to SNPs, these mosquitoes
have at least 2 orders of magnitude more information than humans. Genome size
does not have to be a good proxy for SNP density.

.. info::
  This ends the biological part that you need to know for this course. We will
  now talk a bit about genome sequencing technology, along with its data
  analysis implications.


The Anopheles 1000 genomes project
----------------------------------

We will be using data from the `The Anopheles 1000 genomes project`_. This
project currently makes available genomic information of 765 mosquitoes
across African populations

.. todo::
   Link to metadata (or put image here)

Basic sequencing
================

There are plenty of sequencing technologies around, this text will be based
on the most common one in use. Obviously we will keep this very simple.

Now that you have your DNA available it is time to sequence it. Unfortunately
sequencing technology is very redumentary. Do you think you can get a chromosome
from start to end? We are very far away from that. What we normally get is reads
of around 100 base pairs.

So the first problem that we have to solve is a *mapping* problem: given our
100 bp read where does it fit on the genome (That is a search space of 3Gbp for
humans or 270). If you think about it, this is a massive puzzle to solve. Years
of research and millions of dollars have been put into this.

Now the biggest problem is that the read from a sequencer can have errors. So
algorithms will have to deal with that. The sequencer gives you a measure of
trust for each base read (A `PHRED score`_) - i.e. the probability of
being a correct read. So you get not only the base, but
a level of trust. So, for a 3 Gbp genome, you now can expect to deal with 6 Gbp
of data (50% DNA reads, 50% trust levels).

How do the algorithms deal with errors? They do that by requiring you to
sequence *a lot* of data. Ideally you should cover each position around
30 times. You need 30 times coverage. So, a 3 Gbp human genome will generate
6Gbp of data times 30. We are now at 180 Gigabytes (uncompressed) per human
sample.

So after solving the puzzle with *mapping*, where you assign each 100 bp read
to a position in a reference genome you can now think in *SNP calling* where
you call your SNPs per sample. This is a fairly complex process as it will
have to look at error rates per position and available coverage.

So, at the end you will have a file with SNP calls, because calling SNPs is
not trivial, you get the calls *and* a lot of other metrics that you can use
to *filter* the data yourself.

The data that we will be using is made available in VCF format, lets check that now.

.. info::
  In this course we will only be working with VCF files or products derived
  from them. There are plenty of interesting formats before VCF (FASTQ, BAM,
  CRAM) dealing with raw sequencer data and mapped reads, but that is beyond
  our scope here.

VCF Files
=========



.. todo::

  Links to wikipedia

.. _`PHRED score`: https://en.wikipedia.org/wiki/Phred_quality_score
.. _`The Anopheles 1000 genomes project`: https://www.malariagen.net/projects/ag1000g
