import logging

from BuildingType import BuildingType
from Door import Door
from DoorName import DoorName
from Request import Request
from RequestStatus import RequestStatus
from Room import Room
from sqla_util import *

import ClassHandling

def consoleUI() -> None:
    check = False
    while check is not True:
        #display options
        print("Database UI:")
        print("Enter a to create a new key")
        print("Enter b to create a request with a given employee")
        print("Enter c to report a lost key")
        print("Enter d to report all the rooms an employee can enter with their current key")
        print("Enter e to delete a key")
        print("Enter f to delete an employee")
        print("Enter g to enter a new door that can be opened by an existing hook")
        print("Enter h to update an access request to move it to a new employee")
        print("Enter i to get a report on all employees who can get into a room")
        print("Enter j to exit")


        userPrompt = input()
        #Initial cases check; none of these call the functions
        match userPrompt:
            case 'a': #addKey
                userInput = []
                print('Enter a key_id: ')
                key_id_prompt = input()
                userInput.append(key_id_prompt)
                print('Enter a hook to associate with the key: ')
                hook_id_prompt = input()
                userInput.append(hook_id_prompt)
                ClassHandling.addKey(key_id_prompt,hook_id_prompt)
            case 'b':#makeRequest
                print('Enter an employee number: ')
                employ_id_prompt = input()
                print('Enter a building name: ')
                build_name_prompt = input()
                print('Enter a room number')
                room_num_prompt = input()
                ClassHandling.makeRequest(employ_id_prompt,build_name_prompt,room_num_prompt)
            #come back to this using Jared's suggestion
            case 'c': #updateStatus on LOST key specifically
                print('Enter Request ID: ')
                request_id_prompt = input()
                request_status = RequestStatus.LOST
                ClassHandling.updateStatus(request_id_prompt,request_status)
            case 'd': #getDoor; iterate through door list
                print('')
            case 'e': #deleteKey
                print('')
            case 'f': #deleteEmployee
                print('')
            case 'g': #addDoor
                print('Enter building: ')
                building_prompt = input()
                print('Enter Room number: ')
                room_num_prompt = input()
                print('Enter Door Location: ')
                location_prompt = input()
                ClassHandling.addDoor(building_prompt,room_num_prompt,location_prompt)
            case 'h': #deleteRequest then makeRequest with new employee
                print('')
            case 'i': #report all employees that can get into a room
                print('')
            case 'j': #finish
                print('Done')
                check = True


def main():
    logging.basicConfig()
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
    logging.getLogger("sqlalchemy.pool").setLevel(logging.DEBUG)

    consoleUI()


if __name__ == '__main__':
    main()
