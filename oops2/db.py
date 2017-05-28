class Statistics:
    def get_view_count(self):
        pass

    def get_normalized_vote(self):
        pass


class Vote:

    def like(self):
        pass

    def dislike(self):
        pass


class Video(Vote, Statistics):
    all_videos = []

    def __init__(self, title):
        self.title = title

    def play(self):
        pass

    def upload(self):
        pass

    def flag(self):
        pass
