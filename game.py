import sys
import copy, random, string

class Validator(object):

    def __init__(self):
        self.number_of_players = 0
        self.list_of_scores = []
        self.allowed_score = 10**9
        self.allowed_players = 2*(10**5)
        self.rank = []
        self.alice_game = 0
        self.alice_scores = []

    def remove_spaces_in_list(self, list_values):
        '''
        TO remove the white spaces in the scores array
        :param list_values: List of scores
        '''
        print("Removing the white spaces in the list")

        while ' ' in list_values:
            list_values.remove(' ')

        while '' in list_values:
            list_values.remove('')

        return list_values


    def validate_scores_and_players_equal(self, players, scores):
        '''
        To validate the length of the scores and
        number of players are equal
        :param players: Total number of players
        :param scores: Scores list
        '''
        print("Equality check in scores and number of plays or players")
        if players != len(scores):
            sys.exit("You have entered {0} scores. You need to enter {1} scores to match your input".format(
            len(self.list_of_scores), self.number_of_players))


    def maximum_players(self, players):
        '''
        To check the maximum allowed players constraints
        :param players:Number of players
        '''
        print("Maximum allowed players or plays check")
        if players > self.allowed_players:
            sys.exit(
                "The maximum allowed number of plays or players is {0}. You have entered {1} plays or players".format(self.allowed_players,
                                                                                                    players))

    def maximum_scores(self, score):
        '''
        To check the maximum allowed score constraint
        :param score: scores[i] value
        '''
        if score > self.allowed_score:
            sys.exit("The allowed maximum score is {0}.You have entered {1}".format(self.allowed_score, score))


    def check_int_in_list(self, score):
        '''
        To check whether the scores list contains only Integers
        :param score: scores[i] value
        '''
        try:
            score = int(score)
            return score
        except ValueError:
            sys.exit("This {0} Value is not a number".format(score))


    def sort(self, scores_list, descending=False, ascending=False):
        '''
        Sorts the list based on the function call
        if none is set to True, then it will return the list
        :param scores_list:
        :param descending:
        :param ascending:
        :return:
        '''
        if descending:
            return sorted(scores_list, reverse=True)
        elif ascending:
            return sorted(scores_list)
        return scores_list


class Scores(Validator):

    def set_rank(self):
        '''
        To determine the rank for the given users scores
        '''
        print("Calculate the ranks for the provided input")
        rank_list = []
        scores = copy.deepcopy(self.list_of_scores)
        rank = 1
        for index, value in enumerate(self.list_of_scores):
            string_val = 'testuser'
            if value in scores:
                rank_dict = {}
                scores.remove(value)
                rank_dict[string_val] = {value:rank}
                rank_list.append(rank_dict)
                while value in scores:
                    rank_dict = {}
                    scores.remove(value)
                    rank_dict[string_val] = {value:rank}
                    rank_list.append(rank_dict)
                rank +=1

        self.rank = rank_list
        self.show_leader_board()


    def show_leader_board(self):
        '''
        To display the leader board status of the current test users
        '''
        print("\n\nLeaderBoard Status")
        for rank in self.rank:
            for key, value in rank['testuser'].items():
                print("Rank {0} is held by {1} with score {2}".format(value, 'testuser', key))



    def show_leader_board_afte_a_game(self, game, alice_score):
        '''
        To show the leader board status and alice's rank of the alice jth game
        '''
        print("\n\nLeaderBoard status after {} game(s) of alice".format(game))
        alice_status = False
        for rank in self.rank:
            for key, value in rank.items():
                for k, v in value.items():
                    if k == alice_score and alice_status == False:
                        print("Rank {0} is held by {1} with score {2}".format(v, 'alice', k))
                        alice_status = True
                    else:
                        print("Rank {0} is held by {1} with score {2}".format(v, key, k))


    def calculate_alice_rank(self):
        '''
        To determine the rank for the given users scores
        '''
        print("Calculating alice rank")
        for game in range(1, self.alice_game + 1):
            alice_game_score = self.alice_scores[game-1]
            rank_list = []
            scores = copy.deepcopy(self.list_of_scores)
            scores.append(alice_game_score)
            scores = self.sort(scores, descending=True)
            self.list_of_scores.append(alice_game_score)
            self.list_of_scores = self.sort(self.list_of_scores, descending=True)
            rank = 1
            for index, value in enumerate(self.list_of_scores):
                string_val = 'testuser'
                if value in scores:
                    rank_dict = {}
                    scores.remove(value)
                    rank_dict[string_val] = {value:rank}
                    rank_list.append(rank_dict)
                    while value in scores:
                        rank_dict = {}
                        scores.remove(value)
                        rank_dict[string_val] = {value:rank}
                        rank_list.append(rank_dict)
                    rank +=1

            self.rank = rank_list
            self.list_of_scores.remove(alice_game_score)
            self.list_of_scores = self.sort(self.list_of_scores, descending=True)
            self.show_leader_board_afte_a_game(game, alice_game_score)



class Main(Scores):


    def validate(self):
        '''
        To validate the inputs provided
        '''
        try:
            self.number_of_players = int(self.number_of_players)
            self.maximum_players(self.number_of_players) if self.number_of_players > 0 else sys.exit(
                "Number of players must be greater than 0")
        except ValueError:
            sys.exit("Number of players must be an integer")

        self.list_of_scores = input("Enter the scores for the players separated by space:").split(' ')
        self.list_of_scores = self.remove_spaces_in_list(self.list_of_scores)
        print("Checking the entered scores are numbers")
        self.list_of_scores = list(map(self.check_int_in_list, self.list_of_scores))
        self.validate_scores_and_players_equal(self.number_of_players, self.list_of_scores)
        print("Maximum allowed score check")
        list(map(self.maximum_scores, self.list_of_scores))
        self.list_of_scores = self.sort(self.list_of_scores, descending=True)


    def validate_alice_scores(self):
        '''
        To get and validate the scores of the Alice
        '''
        try:
            self.alice_game = int(input("\n\nEnter the number of games alice had played:"))
            self.maximum_players(self.alice_game) if self.alice_game > 0 else sys.exit(
                "Number of games must be greater than 0")
        except ValueError:
            sys.exit("Number of games must be an integer")

        self.alice_scores = input("Enter the scores of alice in each game separated by space:").split(' ')
        self.remove_spaces_in_list(self.alice_scores)
        print("Checking the entered scores are numbers")
        self.alice_scores = list(map(self.check_int_in_list, self.alice_scores))
        self.validate_scores_and_players_equal(self.alice_game, self.alice_scores)
        print("Maximum allowed score check")
        map(self.maximum_scores, self.alice_scores)
        self.alice_scores = self.sort(self.alice_scores, ascending=True)


    def start(self, players):
        '''
        To validate and start the game
        :param players:
        :return:
        '''
        self.number_of_players = players
        self.validate()
        self.set_rank()
        self.validate_alice_scores()
        self.calculate_alice_rank()


players = input("Enter the number_of_players:")

main_class = Main()
main_class.start(players)


