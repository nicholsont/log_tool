#!/usr/bin/env python
from log_tooldb import get_articles, get_authors, get_access_logs
from datetime import datetime
import os

# Creates analysis log


def prep_log():
    print('Processing Request log...')
    # Retrive data from DB
    articles = get_articles()
    authors = get_authors()
    access_logs = get_access_logs()

    # Process data for log file output
    articles_data = process_articles(articles)
    authors_data = process_authors(authors)
    access_logs_data = process_access_logs(access_logs)

    # Create log file
    path = os.path.dirname(os.path.abspath(__file__))
    output_file = open(path + '/request_log.txt', 'w')
    output_file.write(articles_data + authors_data + access_logs_data)
    output_file.close()
    print('Log created.')


def process_articles(articles):
    '''
    :Process logs for top 3 viewed articles
    :param articles: (list) a list of two element tuples containing title and view count of the top 3 viewed articles
    :return log_data: (string) a string containing a ready print list of the top 3 articles
    '''
    log_data = ''
    log_data += '***Top 3 most viewed articles***\n'
    for title, view in articles:
        log_data += '\t"{0:<30}" {1:>12} views\n'.format(title, view)
    return log_data


def process_authors(authors):
    '''
    :Process logs for authors ordered by most article views
    :param authors: (list) a list of two element tuples containing title and view count of authors by article views
    :return log_data: (string) a string containing a ready print list of most popular authors by article views
    '''
    log_data = ''
    log_data += '\n***Authors by most article views***\n'
    for title, view in authors:
        log_data += '\t{0:<30} {1:>16} views\n'.format(title, view)
    return log_data


def process_access_logs(access_logs):
    '''
    :Process logs for access errors exceeding 1%
    :param access_logs: (list) a list of four elements containing log's date, total view count, error count,
    and error percentage
    :return log_data: (string) a string containing a ready print list of dates where error exceeded 1% of total views
    '''
    log_data = ''
    log_data += '\n***Request errors that exceed 1%***\n'
    for date, totalViews, errorViews, errorPercentage in access_logs:
        percent = round(errorPercentage, 2)
        # Filters error percentages over 1%
        if percent >= 1:
            log_date = datetime.strptime(date, '%Y-%m-%d')
            log_data += '\t{0:<30} {1:>14}% errors\n'.format(log_date.strftime('%B %d, %Y'), percent)
    return log_data


if __name__ == '__main__':
    prep_log()
