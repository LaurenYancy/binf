## HMM search
## Lauren Yancy
## 13 March 2020

import argparse


def main():

    print('foo')

    # parser = argparse.ArgumentParser(description='A Hidden Markov Model based program to find transmembrane sequence')
    # parser.add_argument('-sol', dest='solubleSequence', required=True, help='A file containing the soluble sequence')
    # parser.add_argument('-trans', dest='transmembraneSequence', required=True, help='A file containing the transmembrane sequence')
    # parser.add_argument('-state', dest='stateSequence', required=True, help='A file containing the state sequence')
    # parser.add_argument("-o", dest='output_file', help='output file')

    # args = parser.parse_args()

    # print(args)

    # print('error check')

def solubleSequenceFrequency(solubleSequence):
    # open sequence file
    file = open('solubleSequences', 'r')

    solubleFrquency = 0
    ## Create a dictionary of all amino acids in sequence

    solubleAminoAcidDictionary = {}

    for item in solubleSequence:

        aminoAcid = item
        # check to see if aminoAcid is in dictionary
        # add if not and set count to 0
        if solubleAminoAcidDictionary.has_key(aminoAcid):

            # use key to update value by 1
            solubleAminoAcidDictionary.update(aminoAcid=(solubleAminoAcidDictionary.get(aminoAcid)+1))
        else:

            # Add new Amino Acid and set value to 1
            solubleAminoAcidDictionary.append(aminoAcid:1)




    file.close()

    return solubleFrequency



    #aminoFrequency()





## Calculate frequencies of AA for Sol and trans membrane sequence (PS1)
##


def aminoFrequency():

    count = 0


    return count


## Calculate beginning sequence in state

## Calculate transition probabilities



## Calculate the number of occurrences of each digram in the state file. (e.g., SS or TT or ST or TS. A
## digram is a 2 character string. In general, a string of n characters is an n-gram.) You can use your other
## program from problem set#1 for this. From the numbers of observations, you should be able to
## construct the transition probability matrix for the HMM.


if __name__ == '__main__' :
    main()

