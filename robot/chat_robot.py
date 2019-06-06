import csv


class ChatRobot(object):
    """
    クライアントと交信するチャットロボット
    """

    def __init__(self, name):
        """
        インスタンス生成時ロボット名を決定

        :param name: ロボット名
        """
        self.name = name
        self.restaurant_dict = self.load_restaurant()

    def greeting(self):
        """
        交信スタート時の初めの会話

        """
        print('こんにちは！私は{0}です。あなたの名前はなんですか？'.format(self.name))

    def ask_restaurant(self, guest_name):
        """
        好きなレストランを尋ねる

        :param guest_name: クライアントの名前
        :return sorted_restaurant_dict:ソートした辞書
        """
        NO_RESTAURANT = 1

        sorted_restaurant_dict = {}
        if len(self.restaurant_dict) == NO_RESTAURANT:
            print('{0}さん。どこのレストランが好きですか?'.format(guest_name))
        else:
            sorted_restaurant_dict = sorted(self.restaurant_dict().items(), key=lambda x: x[1])

        return sorted_restaurant_dict

    def various_question(sorted_restaurant_dict):
        """
        レストラン名によって質問を変える
        :return: レストラン名が一つならTrue違うならFalse
        """
        # レストランが一つしかない
        ONLY_REATAURANT = True
        max_val = max(sorted_restaurant_dict.values())
        keys_of_max_val = [key for key in sorted_restaurant_dict if sorted_restaurant_dict[key] == max_val]

        ONLY = 1

        if len(sorted_restaurant_dict) == ONLY or len(max_val) == len(sorted_restaurant_dict):
            print("私のおススメのレストランは、{0}です。\nこのレストランは好きですか?[Yes/No]")
            return ONLY_REATAURANT



    def good_bye(self, guest_name):
        """
        交信終了時の会話

        """
        print('{0}さん。ありがとうございました。\n良い一日を！さようなら。'.format(guest_name))

    def load_restaurant(self):
        """
        レストラン情報を読み込む

        :return restaurant_dict:レストラン一覧辞書

        """

        with open('./restaurant.txt', 'r') as f:
            reader = csv.reader(f)
            restaurant_dict = {}
            for restaurant_name, restaurant_number in reader:
                restaurant_dict[restaurant_name] = restaurant_number
            del restaurant_dict["NAME"]
        return restaurant_dict
