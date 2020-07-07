# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/16 18:13
 @Author  : QDY
 @FileName: 识别_解数独.py
 @Software: PyCharm
"""


# # 从截图中识别文字 pip install baidu-aip
# from PIL import ImageGrab
# from aip import AipOcr
# import keyboard
# import pytesseract
# import time


def solveSudoku(board):
    """
    Do not return anything, modify board in-place instead.
    """
    rows = [set() for i in range(9)]
    columns = [set() for i in range(9)]
    boxes = [[set(), set(), set()] for i in range(3)]

    for i in range(9):  # 把已有的元素放入
        for j in range(9):
            if board[i][j] != '/':
                rows[i].add(board[i][j])
                columns[j].add(board[i][j])
                boxes[i // 3][j // 3].add(board[i][j])

    # print(boxes)
    def check(num, x, y):  # 检查num是否可以放在(x,y)处
        if num in rows[x] or num in columns[y] or num in boxes[x // 3][y // 3]:
            return False
        return True

    def place_next(row, col):  # 放置（row,col）的下一个数
        if row == 8 and col == 8:  # 若到达了最后一个，说明找到了一种解法
            nonlocal solved
            solved = True
        else:
            if col == 8:  # 到了最后一列，下一个要处理的位置是(row+1,0)
                backtrace(row + 1, 0)
            else:  #
                backtrace(row, col + 1)

    def backtrace(row, col):
        if board[row][col] == '/':
            for i in range(1, 10):
                n = str(i)
                if check(n, row, col):
                    rows[row].add(n)  # 添加n
                    columns[col].add(n)
                    boxes[row // 3][col // 3].add(n)
                    board[row][col] = n

                    place_next(row, col)  # 设置下一个元素

                    if not solved:  # 若solved仍为False，说明这个位置不能放n，需要尝试下一个(n+1)
                        rows[row].remove(n)  # 还原
                        columns[col].remove(n)
                        boxes[row // 3][col // 3].remove(n)
                        board[row][col] = '/'
        else:  # 若已有设置好的元素，直接设置下一个位置
            place_next(row, col)

    solved = False
    backtrace(0, 0)
    return board


if __name__ == '__main__':
    # # 获取截图
    # keyboard.wait(hotkey='alt+a')
    # keyboard.wait(hotkey='enter')
    # time.sleep(0.1)
    #
    # # 保存截图
    # image = ImageGrab.grabclipboard()
    # image.save("screen.png")
    #
    # # 利用百度API
    # APP_ID = '18502413'
    # API_KEY = 'kDwiHVaGzhWA0UMXrvMhjbOS'
    # SECRET_KEY = 'GXdKyckq9V4FUGoHm5EHH2HL9S8IGET2'
    #
    # client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    #
    # # 读取图片
    # with open("screen.png", 'rb') as f:
    #     image = f.read()
    #
    #     # 调用百度API通用文字识别（高精度版），提取图片中的内容
    #     text = client.basicAccurate(image)
    #     result = text["words_result"]
    #     for i in result:
    #         print(i["words"])

    #
    board = []
    for i in range(9):
        tmp = list(input())
        board.append(tmp)
    solveSudoku(board)
    for i in board:
        print(i)
