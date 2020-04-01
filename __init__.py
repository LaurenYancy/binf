

seq_filename = "Hinfluenzae.txt"
total_length = 0

nucleotide_Dictionary = {} # create an empty dictionary
seq_file = open(seq_filename, "r")

for filename_line in seq_file:
    line = filename_line .rstrip("\r\n")
    #print(line)
    #print(len(line))
    length = len(line)
    #print(length)
    # works but low?

    for nuc in line:
        if nuc in nucleotide_Dictionary:
            nucleotide_Dictionary[nuc] += 1
            #print(nucleotide_Dictionary[nuc])
            # Prints occurrence number
        else:
            # Assigns a key with value 1
            nucleotide_Dictionary[nuc] = 1

    total_length += length


print("this is the length:")
print(total_length)
print(nucleotide_Dictionary)

for n in nucleotide_Dictionary.keys():
    fraction = 100.0 * nucleotide_Dictionary[n] / total_length
    print("In the file {0}, the nucleotide {1} occurs {2} times, or {3} %".format(seq_filename, n, nucleotide_Dictionary[n], fraction))
seq_file.close()

seq_filename = "Taquaticus.txt"
total_length = 0

nucleotide_Dictionary = {} # create an empty dictionary
seq_file = open(seq_filename, "r")

for filename_line in seq_file:
    line = filename_line .rstrip("\r\n")
    #print(line)
    #print(len(line))
    length = len(line)
    #print(length)
    # works but low?

    for nuc in line:
        if nuc in nucleotide_Dictionary:
            nucleotide_Dictionary[nuc] += 1
            #print(nucleotide_Dictionary[nuc])
            # Prints occurrence number
        else:
            # Assigns a key with value 1
            nucleotide_Dictionary[nuc] = 1

    total_length += length


print("this is the length:")
print(total_length)
print(nucleotide_Dictionary)

for n in nucleotide_Dictionary.keys():
    fraction = 100.0 * nucleotide_Dictionary[n] / total_length
    print("In the file {0}, the nucleotide {1} occurs {2} times, or {3} %".format(seq_filename, n, nucleotide_Dictionary[n], fraction))

seq_file.close()


#### Dinucleotide
seq_filename = "Hinfluenzae.txt"
total_length = 0
dinucleotide_list = []
dinucleotide_Dictionary = {} # create an empty dictionary
seq_file = open(seq_filename, "r")

for filename_line in seq_file:
    line = filename_line .rstrip("\r\n")
    length = len(line)

    for nuc in line:
        dinucleotide_list.append(nuc)
        #print(dinucleotide_list)


for i in range(len(dinucleotide_list)-1):

    first_nucleotide = dinucleotide_list[i]
    second_nucleotide = dinucleotide_list[i + 1]
    dinucleotide = first_nucleotide + second_nucleotide
    #print(dinucleotide)

    if dinucleotide in dinucleotide_Dictionary:
        dinucleotide_Dictionary[dinucleotide] += 1
    else:
        # Assigns a key with value 1
        dinucleotide_Dictionary[dinucleotide] = 1

    total_length += 1

print("this is the length:")
print(total_length)
print(dinucleotide_Dictionary)

for n in dinucleotide_Dictionary.keys():
    fraction = 100.0 * dinucleotide_Dictionary[n] / total_length
    print("In the file {0}, the dinucleotide {1} occurs {2} times, or {3} %".format(seq_filename, n, dinucleotide_Dictionary[n], fraction))


#### Dinucleotide
seq_filename = "Taquaticus.txt"
total_length = 0
dinucleotide_list = []
dinucleotide_Dictionary = {} # create an empty dictionary
seq_file = open(seq_filename, "r")

for filename_line in seq_file:
    line = filename_line .rstrip("\r\n")
    length = len(line)

    for nuc in line:
        dinucleotide_list.append(nuc)
        #print(dinucleotide_list)


for i in range(len(dinucleotide_list)-1):

    first_nucleotide = dinucleotide_list[i]
    second_nucleotide = dinucleotide_list[i + 1]
    dinucleotide = first_nucleotide + second_nucleotide
    #print(dinucleotide)

    if dinucleotide in dinucleotide_Dictionary:
        dinucleotide_Dictionary[dinucleotide] += 1
    else:
        # Assigns a key with value 1
        dinucleotide_Dictionary[dinucleotide] = 1

    total_length += 1

