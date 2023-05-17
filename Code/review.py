from enum import Enum

class Score(Enum):
    ZERO = 0
    HALF = 0.5
    ONE = 1
    ONE_HALF = 1.5
    TWO = 2
    TWO_HALF = 2.5
    THREE = 3
    THREE_HALF = 3.5
    FOUR = 4
    FOUR_HALF = 4.5
    FIVE = 5

class Review:
    #all = []
    id_incrementer = 0;
    def __init__(self, reviewer_id:int, reviewee_id:int, score:Score, review_text:str):

        assert reviewer_id >= 0, f"Reviewer User ID {reviewer_id} is not greater or equal to zero!"
        assert reviewee_id >= 0, f"Reviewee User ID {reviewee_id} is not greater or equal to zero!"
        assert reviewer_id != reviewee_id, f"Reviewer User ID {reviewer_id} is the same as Reviewee User ID {reviewee_id}!"

        self.__id = Review.id_incrementer
        Review.id_incrementer+=1
        self.__reviewer_id = reviewer_id
        self.__reviewee_id = reviewee_id
        self.__score = score
        self.__review_text = review_text

        #Review.all.append(self)

    def __repr__(self):
        return f"ID: {self.__id}, Reviewer User ID: {self.__reviewer_id}, Reviewee User ID: {self.__reviewee_id}, Score: {self.__score}, Review Text: {self.__review_text}"

#review1 = Review(1, 2, Score.FIVE, "Perfect book!")
#print(review1)
