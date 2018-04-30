import nltk
from nltk import sent_tokenize, word_tokenize, pos_tag
import string
import operator
from textblob import TextBlob
from collections import Counter
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
import re

SERIES = [
    'A_Series_of_Unfortunate_Events',
    'BoJack_Horseman',
    'La_casa_de_papel',
    'Lost_in_Space',
    'Stranger_Things',
    'house_of_cards'
]
RESERVED_WORDS = ['rt', 'netflix', 'episode', 'season'] + \
    list(string.ascii_lowercase) + list(string.ascii_uppercase)
PATH = 'C:/Users/skconan/Desktop/Workspace/wordCloud/data'


def generate_reserved_word():
    global SERIES, RESERVED_WORDS
    for word in SERIES:
        w = word.split('_')
        RESERVED_WORDS += [w.lower() for w in w]


def formatting(text):
    tmp = ''
    if text[:13] == '{"created_at"':
        text = text.split('"text"')
        tmp = text[1]
        tmp = tmp.split('"source"')
        text = tmp[0]
        text = text.split(' "')
        tmp = text[1][:-3]
    else:
        text = text.split('\n')
        for t in text:
            tmp += t + ' '
    tmp += '\n'
    print(tmp)
    return tmp


def filtered_statement(statement):
    global RESERVED_WORDS
    words = statement.split(' ')
    str = ''
    for word in words:
        for s in RESERVED_WORDS:
            if word == s:
                word = ''
        str += word + ' '
    return str


def merge_file():
    global SERIES
    for s in SERIES:
        text_file = ''
        for i in range(1, 11):
            filename = PATH+'/'+str(s)+'/' + str(s)+'_'+str(i)+'.txt'
            print('Open file : ', filename)
            try:
                f = open(filename, 'r', encoding="utf8")
            except:
                continue
            with f as infile:
                text = ''
                for line in infile:
                    # print(line)
                    if line[:13] == '{"created_at"':
                        text_file += formatting(line)
                    elif line is not '\n':
                        text += line
                    else:
                        text_file += formatting(text)
                        text = ''

        f.close()
        filename = PATH+'/'+str(s)+'/' + str(s)+'.txt'
        f = open(filename, 'w', encoding="utf8")
        f.write(text_file)
        f.close()


def merge_file_time():
    global SERIES
    for s in SERIES:
        text_file = ''
        for i in range(1, 11):
            filename = PATH+'/'+str(s)+'/' + str(s)+'_'+str(i)+'.txt'
            print('Open file : ', filename)
            try:
                f = open(filename, 'r', encoding="utf8")
            except:
                continue
            with f as infile:
                # text = ''
                for line in infile:
                    time = line.split('"')[3]
                    time = time.split(' ')[3]
                    text_file += time + '\n'

        f.close()
        filename = PATH+'/'+str(s)+'/' + str(s)+'_time.txt'
        f = open(filename, 'w', encoding="utf8")
        f.write(text_file)
        f.close()


def sentimental_statement(filter_title=False):
    global SERIES
    for s in SERIES:
        filename = PATH+'/'+str(s)+'/' + str(s)+'.txt'
        f = open(filename, 'r', encoding="utf8")
        with f as infile:
            ct_pos = 0
            ct_neg = 0
            ct_neutral = 0
            score_pos = 0
            score_neg = 0
            text_result = ''
            for statement in infile:
                if filter_title:
                    statement_filtered = filtered_statement(statement)
                else:
                    statement_filtered = statement

                sentiment = TextBlob(statement_filtered)
                score = sentiment.sentiment.polarity
                if score > 0:
                    ct_pos += 1
                    score_pos += score
                elif score < 0:
                    ct_neg += 1
                    score_neg += score
                else:
                    ct_neutral += 1
                text_result += statement + ', ' + str(score) + '\n'

            ct_total = ct_pos + ct_neg + ct_neutral
            ffilename = PATH+'/'+str(s)+'/' + str(s) + \
                    '_sentimental_statement.csv'
            if filter_title:
                ffilename = PATH+'/'+str(s)+'/' + str(s) + \
                    '_sentimental_statement_filter.csv'

            ff = open(ffilename, 'w', encoding="utf8")
            ff.write(text_result)
            ff.close()

            print('-'*5, s, '-'*5)
            text = "Data, Value" + '\n'
            text += 'Total tweets, ' + str(ct_total) + '\n'
            text += 'Neutral tweets percent, ' + \
                str(100*ct_neutral/ct_total) + '\n'
            text += 'Positive tweets percent, '+str(100*ct_pos/ct_total) + '\n'
            text += 'Negative tweets percent, '+str(100*ct_neg/ct_total) + '\n'
            text += 'Negative score average, '+str(score_neg/ct_neg) + '\n'
            text += 'Positive score average, '+str(score_pos/ct_pos) + '\n'
            ffilename = PATH+'/'+str(s)+'/' + str(s)+'_sentimental.csv'
            ff = open(ffilename, 'w', encoding="utf8")
            ff.write(text)
            ff.close()
        f.close()


