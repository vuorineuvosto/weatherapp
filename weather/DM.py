#####################################################################################################


class DataManager:


    def extract_data(unsorted_data, master_key, *args):
        
        sorted_data = []
        
        if master_key == "current":


            place_holder = []

            #for "current", there is only one member in the dict/json so this is enough
            for i in range(0, len(args)):
                value = unsorted_data[master_key][args[i]]
                print(value)
                place_holder.append(value)

            sorted_data.append(place_holder)

        else:
            
            day = 0 #day / hour
                #for every entry in the unsorted["forecast"]["x"]
            for _ in unsorted_data[master_key]: #unsorted_data structure: [[point1], [point2], [etc.]]
                place_holder = []               #used to pass only the current point's data to sorted_data[] as nested list
                #searches for every given parameter in one measurepoint's data
                for j in range(0, len(args)):
                    value = unsorted_data[master_key][day][args[j]] #args = ("yksi", "kaksi", "kolme"...)
                    print(value)
                    place_holder.append(value)

                #add one measurepoint as nested list
                sorted_data.append(place_holder)
                
                day = day + 1

        return sorted_data
#####################################################################################################