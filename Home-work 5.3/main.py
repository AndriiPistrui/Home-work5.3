import string


def generate_hashtag(s):
    s = s.translate(str.maketrans('', '', string.punctuation))

    words = s.split()
    words = [word.capitalize() for word in words]


    hashtag = '#' + ''.join(words)

    if len(hashtag) > 140:
        hashtag = hashtag[:140]

    return hashtag



print(generate_hashtag('Python Community'))  # #PythonCommunity
print(generate_hashtag('i like python community!'))  # #ILikePythonCommunity
print(generate_hashtag('Should, I. subscribe? Yes!'))  # #ShouldISubscribeYes
