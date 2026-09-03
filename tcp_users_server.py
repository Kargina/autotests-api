import socket


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)
    server_socket.listen(10)

    messages = []

    while True:
        client_socket, client_addr = server_socket.accept()
        print(f'Пользователь с адресом: {client_addr} подключился к серверу')

        client_message = client_socket.recv(1024).decode()
        print(f'Пользователь с адресом: {client_addr} отправил сообщение: {client_message}')
        messages.append(client_message)
        print(messages)

        client_socket.send('\n'.join(messages).encode())


if __name__ == '__main__':
    server()
