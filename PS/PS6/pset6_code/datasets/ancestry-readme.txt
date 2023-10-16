Task:
Your task is to predict the ethnicity of a person who has sent in their DNA based on Single Nucleotide Polymorphisms (SNPs).

Values:
This dataset contains the genetic variation found in people sampled by the 1000 Genomes Project which sequenced the DNA from different ethnic groups around the world. Each input vector represents the DNA at specific locations in the genome for one individual. There are 20 binary input features. 0 indicates that the user's DNA at the given location matches the human reference genome. 1 indicates that the user's DNA does not match the human reference genome. The output class value represents the super population (ethnicity) of each individual. The super populations contained in this dataset are East Asian or Ad Mixed American, encoded in binary. The training data set contains 283 data vectors, and the testing data set contains 184 data vectors.

Column meaning:
Each column represents a particular location in the human genome. 0 indicates that the user's DNA at the given location matches the human reference genome. 1 indicates that the user's DNA does not match the human reference genome. Though the particular locations in DNA may have semantic meanings -- for this task all you know is that each column is a distinct nucleotide index.

Prediction:
The variable you are predicting is the super population of the user.

Credit:
Thanks to Jim Notwell and Gill Bejerano who is a professor in Computer Science and Genetics 