print("this is the length:")
print(total_length)
print(dinucleotide_Dictionary)

for n in dinucleotide_Dictionary.keys():
    fraction = 100.0 * dinucleotide_Dictionary[n] / total_length
    print("In the file {0}, the dinucleotide {1} occurs {2} times, or {3} %".format(seq_filename, n, dinucleotide_Dictionary[n], fraction))

seq_file.close()


###

#### Dinucleotide
seq_filename = "MysteryGene1.txt"
total_length = 0
dinucleotide_list = []
dinucleotide_Dictionary = {} # create an empty dictionary
seq_file = open(seq_filename, "r")

for filename_line in seq_file:
    line = filename_line .rstrip("\r\n")
    length = len(line)

    for nuc in line:
        dinucleotide_list.append(nuc)
        #print(dinucleotide_list)


for i in range(len(dinucleotide_list)-1):

    first_nucleotide = dinucleotide_list[i]
    second_nucleotide = dinucleotide_list[i + 1]
    dinucleotide = first_nucleotide + second_nucleotide
    #print(dinucleotide)

    if dinucleotide in dinucleotide_Dictionary:
        dinucleotide_Dictionary[dinucleotide] += 1
    else:
        # Assigns a key with value 1
        dinucleotide_Dictionary[dinucleotide] = 1

    total_length += 1

print("this is the length:")
print(total_length)
print(dinucleotide_Dictionary)

for n in dinucleotide_Dictionary.keys():
    fraction = 100.0 * dinucleotide_Dictionary[n] / total_length
    print("In the file {0}, the dinucleotide {1} occurs {2} times, or {3} %".format(seq_filename, n, dinucleotide_Dictionary[n], fraction))

seq_file.close()

#####
#### Dinucleotide
seq_filename = "MysteryGene2.txt"
total_length = 0
dinucleotide_list = []
dinucleotide_Dictionary = {} # create an empty dictionary
seq_file = open(seq_filename, "r")

for filename_line in seq_file:
    line = filename_line .rstrip("\r\n")
    length = len(line)

    for nuc in line:
        dinucleotide_list.append(nuc)
        #print(dinucleotide_list)


for i in range(len(dinucleotide_list)-1):

    first_nucleotide = dinucleotide_list[i]
    second_nucleotide = dinucleotide_list[i + 1]
    dinucleotide = first_nucleotide + second_nucleotide
    #print(dinucleotide)

    if dinucleotide in dinucleotide_Dictionary:
        dinucleotide_Dictionary[dinucleotide] += 1
    else:
        # Assigns a key with value 1
        dinucleotide_Dictionary[dinucleotide] = 1

    total_length += 1

print("this is the length:")
print(total_length)
print(dinucleotide_Dictionary)

for n in dinucleotide_Dictionary.keys():
    fraction = 100.0 * dinucleotide_Dictionary[n] / total_length
    print("In the file {0}, the dinucleotide {1} occurs {2} times, or {3} %".format(seq_filename, n, dinucleotide_Dictionary[n], fraction))

seq_file.close()

#####


#### Dinucleotide
seq_filename = "MysteryGene3.txt"
total_length = 0
dinucleotide_list = []
dinucleotide_Dictionary = {} # create an empty dictionary
seq_file = open(seq_filename, "r")

for filename_line in seq_file:
    line = filename_line .rstrip("\r\n")
    length = len(line)

    for nuc in line:
        dinucleotide_list.append(nuc)
        #print(dinucleotide_list)


for i in range(len(dinucleotide_list)-1):

    first_nucleotide = dinucleotide_list[i]
    second_nucleotide = dinucleotide_list[i + 1]
    dinucleotide = first_nucleotide + second_nucleotide
    #print(dinucleotide)

    if dinucleotide in dinucleotide_Dictionary:
        dinucleotide_Dictionary[dinucleotide] += 1
    else:
        # Assigns a key with value 1
        dinucleotide_Dictionary[dinucleotide] = 1

    total_length += 1

print("this is the length:")
print(total_length)
print(dinucleotide_Dictionary)

for n in dinucleotide_Dictionary.keys():
    fraction = 100.0 * dinucleotide_Dictionary[n] / total_length
    print("In the file {0}, the dinucleotide {1} occurs {2} times, or {3} %".format(seq_filename, n, dinucleotide_Dictionary[n], fraction))

seq_file.close()

