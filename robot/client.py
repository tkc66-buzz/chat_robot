import chat_robot


class Client(object):
    """
    クライアント。チャットロボットと交信をする。
    """

    def __init__(self):
        """
    　　チャットロボットを作成
        """
        robot = chat_robot.ChatRobot(name='Roboko')

    def chat_start(self):
        print('chat start')


if __name__ == '__main__':
    client = Client()
    client.chat_start()
