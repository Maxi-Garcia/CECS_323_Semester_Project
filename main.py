import logging

from BuildingType import BuildingType
from Door import Door
from DoorName import DoorName
from Hook import Hook
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
        if userPrompt == 'a': #addKey
            userInput = []
            print('Enter a key_id: ')
            key_id_prompt = input()
            userInput.append(key_id_prompt)
            print('Enter a hook to associate with the key: ')
            hook_id_prompt = input()
            userInput.append(hook_id_prompt)
            ClassHandling.addKey(key_id_prompt,hook_id_prompt)
        if userPrompt == 'b':#makeRequest
            print('Enter an employee number: ')
            employ_id_prompt = input()
            print('Enter a building name: ')
            build_name_prompt = input()
            print('Enter a room number')
            room_num_prompt = input()
            ClassHandling.makeRequest(employ_id_prompt,build_name_prompt,room_num_prompt)
            #come back to this using Jared's suggestion
        if userPrompt == 'c': #updateStatus on LOST key specifically
            print('Enter Request ID: ')
            request_id_prompt = input()
            request_status = RequestStatus.LOST
            ClassHandling.updateStatus(request_id_prompt,request_status)
        if userPrompt == 'd': #getDoor; iterate through door list
            print('')
        if userPrompt == 'e': #deleteKey
            print('')
        if userPrompt == 'f': #deleteEmployee
            print('')
        if userPrompt == 'g': #addDoor
            print('Enter building: ')
            building_prompt = input()
            print('Enter Room number: ')
            room_num_prompt = input()
            print('Enter Door Location: ')
            location_prompt = input()
            ClassHandling.addDoor(building_prompt,room_num_prompt,location_prompt)
        if userPrompt == 'h': #deleteRequest then makeRequest with new employee
            print('')
        if userPrompt == 'i': #report all employees that can get into a room
            print('')
        if userPrompt == 'j': #finish
            print('Done')
            check = True


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
        print("Enter j to get all")
        print("Enter k to exit")


        userPrompt = input()
        #Initial cases check; none of these call the functions

        if userPrompt == 'a': #addKey # ask jared to make method
            done = False
            while not done:
                print('Current Keys: ') # getHooks -> getKeys so users know if key exists or not
                hookList = ClassHandling.getHooks()
                for item in hookList:
                    print(ClassHandling.getKeys(item))
                print('Enter a key_id: ')
                key_id_prompt = input()
                print('Enter a hook to associate with the key: ')
                hook_id_prompt = input()
                key = ClassHandling.addKey(key_id_prompt, hook_id_prompt)
                key_id = key.key_id
                print('id: ' + str(key_id))
                key_check = ClassHandling.getKey(key_id_prompt)
                #checks if key was inserted
                if key_id == key_check.id:
                    done = True
                    print('Key inserted')
            print('enter exit to finish')
            userPrompt = input()
        if userPrompt == 'b':#makeRequest
            print('Enter an employee number: ')
            employ_id_prompt = input()
            print('Enter a building name: ')
            build_name_prompt = input()
            print('Enter a room number')
            room_num_prompt = input()
            ClassHandling.makeRequest(employ_id_prompt,build_name_prompt,room_num_prompt)
            #come back to this using Jared's suggestion
        if userPrompt == 'c': #updateStatus on LOST key specifically
            print('Enter Request ID: ')
            request_id_prompt = input()
            request_status = RequestStatus.LOST
            ClassHandling.updateStatus(request_id_prompt, request_status)
        if userPrompt == 'd': #getDoor; iterate through door list
            print('Enter an employee_id:')
            employ_id_prompt = input()
            for door in ClassHandling.getDoors():
                print(door)
        if userPrompt == 'e': #deleteKey
            print('')
        if userPrompt == 'f': #deleteEmployee
            print('')
        if userPrompt == 'g': #addDoor
            print('Enter building: ')
            building_prompt = input()
            print('Enter Room number: ')
            room_num_prompt = input()
            print('Enter Door Location: ')
            location_prompt = input()
            ClassHandling.addDoor(building_prompt,room_num_prompt,location_prompt)
        if userPrompt == 'h': #deleteRequest then makeRequest with new employee
            print('')
        if userPrompt == 'i': #report all employees that can get into a room
            print('')
        if userPrompt == 'j': #get keys owned by a specific employee
            print('')
        if userPrompt == 'k': #finish
            print('Done')
            check = True

def main():
    logging.basicConfig()
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
    logging.getLogger("sqlalchemy.pool").setLevel(logging.DEBUG)

<<<<<<< Updated upstream
=======

    building: BuildingType = ClassHandling.addBuilding("VEC")
    room: Room = ClassHandling.addRoom(building, 300)
    doorName: DoorName = ClassHandling.addDoorName("North")
    print(building)
    print(room)
    print(doorName)
    door: Door = ClassHandling.addDoor(building, room, doorName)
    doors = []
    doors.append(door)
    Hook1: Hook = ClassHandling.addHook(1, doors)
    print(door)
>>>>>>> Stashed changes
    consoleUI()


if __name__ == '__main__':
    main()
