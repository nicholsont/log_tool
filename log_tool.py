from log_tooldb import get_articles,get_authors,get_access_logs
from datetime import datetime
import os

#Write request log
def prep_log():
    print('Processing Request log...')
    #Retrive data from DB
    articles = get_articles()
    authors = get_authors()
    access_logs = get_access_logs()

    #Process data for log file output
    articles_data = process_articles(articles)
    authors_data = process_authors(authors)
    access_logs_data = process_access_logs(access_logs)

    #Create log file
    path = os.path.dirname(os.path.abspath(__file__))
    output_file = open(path + '/request_log.txt', 'w')
    output_file.write(articles_data + authors_data + access_logs_data)
    output_file.close()
    print('Log created.')

#Process logs for top 3 viewed articles
#Params: articles
def process_articles(articles):
    log_data = ''
    log_data += '***Top 3 most viewed articles***\n'
    for article in articles:
        log_data += '\t"%(title)s" -- %(count)d views\n' % {'title': article[0].title(),'count': article[1]}
    return log_data

#Process logs for authors ordered by most article views
#Params: authors
def process_authors(authors):
    log_data = ''
    log_data += '\n***Authors by most article views***\n'
    for author in authors:
        log_data += '\t%(author)s -- %(count)d views\n' % {'author': author[0],'count': author[1]}
    return log_data

#Process logs for access errors exceeding 1%
#Params: access_logs
def process_access_logs(access_logs):
    log_data = ''
    log_data += '\n***Request errors that exceed 1%***\n'
    for log in access_logs:
        #Calculate the error percentage('404 status'/'200 status')
        percent = round(float(log[2])/float(log[1]) * 100, 2)
        if percent >= 1:
            log_date = datetime.strptime(log[0], '%Y-%m-%d')
            log_data += '\t%(log)s -- %(count).2f%% errors\n' % {'log': log_date.strftime('%B %d, %Y'),'count': percent}
    return log_data

prep_log()
