import psycopg2
import ProductionCode.psqlConfig as config

class DataSource:
        
     def __init__(self):
        """
        Constructor for DataSource 
        Automatically runs the function to intilize database connection
        """
        self.connection = self.connect()
        pass

     def connect(self):
        """
        Uses the username and password in psqlConfig.py to 
        connect to the remote database
        Prints an error message if connection fails for any reason
        """
        try:
            connection = psycopg2.connect(database=config.database, user=config.user, password=config.password, host="localhost")
        #Failsafe in case of any problems
        except Exception as e:
            print("Connection error: ", e)
            exit()
        return connection

     def getPlanetInfo(self, planet_name):
        """
        Prints a list of information about the specified planet 
        by querying the exoplanet_data database
        Param: string
        Returns: none
        """
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM exoplanet_data WHERE planet_name=%s;"
            cursor.execute(query, (planet_name,))
            databasePlanetList = cursor.fetchall()
            host_id = int(databasePlanetList[0][9])
            query = "SELECT * FROM star_data WHERE host_id=%s;"
            cursor.execute(query, (host_id,))
            databaseStarList = cursor.fetchall()
            print(databaseStarList)

            mergedInfoList = []
            #This is pain
            mergedInfoList.append(databasePlanetList[0][0])
            mergedInfoList.append(databaseStarList[0][1])
            mergedInfoList.append(databaseStarList[0][2])
            mergedInfoList.append(databaseStarList[0][3])
            i = 1
            while i < 7:
                mergedInfoList.append(databasePlanetList[0][i])
                i = i + 1
            mergedInfoList.append(databaseStarList[0][4])
            mergedInfoList.append(databaseStarList[0][5])
            mergedInfoList.append(databaseStarList[0][6])
            mergedInfoList.append(databasePlanetList[0][7])
            mergedInfoList.append(databasePlanetList[0][8])

            return mergedInfoList

            #query2 = 'SELECT * FROM star_data WHERE planet_name=%s'
        
        #Failsafe in case of any problems
        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None

if __name__ == '__main__':
    #Just a test; very similar to the code in app.py 
    my_source = DataSource()
    thing = my_source.getPlanetInfo('14 Her b')
    print(thing)