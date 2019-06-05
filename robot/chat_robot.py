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
