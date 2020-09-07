ROLLING_RADIUS = 30

from matplotlib import pyplot as plt
from re import sub

text = ''
with open('text.txt', 'r') as rf:
    for line in rf:
        text += ''.join(filter(lambda c: c.isalpha() or c in ' \n', list(line)))# remove punctuation
text = text.replace('\n', '\n ')                                                # count newlines as word boundaries
text = text.lower().strip()                                                     # make everything lower case
text = text.split(' ')                                                          # split by words
text = list(filter(lambda w: len(w), text))                                     # remove empty "words"
paragraphs = [1]+[i for i,v in enumerate(text) if v[-1] == '\n']                # get paragraph indices by word number
percent_of_prev_fifty = [                                                       # calculate statistics:
        len(list(filter(lambda w: w in ['siriak', 'he', 'his', 'him'],          # count number of "valid" words
        text[max(i-ROLLING_RADIUS, 0):min(i+ROLLING_RADIUS, len(text))])))      # of the surrounding 2*ROLLING_RADIUS words
        /ROLLING_RADIUS *50 for i in range(len(text))]                          # converted to percent, for every word index
plt.style.use('dark_background')                                                # dark mode
plt.plot(percent_of_prev_fifty)                                                 # plot rolling average
plt.ylabel(f'Percentage of nearby {ROLLING_RADIUS*2} words referencing Siriak') # set axis labels
plt.xlabel('Paragraph number')
plt.xticks(paragraphs, range(1, len(paragraphs)+1))                             # show paragraph markers
plt.savefig('chart', dpi=300)                                                   # save as image
plt.show()                                                                      # show the plot

