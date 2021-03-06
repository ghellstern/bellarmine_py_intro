# -*- coding: utf-8 -*-
"""

Copyright (c) 2015 by Patrick Hall, jpatrickhall@gmail.com
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0
   
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

-------------------------------------------------------------------------------

SOLUTION TO EXERCISE 3

"""

### Import collections module
import collections

# Determine number of lines in the raw file
nlines = sum(1 for line in open('profiles_raw.txt', 'r'))
print 'The number of lines is:  %i.' % (nlines)

# Clean raw file
# Using list comprehensions
# With progress indicator
with open('profiles_raw.txt', 'r') as in_file:
    with open('profiles_clean.txt', 'w') as out_file:
        for j, line in enumerate(in_file):
            out_file.write(' '.join([word.lower() if (len(word.strip()) >= 4\
                and (word.isalpha() or word.isspace())) else '' for word in\
                line.split()]) + '\n')
            print 'Line %i/%i cleaned ...' % (j+1, nlines)
print 'Done.'

# Create a list of every word in the cleaned profiles
words = []
with open('profiles_clean.txt', 'r') as in_file:
    for line in in_file:
        words += line.split()

# Creates a dictionary of term counts for the entire document
term_counts = collections.Counter(words)
print term_counts

# Creates a set that keeps only terms in the dictionary that occured more that
# ten times
keep_set = set([k for k in term_counts.keys() if term_counts[k] >= 10])

# Create a new file with only these frequently occuring terms
with open('profiles_clean.txt', 'r') as in_file:
    with open('profiles_clean_freq.txt', 'w') as out_file:
        for line in in_file:
            line_list = line.split()
            freq_list = [word for word in line_list if word in keep_set]
            out_file.write(' '.join(freq_list) + '\n')

# Print a dictionary of term counts for each individual cleaned profile
# Which of these profiles looks the most compatible to you?
with open('profiles_clean_freq.txt', 'r') as in_file:
    with open('profiles_term_counts.txt', 'w') as out_file:
        for i, line in enumerate(in_file):
            term_counts = collections.Counter(line.split())
            out_file.write('----------------------------------------\n')
            out_file.write('Profile %i term counts: \n' % (i+1))
            for key in term_counts:
                out_file.write(key + ' ' + str(term_counts[key]) + '\n')
                