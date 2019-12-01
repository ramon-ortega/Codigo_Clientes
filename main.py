# -*- coding: utf-8 -*-
import sys

clients = [
    {
        'name': 'name',
        'company': 'company',
        'email': 'email',
        'position': 'position',
    },
    {
        'name': 'Ramon',
        'company': 'Wotbi',
        'email': 'ramon@wotbi.com',
        'position': 'Developtment',
    },
    {
        'name': 'Julian',
        'company': 'UAZ',
        'email': 'julian@fisica.uaz.udu.mx',
        'position': 'Investigator',
    }
]

def create_client(client):
    """ Aqui creamos al cliente"""
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('The client is repeated')


def updated_client_function(client_id, updated_client):
    global clients

    if len(clients) -1 >= client_id:
        clients[client_id] = updated_client
    else:
        print('Client not in client\'s list')


def search_client(client_name):
    global clients

    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True


def delete_client(client_id):
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx]
            break

def list_clients():
    global clients

    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']))


def _get_client_field(field_name):
    field = None

    while not field:
        field = input('Whats is the client {}: '.format(field_name))
    return field

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
        client = {
           'name': _get_client_field('name'),
           'company': _get_client_field('company'),
           'email': _get_client_field('email'),
           'position': _get_client_field('position'),
}
        create_client(client)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'S':
        client_name = _get_client_field('name')

        found = search_client(client_name)

        if found == True:
            print('The client is in the list')
        else:
            print('The client {} is not in the list'.format(client_name))
    elif command == 'U':
        client_id = int(_get_client_field('id'))
        print('*' * 30)
        print('Enter the new customer data')
        updated_client = {
           'name': _get_client_field('name'),
           'company': _get_client_field('company'),
           'email': _get_client_field('email'),
           'position': _get_client_field('position'),
}
        updated_client_function(client_id, updated_client)
        list_clients()
    elif command == 'D':
        client_id = int(_get_client_field('id'))
        delete_client(client_id)
        list_clients()
    else:
        print('invalid command ')
