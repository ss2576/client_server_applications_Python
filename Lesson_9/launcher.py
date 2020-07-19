import subprocess
from argparse import ArgumentParser


class Launcher:
    def __init__(self, num, start):
        self.server = None
        self.clients = []
        self.actions = {
            'q': 'Выход',
            's': 'Запустить сервер и клиенты (s <кол-во>)',
            'x': 'Закрыть все окна',
            'h': 'Справка',
        }
        self.num = num
        if start == 'y':
            self.run()

    @property
    def help_info(self):
        return '\n'.join(
            [f'{key} - {action}' for key, action in self.actions.items()])

    def main(self):
        print(self.help_info)
        while True:
            action = input('Выберите действие: ')
            if action == 'q':
                break
            elif action.startswith('s'):
                command = f'{action} {self.num}'.split(' ')
                print(command)
                print(len(command))
                if command[0] == 's' and len(command) <= 3:
                    try:
                        self.num = int(command[1])
                    except ValueError:
                        continue
                    self.run()
            elif action == 'x':
                self.close()
            elif action == 'h':
                print(self.help_info)

    def run(self):
        self.close()
        self.server = subprocess.Popen('python server.py',
                                         creationflags=subprocess.CREATE_NEW_CONSOLE)
        for i in range(self.num):
            self.clients.append(
                subprocess.Popen(f'python client.py -n test{i}',
                                 creationflags=subprocess.CREATE_NEW_CONSOLE))

    def close(self):
        while self.clients:
            process = self.clients.pop()
            process.kill()
        if self.server:
            self.server.kill()


def parse_args():
    parser = ArgumentParser(description='Запуск сервера.')
    parser.add_argument(
        '-n', '--num', nargs='?', default=2, type=int, choices=range(1, 11),
        help='количество клиентов)'
    )
    parser.add_argument(
        '-r', '--run', nargs='?', default='n', choices=('y', 'n'),
        type=str.lower, help='Моментальный запуск y/n'
    )
    return parser.parse_args()


def run():
    args = parse_args()
    launcher = Launcher(args.num, args.run)
    launcher.main()


if __name__ == '__main__':
    run()