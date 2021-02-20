"""Demonstrates how to make a simple call to the Natural Language API."""
"""Code below is adapted from https://cloud.google.com/natural-language/docs/sentiment-tutorial"""

import argparse
import google.cloud.language as language_v1

def print_result(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    # for index, sentence in enumerate(annotations.sentences):
    #     sentence_sentiment = sentence.sentiment.score
    #     print(
    #         "Sentence {} has a sentiment score of {}".format(index, sentence_sentiment)
    #     )

    print("Overall Sentiment: score of {} with magnitude of {}".format(score, magnitude))
    return score

def analyze(filename):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language_v1.LanguageServiceClient()

    with open(filename, "r") as review_file:
        # Instantiates a plain text document.
        content = review_file.read()

    document = language_v1.Document(content=content, type_=language_v1.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(request={'document': document})

    # Print the results
    print_result(annotations)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "filename",
        help="The filename of text you'd like to analyze.",
    )
    args = parser.parse_args()

    analyze(args.filename)