import multiprocessing as mp
from time import sleep
from Network.networking import send_data, form_packet
from arduino_ver1.Translation import buzzer_on, SetLock, SetAngle, rc_time, light, writeWarning


def start_polling(poll_input_queue: mp.Queue, poll_output_queue: mp.Queue, host: str):
    """Start polling the server for data"""
    while True:
        sleep(1)
        msg = form_packet('GET', host, '/device', {
            'type': 1
        })

        if not poll_input_queue.empty():
            msg = poll_input_queue.get()

        _, _, content = send_data(msg)
        poll_output_queue.put(content)


if __name__ == "__main__":
    input_queue = mp.Queue()
    output_queue = mp.Queue()
    proc = mp.Process(target=start_polling, args=(input_queue, output_queue, '192.168.43.32'))
    proc.daemon = True
    proc.start()

    buzzer_cycle = 0
    isLocked = True

    while True:
        args = []

        # Blocks on getting data
        content = output_queue.get(block=True)
        lock = content['lock']
        buzzer = content['buzzer']
        
        # Check if user wants to activate the buzzer
        if buzzer:

            # Set buzzer cycle = 5
            buzzer_cycle = 5
            writeWarning((
                "Alarm Activated",
                "Locate Box Protocol",
                "Find my box"
            ))

        # Check if the lock state is changed
        if lock != isLocked:

            # Activate / Deactivate lock
            isLocked = lock

            if isLocked:

                writeWarning((
                    "Closing the Lid",
                    "Locking the box",
                    "Thank you for using"
                ))

                # Lock the box
                SetAngle(90)
                sleep(1)
                SetLock(90)

            else:

                writeWarning((
                    "Unlocking the box",
                    "Opening the Lid",
                    "Thank you for using"
                ))

                # Unlock the box
                SetLock(0)
                SetAngle(0)

        # Check if the opening is valid
        # If photosensor and isLocked are contradictory make a buzzer sound
        if rc_time(light) and isLocked:
            buzzer_cycle = 5
            writeWarning((
                "WARNING", 
                "Unauthorized Access",
                "Alarm Activated"
            ))

        # Check if the buzzer still needs ringing
        if buzzer_cycle:

            # Activate buzzer
            buzzer_on()

            # Decrement cycle
            buzzer_cycle -= 1




