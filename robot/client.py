import chat_robot


class Client(object):
    """
    クライアント。チャットロボットと交信をする。
    """

    def __init__(self):
        """
    　　チャットロボットを作成
        """
        self.robot = chat_robot.ChatRobot(name='Roboko')

    def chat_start(self):
        self.robot.greeting()
        guest_name = input('>>>')
        self.robot.ask_restaurant(guest_name)
        restaurant_name = input('>>>')
        # self.robot.update_restaurant(restaurant_name)
        self.robot.good_bye(guest_name)


if __name__ == '__main__':
    client = Client()
    client.chat_start()
