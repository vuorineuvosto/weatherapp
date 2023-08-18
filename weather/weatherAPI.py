#####################################################################################################
import requests
import json


class API:
    #gets the apikey from constructor when "app" object created in "main"
    def __init__(self, apikey):
        self.__apikey = apikey
        self.baseURL = "https://pfa.foreca.com"


    def get_location(self, city_name):
        endpoint = "/api/v1/location/search/"

        #it is possible to use country prefixes to get only certain country's weather data
        """   params = {
                "country" : "FI"
            } """

        response = requests.get(f"{self.baseURL}{endpoint}{city_name}{self.__apikey}")
        
        try: 
            cityID = response.json()["locations"][0]["id"]
        except IndexError:
                print("Check your city input!")
                return
        else:
             pass

        return cityID
   

    def get_current_weather(self, ID):
        endpoint = "/api/v1/current/"

        params = {
            "location" : ID
        }

        response = requests.get(f"{self.baseURL}{endpoint}{self.__apikey}", params=params)
        
        return response.json()


    def get_hourly_weather(self, ID):
         endpoint = "/api/v1/forecast/hourly/"

         params = {
            "location" : ID
        }
         
         response = requests.get(f"{self.baseURL}{endpoint}{self.__apikey}", params=params)
         
         return response.json()
    
    
    def get_daily_weather(self, ID):
         endpoint = "/api/v1/forecast/daily/"

         params = {
            "location" : ID,
            "periods" : "5"
        }
         
         response = requests.get(f"{self.baseURL}{endpoint}{self.__apikey}", params=params)
         
         return response.json()
    
#####################################################################################################