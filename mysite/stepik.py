class CPU:
    def __init__(self, name:str, fr:int):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name:str, volume:int):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name: str, cpu: CPU, *mem_slots: Memory):
        self.total_mem_slots = 4
        self.name = name
        self.cpu = cpu
        self.mem_slots = list(*mem_slots[:4])

    def get_config(self):
        lst = []
        lst.append(f'Материнская плата: {self.name}')
        lst.append(f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}')
        lst.append(f'Слотов памяти: {self.total_mem_slots}')
        lst.append('Память: ' + "; ".join([f'{mem.name} - {mem.volume}' for mem in self.mem_slots]))
        return lst



mb = MotherBoard('Материнка', CPU('суперпроц', 1000), [Memory('мозг1', 100), Memory('мозг2', 200)])

assert isinstance(mb, MotherBoard) and hasattr(MotherBoard, 'get_config')


def get_config():
    mem_str = "; ".join([f"{x.name} - {x.volume}" for x in mb.mem_slots])

    return [f"Материнская плата: {mb.name}",
            f"Центральный процессор: {mb.cpu.name}, {mb.cpu.fr}",
            f"Слотов памяти: {mb.total_mem_slots}",
            f"Память: {mem_str}"]


res1 = ("".join(mb.get_config())).replace(" ", "")
res2 = ("".join(get_config())).replace(" ", "")
assert res1 == res2, "метод get_config возвратил неверные данные"