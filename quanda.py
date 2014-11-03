#!/usr/bin/python -tt

# Access a tab-delimited file of topic, question, answer tuples
# Randomly ask questions, then show answers

import sys, os

from re import sub
from random import randint

from xlrd import open_workbook
from Levenshtein import distance


def list_topics(filename):
    """Print the list of topics in the file
    """
    
    topics = set()
    book = open_workbook(filename)
    sheet = book.sheet_by_index(0)
    for row_index in range(sheet.nrows):
        row_data = sheet.row(row_index)
        topics.add(row_data[0].value)
    for entry in sorted(topics):
        print entry
#        print topics
    return


def read_questions(filename, topic = 'all'):
    """Read the questions using the xlrd processor.
    Lines are organized into lists of topic, question and answer.
    """
    
    book = open_workbook(filename)
    sheet = book.sheet_by_index(0)
    qlist = []
    for row_index in range(sheet.nrows):
        row_data = sheet.row(row_index)
        if topic == 'all' or row_data[0].value == topic:
            list.append(qlist, [x.value for x in row_data])
    print 'Found', len(qlist), 'entries in topic', topic
    return qlist


def rate_answer(given, correct):
    """Compare the answer with the given, attempting to be slightly smart.
    Remove irrelevant words (and, or); remove punctuation; sort alphabetically,
    then compare using Levenshtein.
    Return 1 for correct, 0 for close, -1 for mismatch.
    """

    regex = '[,:;-]+]|, | the | and | or | a | of | per '
    g = sub(regex, '', given).lower()
    c = sub(regex, '', str(correct)).lower()
    g = sub(r'per', '/', g)
    c = sub(r'per', '/', c)
    g = sub(r'\.$', '', g)
    c = sub(r'\.$', '', c)
    g = sub(r'up to', 'max', g)
    c = sub(r'up to', 'max', c)
    g = sub(r' to ', ' - ', g)
    g = sub(r'-', ' - ', g)
    c = sub(r' to ', ' - ', c)
    c = sub(r'-', ' - ', c)
    g = sub(r'\' *x', '\' x ', g)
    g = sub(r' by ', ' x ', g)
    c = sub(r'\' *x', '\' x ', c)
    c = sub(r' by ', ' x ', c)
    g = ''.join(sorted(g.split()))
    c = ''.join(sorted(c.split()))
#    print g, ' | ', c
    dist = distance(g, c)
    if dist == 0:
        return 1
    elif dist < len(g):
        return 0
    else:
        return -1
    return 

    
def do_questions(questions):
    """Iteratively pose questions and report answers.
    Questions are selected at random from the database.
    Type 'x' to exit."""

    maxindex = len(questions) - 1
    r = ''
    repeat = False
    while not r == 'x\n':
        if not repeat:
            question = questions[randint(0, maxindex)]
        print '\nIn topic', question[0], ':', question[1]+'?'
        r = sys.stdin.readline()
        print 'Answer is:', question[2]
        if r.lower() != 'ok\n':
            grade = rate_answer(r, question[2])
            if grade == 1:
                print "Correct!"
                repeat = False
            elif grade == 0:
                print "Close..."
                repeat = False
            elif grade == -1:
                repeat = True
        else:
            print "Skipping..."
    return


def main():
    args = sys.argv[1:]

    if not args:
        print 'usage: [--list] [--topic] file '
        sys.exit(1)

    questions = []
    if args[0] == '--list':
        list_topics(args[1])
            
    elif args[0] == '--topic':
        questions = read_questions(args[2], args[1])

    else:
        questions = read_questions(args[0])
        print len(questions)

    if len(questions) > 0:
        do_questions(questions)
    else:
        print "No questions found."

if __name__ == '__main__':
  main()
