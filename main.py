# -*- coding: utf-8 -*-
import sys
import csv
import os

CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []


def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name, CLIENT_TABLE)


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


def _client_enter_data():
    client = None

    client = {
           'name': _get_client_field('name'),
           'company': _get_client_field('company'),
           'email': _get_client_field('email'),
           'position': _get_client_field('position'),
}

    return client

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
    _initialize_clients_from_storage()
    _print_welcome()

    command = input('What\'s is your choice? ')
    command = command.upper()

    if command == 'C':
        client = _client_enter_data()
        create_client(client)
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
        updated_client = _client_enter_data()
        updated_client_function(client_id, updated_client)
    elif command == 'D':
        client_id = int(_get_client_field('id'))
        delete_client(client_id)
    else:
        print('invalid command ')

    _save_clients_to_storage()
