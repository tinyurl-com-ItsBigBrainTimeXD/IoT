import multiprocessing as mp
from time import sleep
from Network.networking import send_data, form_packet


def start_polling(input_queue: mp.Queue, output_queue: mp.Queue, host: str):
    """Start polling the server for data"""
    while True:
        sleep(1)
        msg = form_packet('GET', host, '/frontend', {
            'type': 1
        })

        if not input_queue.empty():
            msg = input_queue.get()

        _, _, content = send_data(msg)
        output_queue.put(content)


if __name__ == "__main__":
    input_queue = mp.Queue()
    output_queue = mp.Queue()
    proc = mp.Process(target = start_polling, args=(input_queue, output_queue, '192.168.43.32'))
    proc.start()

    # Run Pi processes here
    while True:
        if not output_queue.empty():
            print(output_queue.get())