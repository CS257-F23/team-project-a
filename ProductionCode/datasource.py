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

    
    def getHostInfo(self, host_id):
        """
        Gets information about the specified star 
        by querying the star_data database
        Param: int
        Returns: tuple of lists
        """
        cursor = self.connection.cursor()
        query = "SELECT * FROM star_data WHERE host_id=%s;"
        cursor.execute(query, (host_id,))
        databaseStarList = cursor.fetchall()

        return databaseStarList

    def formatDatabaseLists(self, databasePlanetList, databaseStarList):
        """
        Takes info from exoplanet_data and corresponding info from
        star_data and merges them into a one ordered list
        Param: tuple of lists, tuple of lists
        Returns: list
        """
        mergedInfoList = []
        #The info from exoplanet_data and star_data must be added in a particular order
        #to match how the planet info page wants it 
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

    def getPlanetInfo(self, planet_name):
        """
        Creates a list of information about the specified planet 
        and the star it occupies by querying the exoplanet_data database
        Param: string
        Returns: list
        """
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM exoplanet_data WHERE planet_name=%s;"
            cursor.execute(query, (planet_name,))
            databasePlanetList = cursor.fetchall()

            host_id = int(databasePlanetList[0][9])
            databaseStarList = self.getHostInfo(host_id)

            mergedInfoList = self.formatDatabaseLists(databasePlanetList, databaseStarList)

            return mergedInfoList
        
        #Failsafe in case of any problems
        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None

    def getRandomPlanetInfo(self, planet_id):
        
        """
        Creates a list of information about the planet with the specified planet id
        and the star it occupies by querying the exoplanet_data database
        Called "Random" because the function is only used for the "Random Planet" feature
        Param: int
        Returns: list
        """
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM exoplanet_data WHERE planet_id=%s;"
            cursor.execute(query, (planet_id,))
            databasePlanetList = cursor.fetchall()

            host_id = int(databasePlanetList[0][9])
            databaseStarList = self.getHostInfo(host_id)

            mergedInfoList = self.formatDatabaseLists(databasePlanetList, databaseStarList)

            return mergedInfoList
        
        #Failsafe in case of any problems
        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None
    
    def getPlanetNameFromId (self, planet_id):
        """
        Queries the exoplanet_data database to find the name of a planet
        based on its planet id
        Param: int
        Returns: string
        """
        try:
            cursor = self.connection.cursor()
            query = "SELECT planet_name FROM exoplanet_data WHERE planet_id=%s;"
            cursor.execute(query, (planet_id,))
            planet_name_tuple = cursor.fetchall()
            planet_name = planet_name_tuple[0][0]

            return planet_name
        
        #Failsafe in case of any problems
        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None
