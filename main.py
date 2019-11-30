# -*- coding: utf-8 -*-
import sys

clients = ['pablo','ricardo']

def create_client(client_name):
    """ Aqui creamos al cliente"""
    global clients

    print(client_name)
    if client_name not in clients:
        clients.append(client_name)
    else:
        print('The name of client is repeated')


def updated_client(client_name, updated_name):
    global clients

    for idx, client in enumerate(clients):
        if client_name in clients:
            clients[idx] = updated_name
        else:
            _client_not_in_list()


def search_client(client_name):
    global clients

    for client in clients:
        if client != client_name:
            continue
        else:
            return True


def delete_client(client_name):
    global clients

    for idx, client in enumerate(clients):
        if client_name in clients:
           clients.remove(client_name)
        else:
            _client_not_in_list()


def list_clients():
    global clients

    for idx, client in enumerate(clients):
        print(idx+1,client)


def _get_client():
    client_name = None

    while not client_name:
        client_name = input('Whats\' the name of the client? ')

        if client_name == 'exit':
            sys.exit()

    return client_name

def _print_welcome():
    print("WELCOME TO ZACARTE'S GALLERY")
    print('*' * 30)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist clients')
    print('[S]earh client')
    print('[U]pdate client')
    print('[D]elete client')

def _client_not_in_list():
     return print('The client is not in the list')

if __name__ == '__main__':
    _print_welcome()

    command = input('What\'s is your choice? ')
    command = command.upper()

    if command == 'C':
        client_name = _get_client()
        create_client(client_name)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'S':
        client_name = _get_client()
        found = search_client(client_name)

        if found == True:
            print('The client is in the list')
        else:
            print('The client {} is not in the list'.format(client_name))
    elif command == 'U':
        client_name = _get_client()
        updated_name = input('What\'s is the new name of the client? ')
        updated_client(client_name, updated_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client()
        delete_client(client_name)
        list_clients()
    else:
        print('invalid command ')
