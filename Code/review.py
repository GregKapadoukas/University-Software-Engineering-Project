from enum import Enum
from user import User

class Review:
    all = []
    id_incrementer = 0;
    def __init__(self, reviewer:User, reviewee:User, score:float, review_text:str):

        assert reviewer != reviewee, f"Reviewer User {reviewer} is the same as Reviewee User {reviewee}!"
        assert score in [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5], f"Score {score} is invalid!"

        self.__id = Review.id_incrementer
        Review.id_incrementer+=1
        self.__reviewer = reviewer
        self.__reviewee = reviewee
        self.__score = score
        self.__review_text = review_text

        Review.all.append(self)

    def __repr__(self):
        return f"ID: {self.__id}, Reviewer User ID: {self.__reviewer}, Reviewee User ID: {self.__reviewee}, Score: {self.__score}, Review Text: {self.__review_text}"

    def getReviewer(self):
        return self.__reviewer

    def getReviewee(self):
        return self.__reviewee

    def getScore(self):
        return self.__score

    def getReviewText(self):
        return self.__review_text

    @staticmethod
    def getUserReviews(user:User):
        result = []
        for review in Review.all:
            if review.__reviewee == user:
                result.append(review)
        return result

#review1 = Review(1, 2, Score.FIVE, "Perfect book!")
#print(review1)
