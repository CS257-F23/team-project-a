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
        mergedInfoList.append(databasePlanetList[0][0]) #Planet name
        mergedInfoList.append(databaseStarList[0][1]) #Host (star) name
        mergedInfoList.append(databaseStarList[0][2]) #Number of stars
        mergedInfoList.append(databaseStarList[0][3]) #Number of planets
        mergedInfoList.append(databasePlanetList[0][1]) #Discovery method
        mergedInfoList.append(databasePlanetList[0][2]) #Discovery year
        mergedInfoList.append(databasePlanetList[0][3]) #Discovery facility 
        mergedInfoList.append(databasePlanetList[0][4]) #Semi-major axis
        mergedInfoList.append(databasePlanetList[0][5]) #Planet radius
        mergedInfoList.append(databasePlanetList[0][6]) #Planet mass
        mergedInfoList.append(databaseStarList[0][4]) #Stellar radius
        mergedInfoList.append(databaseStarList[0][5]) #Stellar mass
        mergedInfoList.append(databaseStarList[0][6]) #Stellar luminosity
        mergedInfoList.append(databasePlanetList[0][7]) #Galactic latitude 
        mergedInfoList.append(databasePlanetList[0][8]) #Galactic longitude 

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

    def getHostIdFromPlanet(self, planet_name):
        '''
        Takes a string planet name and returns the associated id of it's host star
        by querying the exoplanet database
        '''
        
        try:
            cursor = self.connection.cursor()
            query = "SELECT host_id FROM exoplanet_data WHERE planet_name=%s;"
            cursor.execute(query, (planet_name,))
            host_id = cursor.fetchall()
            return host_id
        
        #Failsafe in case of any problems
        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None

    def getGoldilocksValue(self, planet_name):
        """
        Takes planet name and returns corresponding in_goldilocks value
        """
        try:
            cursor = self.connection.cursor()
            query = "SELECT in_goldilocks FROM exoplanet_data WHERE planet_name=%s;"
            cursor.execute(query, (planet_name,))
            goldilocksTuple = cursor.fetchall()
            goldilocksValue = goldilocksTuple[0][0]
            return goldilocksValue

        #Failsafe in case of any problems
        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None
    
    def verify_name_in_database(self, planet_name):
        """
        Checks if string planet name given is in the dataset: 
        if not, print error message and return false, otherwise return true
        Param: string
        Returns: boolean
        """

        cursor = self.connection.cursor()
        query = "SELECT * FROM exoplanet_data WHERE planet_name=%s;"
        cursor.execute(query, (planet_name,))
        databasePlanetList = cursor.fetchall()

        if databasePlanetList == []:
            return False
        else:
            return True 
    
    def createPlanetList (self):
        '''
        Creates and returns a list of all planets in the database.
        Param: none
        Returns: list
        '''
        cursor = self.connection.cursor()
        query = "SELECT planet_name FROM exoplanet_data;"
        cursor.execute(query,)
        databasePlanetTupleList = cursor.fetchall()
        available_planets = self.formatPlanetList(databasePlanetTupleList)
        return available_planets

    def createHabitablePlanetList (self):
        """
        Returns the list of habitable planets
        Param: none
        Returns: list
        """
        try:
            cursor = self.connection.cursor()
            query = "SELECT planet_name FROM exoplanet_data WHERE in_goldilocks= True;"
            cursor.execute(query,)
            databaseHabitablePlanetTupleList = cursor.fetchall()
            habitable_planets = self.formatPlanetList(databaseHabitablePlanetTupleList)
            return habitable_planets

        #Failsafe in case of any problems
        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None

    def formatPlanetList (self, databasePlanetTupleList):
        '''
        Takes a list containing tuples and returns a list containing the first item in each tuple.
        Param: list of tuples
        Return: list of strings
        '''
        available_planets = []
        for i in range(len(databasePlanetTupleList)):
            available_planets.append(databasePlanetTupleList[i][0])
        return available_planets

    def printHabitablePlanetList (self): 
        """
        Prints the list of habitable planets
        Param: none
        Returns: none
        """

        habitable_planets = self.createHabitablePlanetList()
        print("The habitable planets (by Solar Equivalent AU) found in this database are")
        for planet in habitable_planets:
            print(planet)

    def setGoldilocks(self, in_goldilocks, planet_name):
        """
        Takes planet name and sets corresponding in_goldilocks value to given boolean
        Params: boolean, string
        Returns: none
        """
        cursor = self.connection.cursor()
        if in_goldilocks == 'NULL':
            query = "UPDATE exoplanet_data SET in_goldilocks=NULL WHERE planet_name=%s;"
            cursor.execute(query, (planet_name,))
        else:
            query = "UPDATE exoplanet_data SET in_goldilocks=%s WHERE planet_name=%s;"
            cursor.execute(query, (in_goldilocks, planet_name,))
        self.connection.commit()

