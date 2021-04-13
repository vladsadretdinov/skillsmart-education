class Heap:
    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи
        self.free_slot_index = 0

    def MakeHeap(self, a, depth):
        # создаём массив кучи HeapArray из заданного
        # размер массива выбираем на основе глубины depth
        # глубина корня считаю равной единице
        self.HeapArray = [None] * ((2 ** depth) - 1)
        for elem in a:
            is_added = self.Add(elem)
            if is_added is False:
                return None
        return None

    def GetMax(self):
        # вернуть значение корня и перестроить кучу
        if self.HeapArray[0] is None:
            # если куча пуста
            return -1

        response = self.HeapArray[0]

        current_root_index = 0
        last_existing_index = self.free_slot_index - 1
        self.free_slot_index = self.free_slot_index - 1
        self.HeapArray[current_root_index] = self.HeapArray[last_existing_index]
        self.HeapArray[last_existing_index] = None
        max_child_index = current_root_index

        while True:
            current_root_index = max_child_index
            left_child_index = current_root_index * 2 + 1
            right_child_index = current_root_index * 2 + 2

            if (
                self.HeapArray[left_child_index] is not None
                and self.HeapArray[left_child_index] > self.HeapArray[max_child_index]
            ):
                max_child_index = left_child_index
            if (
                self.HeapArray[right_child_index] is not None
                and self.HeapArray[right_child_index] > self.HeapArray[max_child_index]
            ):
                max_child_index = right_child_index

            if max_child_index != current_root_index:
                self.HeapArray[current_root_index], self.HeapArray[max_child_index] = (
                    self.HeapArray[max_child_index],
                    self.HeapArray[current_root_index],
                )
            else:
                return response

    def Add(self, key):
        # добавляем новый элемент key в кучу и перестраиваем её

        if self.free_slot_index >= len(self.HeapArray):
            return False

        # если куча пустая - добавить элемент как корень
        if self.HeapArray[0] is None:
            self.HeapArray[0] = key
            self.free_slot_index = self.free_slot_index + 1
            return True

        if self.free_slot_index % 2 == 0:
            parent_index = (self.free_slot_index - 2) // 2
        else:
            parent_index = (self.free_slot_index - 1) // 2

        slot_index = self.free_slot_index
        self.free_slot_index = self.free_slot_index + 1

        while parent_index >= 0 and self.HeapArray[parent_index] < key:
            self.HeapArray[slot_index] = self.HeapArray[parent_index]
            self.HeapArray[parent_index] = key

            slot_index = parent_index
            if parent_index % 2 == 0:
                parent_index = (parent_index - 2) // 2
            else:
                parent_index = (parent_index - 1) // 2
        else:
            self.HeapArray[slot_index] = key
            return True
