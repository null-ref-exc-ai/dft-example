import matplotlib.pyplot as plt


def show_dict_on_graphic(title: str, xlabel: str, ylabel: str, values: dict[int, int], one_line: bool, blocking: bool):
    """
    Отображает словарь на графике

    Параметры:
        title - заголовок графика
        xlabel - метка по оси X
        ylabel - метка по оси Y
        dictionary - словарь точек для отображения
        one_line - необходимо ли между точками проводить линию
        blocking - является ли вызов блокирующим
    """

    xs, ys = zip(*values.items()) 
    plt.figure(figsize=(10,8))
    plt.title(title, fontsize=20) 
    plt.xlabel(xlabel, fontsize=15) 
    plt.ylabel(ylabel, fontsize=15) 
    if one_line:
        plt.plot(xs, ys, color="black")
    else:
        plt.scatter(xs, ys, marker = 'o', color="black") 
        for x, y in values.items():
           plt.annotate("", xy = (x, y)) 
    plt.show(block=blocking)