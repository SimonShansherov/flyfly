from tkinter import *
from tkinter import ttk
import model as m
import os

absFilePath = os.path.abspath(__file__)
path, filename = os.path.split(absFilePath)


def info_table(frame_name, data):
    res_title = data.columns
    res_list = data.values.tolist()
    trv = ttk.Treeview(frame_name, selectmode='browse', height=20)
    trv.place(relx=0.5, rely=1, anchor=S)
    trv['show'] = 'headings'
    trv['column'] = list(res_title)
    for i in res_title:
        trv.column(i, width=150, anchor='c')
        trv.heading(i, text=i)
    for dt in res_list:
        v = [r for r in dt]
        trv.insert("", 'end', values=v)


class App():
    def __init__(self):
        self.root = Tk()
        self.root.title('Find my air-track')
        self.root.geometry('1000x700')
        self.root.iconbitmap(path + "/airplain_icon.ico")
        self.root.resizable(width=False, height=False)

    def clicked(self):
        res = m.get_airports(float(self.latitude_min_entry.get()),
                             float(self.longitude_min_entry.get()),
                             float(self.latitude_max_entry.get()),
                             float(self.longitude_max_entry.get()))
        info_table(self.frame1, res)
        count = Label(self.frame1, text=f'Всего: {res.shape[0]}     ', font=('Arial', 10, 'bold'))
        count.place(x=120, y=210)


    def clicked2(self):
        res = m.get_routes(self.from_entry.get(), self.to_entry.get())
        info_table(self.frame2, res)


    def widgets(self):
        # Создаем набор вкладок
        notebook = ttk.Notebook()
        notebook.pack(expand=True, fill=BOTH)

        # Cоздаем пару фреймвов
        self.frame1 = ttk.Frame(notebook)
        self.frame2 = ttk.Frame(notebook)

        self.frame1.pack(fill=BOTH, expand=True)
        self.frame2.pack(fill=BOTH, expand=True)

        # Фреймы вкладки
        notebook.add(self.frame1, text="Поиск аэропортов")
        notebook.add(self.frame2, text="Поиск маршрутов")


        """ Вкладка "Поиск аэропорта" """
        self.title = Label(self.frame1, text='Координаты', font=('Arial', 15, 'bold'))
        self.title.pack(anchor=N)

        self.frame1_0 = ttk.Frame(self.frame1, borderwidth=0, relief=SOLID)
        self.frame1_0.pack(anchor=N)

        self.frame1_1 = ttk.Frame(self.frame1_0, borderwidth=0, relief=SOLID)
        self.frame1_1.grid(row=0, column=0, sticky="nsew")
        self.frame1_2 = ttk.Frame(self.frame1_0, borderwidth=0, relief=SOLID)
        self.frame1_2.grid(row=0, column=1, sticky="nsew")


        """ Минимальные значения """
        self.min_label = Label(self.frame1_1, text='Минимальные значения', font=('Arial', 10, 'bold'))
        self.min_label.pack(padx=0, pady=0, side=TOP)
        # self.min_label.grid(row=4, column=1 pady=10, padx=10)
        """ Latitude """
        self.latitude_label = Label(self.frame1_1, text='Широта', font=('calibre', 8, 'bold'))
        self.latitude_min_entry = Entry(self.frame1_1, textvariable=StringVar().set(""), font=('calibre', 10, 'normal'))
        self.latitude_label.pack(padx=0, pady=0, side=TOP)
        self.latitude_min_entry.pack(padx=0, pady=0, side=TOP)
        """ Longitude """
        self.longitude_label = Label(self.frame1_1, text='Долгота', font=('calibre', 8, 'bold'))
        self.longitude_min_entry = Entry(self.frame1_1, textvariable=StringVar().set(""), font=('calibre', 10, 'normal'))
        self.longitude_label.pack(padx=0, pady=0, side=TOP)
        self.longitude_min_entry.pack(padx=0, pady=0, side=TOP)

        """ Максимальные значения """
        self.max_label = Label(self.frame1_2, text='Максимальные значения', font=('Arial', 10, 'bold'))
        self.max_label.pack(padx=0, pady=0, side=TOP)
        """ Latitude """
        self.latitude_label = Label(self.frame1_2, text='Широта', font=('calibre', 8, 'bold'))
        self.latitude_max_entry = Entry(self.frame1_2, textvariable=StringVar().set(""), font=('calibre', 10, 'normal'))
        self.latitude_label.pack(padx=0, pady=0, side=TOP)
        self.latitude_max_entry.pack(padx=0, pady=0, side=TOP)
        """ Longitude """
        self.longitude_label = Label(self.frame1_2, text='Долгота', font=('calibre', 8, 'bold'))
        self.longitude_max_entry = Entry(self.frame1_2, textvariable=StringVar().set(""), font=('calibre', 10, 'normal'))
        self.longitude_label.pack(padx=0, pady=0, side=TOP)
        self.longitude_max_entry.pack(padx=0, pady=0, side=TOP)

        "Кнопка поиска"
        self.find_btn = Button(self.frame1, width=15, height=1, text='Поиск', bd=3, command=self.clicked)
        self.find_btn.pack(pady=10)



        """ Вкладка "Поиск маршрутов" """
        self.title2 = Label(self.frame2, text='Из города в город', font=('Arial', 15, 'bold'))
        self.title2.pack(anchor=N, pady=15)

        """ Откуда """
        self.from_label = Label(self.frame2, text='Откуда', font=('Arial', 10, 'bold'))
        self.from_label.pack()
        """ Строка города """
        self.from_entry = Entry(self.frame2, textvariable=StringVar().set(""), font=('calibre', 10, 'normal'))
        self.from_entry.pack()

        """ Куда """
        self.to_label = Label(self.frame2, text='Куда', font=('Arial', 10, 'bold'))
        self.to_label.pack()
        """ Строка города """
        self.to_entry = Entry(self.frame2, textvariable=StringVar().set(""), font=('calibre', 10, 'normal'))
        self.to_entry.pack()

        "Кнопка поиска"
        self.find_btn2 = Button(self.frame2, width=15, height=1, text='Поиск', bd=3, command=self.clicked2)
        self.find_btn2.pack(pady=10)


    def run(self):
        self.widgets()
        self.root.mainloop()



if __name__ == '__main__':
    # app = App()
    # app.run()
    ...
