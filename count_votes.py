def count_votes(votes):
    likes = 0
    dislikes = 0

    for vote in votes:
        if vote == 'like':
            likes += 1
        elif vote == 'dislike':
            dislikes += 1

    dictionary = {'likes': likes, 'dislikes': dislikes}

    return dictionary