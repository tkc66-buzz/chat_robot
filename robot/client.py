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
        """
       チャットロボットの最初の会話
        """
        self.robot.greeting()
        guest_name = input('>>>')
        sorted_restaurant_list = self.robot.ask_restaurant(guest_name)
        # 既存のレストラン名がない場合レストラン名を入力してもらう
        NO_RESTAURANT = 0
        if len(sorted_restaurant_list) != NO_RESTAURANT:
            self.robot.various_question(sorted_restaurant_list, guest_name)
            add_restaurant_name = input('>>>')
            # レストラン名が同じならば＋１
            if add_restaurant_name in self.robot.restaurant_dict:
                self.robot.restaurant_dict[add_restaurant_name] = int(
                    self.robot.restaurant_dict[add_restaurant_name]) + 1
            else:
                self.robot.restaurant_dict[add_restaurant_name] = 1

        else:
            restaurant_name = input('>>>')
            self.robot.add_restaurant(restaurant_name)

        self.robot.update_restaurant()
        self.robot.good_bye(guest_name)


if __name__ == '__main__':
    client = Client()
    client.chat_start()
