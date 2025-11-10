import sys
import asyncio


class Status:
    """A Status represents whether some operation is complete.

    >>> s = Status()
    >>> s.is_done()
    False
    >>> s.done()
    >>> s.is_done()
    True
    """
    def __init__(self):
        self.status = False

    def is_done(self) -> bool:
        return self.status

    def done(self):
        self.status = True


async def get_user_input(status: Status) -> str:
    # Read one line of user input
    # Using "await" means that we're giving up control
    # and letting other coroutines run while we wait for
    # user input.
    result = await asyncio.to_thread(sys.stdin.readline)
    status.done()
    return result.strip()


async def timer(status: Status, period):
    """Print a message every period seconds until status.is_done()."""
    time_passed = 0
    while not status.is_done():
        if time_passed == 1:
            print('1 second has passed...')
        else:
            print(f'{time_passed} seconds have passed...')
        time_passed += period
        await asyncio.sleep(period)
    return time_passed


async def timer_example():
    """An example of using a timer.

    >>> asyncio.run(timer_example())
    0 seconds have passed...
    0.5 seconds have passed...
    1 second has passed...
    1.5 seconds have passed...
    Status updated after 1.7 seconds
    The timer counted up to 2.0 seconds
    """
    async def update_status(status: Status):
        await asyncio.sleep(1.7)
        print('Status updated after 1.7 seconds')
        status.done()

    status = Status()
    _, elapsed = await asyncio.gather(update_status(status), timer(status, 0.5))
    print(f'The timer counted up to {elapsed} seconds')


async def wwpd(challenge: str):
    """Run a WWPD interface.

    >>> simulate_user_input(5, 2.5) # simulate a user entering 5 after 2.5 seconds
    >>> asyncio.run(wwpd('2 + 3'))
    What is 2 + 3
    0 seconds have passed...
    1 second has passed...
    2 seconds have passed...
    5
    The user waited 3 seconds to correctly respond with 5

    >>> simulate_user_input(6, 1.5) # simulate a user entering 6 after 1.5 seconds
    >>> asyncio.run(wwpd('2 + 3'))
    What is 2 + 3
    0 seconds have passed...
    1 second has passed...
    6
    The user waited 2 seconds to incorrectly respond with 6
    """
    print('What is', challenge)
    status = Status()
    response, seconds = await asyncio.gather(get_user_input(status), timer(status, 0.5));

    # Get the correct answer, and compare it to the user input.
    correct_answer = eval(challenge)
    if str(correct_answer) == response.strip():
        print(f'The user waited {seconds} seconds to correctly respond with {response}')
    else:
        print(f'The user waited {seconds} seconds to incorrectly respond with {response}')


def simulate_user_input(response, time):
    """Simulate a user response after an amount of time. This is just for testing."""
    async def f(status):
        await asyncio.sleep(time)
        status.done()
        print(response)
        return str(response)
    global get_user_input
    get_user_input = f


async def main():
    await wwpd('2 + 4')


if __name__ == "__main__":
    asyncio.run(main())