def time_interval():
    global SERIES
    for s in SERIES:
        filename = PATH+'/'+str(s)+'/' + str(s)+'_time.txt'
        f = open(filename, 'r', encoding="utf8")
        with f as infile:
            time = {}
            for t in infile:
                hh = t[:2]
                if not hh in time:
                    time[hh] = 0
                time[hh] += 1

            text = 'Start, End, Frequently\n'
            for t in time:
                text += t + ':00, ' + \
                    "%02d" % (int(t)+1) + ':00, '+str(time[t]) + '\n'

            ffilename = PATH+'/'+str(s)+'/' + str(s) + '_time.csv'
            ff = open(ffilename, 'w', encoding="utf8")
            ff.write(text)
            ff.close()
        f.close()


def tag_checker(word):
    tag = ['DT', 'CC', 'IN', 'TO']
    for t in tag:
        if pos_tag(word_tokenize(word))[0][1] == t:
            return True
    return False


def reg_expression_checker(word):
    reg_list = [
        r'^[`]+',
        r'^[.]+',
        r'^\'+.*',
        r'^/+.*',
        r'^\\+.*',
        r'^[0-9]+',
        r'https?://[^\s<>"]+|www\.[^\s<>"]+',
        r'^https',
    ]

    for reg in reg_list:
        if re.search(reg, word):
            return True
    return False


def word_filter(word_list):
    # True have word don't want
    result = []
    for word in word_list:
        if not (tag_checker(word) or
                reg_expression_checker(word) or
                word in RESERVED_WORDS
                ):
            if '\\u' in word:
                word = word.split('\\u')[0]
            if '\\n' in word:
                word = word.split('\\n')[0]
            result.append(word)
    return result


def find_frequently(number_of_data='all'):
    global SERIES
    for s in SERIES:
        histogram = {}
        filename = PATH+'/'+str(s)+'/' + str(s)+'.txt'
        f = open(filename, 'r', encoding="utf8")
        with f as infile:
            for statement in infile:
                words = nltk.word_tokenize(statement.lower())

                stop_words = stopwords.words(
                    'english') + list(string.punctuation) + \
                    ['', '“', '”', "'", "’", "\\", "/"]

                filtered_words = [
                    word for word in words if word not in stop_words]
                filtered_words = word_filter(filtered_words)
                for word in filtered_words:
                    if not word in histogram:
                        histogram[word] = 1
                    else:
                        histogram[word] += 1
        print('-'*5, 'Top 5 Words of ', s, '-'*5)
        sorted_hist = sorted(
            histogram.items(), key=operator.itemgetter(1), reverse=True)
        # print(sorted_hist[:20])
        f.close()
        filename = PATH+'/'+str(s)+'/' + str(s)+'_hist_all.csv'
        if number_of_data is not 'all':
            sorted_hist = sorted_hist[:int(number_of_data)]
            filename = PATH+'/'+str(s)+'/' + str(s)+'_hist.csv'

        f = open(filename, 'w', encoding="utf8")
        text = 'Data, Value' + '\n'
        for hist in sorted_hist:
            text += hist[0] + ', ' + str(hist[1]) + '\n'
        print(text)
        f.write(text)
        f.close()


def main():
    merge_file()
    generate_reserved_word()
    merge_file_time()
    sentimental_statement(True)
    sentimental_statement(False)
    find_frequently('all')
    find_frequently('10')
    time_interval()


if __name__ == '__main__':
    main()
