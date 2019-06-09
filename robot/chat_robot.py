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
        NO_RESTAURANT = 0
        sorted_restaurant_list = []
        if len(self.restaurant_dict) == NO_RESTAURANT:
            print('{0}さん。どこのレストランが好きですか?'.format(guest_name))
        else:
            sorted_restaurant_list = sorted(self.restaurant_dict.items(), key=lambda x: x[1], reverse=True)

        return sorted_restaurant_list

    def various_question(self, sorted_restaurant_list, guest_name):
        """
        レストラン名によって質問を変える
        :param sorted_restaurant_list: ソートした辞書
        :param guest_name: 顧客名称
        :return: レストラン名が一つならTrue違うならFalse
        """
        # レストランが一つしかない
        ONLY_REATAURANT = False
        threshold = 0
        max_values = [values[1] for values in sorted_restaurant_list if int(values[1]) > threshold]
        max_val = max(max_values)
        keys_of_max_val = [value for value in sorted_restaurant_list if value[1] == max_val]

        ONLY = 1

        if len(sorted_restaurant_list) == ONLY or len(sorted_restaurant_list) == len(keys_of_max_val):

            for vals in keys_of_max_val:
                print("私のおススメのレストランは、{0}です。\nこのレストランは好きですか?[Yes/No]".format(vals[0]))
                yn_answer = input('>>>')
                if yn_answer == 'Yes':
                    self.restaurant_dict[vals[0]] = int(self.restaurant_dict[vals[1]]) + 1
                elif yn_answer != 'No':
                    print('不正な値が入力されました')
            ONLY_REATAURANT = True

        else:

            for vals in sorted_restaurant_list:
                print("私のおススメのレストランは、{0}です。\nこのレストランは好きですか?[Yes/No]".format(vals[0]))
                yn_answer = input('>>>')
                if yn_answer == 'Yes':
                    self.restaurant_dict[vals[0]] = int(self.restaurant_dict[vals[0]]) + 1
                elif yn_answer != 'No':
                    print('不正な値が入力されました')

        print('{0}さん。どこのレストランが好きですか?'.format(guest_name))

        return ONLY_REATAURANT, sorted_restaurant_list[0]

    def add_restaurant(self, restaurant_name):
        """
        新しいレストラン名を追記
        :param restaurant_name:追記するレストラン名
        :return:
        """

        if restaurant_name in self.restaurant_dict:
            self.restaurant_dict[restaurant_name] = int(self.restaurant_dict[restaurant_name]) + 1
        else:
            self.restaurant_dict[restaurant_name] = 1

    def update_restaurant(self):
        """
        おススメレストラン情報をアップデートする
        :return:
        :rtype:
        """
        with open('./restaurant.txt', 'w', newline='') as  f:
            writer = csv.writer(f)

            writer.writerow(['NAME', 'COUNT'])

            for restaurant, number in self.restaurant_dict.items():
                writer.writerow([restaurant, number])

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
