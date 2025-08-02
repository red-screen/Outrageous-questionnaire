from tkinter import *
from tkinter.messagebox import *
from random import randint
from threading import Thread,Timer
from os import system
#一个整活问卷
#update:
#·禁用浏览器，使调查者选择了外语成绩好时就痛不欲生

swap_state = [False]

a = Tk()
a.title("问卷调查")
a.geometry("500x500")
def kill():
    browsers = ["chrome.exe", "msedge.exe", "firefox.exe", "iexplore.exe", "opera.exe"]
    for x in browsers:
        try:
            system(f"taskkill /f /im {x}")
            Timer(1, lambda:kill()).start()
        except:
            continue
Thread(target=lambda:kill())
def main():
    def noclear():
        pass
    def clear_window():
        for widget in root.winfo_children():
            widget.destroy()
    a.destroy()
    root = Tk()
    root.title("问卷调查")
    root.geometry("500x500")
    root.protocol("WM_DELETE_WINDOW",noclear)
    firstquestion = Label(root, text="你喜欢老师这个职业吗？")
    firstquestion.place(x=150, y=150)
    def question1():
        print('就知道你会喜欢的')
        showinfo(title='小惊喜',message='后面好像出现了点东西......')
        def question2(a):
            print('优秀：30分，还行：20分，差：0分')
            print('满分100分')
            print('你的成绩是：{}'.format(a))
            clear_window()
            thirdquestion = Label(root, text="你认同布置作业吗？")
            thirdquestion.place(x=150, y=150)
            def hehehe():
                answer2.place(x=200,y=200)
                root.after(200,lambda:answer2.place(x=120,y=200))
                root.after(300,lambda:answer2.place(x=220,y=250))
                root.after(500,lambda:answer2.place(x=496,y=496))
                print('小提示：只有一个像素（可以点击）\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                showinfo(title='小提示',message='看看后面')
                def OK():
                    huh = askyesno(title='真的？',message='你真的吗选择不认同吗?')
                    if huh:
                        huh = askyesno(title='really?',message='真的吗？')
                        if huh:
                            huh=askyesno(title='huh？',message='真的真的真的吗？')
                            if huh:
                                huh=askyesno(title='真的？',message='确定吗？成败在此一举！')
                                if huh:
                                    huh = askyesno(title='真的？',message='真的吗？你的答案会发送至教育局！')
                                    if huh:
                                        huh = askyesno(title='（沮丧）',message='好吧，你赢了。')
                                        if huh:
                                            OK()
                answer2.config(command=lambda:OK())
            def next():
                clear_window()
                question3 = Label(root, text="你外语成绩好吗？")
                def last_question():
                    clear_window()
                    def will():
                        global swap_state
                        if swap_state[0]:
                            answer1.place(x=150, y=250)
                            answer2.place(x=240, y=250)
                        else:
                            answer1.place(x=240, y=250)
                            answer2.place(x=150, y=250)
                        swap_state[0] = not swap_state[0]
                    def no():
                        showinfo(title='结束', message='问卷调查到此结束，感谢调查!')
                        exit()
                    question1 = Label(root, text="你会把作业烧了吗？")
                    answer1 = Button(root, text="会",bg='red',fg='yellow',command=lambda:will())
                    answer2 = Button(root, text="不会",bg='green',fg='yellow',command=lambda:no())
                    question1.place(x=150, y=150)
                    answer1.place(x=150, y=250)
                    answer2.place(x=240, y=250)
                def trying(a):
                    if a:
                        showinfo(title='试试就逝世',message='既然如此，那就来试试吧！')
                    elif not a:
                        showinfo(title='试试就逝世',message='虽然一般，但还是来试试吧！')
                    clear_window()
                    english1 = Label(root, text="翻译至英文:python是世界上最好的编程语言！")
                    english1.place(x=150, y=150)
                    input1 = Entry(root)
                    input1.place(x=150, y=200)
                    def check(answer):
                        def freach():
                            def check2(ddd):
                                if ddd == 'В качестве команды мы должны быть едиными и неразрывными.':
                                    showinfo(title='恭喜', message='你答对了！')
                                    last_question()
                                else:
                                    showerror(title='错误', message='答案错误！请再试一次。')
                            clear_window()
                            showinfo(title='恭喜', message='你答对了！')
                            french1 = Label(root, text="翻译至俄语：En tant qu’équipe, nous devons être unis et incassables.")
                            input1= Entry(root)
                            input1.place(x=150, y=200)
                            french1.place(x=150, y=150)
                            realy = Button(root, text="提交", command=lambda:check2(input1.get()))
                            realy.place(x=150, y=250)
                        if answer == 'Python is the best programming language in the world!':
                            freach()
                        else:
                            showerror(title='错误', message='答案错误！请再试一次。')
                    realy = Button(root, text="提交", command=lambda:check(input1.get()))
                    realy.place(x=150, y=250)
                answer1 = Button(root, text="好",bg='green',fg='yellow',command=lambda:trying(1))
                answer2 = Button(root, text="还行",bg='red',fg='yellow',command=lambda:trying(0))
                answer3 = Button(root, text="不行",bg='orange',fg='purple',command=lambda:last_question())
                question3.place(x=150, y=150)
                answer1.place(x=300, y=250)
                answer2.place(x=220, y=250)
                answer3.place(x=150, y=250)
            answer1 = Button(root, text="认同",bg='orange',fg='red',command=lambda:next())
            answer2 = Button(root, text="不认同",bg='green',fg='yellow',command=lambda:hehehe())
            answer1.place(x=220, y=250)
            answer2.place(x=150, y=250)
        clear_window()
        secondquestion = Label(root, text="你成绩平均怎么样？")
        secondquestion.place(x=150, y=150)
        answer1 = Button(root, text="优秀",command=lambda:question2(30),bg='green',fg='yellow')
        answer2 = Button(root, text="还行",command=lambda:question2(20),bg='orange',fg='purple')
        answer3= Button(root, text="非常差",command=lambda:question2(0),bg='red',fg='yellow')
        answer1.place(x=300, y=250)
        answer2.place(x=220, y=250)
        answer3.place(x=150, y=250)
    answer1 = Button(root, text="喜欢",command=question1,bg='green',fg='yellow')
    answer1.place(x=240, y=250)
    answer2 = Button(root, text="喜欢",command=question1,bg='orange',fg='yellow')
    answer2.place(x=150, y=250)
start = Button(a, text="开始调查", command=lambda:Thread(target=lambda:main()))
start.place(x=240, y=240)

mainloop()
