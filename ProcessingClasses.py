#------------------------------------------#
# Title: Processing Classes
# Desc: A Module for processing Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# PBhamidipati, 2022-Dec-11, Updated docstrings & code to address all TODOs 
#   and instructions for Assignment 9 (Mod09_B); also, added remove_track() 
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to ran by itself')

import DataClasses as DC

class DataProcessor:
    """Processing the data in the application"""
    @staticmethod
    def add_CD(CDInfo, table):
        """function to add CD info in CDinfo to the inventory table.


        Args:
            CDInfo (tuple): Holds information (ID, CD Title, CD Artist) to be added to inventory.
            table (list of CD objects): 2D data structure (list of CD objects) that holds the data during runtime.

        Returns:
            None.

        """

        cdId, title, artist = CDInfo
        try:
            cdId = int(cdId)
        except:
            raise Exception('ID must be an Integer!')
        row = DC.CD(cdId, title, artist)
        table.append(row)

    @staticmethod
    def select_cd(table: list, cd_idx: int) -> DC.CD:
        """selects a CD object out of table that has the ID cd_idx

        Args:
            table (list): Inventory list of CD objects.
            cd_idx (int): id of CD object to return

        Raises:
            Exception: If id is not in list.

        Returns:
            row (DC.CD): CD object that matches cd_idx

        """
        # TODone add code as required
        cdIndex = 0
        for cd in table:
            if cd.cd_id == int(cd_idx):
                break
            else:
                cdIndex += 1
        return table[cdIndex]

    @staticmethod
    def add_track(track_info: tuple, cd: DC.CD) -> None:
        """adds a Track object with attributes in track_info to cd


        Args:
            track_info (tuple): Tuple containing track info (position, title, Length).
            cd (DC.CD): cd object the tarck gets added to.

        Raises:
            Exception: DESCraised in case position is not an integer.

        Returns:
            None: DESCRIPTION.

        """

        # TODone add code as required
        track = DC.Track()
        track.trPosition = int(track_info[0])
        track.trTitle = track_info[1]
        track.trLength = track_info[2]
        cd.add_track(track)

    @staticmethod
    
    def remove_track(track_position: int, cd: DC.CD) -> None:
        """function to remove a Track from a CD / Album by asking User for the Track position

        Args:
            track_position (int): position no. of the track that is to be deleted from the selected CD.
            cd (DC.CD): CD object
            
        Returns:
            None.
            

        """
        cd.rmv_track(track_position)