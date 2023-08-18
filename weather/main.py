#####################################################################################################
import weatherAPI
import DM
import map2
import map3



def main_run():
    
    #make an instance off weatherAPI class and call it app
    app = weatherAPI.API("&token=YOURAPIKEY")
    
    while True:
        #check for user inputs
        selected_option = input("Type current, 24hrs, 5day, or exit: ")
        if(selected_option == "exit"):
            exit(0)
        elif(selected_option not in ["current", "24hrs", "5day"]):
            print("Check your option input!")
            continue


        city = input("Give city: ")
        cityID = app.get_location(city)
        if cityID == None:
            continue

    
            #cityID returns valid value so call one of the app's methods according to selected option
        if(selected_option == "current"):
            current_data = app.get_current_weather(cityID) #contains all data what Foreca's api returns
            #sort data according to wanted parameters
            current_sorted = DM.DataManager.extract_data(current_data, "current", "symbol", "temperature", "windSpeed", "time")
            
            map3.plot_curret(current_sorted, city)
            
        elif(selected_option == "24hrs"):
            hourly_data = app.get_hourly_weather(cityID) #contains all data what Foreca's api returns
            hourly_sorted = DM.DataManager.extract_data(hourly_data, "forecast", "symbol", "temperature", "windSpeed", "time")
            
            map2.plot_points(hourly_sorted, city, "Windspeed m/s")
        
        elif(selected_option == "5day"):
            daily_data = app.get_daily_weather(cityID) #contains all data what Foreca's api returns
            daily_sorted = DM.DataManager.extract_data(daily_data, "forecast", "symbol", "maxTemp", "minTemp", "date")
    
            map2.plot_points(daily_sorted, city, "Min. Temperature (°C)")
        

main_run()
#####################################################################################################