import customtkinter as CTk
import math
import time
# , command=lambda: count_primes('save')
from tkinter import filedialog, messagebox
# , command=lambda: count_primes('count')

app = CTk.CTk()


def change_appearande_event(new_mode):
    CTk.set_appearance_mode(new_mode)


def dosieve(lower_bund, limit):

    is_prime = [False] * (limit + 1)
    is_prime[2] = True
    is_prime[3] = True

    for x in range(1, int(math.sqrt(limit)) + 1):
        for y in range(1, int(math.sqrt(limit)) + 1):
            n = 4 * x ** 2 + y ** 2
            if (n <= limit) and ((n % 12 == 1) or (n % 12 == 5)):
                is_prime[n] = not is_prime[n]
            n -= x ** 2
            if (n <= limit) and (n % 12 == 7):
                is_prime[n] = not is_prime[n]
            n -= 2 * y ** 2
            if (x > y) and (n <= limit) and (n % 12 == 11):
                is_prime[n] = not is_prime[n]

    for i in range(5, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            k = i ** 2
            n = k
            while n <= limit:
                is_prime[n] = False
                n += k
    primes = []
    for num in range(lower_bund, limit + 1):
        if is_prime[num]:
            primes.append(num)
    return primes


def inserter(value):
    numOfSimple.delete('0.0', "end")
    numOfSimple.insert('0.0', value)


def write(st, ed, num):
    file = filedialog.asksaveasfilename(initialdir="/Downloads", filetypes=[("text file", "*.txt")],
                                        defaultextension=".txt")
    with open(file, 'w', encoding="utf-8") as file:
        pass
        first_file_string = "Количество простых чисел в диапазоне от " + str(st) + " до " + str(
            ed) + " = " + str(num) + "\n"
        file.write(first_file_string)
        start_time = time.time()
        primes = dosieve(st, ed)
        for prime in primes:
            string_num = str(prime) + "\n"
            file.write(string_num)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения программы write: {execution_time} секунд")

    messagebox.showinfo("Сохранение файла", "Файл успешно сохранен.")


def count_primes(event):
    try:
        start_def = int(enter_start_num.get())
        end_def = int(enter_end_num.get())

        if start_def >= end_def:
            messagebox.showerror("Ошибка", "Начальное число должно быть меньше конечного.")
            return
        start_time = time.time()
        k = 0
        primes = dosieve(start_def, end_def)
        k = len(primes)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения программы count_primes: {execution_time} секунд")

        if k == 0:
            messagebox.showinfo("Ошибка","В заданном диапазоне нет простых чисел")
        else:
            inserter(k)

        if event == 'save':
            write(start_def, end_def, k)

    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные целые числа.")




app.geometry("360x400")
app.title("Simple numbers finder")
app.resizable(False, False)


simple_number_text = CTk.CTkLabel(app, text="Поиск простых чисел в заданном диапазоне", width=120, height=20, font=("/Users/victoriachelnokova/Desktop/курсовая/Pioner Sans/PionerSans-Regular.ttf", 16))
simple_number_text.place(x=10, y=15)

start = CTk.CTkLabel(app, text="Начало диапазона", font=("/Users/victoriachelnokova/Desktop/курсовая/Pioner Sans/PionerSans-Regular.ttf", 13))
start.place(x=20, y=45)

enter_start_num = CTk.CTkEntry(app, width=190, height=10, placeholder_text="введите число", font=("/Users/victoriachelnokova/Desktop/курсовая/Pioner Sans/PionerSans-Regular.ttf", 12))
enter_start_num.place(x=150, y=50)

end = CTk.CTkLabel(app, text="Конец диапазона", font=(
        "/Users/victoriachelnokova/Desktop/курсовая/Pioner Sans/PionerSans-Regular.ttf", 13))
end.place(x=21, y=75)

enter_end_num = CTk.CTkEntry(app, width=190, height=10, placeholder_text="введите число", font=(
        "/Users/victoriachelnokova/Desktop/курсовая/Pioner Sans/PionerSans-Regular.ttf", 12))
enter_end_num.place(x=150, y=80)

count_button = CTk.CTkButton(app, text="Рассчитать количество простых чисел", width=320, height=35, font=("/Users/victoriachelnokova/Desktop/курсовая/Pioner Sans/PionerSans-Regular.ttf", 13), text_color="white", fg_color="#9F3ED5", hover_color="#876ED7", command=lambda: count_primes('count'))
count_button.place(x=20, y=120)

numOfSimpleText = CTk.CTkLabel(app, text="Количество простых чисел =", font=(
            "/Users/victoriachelnokova/Desktop/курсовая/Pioner Sans/PionerSans-Regular.ttf", 13))
numOfSimpleText.place(x=20, y=168)

numOfSimple = CTk.CTkTextbox(app, width=130, height=3, font=("/Users/victoriachelnokova/Desktop/курсовая/Pioner Sans/PionerSans-Regular.ttf", 12))
numOfSimple.place(x=210, y=170)
numOfSimple.insert("0.0", "0")

spisok = CTk.CTkLabel(app, text="Список простых чисел в заданном диапазоне вы", height=10, font=(
            "/Users/victoriachelnokova/Desktop/курсовая/Pioner Sans/PionerSans-Regular.ttf", 13))
spisok.place(x=20, y=210)

spisok2 = CTk.CTkLabel(app, text="сможете скачать, нажав на кнопку:", height=10, font=(
            "/Users/victoriachelnokova/Desktop/курсовая/Pioner Sans/PionerSans-Regular.ttf", 13))
spisok2.place(x=20, y=228)

save_button = CTk.CTkButton(app, text="Скачать список простых чисел", width=320, height=35,
                                          font=(
                                          "/Users/victoriachelnokova/Desktop/курсовая/Pioner Sans/PionerSans-Regular.ttf",
                                          13), text_color="white", fg_color="#9F3ED5", hover_color="#876ED7", command=lambda: count_primes('save'))
save_button.place(x=20, y=260)

topic = CTk.CTkLabel(app, text="Выбрать тему приложения:", height=10, font=(
            "/Users/victoriachelnokova/Desktop/курсовая/Pioner Sans/PionerSans-Regular.ttf", 13))
topic.place(x=20, y=325)

appearance = CTk.CTkOptionMenu(app, values=["Light", "Dark", "System"], text_color="white", command=change_appearande_event, fg_color="#9E9EF0", button_hover_color="#9292F0", button_color="#9E9EF0", font=(
                                          "/Users/victoriachelnokova/Desktop/курсовая/Pioner Sans/PionerSans-Regular.ttf",
                                          13))
appearance.place(x=200, y=320)

exit_button = CTk.CTkButton(app, text="Завершить", width=100, height=25,
                                         font=(
                                             "/Users/victoriachelnokova/Desktop/курсовая/Pioner Sans/PionerSans-Regular.ttf",
                                             13), text_color="white", fg_color="#9F3ED5", hover_color="#876ED7", command=app.quit)
exit_button.place(x=130, y=365)


app.mainloop()
