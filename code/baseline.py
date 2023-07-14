
import csv
# Classifies a tweet based on the number of positive and negative words in it

TWEET_FILE = '../dataset/tweets.csv'
POSITIVE_WORDS_FILE = '../dataset/positive-words.txt'
NEGATIVE_WORDS_FILE = '../dataset/negative-words.txt'

def file_to_wordset(filename):
    ''' Converts a file with a word per line to a Python set '''
    words = []
    with open(filename, 'r') as f:
        for line in f:
            words.append(line.strip())
    return set(words)
#This function and dictionary process the file according to the following parameters "Positive Words" and "Negative Words"
def classify(processed_csv, **params):
    positive_words = file_to_wordset(params.pop('positive_words'))
    negative_words = file_to_wordset(params.pop('negative_words'))
    with open(processed_csv) as csvfile:
        #This part of the code creates the proccessed file. 
        with open('predictions.csv', 'w', newline='') as targetFile:
            csvWriter = csv.writer(targetFile, quoting=csv.QUOTE_MINIMAL)
            tweetReader = csv.DictReader(csvfile)
            for row in tweetReader:
                tweet_id = row["id"]
                tweet = row["text"]
                created = row["created"]
                pos_count, neg_count = 0, 0
                #This part of the code counts how many positive and negative words are in each tweet to label the tweet as positive or negative.
                for word in tweet.split():
                    if word in positive_words:
                        pos_count += 1
                    elif word in negative_words:
                        neg_count += 1
                if(pos_count == 0 and neg_count == 0):
                    csvWriter.writerow([tweet_id, 'Neutral', created])
                if(pos_count >= neg_count):
                    csvWriter.writerow([tweet_id, 'Positive', created])
                if(pos_count < neg_count):
                    csvWriter.writerow([tweet_id, 'Negative', created])

#Positive and Negative word Files each contain a list of words that are either positive or negative.
 
if __name__ == '__main__':
    classify(TWEET_FILE, positive_words=POSITIVE_WORDS_FILE, negative_words=NEGATIVE_WORDS_FILE)

#Overall, the code reads a CSV file of tweets and classifies each tweet as positive, negative, or neutral based on the presence of positive and negative words in the tweet.
# The results are then written to a new CSV file called 'predictions.csv'.


'''
import csv
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
'''
'''
TWEET_FILE = '../dataset/tweets.csv'
'''
'''
def count_tweets_by_classification(csv_file):
     #Counts the number of tweets by classification 
    positive_count = 0
    neutral_count = 0
    negative_count = 0
    with open(csv_file, 'r') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            classification = row['classification']
            if classification == 'Positive':
                positive_count += 1
            elif classification == 'Neutral':
                neutral_count += 1
            elif classification == 'Negative':
                negative_count += 1
    return positive_count, neutral_count, negative_count
'''

'''
def plot_line_graph(positive_counts, neutral_counts, negative_counts):
     #Plots the line graph 
    start_time = datetime.strptime('09:22:01', '%H:%M:%S')
    time_intervals = []
    x_ticks = []
    for i in range(144):
        end_time = start_time + timedelta(minutes=10)
        time_interval = f'{start_time.time()} - {end_time.time()}'
        time_intervals.append(time_interval)
        x_ticks.append(start_time)
        start_time = end_time

    plt.plot(x_ticks, positive_counts, label='Positive')
    plt.plot(x_ticks, neutral_counts, label='Neutral')
    plt.plot(x_ticks, negative_counts, label='Negative')

    plt.xlabel('Time Intervals')
    plt.ylabel('Number of Tweets')
    plt.title('Tweet Classification over Time')
    plt.xticks(rotation=90)
    plt.legend()
    plt.tight_layout()
    plt.show()
'''
'''
if __name__ == '__main__':
    positive_counts = []
    neutral_counts = []
    negative_counts = []
    for i in range(144):
        start_time = datetime.strptime(f'00:{i*10}:00', '%H:%M:%S')
        end_time = start_time + timedelta(minutes=10)
        time_interval = f'{start_time.time()} - {end_time.time()}'
        positive_count, neutral_count, negative_count = count_tweets_by_classification(TWEET_FILE)
        positive_counts.append(positive_count)
        neutral_counts.append(neutral_count)
        negative_counts.append(negative_count)

    plot_line_graph(positive_counts, neutral_counts, negative_counts)
'''
