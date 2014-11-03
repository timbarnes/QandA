QandA is a simple utility to extract questions from an Excel spreadsheet and test your knowledge.

usage: ./quanda.py [--list] file.xslx
       ./quanda.py [--topic] topic file.xslx
       ./quanda.py file.xslx

Options:

--list - prints the topics available in the file

--topic - restricts questions to the named topic

[no options] - uses the full list of questions.

After each question is asked, you can respond with your answer, 'ok', or 'x'.

If you provide an answer, the system attempts to figure out if you're right.
If you're way off, you'll be asked the same question again.
'ok' means skip to the next question.
'x' means exit.

Answers are provided after each question as an aide-memoir.

The questions are provided in an Excel spreadsheet with three columns as follows:

Topic / Question / Answer

The software will add a question mark to the question.

This application relies on the xlrd and Levenshtein libraries for Excel access and estimates of correctness respectively.

