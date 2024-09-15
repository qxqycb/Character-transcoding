import tkinter as tk
from tkinter import filedialog, messagebox
import os
import re
input("欢迎使用本程序，按回车键继续")
input("本程序用于将小说文件按章节分割，请确保小说文件格式正确，章节格式为“第X章”，X为数字")
def split_novel_by_chapter():
    # 弹出选择小说文件的窗口
    novel_path = filedialog.askopenfilename(
        title="选择小说文件",
        filetypes=[("文本文件", "*.txt")]
    )
    if not novel_path:
        print("操作已取消。")
        return

    # 检查文件是否存在
    if not os.path.exists(novel_path):
        messagebox.showerror("错误", f"文件 '{novel_path}' 不存在。")
        return

    # 读取文件内容
    try:
        with open(novel_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception as e:
        messagebox.showerror("错误", f"读取文件时发生错误: {e}")
        return

    # 使用正则表达式匹配章节
    chapters = re.split(r'第(\d+)章', content)
    chapter_number = 1

    # 弹出选择保存目录的窗口
    save_dir = filedialog.askdirectory(title="选择保存目录")
    if not save_dir:
        print("保存操作已取消。")
        return

    # 确保保存目录存在
    if not os.path.exists(save_dir):
        messagebox.showerror("错误", f"目录 '{save_dir}' 不存在。")
        return

    # 遍历所有章节并保存为单独的文件
    for i in range(1, len(chapters), 2):
        chapter_title = f"第{chapters[i]}章"
        chapter_content = chapters[i+1].strip()

        # 创建新的文件名
        chapter_filename = os.path.join(save_dir, f"{chapter_title}.txt")

        # 保存章节内容到文件
        try:
            with open(chapter_filename, 'w', encoding='utf-8') as new_file:
                new_file.write(chapter_content)
            print(f"章节 '{chapter_filename}' 已保存。")
        except Exception as e:
            messagebox.showerror("错误", f"保存文件时发生错误: {e}")
            return

    print("章节分割完成！")

if __name__ == "__main__":
    split_novel_by_chapter()