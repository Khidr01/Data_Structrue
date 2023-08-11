class Selection_sort():
    def __init__(self, Arr):
        print("Selection Sort Algorithm is created")
        self.arr = Arr
        self.insert_ind = 0

    def selection_sort(self):
        print("In function Selection Sort")

        len_arr = len(self.arr)
        print("Array length: {}".format(len_arr))
        while self.insert_ind < len_arr:

            print("In loop")
            sm_ind = self.find_sm_index(self.insert_ind)
            print("Smallest NUM index: {}".format(sm_ind))

            print("\nInserting {} at position {}\nresult\n {}\n".
                  format(self.arr[sm_ind], self.insert_ind, self.arr))

            self.arr.insert(self.insert_ind, self.arr[sm_ind])

            del self.arr[sm_ind + 1]
            self.insert_ind += 1

            print("After updating values: ")
            print("Array: {}\nInserting Index Value: {}".
                  format(self.arr, self.insert_ind))

            print("loop number: {} ended\n\n".format(self.insert_ind))

        return self.arr

    def find_sm_index(self, start_pos):

        print("\t\tIn function find_sm_index")
        sm = self.arr[start_pos]
        print("\t\tsm: {}\n\t\tarr[start_pos]: {}".
              format(sm, self.arr[start_pos]))
        id = start_pos
        for i in range(start_pos, len(self.arr)):
            if sm > self.arr[i]:
                sm = self.arr[i]
                id = i
        print("\t\tSmallest NUM: {}\n\t\tITS Index: {}\n\n".
              format(sm, id))
        return id


x_arr = []

arr_len = int(input("How many element you want to enter: "))

for i in range(arr_len):
    x_arr.append(int(input("Element{0}: ". format(i+1))))

selection_obj = Selection_sort(x_arr)
print(f"Result: {selection_obj.selection_sort()}")
