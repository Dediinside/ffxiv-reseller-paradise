import argparse
from pathlib import Path
import tkinter as tk
from reseller.app import Application


def main():
    parser = argparse.ArgumentParser(description='Рай перекупа · FFXIV')
    parser.add_argument('--demo', action='store_true', help='Искусственные цены, без Telegram')
    parser.add_argument('--profile', type=Path, help='Отдельная папка профиля')
    args = parser.parse_args()
    root = tk.Tk()
    Application(root, demo=args.demo, folder=args.profile)
    root.mainloop()


if __name__ == '__main__':
    main()
