from operator import itemgetter


class Musician:
    """Музыкант"""
    def __init__(self, id, fio, salary, orch_id):
        self.id = id
        self.fio = fio
        self.salary = salary
        self.orch_id = orch_id


class Orchestra:
    """Оркестр"""
    def __init__(self, id, name):
        self.id = id
        self.name = name


class MusOrch:
    """Музыканты оркестра (для связи многие-ко-многим)"""
    def __init__(self, orch_id, mus_id):
        self.orch_id = orch_id
        self.mus_id = mus_id


# Оркестры
orchestras = [
    Orchestra(1, 'Академический оркестр'),
    Orchestra(2, 'Камерный оркестр'),
    Orchestra(3, 'Духовой оркестр'),
    Orchestra(4, 'Альтернативный оркестр'),
]

# Музыканты
musicians = [
    Musician(1, 'Соколов', 60000, 1),
    Musician(2, 'Морозова', 55000, 1),
    Musician(3, 'Лебедев', 48000, 2),
    Musician(4, 'Попов', 52000, 2),
    Musician(5, 'Никитина', 45000, 3),
    Musician(6, 'Волков', 47000, 3),
]

# Музыканты оркестров
mus_orch = [
    MusOrch(1, 1),
    MusOrch(1, 2),
    MusOrch(2, 3),
    MusOrch(2, 4),
    MusOrch(3, 5),
    MusOrch(3, 6),
    MusOrch(4, 1),
    MusOrch(4, 3),
    MusOrch(4, 6),
]


def main():
    # Соединение данных один-ко-многим
    one_to_many = [(m.fio, m.salary, o.name)
                   for o in orchestras
                   for m in musicians
                   if m.orch_id == o.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(o.name, mo.orch_id, mo.mus_id)
                         for o in orchestras
                         for mo in mus_orch
                         if o.id == mo.orch_id]

    many_to_many = [(m.fio, m.salary, orch_name)
                    for orch_name, orch_id, mus_id in many_to_many_temp
                    for m in musicians if m.id == mus_id]

    print('Задание Д1')
    res_1 = [(fio, orch) for fio, _, orch in one_to_many if fio.endswith('ов')]
    print(res_1)

    print('\nЗадание Д2')
    res_2_unsorted = []
    for o in orchestras:
        # зарплаты музыкантов оркестра
        sals = [sal for _, sal, name in one_to_many if name == o.name]
        if len(sals) > 0:
            avg_sal = round(sum(sals) / len(sals), 2)
            res_2_unsorted.append((o.name, avg_sal))
    res_2 = sorted(res_2_unsorted, key=itemgetter(1), reverse=True)
    print(res_2)

    print('\nЗадание Д3')
    res_3 = {}
    for o in orchestras:
        if o.name.startswith('А'):
            names = [fio for fio, _, name in many_to_many if name == o.name]
            res_3[o.name] = names
    print(res_3)


if __name__ == '__main__':
    main()
