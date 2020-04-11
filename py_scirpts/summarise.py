# https://becominghuman.ai/text-summarization-in-5-steps-using-nltk-65b21e352b65

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize

# function to generate the frequency of words in the text string
def create_freq_dict(text_str):
    stopWords= set(stopwords.words("english"))
    words= word_tokenize(text_str)
    ps=PorterStemmer()
    freqTable= dict()
    for word in words:
        word=ps.stem(word)
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] +=1
        else:
            freqTable[word]= 1        
    return freqTable


# function that scores each sentence acc to the freq table values of words in 
# the sentence and then divides the value by length of sentence (in words) so 
# that length of sentence does not infulence the value
def score_sentences(sentences, freqTable):
    sent_value= dict()
    for s in sentences:
        word_count= len(word_tokenize(s))
        for word_value in freqTable:
            if word_value in s.lower():
                if s[:10] in sent_value:
                    sent_value[s[:10]] += freqTable[word_value]
                else:
                    sent_value[s[:10]]= freqTable[word_value]
        sent_value[s[:10]]= sent_value[s[:10]]// word_count
    
    return sent_value

# function to compute the average value of sentence values so that threshold 
# for classifying a sentence important is determined
def find_threshold(sent_value):
    sumVal=0
    for e in sent_value:
        sumVal= sumVal + sent_value[e]
    
    avg= int(sumVal/ len(sent_value))
    return avg

# function to generate the summary of the text and return it as a string
def generate_summary(sentences, sent_value, threshold):
    count= 0
    summary= ""
    for s in sentences:
        if s[:10] in sent_value and sent_value[s[:10]] > threshold:
            summary= " " + s
            count= count+1    
    return summary

def driver_fun(text_to_summarize):
    # print("hello")
    # with open('RES.txt', 'r') as file:
    #     text_str= file.read().replace('\n', '')

    text_str = text_to_summarize

    freqTable= create_freq_dict(text_str)
    sentences = sent_tokenize(text_str)
    scores= score_sentences(sentences, freqTable)
    average_score= find_threshold(scores)
    summary= generate_summary(sentences, scores, (1.5* average_score))

    return summary

# driver_fun(text_to_summarize)