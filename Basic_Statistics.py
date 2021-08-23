


class StatisStics:

    def __init__(self):
        pass

    def is_even(self,arr_list):
       if arr_list % 2 ==0:
           return True
       else:
           return False

    def get_mean(self,arr_list):
        sumy = sum(arr_list)
        total = len(arr_list)
        mean = sumy /total

        return mean

    def get_median(self,arr_list):

        sorted_array = sorted(arr_list)
        print("The array in sorted order :",sorted_array)
        arr_size =len(sorted_array)

        if self.is_even(arr_size):
            med_index_l = arr_size // 2
            med_index_r = med_index_l - 1
            index_arr =[sorted_array[med_index_r], sorted_array[med_index_l]]
            median = self.get_mean(index_arr)

        else:
            med_index_l = arr_size // 2
            median = sorted_array[med_index_l]


        return median


stats = StatisStics()
array = []
array = eval(input("Please Enter a array list:\t"))
mean =stats.get_mean(array)
print("The Mean Value of the {}  is {}".format(array,mean))
median =stats.get_median(array)
print("The Median Value of {} is {}". format(array,median))





