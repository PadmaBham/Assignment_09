#------------------------------------------#
# Title: IO Classes
# Desc: A Module for IO Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# PBhamidipati, 2022-Dec-11, Updated docstrings & code to address all TODOs 
#   and instructions for Assignment 9 (Mod09_B); also, added get_track_to_remove()
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to run by itself')

import DataClasses as DC
import ProcessingClasses as PC

class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    @staticmethod
    def save_inventory(file_name: list, lst_Inventory: list) -> None:
        """


        Args:
            file_name (list): list of file names [CD Inventory, Track Inventory] that hold the data.
            lst_Inventory (list): list of CD objects.

        Returns:
            None.

        """

        # TODone modify method to accept a list of file names.
        try:
            file_name_CD = file_name[0]
            with open(file_name_CD, 'w') as file_CD:
                for disc in lst_Inventory:
                    file_CD.write(disc.get_record())
                file_CD.close()
            
            # TODone add code to save track data to file
            file_name_Track = file_name[1]
            with open(file_name_Track, 'w') as file_Track:
                for disc in lst_Inventory:
                    for track in disc.cd_tracks:
                        file_Track.write("{},{}".format(disc.cd_id, track.get_record()))
            file_Track.close()

        except Exception as e:
            print('There was a general error!', e, e.__doc__, type(e), sep='\n')

    @staticmethod
    def load_inventory(file_name: list) -> list:
        """


        Args:
            file_name (list): list of file names [CD Inventory, Track Inventory] that hold the data.

        Returns:
            list: list of CD objects.

        """

        lst_Inventory = []
        
        # TODone modify method to accept a list of file names
        try:
            file_name_CD = file_name[0]
            try:
                with open(file_name_CD, 'r') as file_CD:
                    for line in file_CD:
                        data = line.strip().split(',')
                        row = DC.CD(data[0], data[1], data[2])
                    lst_Inventory.append(row)
                    file_CD.close()
            except FileNotFoundError as e:
                print("File Does not exist. Creating CD Inventory file")
                with open(file_name_CD, 'w') as file_CD:
                    file_CD.close()
                    
            # TODone add code to load track data
            file_name_Track = file_name[1]
            try:
                with open(file_name_Track, 'r') as file_Track:
                    for line in file_Track:
                        data = line.strip().split(',')
                        cd_id = data[0]
                        track_row: DC.Track = DC.Track()
                        track_row.trPosition = int(data[1])
                        track_row.trTitle = data[2]
                        track_row.trLength = data[3]
                        cd : DC.CD = PC.DataProcessor.select_cd(lst_Inventory, int(cd_id))
                        cd.add_track(track_row)
                    file_Track.close()
            except FileNotFoundError as e:
                print("File Does not exist. Creating Track Inventory file")
                with open(file_name_Track, 'w') as file_Track:
                    file_Track.close()
        except Exception as e:
            print('There was a general error!', e, e.__doc__, type(e), sep='\n')
        return lst_Inventory

class ScreenIO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Main Menu\n\n[l] load Inventory from file\n[a] Add CD / Album\n[d] Display Current Inventory')
        print('[c] Choose CD / Album\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, d, c, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'd', 'c', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, d, c, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def print_CD_menu():
        """Displays a sub menu of choices for CD / Album to the user

        Args:
            None.

        Returns:
            None.
        """

        print('CD Sub Menu\n\n[a] Add track\n[d] Display cd / Album details\n[r] Remove track\n[x] exit to Main Menu')

    @staticmethod
    def menu_CD_choice():
        """Gets user input for CD sub menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices a, d, r or x

        """
        choice = ' '
        while choice not in ['a', 'd', 'r', 'x']:
            choice = input('Which operation would you like to perform? [a, d, r or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print(row)
        print('======================================')

    @staticmethod
    def show_tracks(cd):
        """Displays the Tracks on a CD / Album

        Args:
            cd (CD): CD object.

        Returns:
            None.

        """
        print('====== Current CD / Album: ======')
        print(cd)
        print('=================================')
        print(cd.get_tracks())
        print('=================================')

    @staticmethod
    def get_CD_info():
        """function to request CD information from User to add CD to inventory


        Returns:
            cdId (string): Holds the ID of the CD dataset.
            cdTitle (string): Holds the title of the CD.
            cdArtist (string): Holds the artist of the CD.

        """

        cdId = input('Enter ID: ').strip()
        cdTitle = input('What is the CD\'s title? ').strip()
        cdArtist = input('What is the Artist\'s name? ').strip()
        return cdId, cdTitle, cdArtist

    @staticmethod
    def get_track_info():
        """function to request Track information from User to add Track to CD / Album


        Returns:
            position (string): Holds the ID of the Track dataset.
            title (string): Holds the title of the Track.
            length (string): Holds the length (time) of the Track.

        """

        position = input('Enter Position on CD / Album: ').strip()
        title = input('What is the Track\'s title? ').strip()
        length = input('What is the Track\'s length? ').strip()
        return position, title, length
    
    @staticmethod
    def get_track_to_remove(cd: DC.CD):
        """function to ask the User for a Track position from a CD / Album that is to be removed

        Args:
            cd (CD): CD object.
            
        Returns:
            trkId (string): Holds the ID of the Track dataset.
            

        """
        ScreenIO.show_tracks(cd)
        trkId = input('Enter Position on CD / Album to delete: ').strip()
        return trkId