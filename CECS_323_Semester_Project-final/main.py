import logging

from BuildingType import BuildingType
from Door import Door
from DoorName import DoorName
from Employee import Employee
from Hook import Hook
from KeyCopy import KeyCopy
from Request import Request
from RequestStatus import RequestStatus
from Room import Room
from sqla_util import *

import ClassHandling

# def consoleUI() -> None:
#     check = False
#     while check is not True:
#         #display options
#         print("Database UI:")
#         print("Enter a to create a new key")
#         print("Enter b to create a request with a given employee")
#         print("Enter c to report a lost key")
#         print("Enter d to report all the rooms an employee can enter with their current key")
#         print("Enter e to delete a key")
#         print("Enter f to delete an employee")
#         print("Enter g to enter a new door that can be opened by an existing hook")
#         print("Enter h to update an access request to move it to a new employee")
#         print("Enter i to get a report on all employees who can get into a room")
#         print("Enter j to exit")
#
#
#         userPrompt = input()
#         #Initial cases check; none of these call the functions
#         if userPrompt == 'a': #addKey
#             userInput = []
#             print('Enter a key_id: ')
#             key_id_prompt = input()
#             userInput.append(key_id_prompt)
#             print('Enter a hook to associate with the key: ')
#             hook_id_prompt = input()
#             userInput.append(hook_id_prompt)
#             ClassHandling.addKey(key_id_prompt,hook_id_prompt)
#         if userPrompt == 'b':#makeRequest
#             print('Enter an employee number: ')
#             employ_id_prompt = input()
#             print('Enter a building name: ')
#             build_name_prompt = input()
#             print('Enter a room number')
#             room_num_prompt = input()
#             ClassHandling.makeRequest(employ_id_prompt,build_name_prompt,room_num_prompt)
#             #come back to this using Jared's suggestion
#         if userPrompt == 'c': #updateStatus on LOST key specifically
#             print('Enter Request ID: ')
#             request_id_prompt = input()
#             request_status = RequestStatus.LOST
#             ClassHandling.updateStatus(request_id_prompt,request_status)
#         if userPrompt == 'd': #getDoor; iterate through door list
#             print('')
#         if userPrompt == 'e': #deleteKey
#             print('')
#         if userPrompt == 'f': #deleteEmployee
#             print('')
#         if userPrompt == 'g': #addDoor
#             print('Enter building: ')
#             building_prompt = input()
#             print('Enter Room number: ')
#             room_num_prompt = input()
#             print('Enter Door Location: ')
#             location_prompt = input()
#             ClassHandling.addDoor(building_prompt,room_num_prompt,location_prompt)
#         if userPrompt == 'h': #deleteRequest then makeRequest with new employee
#             print('')
#         if userPrompt == 'i': #report all employees that can get into a room
#             print('')
#         if userPrompt == 'j': #finish
#             print('Done')
#             check = True


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
        print("Enter j to get all keys that an employee has")
        print("Enter k to exit")


        userPrompt = input()
        #Initial cases check; none of these call the functions

        if userPrompt == 'a': #addKey
            done = False
            while not done:
                print('Current Keys: ') # getHooks -> getKeys so users know if key exists or not
                hookList = ClassHandling.getHooks()
                for item in hookList:
                    print(ClassHandling.getKeys(item))
                try:
                    key_id: int = int(input('Enter a key_id: '))
                except ValueError:
                    print("That is not a valid integer")
                    continue
                try:
                    hook_id: int = int(input('Enter a hook to associate with the key: '))
                except ValueError:
                    print("That is not a valid integer")
                    continue
                key: KeyCopy = ClassHandling.addKey(key_id, hook_id)
                print('Key:', key)
                done = True
        if userPrompt == 'b': #makeRequest
            print('Enter an employee number: ')
            employ_id_prompt = input()
            print('Enter a building name: ')
            build_name_prompt = input()
            print('Enter a room number')
            room_num_prompt = input()
            request: Request = ClassHandling.makeRequest(employ_id_prompt, build_name_prompt, room_num_prompt)
            print("Request:", request)
        if userPrompt == 'c': #updateStatus on LOST key specifically
            try:
                request_id: int = int(input('Enter Request ID: '))
                if ClassHandling.updateStatus(request_id, RequestStatus.LOST):
                    print(f"Successfully assigned Request ID {request_id} to LOST.")
                else:
                    print(f"Failed to reassign Request ID {request_id}.")
            except ValueError:
                print("That is not a valid integer")
                continue
        if userPrompt == 'd': #getDoor; iterate through door list
            try:
                key_id: int = int(input('Enter a key ID: '))
            except ValueError:
                print("That is not a valid integer")
                continue
            print("Doors:")
            for door in ClassHandling.getDoors(key_id):
                print(f"\t{door}")
        if userPrompt == 'e': #deleteKey
            pass
        if userPrompt == 'f': #deleteEmployee
            pass
        if userPrompt == 'g': #add door to existing hook
            print('Enter building: ')
            building_prompt = input()
            print('Enter Room number: ')
            room_num_prompt = input()
            print('Enter Door Location: ')
            location_prompt = input()
            ClassHandling.addDoor(building_prompt, room_num_prompt, location_prompt)
        if userPrompt == 'h': #deleteRequest then makeRequest with new employee
            pass
        if userPrompt == 'i': #report all employees that can get into a room
            room_name: str = input("Enter Building Name: ")
            try:
                room_id: int = int(input('Enter Room Number: '))
            except ValueError:
                print("That is not a valid integer")
                continue
            room: Room = ClassHandling.getRoom(room_name, room_id)
            if room is None:
                print("That room does not exist!")
                continue
            requestList: [Request] = ClassHandling.getRequestsByRoom(room)

            printStr: str = f"Room accessible by:\n"
            for request in requestList:
                if ClassHandling.getRequestStatus(request) == RequestStatus.OUT:
                    employee: Employee = ClassHandling.getEmployee(request.employees_id)
                    printStr += f"\t{employee}\n"
            print(printStr)
        if userPrompt == 'j': #get keys owned by a specific employee
            try:
                employee_id: int = int(input("Please provide an employee ID: "))
            except ValueError:
                print("That is not a valid integer.")
                continue
            employee: Employee = ClassHandling.getEmployee(employee_id)
            if employee is None:
                print("That is not a valid employee!")
                continue
            keys: [KeyCopy] = ClassHandling.getKeysByEmployee(employee)
            print(f"Employee {employee_id} has the following keys: {keys}")
        if userPrompt == 'k': #finish
            print('Done')
            check = True

def main():
    logging.basicConfig()
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
    logging.getLogger("sqlalchemy.pool").setLevel(logging.DEBUG)

    building: BuildingType = ClassHandling.addBuilding("VEC")
    room: Room = ClassHandling.addRoom(building, 300)
    doorName: DoorName = ClassHandling.addDoorName("North")
    employee: Employee = ClassHandling.addEmployee("Jared Seville")
    print(building)
    print(room)
    print(doorName)
    door: Door = ClassHandling.addDoor(building, room, doorName)
    doors = [door]
    Hook1: Hook = ClassHandling.addHook(1, doors)
    print(door)
    consoleUI()


if __name__ == '__main__':
    main()
