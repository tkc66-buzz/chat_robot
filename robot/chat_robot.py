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

    def greeting(self):
        """
        交信スタート時の初めの会話

        """
        print('こんにちは！私は{0}です。あなたの名前はなんですか？'.format(self.name))

    def ask_restaurant(self, guest_name):
        """
        好きなレストランを尋ねる

        :param guest_name: クライアントの名前

        """
        print('{0}さん。どこのレストランが好きですか?'.format(guest_name))

    def good_bye(self, guest_name):
        """
        交信終了時の会話

        """
        print('{0}さん。ありがとうございました。\n良い一日を！さようなら。'.format(guest_name))
